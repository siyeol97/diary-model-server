import numpy as np
from flask import Flask, request, jsonify, make_response
from init_depress_model import init_depress_model
from  split_audio import split_audio
from extract_features import extract_features
import requests
import os
import io
from pydub import AudioSegment
#from shutil import which


app = Flask(__name__)

depress_model = init_depress_model()

# ffmpeg 경로 설정
#AudioSegment.converter = which("ffmpeg")
AudioSegment.converter = "/opt/bin/ffmpeg"

# URL로부터 오디오 파일을 가져오는 함수
def get_audio_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return io.BytesIO(response.content)
    return None

# webm 또는 mp4 파일을 wav 파일로 변환하는 함수
def convert_audio_to_wav(audio_file, file_format):
    # webm 또는 mp4 둘 다 대응 가능
    audio = AudioSegment.from_file(audio_file, format=file_format)
    
    # WAV 변환
    wav_io = io.BytesIO()
    audio.export(wav_io, format="wav")
    wav_io.seek(0)

    return wav_io

# 음성 우울감 예측 함수
def predict_audio_depress(user_audio):
    features = [] 
    audio_chunks = split_audio(user_audio)

    for i in range(len(audio_chunks)):
        features.append(extract_features(audio_chunks[i]))

    prediction_sum = 0
    for i in range(len(features)):
        # Reshape the feature to match the input shape that model expects
        # 모델이 받아들일 수 있는 형태로 차원을 변경
        feature = np.expand_dims(features[i], axis=0)  # Add a dimension for batch size
        prediction = depress_model.predict(feature)
        prediction_sum += prediction

    predicted_class  = ((prediction_sum/len(features)) > 0.5).astype(int)
    sigmoid_value = (prediction_sum/len(features))

    dep_dict = { 0:'비우울', 1:'우울'}
    
    
    return (dep_dict[int(predicted_class)], sigmoid_value)

# API 엔드포인트 (POST 요청)
@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        data = request.get_json()
        
        if not data or "url" not in data:
            return jsonify({"error": "No audio URL found"}), 400

        audio_url = data["url"]
        audio_file = get_audio_from_url(audio_url)

        if audio_file is None:
            return jsonify({"error": "Failed to fetch audio file"}), 400
        
        # 확장자 추출 ('.mp4' 또는 '.webm' 감지)
        file_extension = os.path.splitext(audio_url)[-1].lower().replace(".", "")
        wav_audio = convert_audio_to_wav(audio_file, file_extension)

        # 감정 분석 수행
        depress_label, sigmoid_value = predict_audio_depress(wav_audio)

        # 결과 반환
        return jsonify({"depress": depress_label, "sigmoid_value": sigmoid_value.tolist()})

    else:
        response = make_response("This is a GET request.")
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_ENV") == "development"  # 개발 환경에서만 debug=True
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
