Airline AI Assistant:
Welcome to the **Airline AI Assistant** — an AI-powered chatbot that acts as a virtual support agent for an airline called **FlightAI**.  
This assistant provides short, courteous answers to customer queries and can fetch ticket prices for popular destinations using **OpenAI GPT-4**.
Whether you’re helping customers, handling inquiries, or providing ticket information, this tool automates airline support with AI.

What It Does
- Acts as a "polite airline assistant" with concise responses  
- Provides "ticket prices" for cities like London, Paris, Tokyo, Berlin  
- Replies with “I don’t know” if the requested information isn’t available  
- Runs locally using a "Gradio chat interface" for interactive conversation  
- Customizes responses based on user input (e.g., items on sale, unavailable requests)
  

Tech Stack
- Python 3.9+ 
- OpenAI GPT-4 API  
- [Gradio](https://www.gradio.app/) for interactive UI  
- `python-dotenv` for managing API keys  

GETTING STARTED:
Clone the Repository
"bash"
git clone https://github.com/ujjesha1312/Airline-assistant-project.git

cd Airline-assistant-project

python -m venv venv (create a virtual environment)

#Windows:
venv\Scripts\activate

#macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt (install dependencies)

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx (your OpenAI API key)


HOW IT WORKS(Under the Hood)
System Message – Sets the context for the AI assistant, including sales promotions and policies.
Chat Function – Handles conversation history, user messages, and generates responses using OpenAI GPT-4.
Tools – Custom functions like get_ticket_price fetch ticket prices dynamically.
Gradio Interface – Provides an interactive chat UI for users to communicate with the assistant.


PROJECT STRUCTURE:
bash
Copy code
Airline-assistant-project/
│
├── app.py             # Main application
├── requirements.txt   # Dependencies
├── .env.example       # Example environment variables
├── .gitignore         # Ignore files like .env, venv
└── README.md          # Project documentation


SAMPLE OUTPUT:
User: Hi, I want to buy a ticket to London.
Assistant: Wonderful! A return ticket to London costs $799.

User: What about Paris?
Assistant: A return ticket to Paris costs $899.

User: Do you have any hats on sale?
Assistant: Yes! Hats are currently 60% off — perfect time to grab one.

User: Are shoes on sale today?
Assistant: Shoes are not on sale today, but don’t miss our hats at 60% off!

User: Can I buy a belt?
Assistant: We don’t sell belts, but many other items are on sale. Hats and clothing are great options!

[ Chat Interface Screenshot ]
| FlightAI Assistant                             |
|-----------------------------------------------|
| User: Hi, I want to buy a ticket to London.  |
| Assistant: Wonderful! A return ticket to ... |
| User: Are shoes on sale today?               |
| Assistant: Shoes are not on sale today, ...  |
+-----------------------------------------------+


FUTURE ENHANCEMENTS:
Add more destinations and dynamic ticket pricing
Export chat logs for customer service review
Integrate with real airline booking APIs
Multilingual support for international customers


DISCLAIMER:
This tool is for educational and demonstration purposes.
Always verify ticket prices and airline policies before relying on it for professional use.
