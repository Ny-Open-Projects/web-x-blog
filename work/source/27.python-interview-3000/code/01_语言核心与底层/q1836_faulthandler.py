"""faulthandler:崩溃时的栈回溯与定时转储。"""
import faulthandler
import sys
import tempfile
import time


def dump_all_threads():
    with tempfile.TemporaryFile(mode="w+") as tf:
        faulthandler.dump_traceback(file=tf)   # 手动转储所有线程的 Python 栈
        tf.seek(0)
        return tf.read()


def timed_dump():
    with tempfile.TemporaryFile(mode="w+") as tf:
        faulthandler.dump_traceback_later(0.05, file=tf, exit=False)
        time.sleep(0.12)                       # 让定时器到期,把栈写进文件
        faulthandler.cancel_dump_traceback_later()
        tf.seek(0)
        return tf.read()


if __name__ == "__main__":
    faulthandler.enable(file=sys.stderr)       # 生产入口的标准动作
    print("enable 后 is_enabled:", faulthandler.is_enabled())
    text = dump_all_threads()
    print("手动转储捕获到本文件:", "q1836_faulthandler.py" in text)
    print("定时转储捕获到本文件:", "q1836_faulthandler.py" in timed_dump())
    faulthandler.disable()
    print("disable 后 is_enabled:", faulthandler.is_enabled())
