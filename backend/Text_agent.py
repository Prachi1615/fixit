from typing import Optional
from pydantic import BaseModel
from agno.agent import Agent
from agno.models.openai import OpenAIChat

class ApplianceDetails(BaseModel):
    brand: str
    model: str
    issue: str
    age: Optional[int] = None
    serial_number: Optional[str] = None
    last_service_date: Optional[str] = None

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions="""\
    Your task is to interact with the user to collect detailed information about their appliance issue. Please ask the following questions in order and wait for the user's response after each question:

    1. "Please describe your issue..."
    2. "Could you please tell me the brand of your appliance?"
    3. "What is the model number of your appliance?"
    4. "Can you describe the issue you are experiencing with the appliance in detail?"
    5. "How old is the appliance? (This is optional, so feel free to skip if unsure.)"
    6. "Do you have the serial number of the appliance? (This is optional.)"
    7. "When was the last time the appliance was serviced? (This is optional.)"

    Please ensure to ask these questions in the specified order and provide a friendly and helpful interaction. If the user is unsure about any optional information, reassure them that it's okay to skip those questions.
    """,
    response_model=ApplianceDetails,
    structured_outputs=True
)

def interactive_session():
    questions = [
        "Please describe your issue...",
        "Could you please tell me the brand of your appliance?",
        "What is the model number of your appliance?",
        "Can you describe the issue you are experiencing with the appliance in detail?",
        "How old is the appliance? (This is optional, so feel free to skip if unsure.)",
        "Do you have the serial number of the appliance? (This is optional.)",
        "When was the last time the appliance was serviced? (This is optional.)"
    ]

    responses = {}
    for question in questions:
        print(question)
        response = input("User: ")
        # Store the response appropriately
        # responses[question] = response

    # Process the collected responses
    # ...

if __name__ == "__main__":
    interactive_session()