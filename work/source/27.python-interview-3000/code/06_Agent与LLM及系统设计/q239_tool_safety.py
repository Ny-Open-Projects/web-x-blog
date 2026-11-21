"""演示带白名单与危险命令拦截的命令执行工具,不真正执行任何系统命令。"""
import shlex

BLACKLIST = {"rm", "sudo", "shutdown", "mkfs", "dd", "curl"}
ALLOWED_BIN = {"ls", "cat", "echo", "date"}


def execute_command(cmdline: str, require_confirm: bool = False) -> str:
    try:
        parts = shlex.split(cmdline)
    except ValueError:
        return "拒绝:无法解析命令"
    if not parts:
        return "拒绝:空命令"
    binary = parts[0]
    if binary in BLACKLIST:
        return f"拒绝:命令 {binary} 在黑名单中"
    if binary not in ALLOWED_BIN:
        return f"拒绝:命令 {binary} 不在白名单,仅允许 {sorted(ALLOWED_BIN)}"
    if any(".." in p or p.startswith("/") for p in parts[1:]):
        return "拒绝:参数包含绝对路径或路径穿越"
    if require_confirm:
        return f"待人工确认后执行:{cmdline}"
    return f"[沙箱模拟] 已执行 {cmdline} -> ok"


if __name__ == "__main__":
    for cmd in ["ls data", "cat /etc/passwd", "rm -rf /", "sudo ls", "echo hello"]:
        print(f"{cmd!r:20} -> {execute_command(cmd)}")
    print(execute_command("rm tmp/file", require_confirm=True))
