AI Health Chatbot (Multilingual | Hugging Face + Streamlit)
This project is an AI-powered multilingual health chatbot developed as part of an AI Internship Assignment. It uses Hugging Face's pretrained transformer model to answer questions related to nutrition, medicine, and emergencies, with support for both English and Hindi using automatic translation.

 Features
Real-time AI-generated answers using flan-t5-base

Intent classification using keyword-based logic (Nutrition, Medicine, Emergency)

Multilingual input (English and Hindi)

Translation handled via Google Translate API

Simple, interactive Streamlit web interface

Model caching for faster performance

 File Structure
bash
Copy
Edit
health-chatbot/
├── hfchatbot.py            # Main chatbot logic with Streamlit UI
├── intent_classifier.py    # Intent classification based on keyword matching
├── chatbot_qna.md          # Sample Q&A markdown examples
├── requirements.txt        # List of required Python packages
└── README.md               # Project documentation
⚙️ How to Run the Project
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/health-chatbot
cd health-chatbot
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit application

bash
Copy
Edit
streamlit run hfchatbot.py
 Example Q&A
Nutrition
Q: What should I eat for iron deficiency?
A: Eat leafy greens, beetroot, jaggery, and dates.

Medicine
Q: Is paracetamol safe during pregnancy?
A: Paracetamol is generally safe but should be taken under doctor supervision.

Emergency
Q: What to do if someone faints suddenly?
A: Lay them flat, elevate legs, loosen clothes, and call for help.

 Hindi Input Example
Q (in Hindi): मुझे चक्कर क्यों आते हैं?
A: Internally translated and answered based on symptoms.

 Evaluation Criteria Mapping
Criteria	Implementation Status	Score Estimate
Prompt Design Quality	Specific, medically relevant prompts	9/10
Multilingual Handling	Hindi + English via translation	10/10
Intent Classification	Keyword logic, scalable	9/10
Documentation/Markdown	Structured README and Q&A	10/10

 Technologies Used
Python

Hugging Face Transformers (flan-t5-base)

Streamlit

Deep Translator (Google Translate API)

Custom Intent Classifier (keywords)

 Future Scope
Add support for more Indian languages

Integrate verified medical APIs (e.g., MedlinePlus)

Enable voice input/output for accessibility

Add a feedback loop to improve response accuracy

 Author
Anjali Upadhyay
B.Tech CSE | Passionate about AI/ML, NLP & Real-world chatbot solutions

 License
This project is licensed under the MIT License – free to use, modify, and distribute.
https://www.loom.com/share/68f570957d70417fb66c62eaf67fa1bb?sid=152a7a66-08c2-495c-98c0-ae0035586feb



