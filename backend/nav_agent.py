import weave
from llama_index.core.chat_engine import SimpleChatEngine

# Initialize Weave with your project name
weave.init("fixit")

chat_engine = SimpleChatEngine.from_defaults()
response = chat_engine.chat(
    "Say something profound and romantic about fourth of July"
)
print(response)