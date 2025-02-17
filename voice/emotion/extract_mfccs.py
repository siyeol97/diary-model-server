import librosa

def extract_mfccs(audio_file):
    y_pre = librosa.effects.preemphasis(audio_file, coef=0.97)
    
    n_fft = 1024
    hop_length = 256
    win_length = 512
    window = 'hamming'
    n_mels = 128
    n_mfcc = 64

    mfccs = librosa.feature.mfcc(y=y_pre,win_length = win_length , sr=22050, n_mfcc=n_mfcc, n_mels=n_mels, n_fft=n_fft, hop_length=hop_length, window=window)
    return mfccs