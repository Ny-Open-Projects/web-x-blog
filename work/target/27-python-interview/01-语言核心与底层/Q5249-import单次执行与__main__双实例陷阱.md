---
title: "[Q5249] import 单次执行语义：sys.modules 缓存、__main__ 双实例与副作用顺序"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5249 · import 单次执行语义：sys.modules 缓存、__main__ 双实例与副作用顺序

难度：P6 ｜ 标签：import、sys.modules、模块单次执行、__main__ 双实例、模块级副作用、初始化顺序、reload、双重导入

**问**：`import mod` 第二次执行为什么不会再跑模块级代码？"脚本被当模块再 import 一次"会得到什么（`__main__` 双实例陷阱）？模块级副作用（注册、建连接、读配置）的执行顺序与单次性怎么保证？`importlib.reload` 会重置什么、保留什么？

**答**：
结论：import 语句的执行模型分两步：先查 **`sys.modules`** 按模块名（不是按文件路径！）找缓存——命中直接返回既有模块对象，**模块级代码一行都不再执行**；未命中才走查找器（sys.meta_path，Q482）加载源码、执行模块体、注册进 `sys.modules`。所以"模块级副作用只跑一次"的保证来自**名字到对象的缓存**，关键推论有三个：①**同名不同路径 = 两个模块对象**——同一文件被两个不同的顶层包路径导入（如 `utils.py` 同时以 `utils` 与 `pkg.utils` 可达），模块体执行两次，装饰器注册器注册两份、`isinstance` 跨实例失效、模块级单例翻倍（Q442 注册器模式的事故源）；②**`__main__` 双实例陷阱**——脚本直接运行时模块名是 `__main__`，若这个文件又被别的模块 import（按文件名作为模块名），会得到**第二个独立模块对象**：模块级可变全局（计数器、连接池、注册表）存在两份，`if __name__ == "__main__"` 保护只防"脚本被 import 时执行入口逻辑"，防不了"共享状态翻倍"——正解是**把入口写薄**（真正的实现放独立模块，脚本只 import 并调用），让任何文件最多以一个名字可达；③**循环导入的部分初始化**——模块 A import B、B 又 import A 时，sys.modules 里 A 已存在（但还在执行中、属性没填满），B 拿到的是"半初始化模块对象"，访问未定义属性即 AttributeError（Q5181 的延迟 getattr 解法）。`importlib.reload`：在**同一模块对象**上重新执行模块体——全局命名空间被重新赋值/新增，但**没有被新代码重新赋值的旧名字会残留**（保留旧对象引用），对象身份（已持有引用的调用方）不变。

取舍：a) 模块级副作用纪律：模块体只做**幂等、无 IO 或廉价 IO**的事（注册表 append、常量表构建）；建连接、起线程、读远程配置一律延后到显式 `init()` 或框架 lifespan（Q6161）——import 顺序敏感是所有"模块级建连接"事故的共同根因；b) 初始化顺序依赖：模块 import 的先后顺序在 PEP 8 分组里只是风格，但**有依赖的模块级初始化必须显式化**（被依赖方不 import 依赖方、依赖方在 init() 里显式调用），靠"恰好 import 在前"是运气；c) reload 的定位：开发期热载工具，不做生产热更新（生产走进程级重启 + 建立新连接池，Q1603 信号热加载是"换配置对象"不是 reload）；d) sys.modules 的手工操作：临时塞入/删除条目是高级技巧（测试 mock、延迟导入），删除条目不会触发模块清理（模块对象靠引用计数释放，残留引用会让它活着）；e) 包的 `__init__.py` 也是模块：包导入先执行 `__init__`，它的 import 子模块语句决定了"import pkg 后哪些属性可用"——API 表面设计在这里完成。

实战：事故形态是"CLI 工具被测试框架当作模块收集（import），同时又被 subprocess 直接运行——两条路径各建一个连接池，CI 里连接数翻倍打满测试库上限；进一步发现装饰器注册的任务表有两份，调度器拿到的是未注册那份。修复为：入口文件瘦身成 20 行薄壳，实现全部下沉 `core/`，注册表单例由 `core.registry` 唯一可达；CI 增加'模块导入计数'探针断言"。下面实测单次执行、双实例与 reload 语义。

```python
# import 单次执行语义: sys.modules 缓存、__main__ 双实例与 reload
import importlib.util
import os
import sys
import tempfile

EXEC_STAMP = []                       # 模块级可变全局: 任何一次执行都会新建属于"自己"的这份

if __name__ == "__main__":
    print("[1] sys.modules 缓存: import 语句按模块名只执行一次模块体")
    d = tempfile.mkdtemp()
    p = os.path.join(d, "counted.py")
    with open(p, "w") as f:
        f.write("COUNTER = 0\nCOUNTER += 1\nprint('    [exec] counted.py 模块体执行, COUNTER ->', COUNTER)\n")
    sys.path.insert(0, d)
    import counted                      # 第一次: 执行模块体, 打印 exec 行
    import counted                      # 第二次: 命中 sys.modules, 无任何输出
    print("    二次 import 无 [exec] 输出; sys.modules 命中:", sys.modules["counted"] is counted)

    print("[2] reload: 同一模块对象上重跑模块体, 旧名字残留")
    importlib.reload(counted)           # 重跑: COUNTER 重新从 0 计到 1
    print("    reload 后 COUNTER =", counted.COUNTER, "(模块体重新初始化, 不是累加)")

    print("[3] __main__ 双实例: 本脚本再以另一个模块名加载同一文件")
    try:
        self_path = os.path.abspath(__file__)          # 落文件运行: 直接拿自身路径
    except NameError:                                  # -c/交互式运行: 无 __file__, 用含同款模块级状态的临时副本代替
        self_path = os.path.join(d, "ghost_copy.py")
        with open(self_path, "w") as f:
            f.write("EXEC_STAMP = []\n")
    spec = importlib.util.spec_from_file_location("ghost_self", self_path)
    ghost = importlib.util.module_from_spec(spec)
    sys.modules["ghost_self"] = ghost
    spec.loader.exec_module(ghost)      # 以 ghost_self 身份再执行一遍本文件
    print("    ghost 的模块对象与 __main__ 不同:", sys.modules["__main__"] is not ghost)
    print("    ghost 的 EXEC_STAMP 是新列表:", ghost.EXEC_STAMP is not EXEC_STAMP, "(共享状态翻倍的根源)")

    print("[4] 同名不同路径 = 两个模块对象 (同名缓存按名字不按路径)")
    spec2 = importlib.util.spec_from_file_location("counted_alias", p)
    alias = importlib.util.module_from_spec(spec2)
    sys.modules["counted_alias"] = alias
    spec2.loader.exec_module(alias)
    print("    counted is counted_alias:", counted is alias, "(两个独立模块对象, 各自 COUNTER=1)")

    print("[5] 工程纪律: 入口薄壳化, 实现下沉唯一可达的模块, 副作用延后到 init()/lifespan")
else:
    # 被 ghost_self 再次加载时走这里: 模块级代码又独立执行了一遍
    EXEC_STAMP.append(f"loaded-as-{__name__}")
    print(f"    [exec] 本文件模块体以 __name__={__name__} 再执行, EXEC_STAMP={EXEC_STAMP} 是全新实例")
```

**追问一**：为什么"同名不同路径导入两次"在包结构重构时高发？如何系统性排查与预防？—— 机制：`sys.modules` 的 key 是**导入时使用的完整模块名**。项目里 `utils/http.py` 既被 `from utils.http import client`（注册为 `utils.http`）引用，又有脚本 `sys.path` 指向 `utils/` 目录后 `import http`（注册为 `http`）——同一文件两个 key、两个模块对象、两份模块级状态。重构高发原因：目录层级变动（包前缀增减）、`sys.path` 手工注入、打包工具把顶层目录也放进路径。排查手段：①探针断言——关键模块顶部 `assert globals().get("_LOADED") is None` 或用注册表长度断言，单元测试里跑一次全模块 import 扫描比对注册表计数；②`sys.modules` 快照对比：同文件路径出现多个 key 即违规（按 `module.__file__` 归并检查）；③lint 层禁止 `sys.path.append` 的散落使用（统一到入口/打包配置）。预防性架构：**一个文件只允许一个导入路径**（包结构自洽 + 不手改 path），入口薄壳化，全局可变状态集中到单一模块并由唯一名字可达——这三条同时消灭双实例与 `__main__` 翻倍。

**追问二**：`importlib.reload` 的"旧名字残留"具体指什么？为什么生产环境用 reload 做热更新是危险操作？—— reload 在**原模块对象的同一命名空间**里重新执行模块体：执行到的赋值会更新/重建对应名字，但模块体没写的旧名字**原样留在命名空间里**——比如旧版模块有 `legacy_hook`、新版代码删掉了它，reload 后 `mod.legacy_hook` 仍然存在且指向旧对象；同样，模块级缓存 dict reload 后被重置为空（模块体重新初始化），而**其他模块持有的旧对象引用不受影响**（它们连着的是对象不是名字）——于是出现"一半调用方用新代码、一半引用旧对象"的混合态。生产热更新的真实风险：①无原子性——reload 过程中并发请求看到半新半旧；②模块间依赖不级联——reload(mod) 不会 reload 依赖它的模块（要自建依赖图逆序 reload，复杂且易漏）；③资源泄漏——旧版类实例、线程、连接池仍被引用活着。正解：配置级热更新用"构建新配置对象 + 原子替换引用"（Q1603），代码级更新走进程重启 + 排空（Q2905）——reload 只属于开发期 REPL/调试场景。

## 背诵要点
- import 两步走：sys.modules 按模块名查缓存（命中不执行模块体）→ 未命中才加载执行并注册；单次性靠名字缓存，同名不同路径 = 两个模块对象两份状态。
- __main__ 双实例：脚本运行名是 __main__、被 import 时是文件名，同一文件两个对象；入口薄壳化 + 全局状态唯一可达模块 + 禁散落 sys.path 注入。
- reload 在原命名空间重跑：旧名字残留、对象引用不更新、依赖不级联、无原子性——生产热更用原子替换引用（配置）或进程重启（代码）。

## 复盘追问
- 同一个文件为什么可能被执行两次、后果是什么？（sys.modules 按 key 是模块名不是路径；两个导入名 → 两个模块对象 → 注册表/连接池/isinstance 全翻倍；探针 + __file__ 归并检查）
- 生产环境为什么禁止 importlib.reload？（半新半旧混合态、依赖不级联、旧引用泄漏；配置热更走原子替换，代码更新走进程重启排空）
