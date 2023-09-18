from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Загрузка модели из файла
loaded_model = load_model('my_model.keras')
num_words = 10000
maxlen = 100

# 1. Токенизация
tokenizer = Tokenizer(num_words=num_words)
# Здесь мы используем только fit_on_texts, чтобы токенизатор знал слова из IMDB.
tokenizer.fit_on_texts(imdb.get_word_index())

def encode_text(text):
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequences, maxlen=maxlen)
    return padded_sequence

# 2. Преобразование текста
#your_text = "The movie was fantastic! I really enjoyed it."  # Пример положительного отзыва
your_text = "The movie was really bad! I really dislike it."  # Пример отрицательного отзыва - пример слабости модели!
# your_text = "The movie was terrible. It was the worst film I've ever seen."  # Пример отрицательного отзыва
encoded_text = encode_text(your_text)

# 3. Предсказание
prediction = loaded_model.predict(encoded_text)

# 4. Интерпретация
if prediction >= 0.5:
    print("Положительный отзыв")
else:
    print("Отрицательный отзыв")