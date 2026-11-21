"""文件下载路径穿越防护:realpath 归一化后限定根目录(纯标准库)。"""
import os

ROOT = os.path.realpath("/tmp/q1365_demo_files")
os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)


def safe_join(root, name):
    """返回安全的绝对路径;非法输入返回 None。"""
    if not name or name.startswith(("/", "\\")) or ":" in name[:2]:
        return None                                    # 绝对路径与盘符
    candidate = os.path.realpath(os.path.join(root, name))
    if candidate != root and not candidate.startswith(root + os.sep):
        return None                                    # 归一化后越界
    return candidate


cases = ["docs/a.txt", "ok.txt", "../../etc/passwd", "/etc/passwd",
         "docs/../../escape", "docs/../../../etc/passwd"]
for c in cases:
    print(f"{c!r:28s} ->", safe_join(ROOT, c))

assert safe_join(ROOT, "../../etc/passwd") is None
assert safe_join(ROOT, "docs/a.txt") is not None
print("路径穿越用例通过;生产实现返回 404 并记录审计日志")
