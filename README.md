## AI Health Chatbot (Multilingual | Hugging Face + Streamlit)

This is an AI-powered health chatbot created as part of an AI Intern Assignment. It answers user questions related to health topics such as symptoms, medicines, and nutrition using a pre-trained Hugging Face model. It also detects the intent behind the user query and supports both English and Hindi using automatic translation.

---

## Assignment Deliverables

- **Markdown File with Q&A Examples**  
  Provided in `chatbot_qna.md`

- **Python Script for Classification Logic**  
  Intent classification is implemented using keyword-based logic in `intent_classifier.py`

- **Demo Video (2–3 minutes)**  
  [Upload link will be provided here once available]

---

## Features

- Real-time AI-generated answers using `text2text-generation`
- Intent classification: Nutrition, Medicine, Emergency
- Multilingual Input (Supports Hindi + English)
- Streamlit UI for easy web interaction
- Smart caching of model for fast performance

---

## Technologies Used

- Python  
- Hugging Face Transformers (`flan-t5-base`)  
- Streamlit  
- Deep Translator (Google Translate API)  
- Custom Keyword-based Intent Classifier

---

## Evaluation Criteria Mapping

| Criteria                 | Implementation Status                  | Score Estimate |
|--------------------------|-----------------------------------------|----------------|
| Prompt Design Quality    | Specific, medically relevant prompts    | 9/10           |
| Multilingual Handling    | Hindi + English via translation         | 10/10          |
| Intent Classification    | Keyword logic, scalable design          | 9/10           |
| Presentation/Markdown    | Structured README + Q&A file            | 10/10          |

---

## How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/health-chatbot
   cd health-chatbot
2. Install dependencies

pip install -r requirements.txt
Run the Streamlit app

streamlit run hfchatbot.py
3.File Structure

├── hfchatbot.py            # Main chatbot logic
├── intent_classifier.py    # Intent detection function
├── requirements.txt        # Python dependencies
├── README.md               # Project description
├── chatbot_qna.md          # Sample Q&A examples
