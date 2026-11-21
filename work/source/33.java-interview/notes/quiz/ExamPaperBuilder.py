# -*- coding: utf-8 -*-
"""模拟卷构建器：从 11 个域的 quiz-bank.md 确定性抽样，生成 10 套 100 分制笔试模拟卷。
用法: python ExamPaperBuilder.py  （在 notes/quiz 下运行）
每卷: 单选正向 15×2分 + 单选反向 5×2分 + 判断 15×2分 + 填空 5×2分 + 简答 5×4分 = 45 题 100 分
题目在前，答案与解析统一附卷尾。固定随机种子，可重复生成。
"""
import re, os, random

random.seed(20261117)
DOMAINS = ['java-basics','concurrency','jvm','spring','mysql','redis','mongodb','mq','distributed','ai','algorithm','java-ai','agent-dev']
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, 'exams')
os.makedirs(OUT, exist_ok=True)

HEAD_RE = re.compile(r'^\*\*Q[\w\-]+（(单选·正向|单选·反向|判断|填空|简答)')

def parse_bank(path):
    """返回 [(kind, 题干行, 答案行)]，kind ∈ 单选·正向/单选·反向/判断/填空/简答"""
    text = open(path, encoding='utf-8').read()
    blocks = re.split(r'\n(?=\*\*Q[\w\-]+（)', text)
    result = []
    for b in blocks:
        if not b.startswith('**Q'):
            continue
        m = HEAD_RE.match(b)
        if not m:
            continue
        lines = b.strip().split('\n')
        cut = None
        for i, l in enumerate(lines):
            if l.startswith('**答案：') or l.startswith('**要点（标准答案）**'):
                cut = i
                break
        if cut is None:
            continue
        qlines = [l for l in lines[:cut] if not l.startswith('**来源：')]
        alines = [l for l in lines[cut:] if not l.startswith('**来源：')]
        result.append((m.group(1), qlines, alines))
    return result

pools = {}
for d in DOMAINS:
    qs = parse_bank(os.path.join(BASE, 'out', d, 'quiz-bank.md'))
    random.shuffle(qs)
    pools[d] = qs
    print(f'{d}: {len(qs)} 题入池')

def take(kind_key, n, cursor):
    """按域轮转均匀抽题；kind_key ∈ 单选正向/单选反向/判断/填空/简答"""
    picked, guard = [], 0
    while len(picked) < n:
        guard += 1
        if guard > 5000:
            raise RuntimeError(f'抽题死循环保护触发: {kind_key} 只取到 {len(picked)}')
        d = DOMAINS[cursor['i'] % len(DOMAINS)]
        cursor['i'] += 1
        for j, (k, q, a) in enumerate(pools[d]):
            kk = '单选正向' if k == '单选·正向' else '单选反向' if k == '单选·反向' else k
            if kk == kind_key:
                picked.append((k, q, a, d))
                pools[d].pop(j)
                break
    return picked

SEC_TITLE = {'单选·正向': '单项选择', '单选·反向': '单项选择（选错误项）',
             '判断': '判断题', '填空': '填空题', '简答': '简答题'}
PLAN = [('单选正向', '单选·正向', 15, 2), ('单选反向', '单选·反向', 5, 2),
        ('判断', '判断', 15, 2), ('填空', '填空', 5, 2), ('简答', '简答', 5, 4)]

for p in range(1, 11):
    cursor = {'i': p}
    body, answers = [], []
    sec_no, total_q, total_score = 0, 0, 0
    for key, kind, n, score in PLAN:
        items = take(key, n, cursor)
        sec_no += 1
        body.append(f'\n## {"一二三四五"[sec_no-1]}、{SEC_TITLE[kind]}（{n} 题 × {score} 分）\n')
        for idx, (k, q, a, d) in enumerate(items, 1):
            stem = re.sub(r'^\*\*Q[\w\-]+（[^）]+）\*\* ', '', '\n'.join(q))
            body.append(f'**{sec_no}.{idx}** {stem}\n')
            answers.append(f'**{sec_no}.{idx}**（来源 {d}）\n' + '\n'.join(a) + '\n')
            total_q += 1
            total_score += score
    header = (f'# 笔试模拟卷 {p:02d}\n\n'
              f'> 总分 {total_score} 分｜建议时长 90 分钟｜共 {total_q} 题\n'
              f'> 结构：单选 20×2 + 判断 15×2 + 填空 5×2 + 简答 5×4\n'
              f'> 11 域轮转抽样（Java 基础/并发/JVM/Spring/MySQL/Redis/MongoDB/MQ/分布式/AI/算法）\n\n---\n')
    answer_sec = '\n\n# 参考答案与解析（自测后再看）\n\n' + '\n'.join(answers)
    path = os.path.join(OUT, f'笔试模拟卷-{p:02d}.md')
    open(path, 'w', encoding='utf-8').write(header + '\n'.join(body) + answer_sec)
    print(f'卷 {p:02d}: {total_q} 题 {total_score} 分 → {path}')

idx = ['# 笔试模拟卷索引\n\n> 由 6145 题生成题库确定性抽样（seed=20261117）切成 10 套 100 分制试卷，\n'
       '> 题目在前、答案统一附卷尾。做完按"来源域名"回 notes/quiz/out/<域名>/quiz-bank.md 溯源。\n\n']
for p in range(1, 11):
    idx.append(f'- [笔试模拟卷-{p:02d}](笔试模拟卷-{p:02d}.md)（45 题 100 分）\n')
open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8').write('\n'.join(idx))
print('索引完成')
