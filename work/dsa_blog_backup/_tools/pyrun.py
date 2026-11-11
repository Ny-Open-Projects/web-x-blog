#!/usr/bin/env python3
# Helper: run a python reference solution's __main__ test block and print stdout.
# Usage: pyrun.py <python_file>
import sys, importlib.util

fpath = sys.argv[1]
src = open(fpath, encoding="utf-8").read()
src = src.replace("if __name__ == '__main__':", "if True:")
src = src.replace('if __name__ == "__main__":', "if True:")
src = src.replace("if __name__=='__main__':", "if True:")
src = src.replace('if __name__=="__main__":', "if True:")

spec = importlib.util.spec_from_file_location("m", fpath)
mod = importlib.util.module_from_spec(spec)
# exec the (guard-stripped) source in the module's namespace
exec(compile(src, fpath, "exec"), mod.__dict__)
