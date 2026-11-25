---
title: "[Q5093] shutil.rmtree 符号链接误删事故复盘"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5093 · shutil.rmtree 符号链接误删事故复盘

难度：P6 | 标签：事故复盘 | shutil.rmtree | 符号链接

**问**：一次清理临时目录的例行任务把线上共享目录删空了。复盘发现路径里混进了符号链接。`shutil.rmtree` 对 symlink 的真实行为是什么？这起事故的正确写法应该是怎样的？

**答**：
结论：`shutil.rmtree` 对"路径本身是符号链接"的情况会直接抛 `OSError("Cannot call rmtree on a symbolic link")`，这是 3.8 起的显式保护；真正的危险在**遍历中间层**：rmtree 默认递归进入目录，如果目录内部嵌套了指向外部（如 `/` 或共享卷）的符号链接目录，默认 `rmtree` 会拒绝吗？——3.8 后对 symlink 入口用 `os.lstat` 判断、只 unlink 不跟进，所以 rmtree 本身不会跟进目录符号链接。事故的真实根因通常是另一类：**清理目标路径本身来自拼接/环境变量**，rmtree 之前没有做边界校验，或者误用了 `rmtree(path, ignore_errors=True)` 把"路径不存在/权限错"和"路径是 symlink"一起吞了。
取舍：`onexc`/`onerror` 回调（3.12 改名 onexc，onerror 已弃用）不能替代边界校验；真正要做的是 rmtree 前的三道闸：`os.path.realpath` 后校验前缀白名单、`os.lstat` 确认 `S_ISDIR` 且非 symlink、清理路径加入告警日志。
实战：凡是"递归删除"代码，强制走一个 `safe_rmtree` 封装；`ignore_errors=True` 只允许在事后清理（幂等兜底）用，主路径禁用。

```python
import os, stat, shutil, tempfile, sys

def safe_rmtree(path: str, allowed_root: str) -> bool:
    """递归删除前的三道闸：realpath 前缀校验、lstat 类型确认、日志。"""
    real = os.path.realpath(path)
    root_real = os.path.realpath(allowed_root)
    # 闸1：realpath 解析所有 symlink 后，必须落在允许根内
    if os.path.commonpath([real, root_real]) != root_real:
        raise PermissionError(f"refuse to delete outside root: {real}")
    # 闸2：lstat 不跟进链接，确认目标本身是真目录
    st = os.lstat(path)
    if stat.S_ISLNK(st.st_mode):
        raise PermissionError(f"refuse to delete symlink: {path}")
    if not stat.S_ISDIR(st.st_mode):
        raise ValueError(f"not a directory: {path}")
    # 闸3：删除 + 错误回调不再吞掉权限问题
    def onexc(func, p, exc_info):
        print(f"[safe_rmtree] failed {func.__name__} on {p}: {exc_info[1]}")
        raise
    shutil.rmtree(path, onexc=onexc)
    return True

tmp = tempfile.mkdtemp()
vault = os.path.join(tmp, "vault")
os.makedirs(vault)
os.makedirs(os.path.join(vault, "work"))

# 场景1：目录里放一个指向外部的符号链接（rmtree 只 unlink 不跟进）
victim = os.path.join(vault, "work", "link_to_tmp")
os.symlink(tmp, victim)
safe_rmtree(os.path.join(vault, "work"), vault)
print("vault 幸存文件:", os.listdir(vault), "| link 只被 unlink:", not os.path.exists(victim))
print("tmp 仍然存在:", os.path.isdir(tmp))

# 场景2：直接对符号链接 rmtree → 显式拒绝
os.symlink(vault, os.path.join(tmp, "alias"))
try:
    shutil.rmtree(os.path.join(tmp, "alias"))
except OSError as e:
    print("rmtree(symlink) 拒绝:", e)

# 场景3：闸1 拦截越界路径
try:
    safe_rmtree(tmp, vault)  # 目标在 allowed_root 之外
except PermissionError as e:
    print("闸1 拦截:", e)
finally:
    for p in [os.path.join(tmp, "alias")]:
        if os.path.islink(p): os.unlink(p)
    shutil.rmtree(tmp, ignore_errors=True)
```

**追问 1**：为什么 `realpath` 是必须的而 `abspath` 不够？
- 追问 2 层：abspath 只做规范化不解析链接，`/vault/work/link/../x` 这类路径仍可能逃逸；realpath 把整条链解析到底再做前缀比较。
- 追问 3 层：realpath 校验存在 TOCTOU 窗口（校验后被换掉），高危场景要在校验后 open 并用 `os.fchmod`/fd 操作，或依赖容器/挂载隔离兜底。

**追问 2**：`onexc` 与旧 `onerror` 的差别？
- 追问 2 层：3.12 起 onerror 弃用，onexc 直接收异常实例而不是 (type, value, tb) 三元组；回调里不抛异常等于吞掉失败，rmtree 会继续。
- 追问 3 层：需要"尽力删、记清单"的批处理应在回调里收集失败路径统一上报，而不是 raise 中断整轮清理。

## 背诵要点
1. rmtree 不跟进符号链接（3.8+ 显式拒绝 symlink 目标、中间层只 unlink），事故根因多在路径拼接与 ignore_errors 吞错。
2. safe_rmtree 三道闸：realpath 前缀白名单 + lstat 确认非链接真目录 + 回调不吞错。
3. realpath 有 TOCTOU 窗口，高危删除要靠挂载隔离/容器边界兜底。

## 复盘追问
1. `ignore_errors=True` 应该用在哪个阶段？——幂等兜底阶段；主删除路径用它会把权限错静默化。
2. 多进程并发 rmtree 同一目录会怎样？——ENTDIR 不存在的竞态 FileNotFoundError，回调里要区分"已被别人删掉"与真失败。
