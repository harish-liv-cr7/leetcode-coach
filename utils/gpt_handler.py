import openai
import json
import os
from typing import Dict, Any

def generate_hints_and_review(problem_title: str, user_code: str) -> Dict[str, Any]:
    """
    Generate hints and code review for a LeetCode problem using OpenAI GPT-4.
    
    Args:
        problem_title (str): The title of the LeetCode problem
        user_code (str): The user's solution code
        
    Returns:
        Dict[str, Any]: Dictionary containing summary, hints, code_review, and test_cases
    """
    
    # Construct the prompt for GPT-4
    prompt = f"""You are an AI LeetCode coach. The user is trying to solve the problem titled: {problem_title}.
They wrote the following code:

{user_code}

Please do the following:
1. Summarize the problem briefly in 2–3 lines.
2. Give 3 helpful hints that guide toward the solution (without spoiling it).
3. Review the user's code for correctness, edge cases, and efficiency.
4. Generate 2 strong edge test cases and explain why they matter.

Return your output in JSON format with keys: summary, hints, code_review, test_cases.

The hints should be an array of 3 strings.
The test_cases should be an array of 2 strings, each describing a test case and why it's important.
The summary and code_review should be strings.

Example format:
{{
    "summary": "Brief problem description...",
    "hints": ["Hint 1", "Hint 2", "Hint 3"],
    "code_review": "Detailed code review...",
    "test_cases": ["Test case 1 with explanation", "Test case 2 with explanation"]
}}"""

    try:
        # Make the API call to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful AI LeetCode coach that provides guidance and code reviews in JSON format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        
        # Extract the response content
        response_content = response.choices[0].message.content.strip()
        
        # Try to parse the JSON response
        try:
            result = json.loads(response_content)
            
            # Validate that all required keys are present
            required_keys = ['summary', 'hints', 'code_review', 'test_cases']
            for key in required_keys:
                if key not in result:
                    raise ValueError(f"Missing required key: {key}")
            
            # Ensure hints and test_cases are lists
            if not isinstance(result['hints'], list) or len(result['hints']) != 3:
                result['hints'] = ["Consider the problem constraints", "Think about edge cases", "Optimize your approach"]
            
            if not isinstance(result['test_cases'], list) or len(result['test_cases']) != 2:
                result['test_cases'] = ["Empty input case", "Large input case"]
            
            return result
            
        except json.JSONDecodeError:
            # If JSON parsing fails, return a structured fallback
            return {
                "summary": f"Problem: {problem_title} - A coding challenge that requires algorithmic thinking.",
                "hints": [
                    "Consider the problem constraints and edge cases",
                    "Think about the time and space complexity of your solution",
                    "Make sure your solution handles all possible inputs correctly"
                ],
                "code_review": "Unable to parse AI response. Please ensure your code handles edge cases and follows best practices.",
                "test_cases": [
                    "Test with empty/null inputs to ensure robustness",
                    "Test with maximum allowed inputs to check performance"
                ]
            }
            
    except Exception as e:
        # Handle any OpenAI API errors or other exceptions
        return {
            "summary": f"Problem: {problem_title} - A coding challenge that requires algorithmic thinking.",
            "hints": [
                "Consider the problem constraints and edge cases",
                "Think about the time and space complexity of your solution", 
                "Make sure your solution handles all possible inputs correctly"
            ],
            "code_review": f"Unable to analyze code due to API error: {str(e)}. Please check your OpenAI API key and internet connection.",
            "test_cases": [
                "Test with empty/null inputs to ensure robustness",
                "Test with maximum allowed inputs to check performance"
            ]
        } 