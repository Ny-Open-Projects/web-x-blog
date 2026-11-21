"""单测的临时数据工厂: 一次调用一份样例, 用完即毁"""

import csv
import os
import tempfile

DEFAULT_ROWS = lambda: [{"id": i + 1, "name": f"用户{i + 1}", "city": "北京", "amount": 100.0 + i}
                        for i in range(5)]


def make_user_csv(dir_path, rows=None, overrides=None):
    """数据工厂: 缺省造 5 行, overrides 按 id 覆盖字段"""
    data = [dict(r) for r in (rows if rows is not None else DEFAULT_ROWS())]
    for rid, patch in (overrides or {}).items():
        for r in data:
            if r["id"] == rid:
                r.update(patch)
    path = os.path.join(dir_path, "users.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "city", "amount"])
        writer.writeheader()
        writer.writerows(data)
    return path


def read_rows(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


if __name__ == "__main__":
    # 用例一: 缺省样例
    with tempfile.TemporaryDirectory() as d1:
        p = make_user_csv(d1)
        rows = read_rows(p)
        assert len(rows) == 5 and rows[0]["amount"] == "100.0"
        print(f"用例一: 缺省工厂产出 {len(rows)} 行, 首行 amount={rows[0]['amount']}")
    assert not os.path.exists(d1), "上下文退出即清理"
    print("用例一目录已自动销毁, 不留跨用例污染")
    # 用例二: 覆盖造边界数据
    with tempfile.TemporaryDirectory() as d2:
        p = make_user_csv(d2, overrides={2: {"amount": 0.0}, 3: {"city": ""}})
        rows = {r["id"]: r for r in read_rows(p)}
        assert rows["2"]["amount"] == "0.0" and rows["3"]["city"] == ""
        print("用例二: overrides 定向造出 0 金额与空城市两个边界行")
    print("要点: 工厂只造数据不造环境, tempfile 托管生命周期, 每个用例拿到的都是全新目录")
