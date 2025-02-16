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

text_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions="""\
    Your task is to interact with the user to collect detailed information about their appliance issue. 
    Answer based on whatever user asks.
    """,
    response_model=ApplianceDetails,
    structured_outputs=True
)

# def interactive_session():
#     questions = [
#         "Please describe your issue...",
#         "Could you please tell me the brand of your appliance?",
#         "What is the model number of your appliance?",
#         "Can you describe the issue you are experiencing with the appliance in detail?",
#         "How old is the appliance? (This is optional, so feel free to skip if unsure.)",
#         "Do you have the serial number of the appliance? (This is optional.)",
#         "When was the last time the appliance was serviced? (This is optional.)"
#     ]

#     responses = {}
#     for question in questions:
#         print(question)
#         response = input("User: ")
#         # Store the response appropriately
#         # responses[question] = response

#     # Process the collected responses
#     # ...
def run_text_agent():
    text = "HEllo, can you help me setup a samsung tv"

    result = text_agent.run(text)  # Assuming this returns a RunResponse object

    # Extracting the assistant's response from the messages attribute
    assistant_response = next((msg.content for msg in result.messages if msg.role == 'assistant'), None)

    return assistant_response  # Return the assistant's response


print(run_text_agent())