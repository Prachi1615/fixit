from typing import List, Optional
from textwrap import dedent

from agno.agent import Agent
from agno.agent import Agent
from agno.media import Video
from agno.models.google import Gemini
from pathlib import Path 
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from pydantic import BaseModel
from utils.video_capture import capture_video
import weave
weave.init('fixit')

class Appliance(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    serial_number: Optional[str] = None
    condition: Optional[str] = None
    warranty_status: Optional[bool] = None
    description: Optional[str] = None


# @weave.op()
# def analyze_appliance_image(image_path: str) -> Appliance:
#     agent = Agent(
#         model=OpenAIChat(id="gpt-4o"),
#         tools=[DuckDuckGoTools()],
#         instructions=dedent("""\
#             You are an expert at analyzing appliances. Your task is to:
#             1. Extract all available information about the appliance from the image
#             2. If any required fields (name, brand, model, price) are missing or unclear:
#            - Ask the user specific questions to obtain the missing information
#            - Explain why you need this information
#         3. For optional fields, ask if the user has additional information about:
#            - Year of manufacture
#            - Serial number
#            - Condition
#            - Warranty status
#         4. Verify the information with the user before finalizing

#         Always maintain a professional and helpful tone. If the image is unclear or unreadable,
#         politely ask the user for a better quality image.
#     """),
#     response_model=Appliance,
#     structured_outputs=True,
# )

#     return agent.print_response("Analyze this image", images=[Image(filepath=image_path)])

# print(analyze_appliance_image(file['filename']))

# video_agent = Agent(
#     model=OpenAIChat(id="gpt-4o"),
#     tools=[DuckDuckGoTools()],
#     instructions=dedent("""\
#         You are an expert at analyzing appliances. Your task is to:
#         1. Extract all available information about the appliance from the image
#         2. If any required fields (name, brand, model, price) are missing or unclear:
#         - Ask the user specific questions to obtain the missing information
#         - Explain why you need this information
#     3. For optional fields, ask if the user has additional information about:
#         - Year of manufacture
#         - Serial number
#         - Condition
#         - Warranty status
#     4. Verify the information with the user before finalizing

#     Always maintain a professional and helpful tone. If the image is unclear or unreadable,
#     politely ask the user for a better quality image.
# """),
# response_model=Appliance,
# structured_outputs=True,
# )

    # return agent.print_response("Analyze this image", images=[Image(filepath=image_path)])

video_agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    markdown=True,
)

# Please download "GreatRedSpot.mp4" using
# wget https://storage.googleapis.com/generativeai-downloads/images/GreatRedSpot.mp4
# video_path = Path(__file__).parent.joinpath(file['filename'])

# agent.print_response("Tell me about this video", videos=[Video(filepath=video_path)])

def run_video_agent():
    file = capture_video()

    video_path = Path(__file__).parent.joinpath(file['filename'])


    result = video_agent.run("Tell me about this video", videos=[Video(filepath=video_path)])

    return result.content

print(run_video_agent())