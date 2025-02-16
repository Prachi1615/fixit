from typing import List, Optional
from textwrap import dedent

from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from pydantic import BaseModel


class Appliance(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    serial_number: Optional[str] = None
    condition: Optional[str] = None
    warranty_status: Optional[bool] = None
    description: Optional[str] = None


agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=dedent("""\
        You are an expert at analyzing appliances. Your task is to:
        1. Extract all available information about the appliance from the image
        2. If any required fields (name, brand, model, price) are missing or unclear:
           - Ask the user specific questions to obtain the missing information
           - Explain why you need this information
        3. For optional fields, ask if the user has additional information about:
           - Year of manufacture
           - Serial number
           - Condition
           - Warranty status
        4. Verify the information with the user before finalizing

        Always maintain a professional and helpful tone. If the image is unclear or unreadable,
        politely ask the user for a better quality image.
    """),
    response_model=Appliance,
    # structured_outputs=True,
)

agent.cli_app(
    "Extract the information from this image",
    images=[Image(filepath="/Users/ab/lab/agno/cookbook/hackathon/examples/hackathon_tv.jpg")],
)