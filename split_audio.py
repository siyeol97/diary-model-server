import librosa
import numpy as np

def split_audio(filename, chunk_length=5):
    # Load the audio file
    y, sr = librosa.load(filename, sr=44100)

    print(f'2. librosa loaded')

    # Calculate the number of 1-minute chunks
    total_length = librosa.get_duration(y=y, sr=sr)
    num_chunks = int(total_length / chunk_length)

    # Split the audio
    audio_chunks = []
    for i in range(num_chunks):
        start = i * chunk_length * sr
        end = (i+1) * chunk_length * sr
        audio_chunk = y[start:end]
        audio_chunks.append(audio_chunk)

    # If there are any leftovers, pad and add them as well
    if total_length > chunk_length * num_chunks:
        start = num_chunks * chunk_length * sr
        audio_chunk = np.pad(y[start:], (0, start + chunk_length * sr - len(y)))
        audio_chunks.append(audio_chunk)

    return audio_chunks