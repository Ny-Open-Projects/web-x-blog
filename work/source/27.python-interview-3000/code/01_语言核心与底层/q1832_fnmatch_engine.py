"""fnmatch:shell 通配与正则的两套引擎。"""
import fnmatch
import re


def shell_match():
    names = ["log_2024.txt", "log_2025.txt", "data.csv", "notes.TXT"]
    # fnmatch 按 os.path.normcase 规范化;POSIX 上区分大小写,Windows 不区分
    return [n for n in names if fnmatch.fnmatch(n, "log_*.txt")]


def case_strict():
    names = ["notes.TXT", "notes.txt"]
    return [n for n in names if fnmatch.fnmatchcase(n, "*.txt")]


def translate_to_regex():
    source = fnmatch.translate("log_*.txt")   # 通配符 -> 正则源码
    rx = re.compile(source)
    return source[:34], bool(rx.match("log_2024.txt"))


def filter_any(names, patterns):
    return [n for n in names
            if any(fnmatch.fnmatchcase(n, p) for p in patterns)]


if __name__ == "__main__":
    print("shell 风格匹配:", shell_match())
    print("严格大小写:", case_strict())
    print("translate 产物:", translate_to_regex())
    print("多模式过滤:", filter_any(["a.csv", "b.TXT", "c.txt"], ["*.csv", "*.TXT"]))
