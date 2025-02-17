from flask import Flask, request, jsonify
from voice.depression.init_voice_depression_model import init_voice_depression_model
from log_resource_usage import log_resource_usage
from voice.depression.predict_audio_depress import predict_audio_depress
import os
import io


app = Flask(__name__)

depress_model = init_voice_depression_model()

@app.route("/voice-depress", methods=["POST"])
def upload():
    if not request.data:
        return jsonify({"error": "No file data found"}), 400

    audio_file = io.BytesIO(request.data)
    print(f'\n1. audio_file loaded: {audio_file}')

    if audio_file is None:
        return jsonify({"error": "Failed to fetch audio file"}), 400

    # 감정 분석 수행
    depression_label, sigmoid_value = predict_audio_depress(audio_file, depress_model)

    log_resource_usage('after prediction')
    print(f'5. Predict completed {depression_label}, {sigmoid_value.tolist()[0][0]}\n')

    # 결과 반환
    return jsonify({"depression": depression_label, "sigmoid_value": sigmoid_value.tolist()[0][0]})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, debug=False)
