---
title: [Q500] inspect.getsource 与运行时源码检查
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q500 · inspect.getsource 与运行时源码检查

> 难度:★★★☆ | 标签:inspect, 调试

**问**:如何在运行时打印任意函数的源码?这类能力有什么正经用途与限制?

**答**:inspect.getsource(obj) 通过 obj.__code__ 的文件名与行号回读源文件切片;getsourcelines 额外给起始行号,getdoc 取文档,getmodule 定位所属模块。正经用途:交互式调试(help() 底层)、框架生成文档、测试失败时打印被测函数上下文、notebook 的 ?? 魔法。限制:源码必须真实存在于磁盘(交互式输入、exec 出来的代码、C 扩展函数都拿不到)、pyc-only 部署会失败。用 try/except 包裹并降级为「只打印签名」是健壮写法。

```python
# file: code/01_语言核心与底层/q500_inspect_getsource.py
import inspect

def important_algorithm(x):
    """文档字符串也会被读取"""
    y = x * 2
    return y + 1

class Widget:
    def render(self):
        return "rendered"

if __name__ == "__main__":
    print(inspect.getsource(important_algorithm))
    print("doc:", inspect.getdoc(important_algorithm))
    print("render starts at line:", inspect.getsourcelines(Widget.render)[1])
    print("module:", inspect.getmodule(Widget).__name__)
    print("len source lines:", len(inspect.getsourcelines(Widget)[0]))
```

**追问**:1) 为什么装饰过的函数还能 getsource 到原始定义?——wraps 保留的 __wrapped__ 与 __module__/__qualname__ 让 inspect 沿链找到原始 code 对象的文件与行号;没有 wraps 的装饰器会定位到 wrapper 自己。2) getsource 的失败模式?——REPL/exec 生成的代码、C 扩展函数、打包环境(无源文件)、源码文件被改动(行号缓存失配)都会失败或给错行;linecache 有缓存,文件编辑后要 checkcache。3) 底层机制?——按 code.co_filename/co_firstlineno 通过 linecache 读文件切片;__wrapped__ 链让 inspect 回到最内层的原始 code 对象。4) 生产陷阱?——PyInstaller 等打包后源码不存在,运行时文档/help 功能崩;doctest 依赖源文本,重排版破坏用例;热路径频繁 getsource 首次有 IO 开销。
