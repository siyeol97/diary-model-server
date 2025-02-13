# 특징 추출
import numpy as np
import librosa
import parselmouth

def extract_features(audio_file):
    sr = 44100
    # Preemphasis
    y_pre = librosa.effects.preemphasis(audio_file, coef=0.97)

    # MFCC and Mel Spectrogram parameters
    n_fft = 1024
    hop_length = 256
    win_length = 512
    window = 'hamming'
    n_mels = 128
    n_mfcc = 64

    # Extract MFCC features
    mfccs = librosa.feature.mfcc(y=y_pre, win_length = win_length , sr=sr, n_mfcc=n_mfcc, n_mels=n_mels, n_fft=n_fft, hop_length=hop_length, window=window)
    # Extract Mel Spectrogram features
    mel_spectrogram = librosa.feature.melspectrogram(y=y_pre, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels, window=window, win_length=win_length)
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram)

    # Load audio file with Parselmouth
    sound = parselmouth.Sound(audio_file)

    # Extract pitch
    pitch = sound.to_pitch(time_step=hop_length/sr)
    pitch_values = pitch.selected_array['frequency']

    # Extract intensity
    intensity = sound.to_intensity(time_step=hop_length/sr)
    intensity_values = intensity.values[0]

    # Interpolate pitch and intensity to match the length of MFCCs
    pitch_interp = np.interp(np.linspace(0, len(pitch_values), mfccs.shape[1]), np.arange(len(pitch_values)), pitch_values)
    intensity_interp = np.interp(np.linspace(0, len(intensity_values), mfccs.shape[1]), np.arange(len(intensity_values)), intensity_values)

    # Normalize MFCCs, pitch, intensity and Mel Spectrogram
    mfccs = (mfccs - np.min(mfccs)) / (np.max(mfccs) - np.min(mfccs))
    mel_spectrogram_db = (mel_spectrogram_db - np.min(mel_spectrogram_db)) / (np.max(mel_spectrogram_db) - np.min(mel_spectrogram_db))

    if not np.isnan(pitch_interp).all() and np.nanmin(pitch_interp) != np.nanmax(pitch_interp):
        pitch_interp = (pitch_interp - np.nanmin(pitch_interp)) / (np.nanmax(pitch_interp) - np.nanmin(pitch_interp))
    else:
        pitch_interp = np.zeros_like(pitch_interp)

    intensity_interp = (intensity_interp - np.min(intensity_interp)) / (np.max(intensity_interp) - np.min(intensity_interp))

    # Stack MFCCs, Mel Spectrogram, pitch and intensity features
    features = np.vstack([mfccs, mel_spectrogram_db, pitch_interp, intensity_interp])

    return features