# LeetCode Coach

A Python Flask backend API that provides AI-powered coaching for LeetCode problems. The service analyzes your code, provides helpful hints, reviews your solution, and suggests edge test cases using OpenAI's GPT-4.

## Features

- **Problem Analysis**: Get a brief summary of any LeetCode problem
- **Smart Hints**: Receive 3 helpful hints that guide you toward the solution without spoiling it
- **Code Review**: Get detailed feedback on your code's correctness, edge cases, and efficiency
- **Edge Test Cases**: Generate 2 strong edge test cases with explanations of why they matter

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd leetcode-coach
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```bash
   # OpenAI API Configuration
   OPENAI_API_KEY=your_openai_api_key_here
   
   # Flask Configuration
   FLASK_ENV=development
   FLASK_DEBUG=True
   ```
   
   **Important**: Replace `your_openai_api_key_here` with your actual OpenAI API key.

5. **Run the application**
   ```bash
   python app.py
   ```
   
   The server will start on `http://localhost:5000`

## API Usage

### Analyze Problem and Code

**Endpoint**: `POST /analyze`

**Request Body**:
```json
{
    "problem_title": "Two Sum",
    "user_code": "def twoSum(nums, target):\n    for i in range(len(nums)):\n        for j in range(i+1, len(nums)):\n            if nums[i] + nums[j] == target:\n                return [i, j]\n    return []"
}
```

**Response**:
```json
{
    "summary": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.",
    "hints": [
        "Consider using a hash map to store previously seen numbers",
        "Think about how you can find the complement of each number",
        "This approach can reduce time complexity from O(n²) to O(n)"
    ],
    "code_review": "Your current solution uses a nested loop approach with O(n²) time complexity. While it's correct, it's not optimal. Consider using a hash map to store numbers as you iterate through the array. For each number, check if its complement (target - current_number) exists in the hash map. This would give you O(n) time complexity.",
    "test_cases": [
        "Test case: nums = [3, 3], target = 6. This tests the case where the same number appears twice and is the solution.",
        "Test case: nums = [2, 7, 11, 15], target = 9. This tests the basic functionality with a valid solution."
    ]
}
```

### Health Check

**Endpoint**: `GET /health`

**Response**:
```json
{
    "status": "healthy",
    "message": "LeetCode Coach API is running"
}
```

## Error Handling

The API includes comprehensive error handling:

- **400 Bad Request**: Missing required fields (`problem_title` or `user_code`)
- **500 Internal Server Error**: OpenAI API failures or other server errors

## Project Structure

```
leetcode-coach/
├── app.py                 # Main Flask application
├── utils/
│   └── gpt_handler.py    # OpenAI GPT-4 integration
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (not tracked in git)
└── README.md            # This file
```

## Future Improvements

### Phase 2 Features
- **User Tracking**: Store user progress and problem history
- **Problem Notes**: Allow users to save personal notes for each problem
- **Revisit Scheduler**: Implement spaced repetition to suggest when to revisit problems
- **Difficulty Tracking**: Track which problems users struggle with most

### Phase 3 Features
- **Database Integration**: PostgreSQL for persistent data storage
- **User Authentication**: JWT-based authentication system
- **Problem Categories**: Organize problems by topic (arrays, trees, graphs, etc.)
- **Performance Analytics**: Track improvement over time

### Phase 4 Features
- **Frontend Interface**: React/Vue.js web application
- **Mobile App**: React Native or Flutter mobile application
- **Social Features**: Share solutions and discuss problems with other users
- **Competition Mode**: Timed problem-solving challenges

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository. 