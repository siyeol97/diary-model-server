from flask import Flask, request, jsonify
from voice.depression.init_voice_depression_model import init_voice_depression_model
from voice.emotion.init_voice_emotion_model import init_voice_emotion_model
from log_resource_usage import log_resource_usage
from voice.depression.predict_audio_depress import predict_audio_depress
from voice.emotion.predict_audio_emotion import predict_audio_emotion
import os
import io


app = Flask(__name__)

# 음성 우울감 분석 모델 초기화
audio_depress_model = init_voice_depression_model()
audio_emotion_model = init_voice_emotion_model()


@app.route("/", methods=["POST"])
def upload():
    if not request.data:
        return jsonify({"error": "No file data found"}), 400

    audio_file = io.BytesIO(request.data)
    print(f'\naudio_file loaded: {audio_file}')

    if audio_file is None:
        return jsonify({"error": "Failed to fetch audio file"}), 400

    # 감정 분석 수행
    depression_label, sigmoid_value = predict_audio_depress(audio_file, audio_depress_model)
    audio_file.seek(0)
    emotions_average, dominant_emotion = predict_audio_emotion(audio_file, audio_emotion_model)

    log_resource_usage('after prediction')
    print(f'Predict completed {depression_label}, {sigmoid_value.tolist()[0][0]}, {dominant_emotion}, {emotions_average}\n')

    # 결과 반환
    return jsonify({ "depression": depression_label, "sigmoid_value": sigmoid_value.tolist()[0][0], "emotion": dominant_emotion, "emotion_prob": emotions_average })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, debug=False)
