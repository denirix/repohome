import multiprocessing
import time

def calculate_sum(n):
    result = sum(range(n))
    print(f"Sum of numbers up to {n} is {result}")

if __name__ == "__main__":
    start_time = time.time()

    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=calculate_sum, args=(10**i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
