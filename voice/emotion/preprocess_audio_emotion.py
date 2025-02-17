from voice.emotion.normalization import normalization
from voice.emotion.extract_mfccs import extract_mfccs
from tensorflow.keras.preprocessing.sequence import pad_sequences

def preprocess_audio_emotion(file_path):
    audio_nor = normalization(file_path)
    mfcc = extract_mfccs(audio_nor)
    audio_seq = pad_sequences(mfcc, padding='post' , truncating='post', maxlen=300, dtype='float32')
    return audio_seq