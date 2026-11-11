#!/usr/bin/env python3
# fetch_official.py — 从 leetcode.cn 官方 GraphQL 拉取真题面（描述 HTML + 提示）
# 输出 _meta/official_meta.json: {lcnum: {title, content, hints}}
# 用途：gen_blog 第 1 节以官方为准（与官方零出入），示例图片随博客落盘
import json, os, re, subprocess, time

DSA = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa"
OUT = f"{DSA}/_meta/official_meta.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

QUERY = ('query q($titleSlug: String!) { question(titleSlug: $titleSlug) '
         '{ translatedTitle translatedContent hints difficulty } }')


def gql(slug):
    payload = json.dumps({"query": QUERY, "variables": {"titleSlug": slug}})
    for attempt in range(3):
        r = subprocess.run(["curl", "-s", "-m", "15", "-X", "POST",
                            "https://leetcode.cn/graphql",
                            "-H", "Content-Type: application/json",
                            "-H", f"Referer: https://leetcode.cn/problems/{slug}/",
                            "-H", f"User-Agent: {UA}",
                            "-d", payload], capture_output=True, text=True)
        try:
            d = json.loads(r.stdout)
            q = (d.get("data") or {}).get("question")
            if q:
                return q
        except Exception:
            pass
        time.sleep(1.2 * (attempt + 1))
    return None


def main():
    slugmap = json.load(open(f"{DSA}/_meta/lc_slugmap.json"))
    cur = json.load(open(f"{DSA}/_meta/curriculum.json"))
    meta = json.load(open(OUT)) if os.path.exists(OUT) else {}
    todo = []
    for c in cur:
        m = re.match(r"lc_(\d+)_", c["problem"])
        if m and m.group(1) in slugmap:
            todo.append((m.group(1), slugmap[m.group(1)]))
    print(f"待拉取 {len(todo)} 题（已有 {len(meta)}）")
    ok = fail = 0
    for i, (lcnum, slug) in enumerate(todo, 1):
        if lcnum in meta:
            continue
        q = gql(slug)
        if q:
            meta[lcnum] = {"title": q.get("translatedTitle"),
                           "content": q.get("translatedContent") or "",
                           "hints": q.get("hints") or [],
                           "slug": slug}
            ok += 1
        else:
            fail += 1
            print(f"  FAIL {lcnum} {slug}")
        if i % 25 == 0:
            json.dump(meta, open(OUT, "w"), ensure_ascii=False)
            print(f"  进度 {i}/{len(todo)}（ok {ok} fail {fail}）")
        time.sleep(0.35)
    json.dump(meta, open(OUT, "w"), ensure_ascii=False)
    n_img = sum(1 for v in meta.values() if "pic.leetcode" in v["content"])
    print(f"完成：成功 {ok} 失败 {fail}，总计 {len(meta)} 题，含图 {n_img} 题")


if __name__ == "__main__":
    main()
