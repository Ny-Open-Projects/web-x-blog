---
title: [Q485] sys.path 治理:污染来源与 -m 运行
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q485 · sys.path 治理:污染来源与 -m 运行

> 难度:★★★☆ | 标签:import, sys.path

**问**:sys.path 里的条目都是哪来的?为什么 `python x.py` 和 `python -m pkg.mod` 的导入行为不同?

**答**:来源按序:脚本所在目录(或 -m 时的当前目录)、PYTHONPATH 环境变量、安装时的 site-packages。污染来源主要是二和三的混用:把工程根塞进 PYTHONPATH 会让本应安装的包被源码目录遮蔽。`python x.py` 把脚本目录放最前——好处是相对资源好找,坏处是脚本目录里的 stdlib 同名文件(如 logging.py)会遮蔽标准库,即「名字遮蔽」事故。`python -m pkg.mod` 把当前目录放最前并以模块身份运行,相对导入可用、且与安装后的运行行为一致,是工程项目的推荐入口。

```python
# file: code/01_语言核心与底层/q485_sys_path.py
import os
import sys

if __name__ == "__main__":
    print("cwd:", os.getcwd())
    print("sys.path[0]:", sys.path[0])
    print("PYTHONPATH entries:", os.environ.get("PYTHONPATH", "(unset)"))
    print("safe_path flag:", getattr(sys.flags, "safe_path", "n/a before 3.11"))
    print("total entries:", len(sys.path))
    shadow = [p for p in sys.path[:3]]
    print("first three search locations:", shadow)
```

**追问**:1) 模块名与第三方包撞名(自己的 email.py)为什么危险?——sys.path[0] 优先级最高,自己的文件遮蔽标准库 email,所有依赖它的导入(如 smtplib)连锁损坏;排查手段是打印模块的 __file__。2) sys.path 的污染源有哪些?——脚本目录(sys.path[0])、PYTHONPATH、site 初始化的 site-packages、.pth 文件、user site;前两个最难控制,容器与 CI 里要显式清理。3) 解析的底层顺序?——先查 sys.modules 缓存,再 meta_path finder,最后逐个尝试 sys.path 条目;首个命中者赢,所以「遮蔽」由路径顺序决定而与文件新旧无关。4) 生产陷阱?——部署包把本地同名脚本一起打包遮蔽标准库;调试用 `import mod; print(mod.__file__)` 与 sys.path 快照定位遮蔽源。
