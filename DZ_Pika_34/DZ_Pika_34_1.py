import threading

even_numbers = []
odd_numbers = []

def find_even_numbers():
    global even_numbers
    for i in range(10, 101):
        if i % 2 == 0:
            even_numbers.append(i)

def find_odd_numbers():
    global odd_numbers
    for i in range(10, 101):
        if i % 2 != 0:
            odd_numbers.append(i)

def print_numbers():
    global even_numbers, odd_numbers
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)

t1 = threading.Thread(target=find_even_numbers)
t2 = threading.Thread(target=find_odd_numbers)
t3 = threading.Thread(target=print_numbers)

t1.start()
t2.start()

t1.join()
t2.join()

t3.start()
t3.join()
