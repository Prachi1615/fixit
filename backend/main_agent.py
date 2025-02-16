from llama_index.core.agent.workflow import AgentWorkflow
from typing import Union, Dict, Any
from PIL import Image
import os
from pathlib import Path
import io  # Add this with other imports

# Import your existing agents
from agent1 import analyze_appliance_image  # Image agent
# from backend.nav_agent import nav_agent  # Audio agent
# from backend.Text_agent import Text_agent  # Text agent
# from backend.video_agent import video_agent  # Video agent

class InputType:
    IMAGE = "image"
    AUDIO = "audio"
    TEXT = "text"
    VIDEO = "video"

def determine_input_type(user_input: Union[str, bytes, Path]) -> str:
    """
    Determine the type of input and return the appropriate type
    """
    if isinstance(user_input, str):
        # Check if it's a file path
        if os.path.isfile(user_input):
            extension = os.path.splitext(user_input)[1].lower()
            if extension in ['.png', '.jpg', '.jpeg', '.gif', '.bmp']:
                return InputType.IMAGE
            elif extension in ['.mp3', '.wav', '.aac']:
                return InputType.AUDIO
            elif extension in ['.mp4', '.avi', '.mov', '.wmv']:
                return InputType.VIDEO
        return InputType.TEXT
    
    # If input is bytes, try to determine if it's an image
    elif isinstance(user_input, bytes):
        try:
            Image.open(io.BytesIO(user_input))
            return InputType.IMAGE
        except:
            pass
    
    return InputType.TEXT

# Main workflow setup
main_workflow = AgentWorkflow(
    agents=[analyze_appliance_image],
    root_agent=None,
    initial_state={
        "input_type": None,
        "status": "Waiting for input"
    }
)

def route_to_agent(user_input: Union[str, bytes, Path]) -> Dict[str, Any]:
    """
    Route the input to the appropriate agent based on input type
    """
    input_type = determine_input_type(user_input)
    
    # Set the appropriate root agent based on input type
    if input_type == InputType.IMAGE:
        main_workflow.root_agent = agent1.name
    elif input_type == InputType.AUDIO:
        main_workflow.root_agent = nav_agent.name
    elif input_type == InputType.VIDEO:
        main_workflow.root_agent = video_agent.name
    else:
        main_workflow.root_agent = Text_agent.name
    
    # Update workflow state
    main_workflow.initial_state.update({
        "input_type": input_type,
        "status": "Processing"
    })
    
    try:
        result = main_workflow.run(user_input)
        return {
            "status": "success",
            "result": result,
            "input_type": input_type
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "input_type": input_type
        }

# Example usage
if __name__ == "__main__":
    # For text input
    text_result = route_to_agent("How can you help me?")
    
    # For image input (assuming it's a file path)
    image_result = route_to_agent("path/to/image.jpg")
    
    # For audio input
    audio_result = route_to_agent("path/to/audio.mp3")
    
    # For video input
    video_result = route_to_agent("path/to/video.mp4")