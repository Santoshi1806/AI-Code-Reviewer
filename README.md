🚀AI-Code-Reviewer APP!🚀

📌 Overview
🤖I built an AI Code Reviewer using Python and Streamlit, integrating GoogleAI API to analyze code and provide insightful feedback. The objective of this project is to develop a Python application that allows users to submit their Python code for review and receive feedback on potential bugs along with suggestions for fixes. This application is user-friendly, efficient, and provides accurate bug reports and fixes code snippets.

✨ Features
🤖 AI-Powered Code Review: Utilizes Google's Gemini 1.5 Pro model for advanced Python code analysis.

🐞 Bug Detection & Fixes: Identifies issues in the submitted code and provides corrected versions

♦️Enhances code quality and efficiency

🏺Code Quality Enhancement: Improve readability, efficiency, and maintainability with AI insights.

📚 Explanations: Offers clear explanations for detected errors and suggested fixes.

⚙️ Installation

🔹 Prerequisites

Ensure you have Python 3.7+ installed on your system.

🔹 Install Dependencies

Run the following command to install the required packages:


[ ]
pip install -r requirements.txt

🚀 Usage

1.📥 Clone the repository or copy the script to your local machine.

2.▶️ Run the Streamlit application


[ ]
python -m streamlit run app.py

3.✍️ Enter your Python code in the text area and click the Review button.

4.✅ The AI will analyze the code and provide:

🔎 Bug Report

🛠 Fixed Code

📖 Explanations

🔧 Configuration

Replace your Google Gemini API key in the script:


[ ]
ai.configure(api_key = "YOUR_API_KEY")

📁 Project Structure

[ ]
/ai_code_reviewer
│── app.py               # Main Streamlit app script
│── README.md            # Documentation
└── requirements.txt      # List of dependencies

🤝 Contributing
Feel free to fork this repository and enhance the functionality!

