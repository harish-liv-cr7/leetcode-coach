from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import os
from utils.gpt_handler import generate_hints_and_review

# Load environment variables
load_dotenv()

# Configure OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_problem():
    """
    POST endpoint to analyze LeetCode problems and user code.
    
    Expected JSON input:
    {
        "problem_title": "Two Sum",
        "user_code": "def twoSum(nums, target): ..."
    }
    
    Returns:
    {
        "summary": "Problem summary...",
        "hints": ["Hint 1", "Hint 2", "Hint 3"],
        "code_review": "Code review and suggestions...",
        "test_cases": ["Test case 1", "Test case 2"]
    }
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate required fields
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        problem_title = data.get('problem_title')
        user_code = data.get('user_code')
        
        if not problem_title:
            return jsonify({"error": "problem_title is required"}), 400
        
        if not user_code:
            return jsonify({"error": "user_code is required"}), 400
        
        # Generate analysis using GPT
        analysis_result = generate_hints_and_review(problem_title, user_code)
        
        return jsonify(analysis_result), 200
        
    except Exception as e:
        # Handle OpenAI API errors and other exceptions
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify the service is running."""
    return jsonify({"status": "healthy", "message": "LeetCode Coach API is running"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
