---
title: [Q6026] Python 运行时升级的发布工程：从依赖锁到金丝雀
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6026 · Python 运行时升级的发布工程：从依赖锁到金丝雀

> 难度:★★★★ | 标签:版本演进, 发布工程, 升级

**问**：把生产服务从 3.11 升到 3.12（乃至跨到 3.13）的完整发布工程是什么？为什么"原地 pip install 新解释器"是错的？依赖锁、镜像、金丝雀、回滚各环节怎么做？哪些语言级行为变化必须进回归清单？

**答**：升级是**运行时替换工程**，不是依赖更新。六个环节：1) **依赖预检**——锁文件按目标版本**重新求解**（不是改个数字）：所有带 C/Rust 扩展的包（pydantic-core、numpy、cryptography、grpcio…）必须有目标版本的 wheel（Q5029 ABI 标签），`pip install --only-binary=:all:` 干跑当门禁，逼出"没有 wheel 就换版本/换包"；2) **镜像重建**——基础镜像换 `python:3.12-slim` 重新构建（不可原地改），顺带重算 manylinux 兼容；3) **CI 双版本矩阵**——新旧两版并行跑全量测试到升级完成才摘旧版，`-W error::DeprecationWarning` 预演目标版本的弃用告警；4) **行为回归清单**——语言级变化点过一遍（3.12：PEP 709 推导式内联对闭包/locals 的可见性变化、PEP 695；3.13：PEP 667 locals 视图、实验性 free-threading 不开；对照 3.11→3.12→3.13 release notes 逐条勾稽）；5) **金丝雀**——新旧镜像按 5%→25%→100% 放量，盯错误率/p99/RSS 三线（Q842 指标护栏）；6) **回滚**——回滚=切回旧镜像 tag（镜像与配置都不可变），数据库无 schema 变化才有此自由度。最容易翻车的点：悄悄转源码编译（CI 干跑拦）、site-packages 里的旧 cp 扩展残留（镜像全新构建天然规避）、行为差异被测试盲区漏掉（双矩阵是唯一保险）。

```python
# file: code/03_Web后端开发/q6026_runtime_upgrade.py
import re, sys

REQUIREMENTS = """
fastapi==0.115.0
pydantic-core==2.23.0     # Rust 扩展: 必须有目标版本 wheel
numpy==1.26.4             # cp311 编译产物,目标版本无 wheel 则拦下
cryptography==43.0.0      # Rust 扩展
httpx==0.27.2             # 纯 py: 通常免重编译
"""

COMPILED = {"pydantic-core", "numpy", "cryptography", "pillow", "lxml", "grpcio", "uvloop"}

def preflight(req_text: str, target: tuple) -> list[tuple[str, str, str]]:
    tgt = ".".join(map(str, target))
    report = []
    for line in req_text.splitlines():
        line = line.split("#")[0].strip()
        if not line or "==" not in line:
            continue
        name, _, ver = line.partition("==")
        if name.lower() in COMPILED:
            report.append((name, ver, f"C/Rust 扩展: 需 {tgt} 版本 wheel"))
        else:
            report.append((name, ver, "纯 py: 通常免重编译"))
    return report

print("当前解释器:", sys.version_info[:3], "| 升级目标: 3.12")
for name, ver, note in preflight(REQUIREMENTS, (3, 12)):
    print(f"  {name:<14} {ver:<10} {note}")

CHECKLIST = [
    "1) 锁文件按目标版本重新求解,--only-binary=:all: 干跑门禁",
    "2) 基础镜像换版重建(禁止原地 pip),无 cp 扩展残留",
    "3) CI 新旧双版本矩阵 + -W error::DeprecationWarning 预演",
    "4) 行为回归清单: PEP709 推导式内联/PEP695/PEP667 逐条勾稽",
    "5) 金丝雀 5%->25%->100%,盯错误率/p99/RSS 三线",
    "6) 回滚 = 切回旧镜像 tag(配置不可变,无 DB schema 变化)",
]
print()
for c in CHECKLIST:
    print(" ", c)
```

**追问**：1) 小版本（3.12.3→3.12.7）升级要不要走全套？——简化版：纯 bugfix 版本仍换镜像重建（顺带安全补丁），金丝雀可缩到 1-2%；但 wheel 标签不变（cp312），依赖不用重解。2) `-W error::DeprecationWarning` 为什么必须在升级前跑？——把"目标版本将弃用"提前暴露成 CI 错误，等升级后修就晚了；注意区分第三方库的告警（先 pin 或上报）与自己代码的告警。3) free-threading（3.13 的 --disable-gil 构建）为什么不顺手开？——独立 ABI 标签（cp313t）扩展生态不齐、单线程性能折损，属于另一次独立工程，不搭升级顺风车。

## 背诵要点
1. 升级 = 运行时替换工程：锁文件重解 → 镜像重建 → CI 双矩阵 → 行为清单 → 金丝雀 → 切 tag 回滚。
2. 门禁 `--only-binary=:all:`：拦"悄悄转源码编译"；镜像全新构建杜绝旧扩展残留。
3. 行为回归重点：PEP 709/695（3.12）、PEP 667（3.13）；free-threading 不搭车，单独立项。

## 复盘追问
1. 升级后某接口 p99 上升 8% 但功能全对，怎么定位是运行时行为变化？（提示：对比新旧镜像的 py-spy 火焰图与 GC 统计，聚焦解释器热点差异（如内联后分配模式变化），必要时 feature flag 回退该路径）
2. 如何把"单次升级工程"沉淀为常态能力？（提示：CI 常驻双版本矩阵、升级演练纳入季度例行、依赖 wheel 覆盖率看板，让下一次升级变成配置变更）
