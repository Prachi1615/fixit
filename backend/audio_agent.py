from agno.agent import Agent
from agno.media import Audio
from agno.models.openai import OpenAIChat

url = "https://openaiassets.blob.core.windows.net/$web/API/docs/audio/alloy.wav"

audio_agent = Agent(
    model=OpenAIChat(id="gpt-4o-audio-preview", modalities=["text"]),
    markdown=True,
)

def run_audio_agent():
   
    result = audio_agent.run("What is in this audio?", audio=[Audio(url=url, format="wav")], stream=True)  # Assuming this returns a RunResponse object

    # Extracting the assistant's response from the messages attribute
    assistant_response = result

    return assistant_response  # Return the assistant's response


print(run_audio_agent())