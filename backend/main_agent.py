from flask import Flask, request, jsonify
# from llama_index.core.agent.workflow import AgentWorkflow
from agent1 import image_agent
from Text_agent import text_agent
# from backend.nav_agent import nav_agent
from video_agent import run_video_agent
from agent1 import run_image_agent
from tex_ import run_text_agent
from audio_agent import run_audio_agent

app = Flask(__name__)

# Initialize agent workflow but do not trigger it yet
# main_workflow = AgentWorkflow(
#     agents=[image_agent, text_agent, video_agent],
#     root_agent=text_agent,  # Default agent
#     initial_state={"input_type": None, "status": "Waiting for input"}
# )

@app.route("/", methods=["GET"])
def health_check():
    """Simple health check to confirm API is running."""
    return jsonify({"status": "API is running"}), 200

@app.route("/process_input", methods=["POST"])
def process_input():
    """API waits for input from UI and triggers agents only when necessary."""
    data = request.json
    input_type = data.get("input_type")
    user_input = data.get("user_input")  # Could be text, file path, or encoded data

    if not input_type or user_input is None:
        return jsonify({"status": "error", "message": "Missing input type or user input"}), 400

    # Simulate dummy data for testing all input types
    dummy_inputs = [
        {"input_type": "image", "user_input": "dummy_image_path.jpg"},
        {"input_type": "video", "user_input": "dummy_video_path.mp4"},
        {"input_type": "audio", "user_input": "dummy_audio_path.mp3"},
        {"input_type": "text", "user_input": "This is a test text input."}
    ]

    results = {}
    
    for input_data in dummy_inputs:
        input_type = input_data["input_type"]
        user_input = input_data["user_input"]

        # Assign the correct agent based on input type
        if input_type == "image":
            response = run_image_agent()  # You may want to pass user_input if needed
            results[input_type] = response
        elif input_type == "video":
            response = run_video_agent()  # You may want to pass user_input if needed
            results[input_type] = response
        elif input_type == "audio":
            response = run_audio_agent()  # You may want to pass user_input if needed
            results[input_type] = response
        else:
            response = run_text_agent()  # You may want to pass user_input if needed
            results[input_type] = response

    return jsonify({"status": "success", "results": results}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
