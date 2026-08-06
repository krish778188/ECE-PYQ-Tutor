🎓 IIITN ECE Buddy
IIITN ECE Buddy is a Generative AI-powered web application specifically designed to assist Electronics and Communication Engineering (ECE) students at the Indian Institute of Information Technology, Nagpur.

This smart assistant streamlines access to academic resources, simplifies complex engineering concepts, and provides instant, AI-synthesized answers for core ECE subjects like Digital Signal Processing (DSP), Control Systems, Analog Communication, and Electromagnetics.

✨ Features
Tailored for IIITN ECE: Contextualized specifically for the curriculum and needs of IIIT Nagpur's ECE students.
Smart Topic Retrieval: Instantly synthesizes and explains core ECE concepts.
Generative AI Powered: Leverages large language models to generate accurate, easy-to-understand explanations for complex engineering queries.
Interactive UI: A clean, intuitive, and highly responsive user interface.
Fast & Lightweight: Optimized deployment ensuring minimal latency during study sessions.
🛠️ Tech Stack
Language: Python 3.x
Frontend/Framework: Streamlit
AI/Machine Learning: Generative AI Integration (LLM API)
🚀 Getting Started
Prerequisites
Ensure you have Python installed on your system. You will also need pip to install the required dependencies.

Installation
Clone the repository:
Bash
git clone https://github.com/yourusername/iiitn-ece-buddy.git
cd iiitn-ece-buddy
Create a virtual environment (optional but recommended):
Bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:
Bash
pip install -r requirements.txt
Set up environment variables:
Create a .env file in the root directory.
Add your necessary API keys (e.g., your Generative AI API key).
Plaintext
API_KEY=your_api_key_here
Running the App
Launch the application locally using Streamlit:

Bash
streamlit run app.py
The application will open in your default web browser at http://localhost:8501.

📂 Project Structure
Plaintext
iiitn-ece-buddy/
│
├── app.py                 # Main Streamlit application file
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables file
├── src/                   # Source code and helper modules
│   └── ai_integration.py  # Generative AI logic and API calls
└── README.md              # Project documentation
👨‍💻 Author
Krish
Student, Electronics and Communication Engineering (Class of 2028)
Indian Institute of Information Technology, Nagpur
