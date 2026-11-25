---
title: [Q5126] warnings 过滤器误配掩盖弃用告警事故
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5126 · warnings 过滤器误配掩盖弃用告警事故

> 难度:★★★☆☆ | 标签:事故复盘, warnings, 升级治理

**问**:一次 Python 小版本升级后服务行为悄悄变了，复盘发现弃用告警早就刷了几个月日志，但没人看。`warnings` 的过滤器机制怎么工作的？为什么"同一告警只显示一次"反而害了大家？怎么用 `-W error` 把告警治理变成硬门禁？

**答**:结论：warnings 的默认行为是 **`default` 过滤器——同一位置（模块+行号）的告警只在第一次打印**，且过滤是**按注册顺序首次匹配生效**的正则匹配链。事故链通常是：某依赖库先注册了 `filterwarnings("ignore")`（或 `__warningregistry__` 已缓存"已打印"），你的告警被吞或只出现过一次，随后被日志采样/告警降噪规则淹没。治理三板斧：a) **CI 硬门禁**：测试入口 `-W error::DeprecationWarning`，让"新告警"直接红；b) **过滤器顺序治理**：`filterwarnings` 是 LIFO 栈——后注册的先匹配，所以"精确放行 + 兜底报错"要把精确规则写在后面；c) **升级演练**：预发以 `-W error` 跑全量回归，把未来版本的弃用清单变成工单。取舍：全局 `-W error` 会把第三方库的噪音也变错误，所以生产用"报错 + 逐条 ignore 白名单"并注明到期时间，白名单过期即删。

```python
import warnings, sys

def old_api(x):
    warnings.warn("old_api() is deprecated, use new_api()",
                  DeprecationWarning, stacklevel=2)
    return x * 2

def new_api(x):
    return x * 2

# ---- 1) 默认行为：同位置只打一次（3.x 默认过滤器近似 default） ----
print("默认过滤器第一次调用:", old_api(1))
print("默认过滤器第二次调用:", old_api(2), "-> 无输出，被 __warningregistry__ 缓存")

# ---- 2) 过滤器是 LIFO 栈：后注册先匹配 ----
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("ignore", DeprecationWarning)     # 先注册兜底忽略
    warnings.filterwarnings("error", message=".*deprecated.*")  # 后注册：精确报错
    try:
        old_api(3)
        print("未被拦截（顺序错了）")
    except DeprecationWarning as e:
        print("LIFO 生效，精确规则拦截:", e)
print(f"record 模式捕获 {len(caught)} 条（不打印、进列表，适合测试断言）")

# ---- 3) -W error::DeprecationWarning 门禁效果（子进程演示） ----
import subprocess
code = "import warnings; warnings.warn('future break', DeprecationWarning)"
r_ok = subprocess.run([sys.executable, "-W", "ignore::DeprecationWarning", "-c", code],
                      capture_output=True, text=True)
r_err = subprocess.run([sys.executable, "-W", "error::DeprecationWarning", "-c", code],
                       capture_output=True, text=True)
print(f"-W ignore 退出码 {r_ok.returncode}（噪音被吞）")
print(f"-W error  退出码 {r_err.returncode}（门禁红，stderr 含 DeprecationWarning: {'DeprecationWarning' in r_err.stderr}）")

# ---- 4) 自定义告警类 + 到期白名单模式 ----
class RemovalIn314Warning(DeprecationWarning): ...
IGN = {"old_module_flag": ("2026-12-31", RemovalIn314Warning)}   # 白名单带到期日
def gated_ignore(name):
    if name in IGN:
        warnings.filterwarnings("ignore", category=IGN[name][1])
        print(f"白名单 {name} 到期 {IGN[name][0]}，过期必须删除")
gated_ignore("old_module_flag")
```

**追问一层**:为什么 `__warningregistry__` 会让 pytest 单测里"第二条同类告警消失"？（registry 挂在模块全局上，"已打印"状态跨测试残留；`catch_warnings(record=True)` 或 `simplefilter("always")` 可重置）。
**追问二层**:stacklevel=2 在告警治理里为什么重要？（定位指向调用方而非库内部——CI 归因到业务代码，stacklevel 错了告警会打到库里，白名单就错了对象）。
**追问三层**:`DeprecationWarning` 默认只在 `__main__` 显示、`PendingDeprecationWarning` 默认忽略，这对"依赖库弃用"的可见性意味着什么？（库内部触发的弃用告警默认静默，必须显式开启 -W 或在测试环境 always，否则升级风险不可见）。

## 背诵要点
- 默认"同位置只打一次"（registry 缓存）+ 过滤器 LIFO 首匹配——吞告警两大元凶。
- 治理三板斧：CI `-W error::DeprecationWarning`、白名单带到期日、预发 -W error 全量回归。
- `stacklevel` 决定归因对象；库内弃用告警默认不可见，测试环境必须 always/error。

## 复盘追问
- 设计一条流水线规则：如何让"新增的 DeprecationWarning"与"存量白名单"分开统计，避免门禁被存量噪音稀释？
- 第三方库 A 递归依赖 B，B 的告警被 A 的 filterwarnings 吞掉，怎么在不改 A 的前提下恢复可见性？
