from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, BatchNormalization, MaxPooling2D, Dropout, Flatten, Dense

def init_voice_depression_model():
    print(f'\nLoading Audio Depression Model...')
    audio_depression_model = Sequential()

    # 1. conv block
    audio_depression_model.add(Conv2D(16, (3,3), padding='same', activation='relu', input_shape=(194, 862, 1)))
    audio_depression_model.add(BatchNormalization())
    audio_depression_model.add(MaxPooling2D(pool_size=(2, 2)))
    audio_depression_model.add(Dropout(0.3))

    # 2. conv block
    audio_depression_model.add(Conv2D(32, (3,3), padding='same', activation='relu'))
    audio_depression_model.add(BatchNormalization())
    audio_depression_model.add(MaxPooling2D(pool_size=(2, 2)))
    audio_depression_model.add(Dropout(0.3))

    # 3. conv block
    audio_depression_model.add(Conv2D(64, (3,3), padding='same', activation='relu'))
    audio_depression_model.add(BatchNormalization())
    audio_depression_model.add(MaxPooling2D(pool_size=(2, 2)))
    audio_depression_model.add(Dropout(0.3))

    # 4. conv block
    audio_depression_model.add(Conv2D(128, (3,3), padding='same', activation='relu'))
    audio_depression_model.add(BatchNormalization())
    audio_depression_model.add(MaxPooling2D(pool_size=(2, 2)))
    audio_depression_model.add(Dropout(0.3))

    # flatten the output of the conv block
    audio_depression_model.add(Flatten())

    # output layer
    audio_depression_model.add(Dense(1, activation='sigmoid'))

    audio_depression_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # 음성 우울감 예측 가중치 로드
    audio_depression_model.load_weights("voice/depression/audio_depression_model.h5")

    print(f'Audio Depression Model loaded')

    return audio_depression_model