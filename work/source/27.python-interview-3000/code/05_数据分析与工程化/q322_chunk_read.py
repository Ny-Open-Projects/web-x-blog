import csv
import os

def write_demo_csv(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["city", "amt"])
        for city, amt in rows:
            w.writerow([city, amt])

def process_chunks(path, chunk_size=3):
    """map-reduce:逐块过滤聚合,最后合并部分结果。生产上用
    pd.read_csv(path, chunksize=chunk_size) 得到同样语义的迭代器。"""
    partial = {}
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) == chunk_size:
                merge_partial(partial, chunk)
                chunk = []
        if chunk:
            merge_partial(partial, chunk)
    return partial

def merge_partial(partial, chunk):
    for r in chunk:
        partial[r["city"]] = partial.get(r["city"], 0) + float(r["amt"])

if __name__ == "__main__":
    try:
        import pandas as pd
        path = "demo_chunk.csv"
        write_demo_csv(path, [("BJ", 10), ("SH", 20), ("BJ", 5), ("SZ", 8)])
        total = {}
        for chunk in pd.read_csv(path, chunksize=2):   # 生产写法
            g = chunk.groupby("city")["amt"].sum()
            total = total.add(g, fill_value=0)
        print(total.to_dict())
        os.remove(path)
    except ImportError:
        path = "demo_chunk.csv"
        write_demo_csv(path, [("BJ", 10), ("SH", 20), ("BJ", 5), ("SZ", 8)])
        print(process_chunks(path))
        os.remove(path)
