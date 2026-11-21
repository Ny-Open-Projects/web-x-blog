"""超限导出的自动分片: 定长切块 清单核账"""

import csv
import json
import os
import tempfile

DEMO_LIMIT = 1000          # 演示用小分片, 真实 xlsx 上限 1048576 行
ROWS = list(range(2450))   # 模拟 2450 行数据


def export_sharded(rows, dir_path, limit=DEMO_LIMIT):
    parts = [rows[i:i + limit] for i in range(0, len(rows), limit)]
    manifest = {"source_rows": len(rows), "limit": limit, "parts": []}
    for i, part in enumerate(parts, 1):
        name = f"users_part{i:03d}.csv"
        path = os.path.join(dir_path, name)
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id"])
            for rid in part:
                writer.writerow([rid])
        manifest["parts"].append({"file": name, "rows": len(part),
                                  "range": [part[0], part[-1]]})
    with open(os.path.join(dir_path, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    return manifest


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        manifest = export_sharded(ROWS, tmp)
        total = sum(p["rows"] for p in manifest["parts"])
        print(f"{len(ROWS)} 行切成 {len(manifest['parts'])} 片: "
              + ", ".join(f"{p['file']}[{p['range'][0]}..{p['range'][1]}]x{p['rows']}" for p in manifest["parts"]))
        assert total == len(ROWS) == 2450, "分片行数之和必须等于源行数"
        read_back = 0
        for p in manifest["parts"]:
            with open(os.path.join(tmp, p["file"]), encoding="utf-8") as f:
                read_back += sum(1 for _ in csv.reader(f)) - 1
        assert read_back == len(ROWS), "回读行数必须守恒"
        print(f"回读核账: {read_back} 行 == 源 {len(ROWS)} 行, manifest 已随片落盘")
    print("要点: 分片名零填充保证排序稳定, 清单记录每片行数与区间, 消费端先核账再合并")
