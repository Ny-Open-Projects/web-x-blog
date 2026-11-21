import os
import tempfile
import textwrap

ADR = textwrap.dedent("""
    # ADR-007 采用 DuckDB 做本地分析
    日期: 2026-11-01
    状态: 已接受
    背景: 报表在 8GB 机器上跑 pandas 频繁 OOM
    决策: 聚合下推到 DuckDB,python 只做展示层
    后果: 新增 duckdb 依赖;查询提速约 6 倍;pandas 用法需迁移
""")

def write_adr(root, idx, content):
    name = f"ADR-{idx:03d}.md"
    with open(os.path.join(root, name), "w", encoding="utf-8") as f:
        f.write(content)
    return name

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as root:
        n = write_adr(root, 7, ADR)
        print("已生成", n)
        with open(os.path.join(root, n), encoding="utf-8") as f:
            print(f.read()[:120])
    print("文档进仓库随代码评审,adr 目录即决策索引")
