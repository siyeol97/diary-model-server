from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, BatchNormalization, Dropout, ReLU, Softmax

def init_voice_emotion_model():
    print(f'Loading Audio Emotion Model')
    audio_emotion_model = Sequential()

    # 1. conv block
    audio_emotion_model.add(Conv2D(16, (3,3), padding='same', activation='relu', input_shape=(64, 300, 1)))
    audio_emotion_model.add(BatchNormalization())
    audio_emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    audio_emotion_model.add(Dropout(0.3))

    # 2. conv block
    audio_emotion_model.add(Conv2D(32, (3,3), padding='same', activation='relu'))
    audio_emotion_model.add(BatchNormalization())
    audio_emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    audio_emotion_model.add(Dropout(0.3))

    # 3. conv block
    audio_emotion_model.add(Conv2D(64, (3,3), padding='same', activation='relu'))
    audio_emotion_model.add(BatchNormalization())
    audio_emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    audio_emotion_model.add(Dropout(0.3))

    # 4. conv block
    audio_emotion_model.add(Conv2D(128, (3,3), padding='same', activation='relu'))
    audio_emotion_model.add(BatchNormalization())
    audio_emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    audio_emotion_model.add(Dropout(0.3))

    # flatten the output of the conv block
    audio_emotion_model.add(Flatten())

    # output layer
    audio_emotion_model.add(Dense(7, activation='softmax'))

    audio_emotion_model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    audio_emotion_model.load_weights("voice/emotion/audio_emotion_model.h5")

    print(f'Audio Emotion Model loaded\n')

    return audio_emotion_model