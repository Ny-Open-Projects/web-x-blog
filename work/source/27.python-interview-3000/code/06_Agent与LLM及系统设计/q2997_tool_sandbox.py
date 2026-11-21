"""Q2997 工具沙箱的受限执行:路径封堵+白名单+输出配额。

Agent 的工具不能拿到「裸权限」:文件类工具必须把可访问范围钉死在
工作区根目录内,绝对路径、.. 穿越、越区软引用一律拒收;可执行表达式
类工具禁止双下划线与危险内建;所有工具的输出有字节配额,防止把
超大文件灌进上下文。沙箱的价值在于默认拒绝:白名单外的行为不是
「警告」而是直接不给执行。
"""

import os


class SandboxViolation(Exception):
    pass


class FileSandbox:
    def __init__(self, root, max_bytes=200, ext_whitelist=(".md", ".txt")):
        self.root = os.path.realpath(root)
        self.max_bytes = max_bytes
        self.ext_whitelist = ext_whitelist
        self.denied = []

    def resolve(self, rel_path):
        """把相对路径钉死在 root 内:穿越与越界全部拒收。"""
        if os.path.isabs(rel_path):
            raise SandboxViolation("拒绝绝对路径:" + rel_path)
        target = os.path.realpath(os.path.join(self.root, rel_path))
        if target != self.root and \
           not target.startswith(self.root + os.sep):
            raise SandboxViolation("路径逃逸:" + rel_path)
        if not target.endswith(self.ext_whitelist):
            raise SandboxViolation("扩展名不在白名单:" + rel_path)
        return target

    def read(self, rel_path):
        try:
            target = self.resolve(rel_path)
        except SandboxViolation as exc:
            self.denied.append(str(exc))
            raise
        with open(target, "r", encoding="utf-8") as fh:
            data = fh.read(self.max_bytes + 1)
        if len(data) > self.max_bytes:
            data = data[:self.max_bytes]
            self.denied.append("输出截断至配额:" + rel_path)
        return data


SAFE_BUILTINS = {"abs": abs, "round": round, "len": len,
                 "min": min, "max": max}


def eval_expr(expr):
    """受限表达式求值:白名单名字+禁双下划线,拒绝一切访问属性。"""
    if "__" in expr:
        raise SandboxViolation("禁止双下划线访问")
    if any(w in expr for w in ("import", "open", "exec", "eval",
                               "getattr", "os.", "system")):
        raise SandboxViolation("出现禁止的调用:" + expr)
    try:
        return eval(expr, {"__builtins__": {}}, dict(SAFE_BUILTINS))
    except Exception as exc:
        raise SandboxViolation("表达式无法安全求值:%s (%s)"
                               % (expr, type(exc).__name__))


def main():
    import tempfile
    tmp = tempfile.mkdtemp(prefix="sbx_")
    with open(os.path.join(tmp, "policy.md"), "w",
              encoding="utf-8") as fh:
        fh.write("退款政策:7 天无理由。" * 3)
    with open(os.path.join(tmp, "huge.txt"), "w",
              encoding="utf-8") as fh:
        fh.write("x" * 1000)

    sbx = FileSandbox(tmp, max_bytes=60)
    # 正常读取 + 超配额截断
    data = sbx.read("policy.md")
    assert data.startswith("退款政策") and len(data) <= 60
    assert len(sbx.read("huge.txt")) == 60

    # 三类逃逸全部拒收且留痕
    for bad in ("/etc/passwd", "../../etc/passwd", "sub/secret.py"):
        try:
            sbx.read(bad)
            raise AssertionError("应当拒绝 " + bad)
        except SandboxViolation as exc:
            pass
    assert len(sbx.denied) == 4                     # 3 次拒收 + 1 次截断

    # 受限表达式:白名单内可用,危险形态全拒
    assert eval_expr("max(2, 5) + abs(-3)") == 8
    assert eval_expr("round(len('abcd') / 2)") == 2
    for evil in ("__import__('os').system('ls')", "open('/etc/passwd')",
                 "().__class__", "1 + "):
        try:
            eval_expr(evil)
            raise AssertionError("应当拒绝 " + evil)
        except SandboxViolation:
            pass
    print("白名单读取:", data[:18], "...")
    print("拒收记录:", sbx.denied[0])
    print("受限求值: max(2, 5) + abs(-3) =", eval_expr("max(2, 5) + abs(-3)"))


if __name__ == "__main__":
    main()
