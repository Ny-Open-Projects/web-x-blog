# -*- coding: utf-8 -*-
"""面试模拟问答卷构建器：从 11 个域的 interview-bank.md 确定性抽样，生成 10 套口述自测卷。
用法: python InterviewPaperBuilder.py  （在 notes/quiz 下运行）
每卷 20 题：概念考察 6 + 误用纠错 4 + 原理深挖 4 + 工程落地 3 + 版本演进 3
题目（面试官问法）在前；【标准回答话术】+【评分点】统一附卷尾；按评分点 0/1/2 三档自评，满分 40。
"""
import re, os, random

random.seed(20261118)
DOMAINS = ['java-basics','concurrency','jvm','spring','mysql','redis','mongodb','mq','distributed','ai','algorithm','java-ai','agent-dev']
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, 'exams')
os.makedirs(OUT, exist_ok=True)

HEAD_RE = re.compile(r'^\*\*Q[\w\-]+（(概念考察|误用纠错|原理深挖|工程落地|版本演进)·(P[\d\-P]+)）\*\*')

def parse_bank(path):
    """返回 [(kind,plevel, 问题行, 答案行)]"""
    text = open(path, encoding='utf-8').read()
    blocks = re.split(r'\n(?=\*\*Q[\w\-]+（)', text)
    result = []
    for b in blocks:
        if not b.startswith('**Q'):
            continue
        m = HEAD_RE.match(b)
        if not m:
            continue
        kind, plevel = m.group(1), m.group(2)
        lines = b.strip().split('\n')
        cut = None
        for i, l in enumerate(lines):
            if l.startswith('【标准回答话术】'):
                cut = i
                break
        if cut is None:
            continue
        qlines = [l for l in lines[:cut] if l.startswith('【面试官】')]
        alines = lines[cut:]
        if not qlines:
            continue
        result.append((kind, plevel, qlines[0], alines))
    return result

pools = {}
for d in DOMAINS:
    qs = parse_bank(os.path.join(BASE, 'out', d, 'interview-bank.md'))
    random.shuffle(qs)
    pools[d] = qs
    print(f'{d}: {len(qs)} 题入池')

def take(kind_key, n, cursor):
    picked, guard = [], 0
    while len(picked) < n:
        guard += 1
        if guard > 5000:
            raise RuntimeError(f'抽题死循环保护触发: {kind_key} 只取到 {len(picked)}')
        d = DOMAINS[cursor['i'] % len(DOMAINS)]
        cursor['i'] += 1
        for j, (k, pl, q, a) in enumerate(pools[d]):
            if k == kind_key:
                picked.append((k, pl, q, a, d))
                pools[d].pop(j)
                break
    return picked

PLAN = [('概念考察', 6), ('误用纠错', 4), ('原理深挖', 4), ('工程落地', 3), ('版本演进', 3)]

for p in range(1, 11):
    cursor = {'i': p}
    body, answers = [], []
    no, total = 0, 0
    for key, n in PLAN:
        items = take(key, n, cursor)
        for (k, pl, q, a, d) in items:
            no += 1
            body.append(f'**第 {no} 题**（{k} · {pl}）\n{q}\n（口述作答后翻卷尾对照）\n')
            answers.append(f'**第 {no} 题**（{k} · {pl} · 来源 {d}）\n' + '\n'.join(a) + '\n自评分（0 未答中 / 1 部分完整 / 2 评分点全中）：____\n')
            total += 1
    header = (f'# 面试模拟问答卷 {p:02d}\n\n'
              f'> 口述自测：每题先自己完整回答（出声、像面试现场），再翻卷尾对照【标准回答话术】，\n'
              f'> 按【评分点】自评 0/1/2，满分 {total*2} 分（{total} 题 × 2）。\n'
              f'> 结构：概念考察 6 + 误用纠错 4 + 原理深挖 4 + 工程落地 3 + 版本演进 3（P1-P10 混合）\n\n---\n')
    answer_sec = '\n\n# 标准回答话术与评分点（口述后再看）\n\n' + '\n'.join(answers)
    path = os.path.join(OUT, f'面试模拟问答卷-{p:02d}.md')
    open(path, 'w', encoding='utf-8').write(header + '\n'.join(body) + answer_sec)
    print(f'面试卷 {p:02d}: {total} 题 → {path}')

idx = open(os.path.join(OUT, 'README.md'), encoding='utf-8').read()
idx += ('\n\n# 面试模拟问答卷索引\n\n> 从 5230 道面试题确定性抽样（seed=20261118）切 10 套口述自测卷，\n'
        '> 每卷 20 题 × 2 分自评。做完按来源域名回 notes/quiz/out/<域名>/interview-bank.md 溯源。\n\n')
for p in range(1, 11):
    idx += f'- [面试模拟问答卷-{p:02d}](面试模拟问答卷-{p:02d}.md)（20 题口述自测）\n'
open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8').write(idx)
print('索引追加完成')
