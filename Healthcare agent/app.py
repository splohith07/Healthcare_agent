from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get("question", "").lower()

    # RULE-BASED SYMPTOM CHECKING
    responses = []

    if "fever" in question:
        responses.append("• Fever suggests an infection. Stay hydrated and monitor temperature.")

    if "cough" in question:
        responses.append("• Cough may indicate a respiratory infection. Warm fluids can help.")

    if "cold" in question or "sneezing" in question:
        responses.append("• Runny nose/cold symptoms likely indicate a viral infection.")

    if "headache" in question:
        responses.append("• Headache can be due to stress, dehydration, or infection.")

    if "throat" in question:
        responses.append("• Sore throat may point to viral or bacterial infection.")

    if "vomit" in question:
        responses.append("• Vomiting could be due to food infection or stomach irritation.")

    if "pain" in question:
        responses.append("• General pain suggests inflammation. Take rest and hydrate.")

    # If no matches found
    if not responses:
        responses = ["I couldn't detect specific symptoms. Please describe more clearly."]

    final_reply = "\n".join(responses)

    return jsonify({"answer": final_reply})


if __name__ == "__main__":
    app.run(debug=True)
