"""数据工厂的边界用例集: 五类脏文件, 加载器必须逐类给出明确拒绝"""

import os
import tempfile

HEADER = "id,name,amount\n"


def w(dir_path, name, content):
    path = os.path.join(dir_path, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def build_cases(d):
    return [
        ("空文件", w(d, "empty.csv", "")),
        ("仅表头", w(d, "header.csv", HEADER)),
        ("必填缺失", w(d, "null_required.csv", HEADER + "1,,100\n")),
        ("主键重复", w(d, "dup.csv", HEADER + "1,张三,100\n1,李四,200\n")),
        ("类型非法", w(d, "bad_type.csv", HEADER + "1,张三,abc\n")),
    ]


def load(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if not content.strip():
        raise ValueError("空文件")
    lines = content.strip().splitlines()
    if len(lines) < 2:
        raise ValueError("无数据行")
    header = lines[0].split(",")
    idx = {name: i for i, name in enumerate(header)}
    seen, rows = set(), []
    for line in lines[1:]:
        cells = line.split(",")
        if not cells[idx["name"]]:
            raise ValueError("必填字段缺失")
        if cells[idx["id"]] in seen:
            raise ValueError("主键重复")
        seen.add(cells[idx["id"]])
        try:
            float(cells[idx["amount"]])
        except ValueError:
            raise ValueError("数值字段非法")
        rows.append(cells)
    return rows


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as d:
        caught = 0
        for label, path in build_cases(d):
            try:
                load(path)
            except ValueError as e:
                caught += 1
                print(f"  [拒绝] {label}: {e}")
            else:
                print(f"  [漏网] {label}: 竟然加载成功!")
        assert caught == 5, "五类脏文件必须全部被拒绝"
    print("边界用例 5/5 被明确拒绝, 无一静默吞掉")
    print("要点: 工厂不只造'好数据', 边界用例集是加载器契约的一部分, 新人改坏立刻红")
