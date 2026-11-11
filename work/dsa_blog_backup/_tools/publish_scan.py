#!/usr/bin/env python3
# publish_scan.py — 出版编辑视角规范扫描（GB/T 15834 标点 / GB/T 15835 数字用法 / 异形词 / 术语一致性）
# 仅审正文：代码围栏跳过、行内代码以等长空格掩码；官方函数签名占位 [..] 不计
# 输出 _meta/publish_scan.json
import glob, json, re
from collections import Counter

DSA = "/Users/Wang/Code/webfault-ai/dsa"
CJK = r'[\u4e00-\u9fff]'

# 高置信异形词/错别字（出版规范方向）
TYPO = {
    '做为': '作为', '其它': '其他', '连表': '链表', '既使': '即使',
    '按装': '安装', '帐号': '账号', '帐户': '账户', '必需要': '必须',
    '一翻功夫': '一番功夫', '急待': '亟待', '考问': '拷问',
}


def mask_inline(ln):
    """行内代码以等长空格掩码（保位不误判）。"""
    return re.sub(r'`[^`]*`', lambda m: ' ' * len(m.group(0)), ln)


def scan_file(f):
    t = open(f, encoding='utf-8').read()
    lines = t.split('\n')
    findings = []
    in_code = False
    for i, raw in enumerate(lines):
        if raw.strip().startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        ln = mask_inline(raw)
        loc = f"L{i+1}"

        # P1 中文语境省略号（…… 之外的三点形态；排除 [..] 占位）
        for m in re.finditer(r'(?<![A-Za-z0-9_\)\]\.])(\.{3,})(?!\.|\w|/)', ln):
            ctx = ln[max(0, m.start() - 3):m.start() + 4]
            if '[' in ctx or '../' in ctx:
                continue  # 官方签名占位符 / 相对路径
            findings.append(('P1-省略号', loc, ln.strip()[:70]))
            break
        # 。。。 形态
        if '。。。' in ln:
            findings.append(('P1-省略号', loc, '。。。'))

        # P2 单破折号
        if re.search(r'(^|' + CJK + r'|\s)—(?!—)(' + CJK + r'|\s|$)', ln):
            findings.append(('P2-单破折号', loc, ln.strip()[:70]))

        # P3 半角标点混排（两侧/前侧为 CJK）
        if re.search(r'(' + CJK + r')\s*[,;]\s*(' + CJK + r')', ln) or \
           re.search(r'(' + CJK + r')\s*[:!?]\s*($|' + CJK + r')', ln):
            findings.append(('P3-半角标点', loc, ln.strip()[:70]))

        # P4 全角字母数字
        if re.search(r'[Ａ-Ｚａ-ｚ０-９]', ln):
            findings.append(('P4-全角字符', loc, ln.strip()[:70]))

        # P5 重复虚词
        m = re.search(r'(的的|了了|是是|地地|得得)', ln)
        if m:
            findings.append(('P5-重复虚词', loc, m.group(1)))

        # P6 异形词/错别字
        for bad, good in TYPO.items():
            if bad in ln:
                findings.append(('P6-异形词', loc, f'{bad} → {good}'))

        # P7 标题末尾句号
        if re.match(r'^#{1,6} .*。$', ln):
            findings.append(('P7-标题句号', loc, ln.strip()[:60]))

    # P8 术语一致性（仅正文，剥代码围栏）
    prose_t, ic = [], False
    for raw in lines:
        if raw.strip().startswith('```'):
            ic = not ic; continue
        if not ic:
            prose_t.append(raw)
    pt = '\n'.join(prose_t)
    terms = {}
    for a, b in (('哈希', '散列'), ('数组', '阵列'), ('队列', '佇列')):
        ca, cb = pt.count(a), pt.count(b)
        if ca > 0 and cb > 0:
            terms[f'{a}/{b}'] = (ca, cb)
    if terms:
        findings.append(('P8-术语一致性', '-', json.dumps(terms, ensure_ascii=False)))
    return findings


def main():
    files = sorted(glob.glob(f'{DSA}/blog/[0-9]*/index.md')) + \
            sorted(glob.glob(f'{DSA}/blog/0?_*二叉树的最大深度/index.md'))
    report = {'scanned': len(set(files)), 'findings': {}}
    counter = Counter()
    for f in sorted(set(files)):
        fs = scan_file(f)
        if fs:
            rel = f.split('blog/')[-1]
            report['findings'][rel] = fs
            for kind, _, _ in fs:
                counter[kind] += 1
    report['summary'] = dict(counter)
    json.dump(report, open(f'{DSA}/_meta/publish_scan.json', 'w'), ensure_ascii=False, indent=1)
    print(f"出版规范扫描 {report['scanned']} 篇：")
    for k, n in counter.most_common():
        print(f"  {n:5d}  {k}")
    if not counter:
        print("  全部符合出版规范")


if __name__ == '__main__':
    main()
