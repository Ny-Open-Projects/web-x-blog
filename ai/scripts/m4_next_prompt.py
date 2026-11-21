#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""M4 夜班滚动助手：打印下一批（2 个未 done 单元）的完整 agent prompt。

用法：python3 ai/scripts/m4_next_prompt.py [数量]
配合每轮心跳：1) 本脚本拿 prompt → 2) Agent 派单 → 3) m4_mark_done.py uXXX uYYY + m4_qc.py
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
M4T = ROOT / "work/target/34-java-suite/m4"
SRC_PREFIX = "/Users/Wang/Code/github/web-x-blog/work/source/34.java-suite/m4-advanced-6projects"

PROJECT_TAGS = {
    "品达物流TMS": "物流TMS", "智牛股": "股票交易",
    "千亿级电商秒杀解决方案": "秒杀", "中台战略与组件化开发": "中台化",
    "物联网新零售-亿可控": "物联网", "物联网新零售-立可得": "新零售",
}

def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    units = json.loads((M4T / "_units.json").read_text(encoding="utf-8"))
    st = json.loads((M4T / "_m4_state.json").read_text(encoding="utf-8"))
    done = set(st["done"])
    todo = [u for u in units if u["id"] not in done][:n]
    if not todo:
        print("ALL_DONE")
        return
    import re
    for k, u in enumerate(todo, 1):
        files = "\n".join(f"{v}_merged.md" for v in u["videos"])
        tag = PROJECT_TAGS.get(u["project"], "项目实战")
        print(f"## 第{'一' if k == 1 else '二'}篇：单元 {u['id']}（{u['project']} · {u['chapter']} · {len(u['videos'])} 视频，{u['bytes']//1000}KB）")
        print(f"源目录前缀：{SRC_PREFIX}/")
        print("逐个 Read：")
        print(files)
        print(f"输出（文件名必须一字不差）：/Users/Wang/Code/github/web-x-blog/work/target/34-java-suite/m4/posts/{u['out']}")
        print(f"categories: [Java后端进阶全套, M4 六大进阶项目, {u['project']}]；tags: [Java, 项目实战, {tag}]")
        print()
    print("（以上为两篇单元的输入/输出事实，写作规范与去口播腔规则见固定模板，稍后拼接）")

if __name__ == "__main__":
    main()
