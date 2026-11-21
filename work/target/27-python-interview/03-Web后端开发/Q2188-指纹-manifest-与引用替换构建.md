---
title: [Q2188] 指纹 manifest 与引用替换构建
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2188 · 指纹 manifest 与引用替换构建

> 难度:★★★☆ | 标签:部署, 构建

**问**:指纹文件有了,页面里的引用怎么改?manifest 文件本身要注意什么?

**答**:构建流水线做三件事:先对产物算指纹并生成 manifest(原始名到指纹名的映射);再在构建期把 HTML、CSS、JS 里对静态资源的引用统一替换成指纹名——替换必须发生在构建期而不是请求期,请求期正则替换既慢又容易漏;manifest 以原子方式落盘(写临时文件后 rename),服务端要么读到旧表要么读到新表,绝不会读到写一半的表。正确性断言是"替换后不得残留任何原始引用",残留即 404 风险。发布顺序上,先上指纹产物(新文件名不冲突),再上引用它们的 HTML,回滚时反向操作,manifest 的双版本共存窗口就是这个用途。

```python
# file: code/03_Web后端开发/q2188_asset_manifest.py
"""指纹 manifest 与引用替换: 构建期改写 HTML 与原子落盘(纯标准库)。"""
import json
import os

MANIFEST = {"app.js": "app.a1b2c3d4e5f6.js", "style.css": "style.9f8e7d6c5b4a.css"}
HTML = ('<html>\n  <link rel="stylesheet" href="/static/style.css">\n'
        '  <script src="/static/app.js"></script>\n</html>')


def rewrite(html, manifest, base="/static/"):
    out = html
    for src, fingerprinted in manifest.items():
        out = out.replace(base + src, base + fingerprinted)
    leftovers = [src for src in manifest if base + src in out]
    return out, leftovers


def write_manifest(path, manifest):
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(manifest, fh, indent=2)
    os.replace(tmp, path)                       # 原子替换, 读侧永不看到半张表


new_html, leftovers = rewrite(HTML, MANIFEST)
print(new_html)
assert leftovers == []                          # 所有引用都被替换, 残留即 404 风险
write_manifest("/tmp/q2188_manifest.json", MANIFEST)
lines = open("/tmp/q2188_manifest.json").read().splitlines()
print("manifest 落盘:", lines[1].strip())
assert os.path.exists("/tmp/q2188_manifest.json") and not os.path.exists("/tmp/q2188_manifest.json.tmp")
print("要点: 引用替换在构建期完成, manifest 原子落盘; 先上产物再上引用, 回滚反向操作")
os.remove("/tmp/q2188_manifest.json")
```

**追问**:
- CSS 里 url() 引用的图片也要替换吗?——要,所有产物内引用统一走替换,否则指纹链断裂导致整链不缓存。
- 服务端模板动态拼引用怎么办?——模板统一从 manifest 取名,禁止手写路径,代码评审把静态路径当坏味道。
