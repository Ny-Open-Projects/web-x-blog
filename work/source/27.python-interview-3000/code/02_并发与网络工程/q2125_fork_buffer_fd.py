# -*- coding: utf-8 -*-
"""fork 后的缓冲区重复输出与 fd 继承。

- fork 复制整份用户态内存, 未 flush 的 stdio 缓冲也被复制;
- 父子各自 flush 同一段缓冲, 内容就会写两遍;
- 已打开的 fd 在父子间共享同一个文件偏移, 追加写不会互相覆盖。
"""
import os
import tempfile

path = tempfile.mktemp(prefix="q2125_forkbuf_")


def main():
    f = open(path, "w", buffering=8192)   # 文件默认全缓冲, 终端才是行缓冲
    f.write("parent-before\n")            # 先写不 flush: 驻留父进程缓冲

    pid = os.fork()
    if pid == 0:
        # 子进程拿到缓冲的完整拷贝, 其中也有 parent-before
        f.write("child\n")
        f.flush()                         # 子进程冲出: parent-before + child
        os._exit(0)

    os.waitpid(pid, 0)
    f.write("parent-after\n")
    f.flush()                             # 父进程又冲出一份 parent-before
    f.close()

    with open(path) as rf:
        content = rf.read()
    print("文件内容:", repr(content))
    dup = content.count("parent-before")
    print("parent-before 出现次数:", dup, "-> 缓冲被 fork 复制后各自 flush")

    # 修复: fork 前 flush, 或者 fork 后子进程立刻重开文件
    f2 = open(path, "w")
    f2.write("clean-parent\n")
    f2.flush()                            # 关键: fork 前冲掉
    pid2 = os.fork()
    if pid2 == 0:
        f2.write("clean-child\n")
        f2.flush()
        os._exit(0)
    os.waitpid(pid2, 0)
    f2.write("clean-after\n")
    f2.flush()
    f2.close()
    with open(path) as rf:
        print("flush 后内容:", repr(rf.read()))
    os.remove(path)


if __name__ == "__main__":
    main()
