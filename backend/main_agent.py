from flask import Flask, request, jsonify
from llama_index.core.agent.workflow import AgentWorkflow
from agent1 import image_agent
from Text_agent import text_agent
# from backend.nav_agent import nav_agent
from video_agent import video_agent
from agent1 import run_image_agent

app = Flask(__name__)

# Initialize agent workflow but do not trigger it yet
main_workflow = AgentWorkflow(
    agents=[image_agent, text_agent, video_agent],
    root_agent=text_agent,  # Default agent
    initial_state={"input_type": None, "status": "Waiting for input"}
)

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

    # Assign the correct agent based on input type
    if input_type == "image":
        print(run_image_agent())
        # main_workflow.root_agent = image_agent
    # elif input_type == "audio":
    #     main_workflow.root_agent = nav_agent
    elif input_type == "video":
        main_workflow.root_agent = video_agent
    else:
        main_workflow.root_agent = text_agent

    main_workflow.initial_state.update({"input_type": input_type, "status": "Processing"})

    try:
        result = main_workflow.run(user_input)
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
