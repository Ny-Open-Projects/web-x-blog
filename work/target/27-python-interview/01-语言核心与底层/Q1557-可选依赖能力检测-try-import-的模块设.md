---
title: [Q1557] 可选依赖能力检测:try import 的模块设计
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1557 · 可选依赖能力检测:try import 的模块设计

> 难度:★★★☆☆ | 标签:import, 依赖管理, 模块设计

**问**:库同时支持「有 uvloop 用 uvloop,没有就用默认 asyncio」,模块层怎么组织?import 失败的异常时机怎么设计?

**答**:可选依赖的模块设计:顶层 try/except ImportError 检测一次,置 HAS_X 标志与实现引用,进程生命周期内不再重复;降级要留原因(把 err.name 与安装提示存成字符串),供诊断与用户提示。要点:① 用户覆盖——环境变量强制开/关某后端,强制开启而依赖缺失时 RuntimeError 带修复指令;② 区分两种失败——ModuleNotFoundError(ImportError 子类,带 name 属性、仅找不到时抛)可静默降级,模块存在但导入期崩溃是环境损坏,不该被降级逻辑吞掉;③ 检测放模块顶层、线程启动前,避免运行中竞态;④ 打包层配套:extras 声明(pip install pkg[extra])让依赖关系在元数据层可见。

```python
# file: code/01_语言核心与底层/q1557_optional_dependency.py
import os

try:                                   # 顶层检测一次:标准库 json 一定在
    import json as _fast_json
    HAS_FAST = True
    FAST_REASON = ""
except ImportError as err:             # 实际不会走到:演示结构
    HAS_FAST = False
    FAST_REASON = str(err)

try:                                   # 第三方包:本机大概率没有
    import uvloop as _loop_impl
    HAS_UVLOOP = True
    LOOP_REASON = ""
except ImportError as err:
    HAS_UVLOOP = False
    LOOP_REASON = "%s 未安装: pip install uvloop" % err.name


def pick_loop(force=None):
    """env 可覆盖自动检测:FORCE_UVLOOP=1 或 0。"""
    if force is None:
        force = os.environ.get("FORCE_UVLOOP")
    if force == "1":
        if not HAS_UVLOOP:
            raise RuntimeError("FORCE_UVLOOP=1 但依赖缺失: " + LOOP_REASON)
        return "uvloop"
    if force == "0":
        return "asyncio 默认循环"
    return "uvloop" if HAS_UVLOOP else "asyncio 默认循环"


if __name__ == "__main__":
    print("HAS_FAST:", HAS_FAST, "| HAS_UVLOOP:", HAS_UVLOOP)
    print("auto      :", pick_loop())
    print("forced off:", pick_loop(force="0"))
    try:
        pick_loop(force="1")
    except RuntimeError as err:
        print("forced on :", err)
    print("reason kept:", LOOP_REASON)
```

**追问**:1) 怎么区分「模块不存在」和「模块存在但导入炸了」?——ModuleNotFoundError 带 name 且只在找不到时抛;导入期崩溃是别的异常类型,不该被降级逻辑吞掉。2) 探测与导入的两种姿势?——try/except ImportError 是「导入即探测」;importlib.util.find_spec 只查存在性不执行模块,适合启动期依赖清单检查;两者粒度都要锁定到具体模块名。3) 降级设计?——HAS_X 常量 + 优雅降级提示(告诉用户怎么装);可选依赖写进文档与 extras_require;能力缺失是「可运行」而不是「崩」。4) 生产陷阱?——裸 except ImportError 吞掉依赖损坏的真实错误;探测与导入结果不一致(TOCTOU);忘记区分「依赖缺失」与「依赖版本不兼容」。
