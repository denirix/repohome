import threading
import time

def calculate_sum(n):
    result = sum(range(n))
    print(f"Sum of numbers up to {n} is {result}")

if __name__ == "__main__":
    start_time = time.time()

    threads = []
    for i in range(3):
        t = threading.Thread(target=calculate_sum, args=(10**i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
