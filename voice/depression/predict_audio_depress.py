import numpy as np
from voice.depression.split_audio_depression import split_audio_depression
from voice.depression.extract_features import extract_features
from log_resource_usage import log_resource_usage

# 음성 우울감 예측 함수
def predict_audio_depress(user_audio, depress_model):
    features = [] 
    audio_chunks = split_audio_depression(user_audio)

    log_resource_usage('after split audio depression')
    print(f'Number of audio chunks: {len(audio_chunks)}')

    for i in range(len(audio_chunks)):
        features.append(extract_features(audio_chunks[i]))
    
    log_resource_usage('after extract_features')
    print(f'Features extracted')

    prediction_sum = 0
    for i in range(len(features)):
        # 모델이 받아들일 수 있는 형태로 차원을 변경
        feature = np.expand_dims(features[i], axis=0)
        prediction = depress_model.predict(feature)
        prediction_sum += prediction

    predicted_class  = ((prediction_sum/len(features)) > 0.5).astype(int)
    sigmoid_value = (prediction_sum/len(features))
    

    dep_dict = { 0:'비우울', 1:'우울'}
    
    print(f'Predict depression completed\n========================\n')
    
    return (dep_dict[predicted_class.item()], sigmoid_value)