"""difflib:相似度、模糊建议与统一 diff 的最小工具箱。"""
import difflib

KNOWN = ["timeout", "traceback", "template", "truncate"]


if __name__ == "__main__":
    print("拼写建议:", difflib.get_close_matches("timout", KNOWN, n=2, cutoff=0.6))
    print("相似度比率:", round(difflib.SequenceMatcher(None, "timout", "timeout").ratio(), 3))

    old = ["timeout = 30", "retries = 3", "verbose = False"]
    new = ["timeout = 60", "retries = 3", "verbose = True"]
    diff = difflib.unified_diff(old, new, fromfile="old.conf", tofile="new.conf", lineterm="")
    print("\n".join(diff))
