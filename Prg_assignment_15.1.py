import multiprocessing, datetime, time, random

def comepleteRand():
    wait = random.random()
    time.sleep(wait)
    curr_time = datetime.date.today().strftime("%Y-%m-%d %H:%M:%S")
    print("Current time :", curr_time)

if __name__ == "__main__":
    processes = []
    for _ in range(3):
        process = multiprocessing.Process(target=comepleteRand)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()