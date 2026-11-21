---
title: [Q2106] 模块导入副作用治理:main 守卫与延迟初始化
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2106 · 模块导入副作用治理:main 守卫与延迟初始化

> 难度:★★☆☆☆ | 标签:导入副作用, main 守卫, 延迟初始化

**问**:为什么「import 时连接数据库」是坏味道?正确的初始化时机是什么?

**答**:模块顶层代码在**每次被 import 时**执行——测试收集、脚本复用、文档工具、frozen 分析都会触发它,于是连接生产库的副作用在所有这些场景里意外发生,还拖慢启动。治理两板斧:if __name__ == "__main__": 守卫把「脚本直跑才做」的事(演示、CLI 入口)圈进守卫;连接、句柄这类昂贵资源改成延迟初始化——模块级 _client = None,首次调用 get_client() 才真正建立。收益:import 恒定无副作用、可测试(测试可以 import 模块而不触发任何 IO)、启动快。边界也要知道:模块级定义常量、注册表、装饰器注册是合法的「声明性副作用」,要禁的是 IO 与全局可变状态。

```python
# file: code/01_语言核心与底层/q2106_import_side_effect.py
"""模块导入副作用治理:main 守卫与延迟初始化。"""
import pathlib
import sys
import tempfile

BAD_SRC = '''print("connecting to production db ...")

def query():
    return "data"
'''

GOOD_SRC = '''_client = None

def get_client():
    global _client
    if _client is None:
        _client = "db-conn"        # 首次使用才初始化
    return _client

def query():
    return get_client() + ":data"

if __name__ == "__main__":
    print("only when run directly:", query())
'''


def run_import(src, label):
    with tempfile.TemporaryDirectory() as tmp:
        (pathlib.Path(tmp) / "dbmod.py").write_text(src, encoding="utf-8")
        sys.modules.pop("dbmod", None)
        sys.path.insert(0, tmp)
        try:
            print(f"[{label}] import 开始")
            __import__("dbmod")
            print(f"[{label}] import 结束")
        finally:
            sys.path.remove(tmp)
            sys.modules.pop("dbmod", None)


if __name__ == "__main__":
    run_import(BAD_SRC, "坏味道")
    run_import(GOOD_SRC, "治理后")
```

**追问**:1) import 时建立连接还会出什么事?——测试、工具、文档全部被殃及,还可能绕过环境检查直连生产;延迟初始化线程安全吗?——单例检查非原子,多线程要加锁或接受重复建连,import 锁保护不了函数体(见 Q550)。2) main 守卫的完整语义?——if __name__ == "__main__" 隔离「被导入时的副作用」;模块级只放定义与常量;初始化(连接/线程/日志配置)放显式入口函数。3) 延迟初始化的模式?——首次使用时初始化(get_or_create)+ 锁(Q489 双检);框架钩子(app startup);配置读取同理推迟。4) 生产陷阱?——import 读配置文件(路径不存在直接崩);被 import 即起线程;测试导入触发真实网络;初始化竞态建两个池。
