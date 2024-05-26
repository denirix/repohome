import threading

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calculate_factorial(num, result_list):
    result = factorial(num)
    result_list.append(result)

if __name__ == "__main__":
    number = int(input("Введите число для вычисления факториала: "))

    threads = []
    results = []
    for i in range(3):
        thread = threading.Thread(target=calculate_factorial, args=(number, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_result = results[0]
    print(f"Факториал числа {number}: {final_result}")
