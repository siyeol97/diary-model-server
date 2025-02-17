from voice.emotion.split_audio_emotion import split_audio_emotion
from voice.emotion.preprocess_audio_emotion import preprocess_audio_emotion
import numpy as np
from log_resource_usage import log_resource_usage

def predict_audio_emotion(user_audio, emotion_model):
    emotions = ['기쁨', '슬픔', '분노', '불안', '상처', '당황', '중립']
    
    features = [] 
    audio_chunks = split_audio_emotion(user_audio)

    log_resource_usage('after split_audio')
    print(f'Number of audio chunks: {len(audio_chunks)}')

    for i in range(len(audio_chunks)):
        features.append(preprocess_audio_emotion(audio_chunks[i]))
    
    predictions = []
    for i in range(len(features)):
        feature = np.expand_dims(features[i], axis=0)
        prediction = emotion_model.predict(feature)
        predictions.append(prediction)
    
    predictions = np.array(predictions)

    average_prediction = np.mean(predictions, axis=0)

    max_index = np.argmax(average_prediction)
    dominant_emotion = emotions[max_index]

    emotions_average = dict(zip(emotions, average_prediction.tolist()[0]))

    return emotions_average, dominant_emotion