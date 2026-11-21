import argparse
import contextlib
import io
import os
import subprocess
import sys

EX_USAGE = getattr(os, "EX_USAGE", 64)     # BSD sysexits,macOS 可用


def build_parser():
    parser = argparse.ArgumentParser(prog="scaler", add_help=False)
    parser.add_argument("--scale", type=float, default=1.0)
    parser.add_argument("value", type=float)
    return parser


def main(argv):
    try:
        args = build_parser().parse_args(argv)
    except SystemExit as err:
        return EX_USAGE if err.code == 2 else err.code
    if args.scale == 0:
        print("scale 不能为 0", file=sys.stderr)
        return 1
    print(args.value * args.scale)
    return 0


if __name__ == "__main__":
    for argv in (["3", "--scale", "2"], ["3", "--scale", "0"], ["--bogus", "3"]):
        noise = io.StringIO()
        with contextlib.redirect_stderr(noise):
            code = main(argv)
        print(argv, "-> exit", code)

    # 独立进程视角:shell 里看 $? 与 subprocess 的 returncode
    probes = ["sys.exit(3)", "sys.exit('boom')", "sys.exit(None)",
              "raise KeyboardInterrupt"]
    for body in probes:
        done = subprocess.run([sys.executable, "-c", "import sys\n" + body],
                              capture_output=True, text=True)
        note = done.stderr.strip().splitlines()[-1] if done.stderr.strip() else ""
        print("%-26s -> returncode %s %s" % (body, done.returncode, note[:40]))
