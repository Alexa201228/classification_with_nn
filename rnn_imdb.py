from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Загрузка и предобработка данных
num_words = 10000
maxlen = 100
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=num_words)

train_data = pad_sequences(train_data, maxlen=maxlen)
test_data = pad_sequences(test_data, maxlen=maxlen)

# Создание модели
model = Sequential([
    Embedding(num_words, 32, input_length=maxlen),
    LSTM(32),
    Dense(1, activation='sigmoid')
])

# Компиляция модели
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Обучение модели
model.fit(train_data, train_labels, epochs=10, batch_size=128, validation_split=0.2)

# Оценка модели
test_loss, test_acc = model.evaluate(test_data, test_labels)
print("\nТочность на тестовых данных:", test_acc)