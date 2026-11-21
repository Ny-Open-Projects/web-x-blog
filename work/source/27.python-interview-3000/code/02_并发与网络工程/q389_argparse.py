"""argparse 命令行工具骨架 + 自定义校验 + 交互输入校验。"""
import argparse
import pathlib
import sys


def port_type(value: str) -> int:
    port = int(value)
    if not 1 <= port <= 65535:
        raise argparse.ArgumentTypeError(f"端口 {port} 不在 1-65535 范围")
    return port


def build_parser():
    p = argparse.ArgumentParser(prog="deploy", description="部署工具示例")
    p.add_argument("target", help="部署目标目录")
    p.add_argument("--port", type=port_type, default=8000)
    p.add_argument("--env", choices=["dev", "staging", "prod"], default="dev")
    sub = p.add_subparsers(dest="action")
    sub.add_parser("plan", help="只做 dry-run")
    sub.add_parser("apply", help="真正执行")
    return p


def ask_int(prompt, lo, hi, default=None):
    """交互输入校验:非法输入循环重试。

    非交互环境(stdin 关闭, 如 CI/演示脚本)input() 会抛 EOFError,
    此时直接回退默认值, 不让交互把脚本挂死。
    """
    while True:
        try:
            raw = input(f"{prompt} [{lo}-{hi}]{' 默认 ' + str(default) if default else ''}: ").strip()
        except EOFError:
            print(f"(检测到无交互输入, 使用默认值 {default})")
            return default
        if not raw and default is not None:
            return default
        try:
            v = int(raw)
            if lo <= v <= hi:
                return v
        except ValueError:
            pass
        print("输入无效, 请重试")


if __name__ == "__main__":
    argv = sys.argv[1:] or ["./app", "--port", "9443", "--env", "prod", "apply"]
    args = build_parser().parse_args(argv)  # 实际使用时让命令行传入
    target = pathlib.Path(args.target)
    print(f"action={args.action} target={target} port={args.port} env={args.env}")
    if sys.stdin and sys.stdin.isatty():
        replicas = ask_int("请输入副本数", 1, 10, default=3)
    else:
        replicas = 3
        print("(非交互环境, 副本数取默认值 3)")
    print("副本数 =", replicas)
