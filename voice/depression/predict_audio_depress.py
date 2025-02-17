import numpy as np
from  voice.depression.split_audio import split_audio
from voice.depression.extract_features import extract_features
from log_resource_usage import log_resource_usage

# 음성 우울감 예측 함수
def predict_audio_depress(user_audio, depress_model):
    features = [] 
    audio_chunks = split_audio(user_audio)

    log_resource_usage('after split_audio')
    print(f'3. Number of audio chunks: {len(audio_chunks)}')

    for i in range(len(audio_chunks)):
        features.append(extract_features(audio_chunks[i]))
    
    log_resource_usage('after extract_features')
    print(f'4. Features extracted')

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
    
    
    return (dep_dict[predicted_class.item()], sigmoid_value)