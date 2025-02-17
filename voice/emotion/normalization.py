import numpy as np

def normalization(audio_np):
    normed_wav = audio_np / max(np.abs(audio_np))
    return normed_wav