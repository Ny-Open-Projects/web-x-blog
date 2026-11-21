import time

if __name__ == "__main__":
    print("time.time()      :", time.time(), "wall clock")
    print("time.monotonic() :", time.monotonic(), "monotonic")
    print("time.perf_counter():", time.perf_counter(), "high-res")
    print("time.process_time():", time.process_time(), "cpu only")

    start_wall = time.perf_counter()
    start_cpu = time.process_time()
    time.sleep(0.05)                      # 睡眠计入墙钟,不计 CPU
    print("wall elapsed:", round(time.perf_counter() - start_wall, 4))
    print("cpu elapsed :", round(time.process_time() - start_cpu, 4))
    print("monotonic non-decreasing:", time.monotonic() >= start_wall)
