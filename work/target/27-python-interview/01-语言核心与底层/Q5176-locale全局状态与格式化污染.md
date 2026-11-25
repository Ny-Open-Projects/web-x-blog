---
title: "[Q5176] locale 是进程全局状态：格式化与排序被并发污染"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5176 · locale 是进程全局状态：格式化与排序被并发污染

难度：P6-P7 ｜ 标签：locale、setlocale、国际化、线程污染、strxfrm

**问**：一个多语言 Web 服务在每个请求里根据 `Accept-Language` 调 `locale.setlocale(LC_ALL, ...)`，再格式化金额和月份。压测时出现"英文响应里冒出德语月份"、"同一个金额千分位一会儿逗号一会儿点"。`locale` 到底是进程级还是线程局部？为什么 `setlocale` 会影响别的请求？`str.upper()` 会不会有著名的"土耳其 i"问题？`format(n)`、`time.strftime`、`locale.strcoll` 各自受什么影响？容器里为什么 `setlocale` 直接抛 `locale.Error`？

**答**：
结论：`locale.setlocale()` 改的是**进程级**的 C locale（POSIX locale），不是线程局部变量；同一进程的所有线程、所有请求共享这一份状态。A 请求设了 `de_DE`，B 请求正在渲染英文金额，就可能读到 `de_DE` 的 `decimal_point=','`、月份 `März`、排序规则。更糟的是 `setlocale` 本身不保证线程安全，两个请求并发设置会互相覆盖，行为不可预测。受影响的典型 API：`locale.format_string`/`format(x, "n")`（数字/货币）、`time.strftime`（月份/星期名）、`locale.strcoll`/`strxfrm`（排序）、`gettext` 的某些路径；**不受影响**的是 Python 的 `str.upper/lower/casefold`——它们用 Unicode 默认大小写映射，土耳其 i 的 locale 特例只影响 C 库的 `toupper/tolower`、`strcoll` 等，不会让 `"i".upper()` 变成 `İ`。

取舍：不要用进程级 `setlocale` 做"每请求国际化"。正确做法：a) 启动时把 locale 固定成可预测的值（如 `C.UTF-8`/`en_US.UTF-8`），全进程只设一次；b) 业务格式化用显式 API（`f"{v:,.2f}"` 固定风格，或用 Babel/ICU 的 `format_currency(..., locale="de_DE")` 显式传 locale，不依赖进程状态）；c) 必须调用 C 库 locale 的遗留代码，隔离到子进程/独立 worker。容器镜像常只带 `C`/`C.UTF-8`，`setlocale("de_DE.UTF-8")` 会因缺 locale 数据抛 `locale.Error`，启动时就要 fail fast 或固定值，别等请求期才炸。

实战：事故形态是"财务报表的千分位在并发下随机变化，单测永远复现不了；日志里同一个请求的月份名和语言头不一致"。下面依次切到 `C`、`en_US`、`de_DE`，观察整数千分位、金额小数点、月份名、`strxfrm` 排序都随全局 locale 变化，而 `"i".upper()` 始终是 `"I"`——证明"str 方法不受 locale 影响"。

```python
import locale
import time

when = (2024, 3, 15, 0, 0, 0, 0, 0, 0)


def snapshot(tag):
    grouped = locale.format_string("%d", 1234567, grouping=True)
    money = locale.format_string("%.2f", 1234.5, grouping=True)
    print(f"[{tag}] 整数={grouped!r} 金额={money!r} "
          f"月份={time.strftime('%B', when)!r} "
          f"排序={sorted(['z', 'ä'], key=locale.strxfrm)} "
          f"upper(i)={'i'.upper()!r}")


for name in ("C", "en_US.UTF-8", "de_DE.UTF-8"):
    locale.setlocale(locale.LC_ALL, name)
    snapshot(name)

locale.setlocale(locale.LC_ALL, "C")
```

**追问一**：为什么 `str.upper()` 没有土耳其 i 问题，而 `strcoll` 有？——Python 的 `str.upper/lower` 走 Unicode 默认大小写映射（`"i" -> "I"`），与进程 locale 无关；土耳其语的 `i/ı` 特例属于**语言敏感的 collation/casing**，只有 C 库的 `toupper_l`/`strcoll_l` 或显式 locale 的 ICU/Babel 才会处理。所以"Python 字符串大小写受 locale 影响"是常见误解；真正会被 locale 污染的是排序、数字/日期格式化、`gettext`。要语言敏感的大小写，用 `str.casefold()` 做通用折叠，或用 Babel/ICU 显式指定 locale。

**追问二**：`setlocale(LC_ALL, "")` 和显式 `"C.UTF-8"` 有什么区别？——空字符串表示"按环境变量（`LC_ALL`/`LC_*`/`LANG`）初始化"，结果依赖部署环境：本地可能是 `zh_CN.UTF-8`，容器里可能只有 `C`，行为不可复现；显式值则确定。生产建议启动时显式设一个固定 locale（或至少显式 `setlocale(LC_ALL, "C.UTF-8")`），并检查返回值/捕获 `locale.Error`。注意它只影响 C locale，不改变 Python 的源码/文件编码（那是 `PYTHONUTF8`/`encoding=` 的范畴，Q5028）。

## 背诵要点
- `locale.setlocale` 改的是进程级 C locale，所有线程共享且非线程安全；不能做请求级国际化。
- 受影响：数字/货币格式化、`strftime` 月份、`strcoll/strxfrm` 排序、gettext；不受影响：`str.upper/lower`（Unicode 默认映射）。
- 启动时固定 locale（`C.UTF-8`），业务格式化用显式 API/Babel；容器缺 locale 数据会 `locale.Error`。

## 复盘追问
- 并发下金额千分位/月份语言随机串，如何用进程级 locale 解释并修复？（全局状态、请求级 setlocale 竞争、显式格式化）
- 为什么 `"i".upper()` 不受土耳其 locale 影响？哪些 API 才真正语言敏感？（Unicode 默认 casing vs C 库 collation/casing）
