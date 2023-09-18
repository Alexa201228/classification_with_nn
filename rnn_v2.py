from keras.datasets import imdb
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from rnn_imdb import num_words, maxlen, model

# 1. Токенизация
tokenizer = Tokenizer(num_words=num_words)
# Здесь мы используем только fit_on_texts, чтобы токенизатор знал слова из IMDB.
tokenizer.fit_on_texts(imdb.get_word_index())

def encode_text(text):
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequences, maxlen=maxlen)
    return padded_sequence

# 2. Преобразование вашего текста
your_text = "The movie was fantastic! I really enjoyed it."  # Пример положительного отзыва
encoded_text = encode_text(your_text)

# 3. Предсказание
prediction = model.predict(encoded_text)

# 4. Интерпретация
if prediction >= 0.5:
    print("Положительный отзыв")
else:
    print("Отрицательный отзыв")

# Сохранение всей модели в файл
model.save('my_model.keras')
