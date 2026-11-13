#!/usr/bin/env python3
# parse_official.py — leetcode.cn 官方 HTML → 结构化题面 + 示例图片落盘
# 输出 _meta/official_parsed.json: {lcnum: {desc[], examples[], hints[], images[]}}
# 图片下载到 _meta/lc_imgs/{lcnum}/，gen_blog 复制进博客目录引用
import json, os, re, subprocess, html as H

DSA = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
IMGDIR = f"{DSA}/_meta/lc_imgs"


def inline_to_md(s):
    s = re.sub(r"<code>(.*?)</code>", r"`\1`", s, flags=re.S)
    s = re.sub(r"<(strong|em|b|i)[^>]*>", "", s)
    s = re.sub(r"</(strong|em|b|i)>", "", s)
    s = re.sub(r"<sup>(.*?)</sup>", r"^\1", s, flags=re.S)
    s = re.sub(r"<sub>(.*?)</sub>", r"_\1", s, flags=re.S)
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = H.unescape(s).replace("\u00a0", " ")
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip()


def strip_bold(s):
    return H.unescape(s).replace("\u00a0", " ")


def parse_content(h):
    """官方 translatedContent → desc / examples / hints（保持图片位置）。"""
    out = {"desc": [], "examples": [], "hints": [], "images": []}
    h = re.sub(r"<p>\s*(?:&nbsp;|\u00a0)?\s*</p>", "\n\x00SEP\x00\n", h)
    # 示例分段：class="example" 或普通 strong 均适配
    marks = list(re.finditer(r'<p><strong[^>]*>\s*(示例\s*\d+|说明)[^<]*：</strong></p>', h))
    if not marks:
        marks = list(re.finditer(r'<p><strong[^>]*>\s*(示例\s*\d+)[：:]?</strong></p>', h))
    desc_html = h[:marks[0].start()] if marks else h
    for para in re.split(r"\x00SEP\x00", desc_html):
        t = inline_to_md(para)
        t = re.sub(r"^（?\s*进阶\s*）?[:：]\s*", "", t)
        if t and not re.match(r"^(提示|说明)[：:]?$", t):
            out["desc"].append(t)
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(h)
        seg = h[m.end():end]
        ex = {"head": m.group(1), "imgs": [], "body": "", "note": ""}
        im = re.search(r'<img[^>]*src="([^"]+)"[^>]*>', seg)
        if im:
            alt = re.search(r'alt="([^"]*)"', im.group(0))
            ex["imgs"].append({"url": im.group(1), "alt": alt.group(1) if alt else ""})
        pre = re.search(r"<pre>(.*?)</pre>", seg, re.S)
        if pre:
            raw = re.sub(r"<[^>]+>", "", pre.group(1))
            raw = H.unescape(raw).replace("\u00a0", " ").strip("\n")
            # 拆 解释 说明 出围栏
            lines = raw.split("\n")
            body, note = [], []
            tgt = body
            for ln in lines:
                ls = ln.strip()
                if re.match(r"^(解释|说明)[:：]", ls):
                    tgt = note
                    tgt.append(re.sub(r"^(解释|说明)[:：]\s*", "", ls))
                    continue
                tgt.append(ln.replace("**", ""))
            ex["body"] = "\n".join(body).strip()
            ex["note"] = " ".join(x.strip() for x in note if x.strip())
        out["examples"].append(ex)
    # 提示
    hm = re.search(r'<p><strong[^>]*>\s*提示[:：]?\s*</strong></p>(.*)$', h, re.S)
    if hm:
        for li in re.findall(r"<li>(.*?)</li>", hm.group(1), re.S):
            t = inline_to_md(li)
            if t:
                out["hints"].append(t)
    # 尾部「进阶：」段落并入 hints
    am = re.search(r'<p><strong[^>]*>\s*进阶\s*[:：]\s*</strong>(.*?)</p>', h, re.S)
    if am:
        t = inline_to_md(am.group(1))
        if t:
            out["hints"].append("进阶：" + t)
    return out


def dl(url, path):
    if os.path.exists(path):
        return True
    r = subprocess.run(["curl", "-s", "-m", "20", "-L", url, "-o", path,
                        "-H", "User-Agent: Mozilla/5.0", "-H", "Referer: https://leetcode.cn/"])
    return os.path.exists(path) and os.path.getsize(path) > 500


def main():
    meta = json.load(open(f"{DSA}/_meta/official_meta.json"))
    parsed = {}
    n_img = 0
    for lcnum, v in sorted(meta.items(), key=lambda x: int(x[0])):
        r = parse_content(v["content"])
        # 图片落盘
        for k, ex in enumerate(r["examples"]):
            for j, img in enumerate(ex["imgs"]):
                ext = ".png"
                d = f"{IMGDIR}/{lcnum}"
                os.makedirs(d, exist_ok=True)
                local = f"{k+1}_{j+1}{ext}"
                if dl(img["url"], f"{d}/{local}"):
                    img["local"] = local
                    n_img += 1
                else:
                    img["local"] = ""
        r["slug"] = v.get("slug", "")
        parsed[lcnum] = r
    json.dump(parsed, open(f"{DSA}/_meta/official_parsed.json", "w"), ensure_ascii=False, indent=1)
    n_d = sum(1 for v in parsed.values() if v["desc"])
    n_e = sum(1 for v in parsed.values() if v["examples"])
    n_h = sum(1 for v in parsed.values() if v["hints"])
    print(f"解析 {len(parsed)} 题：desc {n_d} / examples {n_e} / hints {n_h}，图片落盘 {n_img}")


if __name__ == "__main__":
    main()
