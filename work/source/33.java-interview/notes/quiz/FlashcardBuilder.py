# -*- coding: utf-8 -*-
"""闪卡构建器：11 域知识点事实矩阵 → 背诵闪卡。
输出：
  1. notes/quiz/flashcards.md        —— Markdown 闪卡（按域分组，正面/背面）
  2. notes/quiz/exams/anki-cards.csv —— Anki 可导入 CSV（Tab 分隔，UTF-8 BOM）
卡片结构：正面 = 域｜topic｜term（提问式）；背面 = 事实 + 原理 + 用法要点 + 版本锚点。
用法: python FlashcardBuilder.py
"""
import os

DOMAINS = ['java-basics','concurrency','jvm','spring','mysql','redis','mongodb','mq','distributed','ai','algorithm','java-ai','agent-dev']
DOM_NAME = {'java-basics':'Java 基础','concurrency':'并发','jvm':'JVM','spring':'Spring','mysql':'MySQL',
            'redis':'Redis','mongodb':'MongoDB','mq':'MQ','distributed':'分布式','ai':'AI/Agent','algorithm':'算法','java-ai':'Java AI 框架','agent-dev':'Agent 开发'}
BASE = os.path.dirname(os.path.abspath(__file__))

cards = []
for d in DOMAINS:
    path = os.path.join(BASE, 'facts', f'{d}.txt')
    for line in open(path, encoding='utf-8'):
        t = line.strip()
        if not t or t.startswith('#') or len(t.split('|')) != 12:
            continue
        f = t.split('|')
        rid, topic, dim, term = f[0], f[2].strip(), f[3].strip(), f[4].strip()
        fact, why, usage, ver = f[5].strip(), f[6].strip(), f[10].strip(), f[11].strip()
        front = f'{topic} · {term if term else dim}（{dim}）'
        back_parts = [fact, f'原理：{why}']
        if usage:
            back_parts.append(f'用法：{usage}')
        if ver:
            back_parts.append(f'锚点：{ver}')
        cards.append({'id': rid, 'dom': d, 'domName': DOM_NAME[d],
                      'front': front, 'back': '\n'.join(back_parts)})
print(f'闪卡: {len(cards)} 张')

# Markdown 版（按域分组）
md = [f'# 闪卡全量版（{len(cards)} 张 · 11 域）\n',
      '> 背法：遮住背面看正面自问 → 展开对照。正面格式「topic · term（维度）」，背面四件套：事实/原理/用法/锚点。\n']
cur = None
for c in cards:
    if c['dom'] != cur:
        cur = c['dom']
        md.append(f'\n## {c["domName"]}（{sum(1 for x in cards if x["dom"]==cur)} 张）\n')
    md.append(f'### {c["front"]}\n')
    md.append(f'<details><summary>看背面</summary>\n\n{c["back"]}\n\n</details>\n')
open(os.path.join(BASE, 'flashcards.md'), 'w', encoding='utf-8').write('\n'.join(md))

# Anki CSV（Tab 分隔 + BOM）
import codecs
csv_path = os.path.join(BASE, 'exams', 'anki-cards.csv')
with codecs.open(csv_path, 'w', 'utf-8-sig') as fh:
    fh.write('#separator:tab\n#html:false\n')
    for c in cards:
        front = c['front'].replace('\t', ' ').replace('\n', ' ')
        back = c['back'].replace('\t', ' ').replace('\n', '<br>')
        fh.write(f'{c["id"]} {front}\t{back}\n')
print(f'输出: flashcards.md + exams/anki-cards.csv')
