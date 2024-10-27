import threading
import time
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f'Какое-то слово № {i}\n'
            file.write(word)
            print(f'Записано слово: {word.strip()}')
            sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')


# Вызываем функцию последовательно 4 раза
start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
print(f"Время последовательного выполнения: {end_time - start_time:.2f} секунд")

# Создаем потоки для параллельного выполнения
threads = []

start_threads_time = time.time()

for params in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = threading.Thread(target=write_words, args=params)
    threads.append(thread)
    thread.start()  # запускаем поток

# Ожидаем завершения всех потоков
for t in threads:
    t.join()

end_threads_time = time.time()
print(f"Время выполнения в потоках: {end_threads_time - start_threads_time:.2f} секунд")