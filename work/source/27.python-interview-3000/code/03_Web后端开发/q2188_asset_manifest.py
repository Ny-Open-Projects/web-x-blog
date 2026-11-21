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
