import csv
import os
import tempfile

def robust_import(path, expect_cols=2):
    good, bad = [], []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for lineno, row in enumerate(reader, start=2):
            if len(row) != expect_cols:          # 脏行进 reject,不中断
                bad.append((lineno, row))
                continue
            try:
                amt = float(row[1].replace(",", ""))   # 处理千分位
            except ValueError:
                bad.append((lineno, row))
                continue
            good.append((row[0], amt))
    return good, bad

def export_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:  # Excel 兼容
        w = csv.writer(f)
        w.writerow(["city", "amt"])
        w.writerows(rows)

if __name__ == "__main__":
    # 演示文件放临时目录,避免污染当前工作目录
    tmpdir = tempfile.mkdtemp()
    dirty_path = os.path.join(tmpdir, "dirty.csv")
    clean_path = os.path.join(tmpdir, "clean.csv")
    with open(dirty_path, "w", newline="", encoding="utf-8") as f:
        f.write("city,amt\nBJ,1,000\nSH,20\nSZ\nBJ,30\n")
    good, bad = robust_import(dirty_path)
    print("good:", good)
    print("bad lines:", bad)
    export_csv(clean_path, good)
    os.remove(dirty_path); os.remove(clean_path)
    os.rmdir(tmpdir)
