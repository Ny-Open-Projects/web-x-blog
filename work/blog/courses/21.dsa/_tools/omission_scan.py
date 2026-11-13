#!/usr/bin/env python3
# omission_scan.py — 原文优秀思路/备注遗漏检测
# 对每篇爬取文章：定位题目章节（多题文按 LeetCode 标题切分），提取散文段落，
# 与对应博客 index.md 归一比对；无重叠的关键字段落 = 疑似遗漏。
# 输出 _meta/omission_scan.json
import glob, html, json, os, re

DSA = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa"
KEY = re.compile(r'思路|分析|注意|解释|说明|复杂度|优化|为什么|要点|坑|技巧|边界|推导|证明|核心|本质|关键')

def article_text(path):
    h = open(path, encoding='utf-8', errors='ignore').read()
    m = re.search(r'<div[^>]*id="content_views"[^>]*>(.*)', h, re.S)
    body = m.group(1) if m else ''
    for mk in ['id="blogColumnPayAdvert"', 'class="hide-article-box', 'id="treeSkill',
               'class="recommend', 'id="recommend', '相关文章', '相关推荐']:
        j = body.find(mk)
        if j > 0:
            body = body[:j]
    t = re.sub(r'<script.*?</script>|<style.*?</style>', '', body, flags=re.S)
    t = re.sub(r'<br\s*/?>', '\n', t)
    t = re.sub(r'</(p|div|h\d|li|pre|ul|ol)>', '\n', t)
    t = re.sub(r'<[^>]+>', '', t)
    import html as H
    t = H.unescape(t).replace('\u00a0', ' ')
    return re.sub(r'\n[ \t]*\n+', '\n', t).strip()

def norm(s):
    return re.sub(r'[\s,，。;；:：、\u4e00-\u9fff]*', lambda m: '' if re.match(r'[\s,，。;；:：、]', m.group(0)) else m.group(0), s) if False else re.sub(r'[\s，。；：、,.:;]+', '', s)

def problem_sections(txt, title_lc):
    """文章切分：正文有 LeetCode 标记时按标记切多题；否则整篇归 title_lc。"""
    lines = txt.split('\n')
    marks = []
    for i, ln in enumerate(lines):
        m = re.search(r'LeetCode\s*(\d+)', ln)
        if m:
            marks.append((i, int(m.group(1))))
    if not marks:
        return {int(title_lc): lines} if title_lc else {}
    secs = {}
    for k, (i, num) in enumerate(marks):
        end = marks[k + 1][0] if k + 1 < len(marks) else len(lines)
        secs.setdefault(num, []).extend(lines[i:end])
    # 标题题号的章节若正文标记未覆盖（正文无标记的整篇），并入
    if title_lc and int(title_lc) not in secs:
        secs[int(title_lc)] = lines
    return secs

def prose_paras(lines):
    out, buf = [], []
    for ln in lines:
        s = ln.strip()
        if not s:
            if buf:
                p = ' '.join(buf)
                if len(p) >= 30 and KEY.search(p) and not re.match(r'^\d+\s*\)', p):
                    out.append(p)
                buf = []
            continue
        if re.match(r'^(function|class|def|func|public|import|package|const|var|let|#include|fn |use )', s):
            if buf:
                buf = []
            continue
        if re.search(r'[{};]\s*$', s):
            buf = []
            continue
        buf.append(s)
    if buf:
        p = ' '.join(buf)
        if len(p) >= 30 and KEY.search(p):
            out.append(p)
    return out


def main():
    all_urls = {}
    for ln in open(f'{DSA}/_meta/all_urls.tsv').read().strip().split('\n')[1:]:
        f = ln.split('\t')
        if len(f) >= 3:
            all_urls[f[0]] = f[1]
    # 博客 lc 号 → 博客文本
    blog_by_lc = {}
    cur = json.load(open(f'{DSA}/_meta/curriculum.json'))
    for c in cur:
        m = re.match(r'lc_(\d+)_', c['problem'])
        if m:
            f = glob.glob(f'{DSA}/{c["blog_id"]}_*/index.md')
            if f:
                blog_by_lc[m.group(1)] = open(f[0], encoding='utf-8').read()
    report = {}
    for aid_html in sorted(os.listdir(f'{DSA}/_meta/articles')):
        aid = aid_html.replace('.html', '')
        title_lc = None
        mt = re.search(r'LeetCode\s*(\d+)', all_urls.get(aid, ''))
        if mt:
            title_lc = mt.group(1)
        txt = article_text(f'{DSA}/_meta/articles/{aid_html}')
        secs = problem_sections(txt, title_lc)
        for lcnum, lines in secs.items():
            blog = blog_by_lc.get(str(lcnum))
            if not blog:
                continue
            bn = norm(blog)
            missed = []
            for p in prose_paras(lines):
                pn = norm(p)
                # 取段落中每个 12 字滑窗，看是否在博客中出现
                frags = [pn[i:i + 12] for i in range(0, max(1, len(pn) - 11), 6)]
                hit = sum(1 for fr in frags if fr and fr in bn)
                ratio = hit / max(1, len(frags))
                if ratio < 0.34:
                    missed.append((round(ratio, 2), p[:160]))
            if missed:
                key = f'lc_{lcnum}'
                prev = report.get(key, {'aid': [], 'missed': []})
                prev['aid'].append(aid)
                prev['missed'].extend(missed)
                report[key] = prev
    # 只保留疑似遗漏 ≥2 段的
    report = {k: v for k, v in report.items() if len(v['missed']) >= 2}
    json.dump(report, open(f'{DSA}/_meta/omission_scan.json', 'w'), ensure_ascii=False, indent=1)
    print(f"疑似遗漏题数: {len(report)}")
    for k, v in sorted(report.items(), key=lambda x: -len(x[1]['missed']))[:12]:
        print(f"  {k}: 疑似遗漏 {len(v['missed'])} 段 (aid {v['aid']})")
        print("     例:", v['missed'][0][1][:90])


if __name__ == '__main__':
    main()
