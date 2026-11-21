#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""M4 重写稿机械质检门禁：对 _units.json 中已 done 的单元逐一验稿。

检查：front-matter 四字段 / CJK 字数 ≥1500 / 口播腔残留 / 围栏成对 / 文件存在。
输出：逐篇 PASS/FAIL + 汇总；FAIL 写回 _m4_state.json 的 failed 列表（幂等重建）。

用法：python3 ai/scripts/m4_qc.py
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
M4T = ROOT / "work/target/34-java-suite/m4"
UNITS = M4T / "_units.json"
STATE = M4T / "_m4_state.json"
POSTS = M4T / "posts"

BANNED = re.compile(r"各位同学|大家好|欢迎回来|咱们|接下来我们|好了，那")
FM = re.compile(r"^---\ntitle: \"(.+)\"\ndate: (\d{4}-\d{2}-\d{2})\ncategories: \[(.+)\]\ntags: \[(.+)\]\n---\n")

def main() -> None:
    units = {u["id"]: u for u in json.loads(UNITS.read_text(encoding="utf-8"))}
    st = json.loads(STATE.read_text(encoding="utf-8"))
    fails: list[dict] = []
    npass = 0
    for uid in st["done"]:
        u = units.get(uid)
        if not u:
            continue
        f = POSTS / u["out"]
        if not f.exists():
            fails.append({"unit": uid, "why": "文件缺失"})
            print(f"FAIL {uid} 文件缺失: {u['out']}")
            continue
        t = f.read_text(encoding="utf-8")
        m = FM.match(t)
        body = t[m.end():] if m else t
        problems = []
        if not m:
            problems.append("front-matter 不合规")
        else:
            cats = m.group(3)
            if "M4 六大进阶项目" not in cats or u["project"] not in cats:
                problems.append(f"categories 未含项目名: {cats}")
        cjk = len(re.findall(r"[\u4e00-\u9fff]", body))
        # 门槛按源料体量分级：小单元（<40KB，通常 1-3 视频）1200 字，其余 1500 字
        floor = 1200 if u.get("bytes", 0) < 40_000 else 1500
        if cjk < floor:
            problems.append(f"CJK {cjk} < {floor}")
        hits = BANNED.findall(body)
        if hits:
            problems.append(f"口播腔残留 {len(hits)} 处")
        if t.count("```") % 2:
            problems.append("围栏不成对")
        if not body.lstrip().startswith("# "):
            problems.append("正文首行不是 # 标题")
        if problems:
            fails.append({"unit": uid, "why": problems})
            print(f"FAIL {uid} {u['out']}: {'; '.join(problems)}")
        else:
            npass += 1
            print(f"PASS {uid} {u['out']}  CJK={cjk}")
    st["failed"] = [f["unit"] for f in fails]
    json.dump(st, open(STATE, "w"), ensure_ascii=False)
    print(f"\n汇总: PASS {npass} / FAIL {len(fails)}（failed 已写回 state）")

if __name__ == "__main__":
    main()
