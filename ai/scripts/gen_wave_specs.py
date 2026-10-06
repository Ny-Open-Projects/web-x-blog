#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_wave_specs.py —— 依据覆盖率缺失清单，生成「自包含派发规格」/tmp/waveN_{group}.md

设计：
  - 读各课程 _MANIFEST.json 拿 article(id/title/chapter/sources/code_refs)
  - 读 work/target/_COVERAGE_ALL.json 拿 missing 清单（权威，能识别 点号=短横 同 id）
  - 按传入的 segment 计划，对每个 (group, course, ids) 生成一份规格 md
  - 规格内含：必读规范、代码策略、硬性红线、目标卡片表（绝对路径）、汇报格式

用法:
  python3 gen_wave_specs.py --wave 6 --plan /tmp/wave6_plan.json
  plan json 形如:
    {"storageA": {"course":"storage","ids":["8-13","8-2",...]},
     "apmA":     {"course":"apm","ids":["7-9","7-10",...]}, ...}
"""
import json, re, sys
from pathlib import Path

ROOT = Path('/Users/Wang/Code/github/web-x-blog')
COURSE_PREFIX = {'campus': '校园社区项目从0到1', 'storage': '六大数据库存储实战', 'apm': 'Go APM 监控系统实战'}
COURSE_DIR = {'campus': 'campus', 'storage': 'storage', 'apm': 'apm'}

SPEC_TMPL = '''# 博客卡片产出任务（Wave {wave} 派发规格）

你是一名资深后端/Golang 工程师子 agent。任务：基于机器翻译讲稿，产出高质量技术博客卡片。

## 第一步：先读完以下规范，再动手
- 必读：`/Users/Wang/Code/github/web-x-blog/ai/prompts/blog_prompt.md`（产出唯一依据）
- 必读：`/Users/Wang/Code/github/web-x-blog/ai/prompts/card-qc.md`（落盘前最后一道闸，逐张自检）
- 风格参照：先读 `/Users/Wang/Code/github/web-x-blog/work/target/{course_dir}/..` 下 2~3 个已有的非 `_` 开头 .md 卡片，严格对齐结构：
  `# 课程名: 具体内容` → `## 纲要` → `## 素材索引`（mermaid）→ 正文 → 结尾 `相关度：XX%。是否需要继续：[是/否]。代码是否可运行：[是/否]。`
  - 标题层级不用数字序号；代码围栏统一标准三反引号（```go / ```mermaid / ```sql）；严禁三单引号。
  - 删除一切机翻痕迹、语气词、课程推广、IDE 广告、引流。

## 代码策略
- `code_refs` 非空：优先读这些代码文件，提炼可运行片段嵌入（保持可运行，可裁剪）。
- 讲稿偏概念：不强塞代码，`代码是否可运行：[否]`。
- apm `code_refs` 恒为空：按讲稿逻辑自补简明可运行 Go 示例，注明"根据讲稿逻辑补充"。

## 硬性红线
- 只写 `/Users/Wang/Code/github/web-x-blog/work/target/{course_dir}/<id>_<短标题>.md`，不要改 `_MANIFEST.json` / `_PROGRESS.md` / 其他卡片。
- `<id>` 严格用下方 clean_id；短标题中文概括、不含空格与特殊符号。
- 每篇写盘前按 card-qc.md 七项逐张自检，命中即重写，不许带病入库。
- **质量优先于速度；若遇到 429 限流，立即停止并如实报告，不要盲重试。**

## 本段要产出的卡片（互斥，不要碰其他 id；若某 id 盘上已有任意命名形态文件，说明后跳过，勿重复产出）

课程 key=`{course_key}`，课程名前缀=`{course_prefix}`，输出目录=`/Users/Wang/Code/github/web-x-blog/work/target/{course_dir}`

| clean_id | 标题提示 | 源讲稿(绝对路径) | 代码文件(绝对路径) | 章节 |
| --- | --- | --- | --- | --- |
{cards_table}## 完成后汇报
逐行列结果，最后一行：`WAVE{wave}_DONE: <已产出数>/<应产出数>`
'''


def canon(token: str) -> str:
    return re.sub(r'[.\-]', '', token)


def mcanon(raw_id: str) -> str:
    """manifest id 归一成可比较串：先剥 [..]-- 前缀，再取首个 N[.-]M 编号，最后去点横。"""
    s = re.sub(r'^\[[^\]]*\]\s*--\s*', '', raw_id)
    m = re.search(r'\d+(?:[.\-]\d+)*', s)
    return canon(m.group(0)) if m else canon(s)


def load_manifest(course_key):
    m = json.load(open(ROOT / 'work' / 'target' / COURSE_DIR[course_key] / '_MANIFEST.json', encoding='utf-8'))
    by_canon = {}
    for a in m['articles']:
        by_canon[mcanon(a['id'])] = a
    return by_canon


def abs_src(rel):
    return str((ROOT / rel).resolve())


def main():
    wave = None
    plan_path = None
    for i, a in enumerate(sys.argv):
        if a == '--wave':
            wave = sys.argv[i + 1]
        if a == '--plan':
            plan_path = sys.argv[i + 1]
    wave = wave or '6'
    plan = json.load(open(plan_path, encoding='utf-8'))

    manifests = {k: load_manifest(k) for k in ('storage', 'apm', 'campus')}

    for group, spec in plan.items():
        course_key = spec['course']
        ids = spec['ids']
        m = manifests[course_key]
        rows = []
        for cid in ids:
            art = m.get(canon(cid))
            if not art:
                rows.append(f"| {cid} | (MANIFEST 未匹配到，请检查 id) |  |  |  |")
                continue
            srcs = art.get('sources', [])
            src_str = ' '.join(abs_src(s) for s in srcs) if srcs else '（无，按概念或自补）'
            cr = art.get('code_refs', [])
            if cr:
                cr_abs = [abs_src(c) for c in cr if (ROOT / c).exists()]
                cr_str = ' '.join(cr_abs) if cr_abs else '（无现存代码文件，按概念或自补）'
            else:
                cr_str = '（无，按概念或自补）'
            title = art.get('title', '')
            # 标题提示：去掉开头的 [x.x]-- 脏前缀
            title_hint = re.sub(r'^\[[^\]]*\]\s*--\s*', '', title)
            chapter = art.get('chapter', '')
            rows.append(f"| {cid} | {title_hint} | {src_str} | {cr_str} | {chapter} |")
        cards_table = '\n'.join(rows) + '\n'
        out = SPEC_TMPL.format(
            wave=wave, course_dir=COURSE_DIR[course_key], course_key=course_key,
            course_prefix=COURSE_PREFIX[course_key], cards_table=cards_table)
        outp = Path(f'/tmp/wave{wave}_{group}.md')
        outp.write_text(out, encoding='utf-8')
        print(f'wrote {outp} ({len(ids)} ids)')


if __name__ == '__main__':
    main()
