🤖 AI Resume Analyser

AI Resume Analyser is a web-based application that parses resumes and extracts structured information using NLP techniques.  
It helps users understand their resume content better by identifying skills, experience, and other key details.

---

🚀 Features

- 📄 Resume parsing (PDF / text-based resumes)
- 🧠 Skill extraction and analysis
- 🔍 Keyword identification
- 📊 Structured output for resume data
- 🧩 Modular and agent-based design
- 🌐 Simple web interface

---

🧠 Tech Stack

- **Backend:** Python
- **Web Framework:** Flask
- **NLP:** Custom resume parsing logic
- **Frontend:** HTML templates
- **AI Integration:** Bedrock client (if configured)

---

## 📂 Project Structure
AI-Resume-Analyser/
│
├── agents/ # AI / analysis agents
├── templates/ # HTML templates
├── app.py # Main Flask application
├── resume_parser.py # Resume parsing logic
├── bedrock_client.py # AI model integration
├── .gitignore
└── README.md


---

## ⚙️ Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

Clone the repository:

```bash
git clone https://github.com/priyanshuagarkar/AI-Resume-Analyser.git
cd AI-Resume-Analyser

Install dependencies:

pip install -r requirements.txt

(If requirements.txt is missing, install Flask and required NLP libraries manually.)

▶️ Running the Application
python app.py

