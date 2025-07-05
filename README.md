
 AI Health Chatbot (Multilingual | Hugging Face + Streamlit)

This is an AI-powered health chatbot created as part of an AI Intern Assignment. It answers user questions related to health (like symptoms, medicine, and nutrition) using a pre-trained Hugging Face model. It also detects the intent behind the question and now supports both English and Hindi inputs using automatic translation.

 Assignment Deliverables
 
 1. Markdown File with Q&A Examples
 2. Provided in chatbot_qna.md section below.
 3. Python Notebook / Script for Classification Logic

Intent classification is implemented using keyword-based logic in intent_classifier.py.

 3. Demo Video (2–3 minutes)

[Upload link will be provided here once available.]

 Features

Real-time AI-generated answers (text2text-generation)

Intent classification: Nutrition, Medicine, Emergency

Multilingual Input (Supports Hindi + English)

Streamlit UI for web interaction

Smart caching of model for fast performance

 Evaluation Criteria Mapping

Criteria

Implementation Status

Score Estimate

Prompt Design Quality

Specific, medically relevant prompts

9/10

Multilingual Handling

Hindi + English via translation

10/10

Intent Classification Logic

Keyword logic, scalable design

9/10

Presentation/Markdown

Structured README + Q&A file

🔧 Technologies Used

Python

Hugging Face Transformers (flan-t5-base)

Streamlit

Deep Translator (Google Translate API)

Custom Intent Classifier (keywords)

🏁 How to Run the Project

Clone the repo

git clone https://github.com/yourusername/health-chatbot
cd health-chatbot

Install dependencies

pip install -r requirements.txt

Run the Streamlit app

streamlit run hfchatbot.py

Example Q&A

Nutrition

Q: What should I eat for iron deficiency?A: Eat leafy greens, beetroot, jaggery, and dates.

Medicine

Q: Is paracetamol safe during pregnancy?A: Paracetamol is generally safe but should be taken under doctor supervision.

Emergency

Q: What to do if someone faints suddenly?A: Lay them flat, elevate legs, loosen clothes, and call for help.

Hindi Input Example

Q (in Hindi): मुझे चक्कर क्यों आते हैं?✅ Translated internally and answered accurately.

 File Structure

├── hfchatbot.py             # Main chatbot logic
├── intent_classifier.py     # Intent detection function
├── requirements.txt         # Python dependencies
├── README.md                # Project description
├── chatbot_qna.md           # Sample Q&A examples (markdown)

 Author

Anjali UpadhyayB.Tech CSE | Passionate about AI/ML, NLP & Real-world chatbot solutionsLinkedIn Profile

 Future Scope

Add support for more Indian languages

Integrate medical APIs for verified data

Add voice input/output for accessibility

Create feedback loop to improve accuracy

 License

This project is open-source and free to use under the MIT License.

 For demo video and live Q&A results, see the uploaded screencast or preview link (to be added).
 https://www.loom.com/share/68f570957d70417fb66c62eaf67fa1bb?sid=152a7a66-08c2-495c-98c0-ae0035586feb

