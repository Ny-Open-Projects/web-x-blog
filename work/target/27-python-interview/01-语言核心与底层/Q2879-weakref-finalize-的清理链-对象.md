---
title: [Q2879] weakref.finalize 的清理链:对象消亡触发的级联释放
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2879 · weakref.finalize 的清理链:对象消亡触发的级联释放

> 难度:★★★★☆ | 标签:weakref, finalize, 资源清理

**问**:对象持有临时文件、连接这类外部资源,想让它「死的时候」自动清理,为什么推荐 weakref.finalize 而不是 __del__?

**答**:`weakref.finalize(obj, func, *args)` 注册一个「对象消亡后执行」的回调,比 `__del__` 安全在三点:第一,回调与参数由 finalize 注册表**强引用**,只要不把 self 或绑定方法传进去,对象就能正常回收——本例用 staticmethod 把 path 和 user 变成普通数据再闭包,这是最常见的正确姿势;第二,回调至多执行一次,显式 close 与对象消亡两条清理路径天然幂等,`alive` 属性还能查询状态;第三,回调里的异常只会打到 stderr,不会像 `__del__` 那样在解释器退出或半析构状态下制造不可预测的二次伤害,并且解释器退出时自带 atexit 兜底。级联的思路是把「该清理什么」编码成回调参数链:文件路径、注销句柄都作为参数闭包进 finalize,对象一死整条链依次执行,本机实测 bob 的临时文件在引用归零后立即被删除。

```python
# file: code/01_语言核心与底层/q2879_finalize_chain.py
"""weakref.finalize 清理链:对象消亡触发的级联资源释放。"""
import gc
import os
import tempfile
import weakref


class Session:
    """持有临时文件;对象消亡时由 finalize 回调清理,回调不持有 self。"""

    def __init__(self, user):
        self.user = user
        fd, path = tempfile.mkstemp(prefix="sess_")
        os.close(fd)
        self.path = path
        # 关键:回调与参数必须是普通函数和数据,一旦引用 self 对象就永远不死
        self._finalizer = weakref.finalize(self, Session._cleanup, path, user)

    @staticmethod
    def _cleanup(path, user):
        os.unlink(path)
        print(f"  finalize 触发:{user} 的临时文件已删除")

    def close(self):
        """显式关闭:finalize 至多执行一次,重复调用是安全的。"""
        if self._finalizer.alive:
            self._finalizer()
        print(f"  close {self.user}:alive={self._finalizer.alive}")


if __name__ == "__main__":
    sessions = [Session("alice"), Session("bob")]
    paths = [s.path for s in sessions]
    print("临时文件存在:", all(os.path.exists(p) for p in paths))

    print("alice 走显式 close:")
    sessions[0].close()
    print("重复 close:")
    sessions[0].close()

    print("bob 走对象消亡触发的隐式清理:")
    del sessions[1]
    gc.collect()                 # CPython 引用归零即触发,collect 只是兜底

    print("bob 的临时文件已不存在:", not os.path.exists(paths[1]))
```

**追问**:1) 如果把 self 当参数传给了 finalize 会怎样?——回调持有对象强引用,对象永远到不了引用计数零,finalize 永远不触发,资源静默泄漏,这是 finalize 最经典的误用。2) 级联清理链的机制?——资源对象 A finalize 触发时释放它持有的 B,B 的 finalize 再触发下一层——清理链按引用关系自然级联;或显式管理「关闭组」。3) finalize 的正确参数?——传「资源句柄/标识」(fd、连接对象)而不是宿主 self(Q488);回调不能引用目标;detach 显式注销。4) 生产陷阱?——self 进回调(永不回收);回调里抛异常被吞(Q1561 unraisable);级联链中某层清理失败卡住下游;fork 后 finalize 注册表重复触发。
