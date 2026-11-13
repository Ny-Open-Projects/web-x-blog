#!/usr/bin/env python3
# extract_problem.py — 从 _meta/articles 的 CSDN 原文提取真题面
# 输出 _meta/problem_meta.json: {lcnum: {title, desc[], examples[], hints[], ts_names[]}}
# 用途：gen_blog 第 1 节真实题面/示例/数据范围，第 2/5 节真实方案名
import json, os, re, html

DSA = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
ART = f"{DSA}/_meta/articles"

LANG_HEAD = re.compile(r"^\s*((TypeScript|Typescript|TS|JavaScript|JS|Python3?|Java|Golang|Go|C\+\+|CPP|C|Rust|PHP|Kotlin|Swift|Dart)\s*版算法|解题思路|思路分析|题解|实现方案|方案实现)")


def clean_mathml(s):
    s = s.strip()
    # KaTeX mathml 是「渲染形 + 源码形」拼接：n2n^2 / 10410^4 / i1i_1
    m = re.match(r"^(.+?)(\d+)\1\^\2$", s)
    if m:
        return f"{m.group(1)}^{m.group(2)}"
    m = re.match(r"^([A-Za-z]+)(\w+)\1_\2$", s)
    if m:
        return f"{m.group(1)}_{m.group(2)}"
    return s


SPAN_RE = re.compile(r"<span\b|</span>")


def _span_end(h, k):
    """从 h[k] 处的一个 <span ...> 开始，返回其闭合 </span> 之后的位置（括号配平扫描）。"""
    depth = 0
    while k < len(h):
        mo = SPAN_RE.search(h, k)
        if not mo:
            return len(h)
        if mo.group(0) == "<span":
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return mo.end()
        k = mo.end()
    return len(h)


def replace_katex(body):
    """每个 KaTeX 内联公式块 → 其 mathml 注释文本（如 10^4），丢掉视觉层避免重复。"""
    out, i = [], 0
    while True:
        j = body.find('<span class="katex--inline">', i)
        if j < 0:
            out.append(body[i:])
            break
        out.append(body[i:j])
        ms = body.find('<span class="katex-mathml">', j)
        hs = body.find('<span class="katex-html">', j)
        if ms >= 0 and (hs < 0 or ms < hs):
            mm = re.match(r'<span class="katex-mathml">(.*?)</span>', body[ms:], re.S)
            mtxt = clean_mathml(re.sub(r"\s+", "", re.sub(r"<[^>]+>", "", mm.group(1)))) if mm else ""
            out.append("\x02" + mtxt + "\x03")
            i = ms + 27
        else:
            i = j + 27
        if hs >= 0:
            i = max(i, _span_end(body, hs))
    return "".join(out)


def article_text(path):
    h = open(path, encoding="utf-8", errors="ignore").read()
    m = re.search(r'<div[^>]*id="content_views"[^>]*>(.*)', h, re.S)
    body = m.group(1) if m else ""
    for marker in ['id="blogColumnPayAdvert"', 'class="hide-article-box', 'id="treeSkill',
                   'class="recommend', 'id="recommend', '相关文章', '相关推荐']:
        j = body.find(marker)
        if j > 0:
            body = body[:j]
    body = replace_katex(body)
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", body, flags=re.S)
    t = re.sub(r"<br\s*/?>", "\n", t)
    t = re.sub(r"</(p|div|h\d|li|pre|ul|ol)>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    t = t.replace("\x02", "").replace("\x03", "")
    t = re.sub(r"[ \t]+", " ", t)
    return re.sub(r"\n[ \t]*\n+", "\n", t).strip()


def clean_name(s):
    s = s.strip().strip("：:").strip()
    s = re.sub(r"^方案\s*\d+\s*[:：]\s*", "", s)
    s = re.sub(r"^算法\s*\d+\s*[:：]\s*", "", s)
    return s.strip()


def bad_name(s):
    return (not s or len(s) > 30 or "。" in s or "版算法" in s or "时间复杂度" in s
            or re.match(r"^(问题描述|分析|题目|注意|提示|示例)", s)
            or re.match(r"^(O\(|\d+$|10\^)", s)
            or re.match(r"^方案\s*\d*$", s))


def parse_article(txt):
    lines = txt.split("\n")
    out = {"desc": [], "examples": [], "hints": [], "ts_names": [], "ts_codes": []}
    # 定位题面锚点
    i_desc = next((i for i, l in enumerate(lines) if l.strip() in ("描述", "题目描述", "问题描述")), None)
    i_ex1 = next((i for i, l in enumerate(lines) if re.match(r"^\s*示例\s*1\b", l.strip())), None)
    i_hint = next((i for i, l in enumerate(lines) if re.match(r"^\s*提示\b", l.strip())), None)
    if i_desc is None and i_ex1 is None:
        return out
    start = (i_desc + 1) if i_desc is not None else 0
    end = i_ex1 if i_ex1 is not None else (i_hint or len(lines))
    out["desc"] = [l.strip() for l in lines[start:end]
                   if l.strip() and not re.match(r"^(https?://|力扣|leetcode\.cn)", l.strip(), re.I)]
    # 示例块
    if i_ex1 is not None:
        seg_end = i_hint if i_hint is not None else len(lines)
        cur = None
        for l in lines[i_ex1:seg_end]:
            s = l.strip()
            if re.match(r"^示例\s*\d+", s):
                if cur:
                    out["examples"].append(cur)
                cur = {"input": "", "output": "", "note": ""}
                continue
            if LANG_HEAD.match(s) or (s.startswith(("方案", "解题", "题解", "思路")) and cur and cur["output"]):
                break
            if cur is None:
                continue
            m = re.match(r"^(输入|输出|解释|说明)\s*[:：]\s*(.*)$", s)
            if m:
                key = {"输入": "input", "输出": "output", "解释": "note", "说明": "note"}[m.group(1)]
                cur[key] = m.group(2).strip()
            elif s and not s.startswith(("示例", "提示")):
                # 续行（解释较长时换行）
                if cur["output"] and not cur["note"]:
                    cur["note"] = s
                elif cur["input"] and not cur["output"]:
                    cur["input"] += s
        if cur and (cur["input"] or cur["output"]):
            out["examples"].append(cur)
    # 提示/数据范围
    if i_hint is not None:
        for l in lines[i_hint + 1:]:
            s = l.strip()
            if LANG_HEAD.match(s) or re.match(r"^\s*\d+\s*[)）]", s) or s.startswith(("方案", "解题", "题解")):
                break
            if s and not s.startswith("提示") and not re.match(r"^-?\d+(\.\d+)?$", s) and s not in out["hints"]:
                out["hints"].append(s)
    # TypeScript 段方案名 + 各方案原文代码（供按代码相似度回配名字）
    i_ts = next((i for i, l in enumerate(lines)
                 if re.match(r"^\s*(TypeScript|Typescript|TS|JavaScript|JS)\s*版算法", l, re.I)), None)
    if i_ts is not None:
        i_next = len(lines)
        for j in range(i_ts + 1, len(lines)):
            if re.match(r"^\s*\S+\s*版算法", lines[j]) and j != i_ts:
                i_next = j
                break
        cur_name, cur_code = None, []
        heads = [(k, clean_name(m.group(1))) for k, l in enumerate(lines[i_ts + 1:i_next], i_ts + 1)
                 if (m := re.match(r"^\s*\d+\s*[)）]\s*(.+)$", l)) and not bad_name(clean_name(m.group(1)))]
        for pos, (k, name) in enumerate(heads):
            end = heads[pos + 1][0] if pos + 1 < len(heads) else i_next
            seg = [l.strip() for l in lines[k + 1:end] if l.strip()]
            out["ts_names"].append(name)
            out["ts_codes"].append("\n".join(seg))
    return out


def main():
    # 文章 id → 标题（用于 LeetCode 号匹配）
    num2arts = {}
    for ln in open(f"{DSA}/_meta/all_urls.tsv").read().strip().split("\n")[1:]:
        f = ln.split("\t")
        if len(f) < 3:
            continue
        m = re.search(r"LeetCode\s*([A-Z]{0,3})\.?\s*(\d+)", f[1], re.I)
        if m:
            num2arts.setdefault(m.group(2), []).append(f[0])

    meta = {}
    for lcnum, aids in sorted(num2arts.items(), key=lambda x: int(x[0])):
        best = None
        for aid in aids:
            p = f"{ART}/{aid}.html"
            if not os.path.exists(p):
                continue
            r = parse_article(article_text(p))
            score = (len(r["desc"]) > 0) + (len(r["examples"]) > 0) + (len(r["hints"]) > 0) + (len(r["ts_names"]) > 0)
            if score >= 2 and (best is None or score > best[0]):
                best = (score, r)
        if best:
            meta[lcnum] = best[1]

    with open(f"{DSA}/_meta/problem_meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    n_d = sum(1 for v in meta.values() if v["desc"])
    n_e = sum(1 for v in meta.values() if v["examples"])
    n_h = sum(1 for v in meta.values() if v["hints"])
    n_n = sum(1 for v in meta.values() if v["ts_names"])
    print(f"共 {len(meta)} 题有元数据：desc {n_d} / examples {n_e} / hints {n_h} / ts_names {n_n}")


if __name__ == "__main__":
    main()
