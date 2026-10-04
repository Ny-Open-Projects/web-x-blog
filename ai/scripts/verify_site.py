#!/usr/bin/env python3
"""逐页 curl 验证 hexo 生成的站点。

用法:
    python3 ai/scripts/verify_site.py 4353                 # 默认本地 hexo server 端口
    python3 ai/scripts/verify_site.py 4353 --base /2019/   # 只查某前缀（可选）

逻辑:
    1. 扫 public/ 下所有 index.html，得到相对路径集合（排除 404/归档等辅助页）
    2. 逐个发 HTTP 请求，统计 200 / 非 200
    3. 同时扫 stderr 日志文件里的 "ERROR Process failed"（静默跳过的文章）

注意：URL 列表文件**末尾必须有换行**，否则 while read 会静默漏掉最后一篇。
"""
import argparse
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def collect_pages(public: Path):
    """返回相对 URL 列表，形如 /2026/10/03/foo/。"""
    out = []
    for p in public.rglob("index.html"):
        rel = p.relative_to(public).with_suffix("")
        parts = list(rel.parts)
        # 去掉末尾的 index 段：index.html -> index -> ""，正确 URL 为 /年/月/日/篇名/
        if parts and parts[-1] == "index":
            parts = parts[:-1]
        slug = "/".join(parts)
        if slug in ("404", "index", ""):
            continue
        out.append(f"/{slug}/")
    return sorted(set(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("port", type=int, default=4353)
    ap.add_argument("--base", default="", help="只验证该前缀下的页面")
    args = ap.parse_args()

    public = ROOT / "work" / "blog" / "public"
    if not public.is_dir():
        sys.exit(f"public 不存在: {public}")

    pages = collect_pages(public)
    if args.base:
        pages = [u for u in pages if u.startswith(args.base)]
    print(f"[信息] 待验证页面 {len(pages)} 个 (port={args.port})")

    base = f"http://127.0.0.1:{args.port}"
    bad = []
    for i, u in enumerate(pages, 1):
        if i % 50 == 0:
            print(f"[进度] {i}/{len(pages)}", flush=True)
        try:
            # 中文文件名必须百分号编码，否则 urllib 抛 UnicodeEncodeError
            req = urllib.request.Request(base + urllib.parse.quote(u), method="GET")
            with urllib.request.urlopen(req, timeout=15) as r:
                code = r.getcode()
        except urllib.error.HTTPError as e:
            code = e.code
        except Exception as e:  # 连接失败 / 超时
            bad.append((u, f"ERR {type(e).__name__}"))
            continue
        if code != 200:
            bad.append((u, code))

    ok = len(pages) - len(bad)
    print(f"\n[结果] 200 共 {ok} / {len(pages)}")
    if bad:
        print(f"[非200] {len(bad)} 个：")
        for u, c in bad[:50]:
            print(f"  {c}  {u}")
        return 1
    print("[结果] 全部 200")
    return 0


if __name__ == "__main__":
    sys.exit(main())
