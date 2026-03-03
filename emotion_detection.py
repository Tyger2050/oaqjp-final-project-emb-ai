from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/emotion", methods=["POST"])
def detect_emotion():
    data = request.get_json()
    text = data.get("text", "")

    text_lower = text.lower()

    if "happy" in text_lower or "feliz" in text_lower:
        emotion = "joy"
    elif "sad" in text_lower or "triste" in text_lower:
        emotion = "sadness"
    elif "angry" in text_lower or "molesto" in text_lower:
        emotion = "anger"
    else:
        emotion = "neutral"

    return jsonify({"emotion": emotion})

