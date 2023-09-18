from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Загрузка и предобработка данных
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Нормализация изображений в диапазоне [0, 1]
train_images = train_images / 255.0
test_images = test_images / 255.0

# Кодирование меток
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Создание модели
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Преобразование изображений в одномерный массив
    Dense(128, activation='relu'),  # Полносвязный слой с 128 нейронами
    Dense(10, activation='softmax') # Выходной слой с 10 нейронами (по числу классов)
])

# Компиляция модели
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Обучение модели
model.fit(train_images, train_labels, epochs=5, batch_size=32, validation_data=(test_images, test_labels))

# Оценка модели на тестовых данных
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("\nТочность на тестовых данных:", test_acc)
