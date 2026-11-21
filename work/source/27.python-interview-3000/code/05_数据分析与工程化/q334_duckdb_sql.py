import csv
import os

def write_csv(path):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["city", "amt"])
        for city, amt in [("BJ", 10), ("SH", 20), ("BJ", 30)]:
            w.writerow([city, amt])

if __name__ == "__main__":
    path = "demo_duck.csv"
    write_csv(path)
    try:
        import duckdb
        con = duckdb.connect()                 # 进程内,零部署
        out = con.execute(
            "SELECT city, sum(amt) AS total "
            "FROM read_csv_auto(?) GROUP BY city ORDER BY total DESC",
            [path],
        ).fetchall()
        print(out)
        con.close()
    except ImportError:
        # 降级:纯标准库实现同样语义
        groups = {}
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                groups[row["city"]] = groups.get(row["city"], 0) + float(row["amt"])
        print(sorted(groups.items(), key=lambda kv: -kv[1]))
    os.remove(path)
