# -*- coding: utf-8 -*-
"""excepthook 工程化: 崩溃上报与落盘。

- 钩子里做三件事: 记现场、落盘成 JSONL、限流防止雪崩刷盘;
- traceback.format_exception 拿完整栈, 线程名是定位的首要线索;
- 钩子内部绝不能再抛异常, 否则解释器只能再次打印并继续。
"""
import json
import os
import tempfile
import threading
import time
import traceback


class CrashReporter:
    def __init__(self, path, max_reports=5):
        self.path = path
        self.max_reports = max_reports
        self.count = 0
        self._lock = threading.Lock()
        self._previous = threading.excepthook

    def __call__(self, args):
        try:
            with self._lock:
                if self.count >= self.max_reports:
                    return
                self.count += 1
            entry = {
                "time": round(time.time(), 3),
                "thread": args.thread.name if args.thread else None,
                "type": args.exc_type.__name__,
                "msg": str(args.exc_value),
                "stack": "".join(traceback.format_exception(
                    args.exc_type, args.exc_value, args.exc_traceback)),
            }
            with open(self.path, "a") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
            print("[reporter] 已记录崩溃:", entry["type"], "来自", entry["thread"])
        except Exception:
            pass   # 钩子里吞掉一切, 绝不二次引爆

    def install(self):
        threading.excepthook = self

    def uninstall(self):
        threading.excepthook = self._previous


def crashy(tag):
    if tag == "big":
        raise RuntimeError("数据库连接耗尽")
    raise KeyError("missing-config")


def main():
    path = tempfile.mktemp(prefix="q2115_crash_", suffix=".jsonl")
    reporter = CrashReporter(path)
    reporter.install()
    try:
        for tag in ("net", "big", "cfg"):
            t = threading.Thread(target=crashy, args=(tag,),
                                 name="worker-" + tag)
            t.start()
            t.join()
    finally:
        reporter.uninstall()
    with open(path) as f:
        rows = [json.loads(ln) for ln in f if ln.strip()]
    print("报告条数:", len(rows))
    for r in rows:
        print("-", r["thread"], r["type"], r["msg"], "| 栈行数:",
              len(r["stack"].splitlines()))
    os.remove(path)


if __name__ == "__main__":
    main()
