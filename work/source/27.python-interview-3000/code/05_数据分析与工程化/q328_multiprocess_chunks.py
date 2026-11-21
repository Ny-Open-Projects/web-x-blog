import csv
import os
from concurrent.futures import ProcessPoolExecutor

CSV_PATH = "demo_mp.csv"

def write_csv(path, n=1000):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "amt"])
        for i in range(n):
            w.writerow([i, i % 7 + 1])

def process_range(args):
    """每个进程只读自己的行区间,返回局部聚合。"""
    start, end = args
    total = 0.0
    with open(CSV_PATH, newline="") as f:
        for i, row in enumerate(csv.reader(f)):
            if i == 0:
                continue
            if start <= i < end:
                total += float(row[1])
            if i >= end:
                break
    return total

def main():
    n = sum(1 for _ in open(CSV_PATH)) - 1
    k = 4
    bounds = [(i * n // k, (i + 1) * n // k) for i in range(k)]
    with ProcessPoolExecutor(max_workers=k) as pool:
        partials = list(pool.map(process_range, bounds))
    print("total =", sum(partials), "partials =", partials)

if __name__ == "__main__":
    write_csv(CSV_PATH)
    main()
    os.remove(CSV_PATH)
