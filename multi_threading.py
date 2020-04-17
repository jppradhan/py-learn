from threading import Thread
from time import sleep, time
from concurrent.futures import ThreadPoolExecutor, as_completed
# Basic example threading


# class Hello(Thread):
#     def run(self):
#         for _ in range(5):
#             print('Hello')
#             sleep(0.1)


# class Hi(Thread):
#     def run(self):
#         for _ in range(5):
#             print('Hi')
#             sleep(0.1)


# hello = Hello()
# hi = Hi()

# hello.start()
# hi.start()

# hello.join()
# hi.join()

# print("Am done here ::::::::::::: Bye")
# print("Advanced example threading")

files = {
    'niroj': 'niroj gote banda pila',
    'tushar': 'tushar gote banda pila',
    'samir': 'samir gote banda pila',
    'baba': 'baba gote banda pila',
    'litu': 'baba gote banda pila'
}

start = time()


def write_file(name, text):
    with open(f'downloads/{name}.txt', 'a') as f:
        f.write(text)
    return f'{name} profile updated...'


# for name, text in files.items():
#     write_file(name, text)
# print('completed in: ', time() - start)

threads = []


def write_file_async(name, text):
    t = Thread(target=write_file, args=[name, text])
    t.start()
    threads.append(t)


for name, text in files.items():
    write_file_async(name, text)

for t in threads:
    t.join()


print('completed in: ', time() - start)
print("Created files")


# Concurrent thread pool
with ThreadPoolExecutor() as executor:
    res = []
    for name, text in files.items():
        t = executor.submit(write_file, name, text)
        res.append(t)

    for f in as_completed(res):
        print(f.result())

print("Created files by pool")
