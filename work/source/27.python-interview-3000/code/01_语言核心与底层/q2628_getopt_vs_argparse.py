"""getopt 与 argparse 的同一需求两种写法对照。"""
import argparse
import getopt
import sys


def run_getopt(argv):
    """getopt:手动切分,手写错误。"""
    try:
        opts, args = getopt.getopt(argv, "vo:", ["verbose", "output="])
    except getopt.GetoptError as exc:
        return f"解析失败: {exc}"
    out = {"verbose": False, "output": None}
    for opt, val in opts:
        if opt in ("-v", "--verbose"):
            out["verbose"] = True
        elif opt in ("-o", "--output"):
            out["output"] = val
    return out, args


def build_argparse():
    """argparse:声明即文档。"""
    p = argparse.ArgumentParser(description="演示")
    p.add_argument("-v", "--verbose", action="store_true")
    p.add_argument("-o", "--output")
    p.add_argument("files", nargs="*")
    return p


if __name__ == "__main__":
    argv = ["-v", "--output=out.txt", "f1", "f2"]
    print("getopt:", run_getopt(argv))

    ns = build_argparse().parse_args(argv)
    print("argparse:", ns.verbose, ns.output, ns.files)
