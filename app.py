import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr
load_dotenv(override=True)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL", "gpt-4o-mini")
if OPENAI_API_KEY:
    print(f"OpenAI API Key found (first 8 chars): {OPENAI_API_KEY[:8]}")
else:
    print("OPENAI_API_KEY not set. Set it in .env")
# Initialize client (the OpenAI client picks up API key automatically from env in many installs)
# If your client requires explicit api_key arg, you can pass it: OpenAI(api_key=OPENAI_API_KEY)
client = OpenAI()
TICKET_PRICES = {
    "london": "$799",
    "paris": "$899",
    "tokyo": "$1400",
    "berlin": "$499"
}
def get_ticket_price(destination_city: str) -> str:
    """Return price for a city or 'Unknown'."""
    if not destination_city:
        return "Unknown"
    key = destination_city.strip().lower()
    price = TICKET_PRICES.get(key)
    return price or "Unknown"
price_function = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket to the destination city.",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that the customer wants to travel to",
            }
        },
        "required": ["destination_city"],
        "additionalProperties": False,
    },
}
system_message = (
    "You are a helpful assistant for an Airline called FlightAI. "
    "Give short, courteous answers, no more than 1 sentence. "
    "Always be accurate. If you don't know the answer, say so."
)
def _get_content(msg_obj):
    """Return content whether msg_obj is dict-like or object-like."""
    if msg_obj is None:
        return None
    if hasattr(msg_obj, "content"):
        return getattr(msg_obj, "content")
    if isinstance(msg_obj, dict):
        return msg_obj.get("content")
    return None
def _get_function_call(msg_obj):
    """Return function_call payload if present."""
    if msg_obj is None:
        return None
    if hasattr(msg_obj, "function_call"):
        return getattr(msg_obj, "function_call")
    if isinstance(msg_obj, dict):
        return msg_obj.get("function_call") or msg_obj.get("tool_call")
    return None
def chat(message, history):
    """
    Gradio chat function.
    - Sends system + history + user message to the model.
    - If the model requests to call get_ticket_price, we call it,
      add the tool result, and ask the model to finish the reply.
    """
    messages = [{"role": "system", "content": system_message}] + history + [
        {"role": "user", "content": message}
    ]
    response = client.chat.completions.create(
        model=MODEL, messages=messages, functions=[price_function], function_call="auto"
    )
    choice = response.choices[0]
    assistant_msg = choice.message
    function_call = _get_function_call(assistant_msg)
    if function_call:
        function_name = function_call.get("name") if isinstance(function_call, dict) else getattr(function_call, "name", None)
        arguments_text = (
            function_call.get("arguments")
            if isinstance(function_call, dict)
            else getattr(function_call, "arguments", "{}")
        )
        try:
            arguments = json.loads(arguments_text or "{}")
        except Exception:
            arguments = {}

        if function_name == "get_ticket_price":
            destination = arguments.get("destination_city")
            price = get_ticket_price(destination)
            tool_response_message = {
                "role": "tool",
                "name": "get_ticket_price",
                "content": json.dumps({"destination_city": destination, "price": price}),
            }
            messages.append({"role": "assistant", "content": _get_content(assistant_msg), "function_call": function_call})
            messages.append(tool_response_message)

            final_resp = client.chat.completions.create(model=MODEL, messages=messages)
            final_choice = final_resp.choices[0]
            return _get_content(final_choice.message) or ""
    return _get_content(assistant_msg) or ""
if __name__ == "__main__":
    # Launch a small Gradio chat UI
    gr.ChatInterface(fn=chat, type="messages").launch()
