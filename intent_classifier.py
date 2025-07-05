def classify_intent(question):
    question = question.lower()

    if any(word in question for word in ["eat", "diet", "nutrition", "iron", "fruits"]):
        return "Nutrition"

    elif any(word in question for word in ["paracetamol", "medicine", "antibiotics", "safe", "painkiller"]):
        return "Medicine"

    elif any(word in question for word in ["emergency", "faint", "asthma", "bleeding", "chest pain"]):
        return "Emergency"

    else:
        return "Unknown"
