#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
blog_coverage.py —— 课程 8/9/10 博客产出覆盖率核查 + 续跑分块计划（纯计算，零 API 成本）

用法:
  python3 blog_coverage.py                 # 打印 campus/storage/apm 覆盖率与缺失 id
  python3 blog_coverage.py --fix-dups      # 对重复 id 保留字节数最大者、删除其余（仅作用于 >1 文件的 id）
  python3 blog_coverage.py --chunks 11     # 额外按 manifest 顺序把缺失 id 切成每块 11 个的续跑计划

输出:
  work/target/_COVERAGE_ALL.json  (结构化报告，供自动化 agent 读取)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path('/Users/Wang/Code/github/web-x-blog')
COURSES = {'campus': '8', 'storage': '9', 'apm': '10'}


def core(token: str) -> str:
    """把 '4-7' / '1.5' / '3.2' 归一成 '47' / '15' / '32'，用于跨文件名与 manifest id 匹配。"""
    return re.sub(r'[.\-]', '', token)


def canon(s: str) -> str:
    """从 manifest id 或文件名提取规范讲稿编号并归一成可比较串。
    manifest id 形如 '[1.1]--1-1新后端校招...' 或干净的 '2-7'；
    先剥掉开头的 '[...]--' 脏前缀，再取首个 N[.-]M 编号。
    """
    s = re.sub(r'^\[[^\]]*\]\s*--\s*', '', s)
    m = re.search(r'\d+(?:[.\-]\d+)*', s)
    return core(m.group(0)) if m else core(s)


def main():
    fix_dups = '--fix-dups' in sys.argv
    chunks = 0
    if '--chunks' in sys.argv:
        i = sys.argv.index('--chunks')
        chunks = int(sys.argv[i + 1])

    report = {}
    for key in COURSES:
        tdir = ROOT / 'work' / 'target' / key
        m = json.load(open(tdir / '_MANIFEST.json', encoding='utf-8'))
        arts = m['articles']
        have = {}
        for p in tdir.glob('*.md'):
            if p.name.startswith('_'):
                continue
            mm = re.match(r'(\d+(?:[.\-]\d+)*)', p.stem)
            if mm:
                have.setdefault(canon(mm.group(1)), []).append(p)
        done_ids, missing, dups = [], [], {}
        for a in arts:
            aid = a['id']
            files = have.get(canon(aid), [])
            if files:
                done_ids.append(aid)
                if len(files) > 1:
                    dups[aid] = [p.name for p in files]
            else:
                missing.append(aid)
        report[key] = {
            'course': COURSES[key],
            'total': len(arts),
            'done': len(done_ids),
            'missing': missing,
            'duplicates': {k: v for k, v in dups.items()},
        }
        print(f'=== {key} (课程{COURSES[key]}) ===')
        print(f'  total={len(arts)}  done={len(done_ids)}  missing={len(missing)}  duplicates={len(dups)}')
        if missing:
            print('  MISSING(' + str(len(missing)) + '): ' + ', '.join(missing))
        if dups:
            print('  DUP:')
            for k, v in dups.items():
                sizes = {p: (tdir / p).stat().st_size for p in v}
                print(f'    {k}: ' + ', '.join(f'{p}({sizes[p]}B)' for p in v))

        if fix_dups and dups:
            print('  --fix-dups: 保留最大文件，删除其余')
            for aid, names in dups.items():
                paths = [(tdir / n) for n in names]
                paths.sort(key=lambda p: p.stat().st_size, reverse=True)
                keep = paths[0]
                for p in paths[1:]:
                    print(f'    DEL {p.name} ({p.stat().st_size}B)  <- keep {keep.name} ({keep.stat().st_size}B)')
                    p.unlink()
            # 重新统计
            remain = [p.name for p in (tdir.glob('*.md')) if not p.name.startswith('_')]
            print(f'    after dedup: {len(remain)} files for {key}')

        if chunks:
            print(f'  CHUNK PLAN (size={chunks}):')
            for ci in range(0, len(missing), chunks):
                chunk = missing[ci:ci + chunks]
                print(f'    chunk {ci // chunks}: ' + ', '.join(chunk))

    out = ROOT / 'work' / 'target' / '_COVERAGE_ALL.json'
    json.dump(report, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f'\nwrote {out}')


if __name__ == '__main__':
    main()
