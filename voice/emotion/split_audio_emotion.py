import librosa
import numpy as np
from log_resource_usage import log_resource_usage

def split_audio_emotion(filename, chunk_length=3):
    # Load the audio file
    y, sr = librosa.load(filename, sr=22050)

    log_resource_usage('after loading librosa - audio_emotion')
    print(f'librosa loaded')

    total_length = librosa.get_duration(y=y, sr=sr)
    num_chunks = int(total_length / chunk_length)

    # Split the audio
    audio_chunks = []
    for i in range(num_chunks):
        start = i * chunk_length * sr
        end = (i+1) * chunk_length * sr
        audio_chunk = y[start:end]
        audio_chunks.append(audio_chunk)

    if total_length > chunk_length * num_chunks:
        start = num_chunks * chunk_length * sr
        audio_chunk = np.pad(y[start:], (0, start + chunk_length * sr - len(y)))
        audio_chunks.append(audio_chunk)

    return audio_chunks