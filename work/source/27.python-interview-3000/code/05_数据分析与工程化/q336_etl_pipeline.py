import json
import os

def extract(src_path, processed_marker):
    """Extract:带水位标记,幂等拉取。"""
    if os.path.exists(processed_marker):
        print("already processed, skip")
        return []
    with open(src_path) as f:
        return [line.strip() for line in f if line.strip()]

def transform(records):
    """Transform:纯函数,输入输出明确,可单测。"""
    return [r.upper() for r in records if "bad" not in r]

def load(rows, dst_path, marker, batch_meta):
    """Load:先写临时文件再原子 rename。"""
    tmp = dst_path + ".tmp"
    with open(tmp, "w") as f:
        f.write("\n".join(rows))
    os.replace(tmp, dst_path)                      # 原子替换
    with open(marker, "w") as f:
        json.dump(batch_meta, f)

if __name__ == "__main__":
    src, dst, marker = "src.txt", "dst.txt", ".processed"
    with open(src, "w") as f:
        f.write("apple\nBAD seed\nbanana\n")
    rows = transform(extract(src, marker))
    load(rows, dst, marker, {"batch": "2026-11-01", "rows": len(rows)})
    print(open(dst).read().splitlines(), open(marker).read())
    os.remove(src); os.remove(dst); os.remove(marker)
