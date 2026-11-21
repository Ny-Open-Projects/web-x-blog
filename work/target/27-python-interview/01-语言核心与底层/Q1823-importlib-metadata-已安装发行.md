---
title: [Q1823] importlib.metadata:已安装发行版的版本与元数据探测
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1823 · importlib.metadata:已安装发行版的版本与元数据探测

> 难度:★★☆☆☆ | 标签:importlib.metadata, 打包, 内省

**问**:不靠 pip 子进程,运行期怎么查某个发行版的版本与元数据?

**答**:importlib.metadata(3.8+)读的是安装时写进 dist-info 的元数据,零外部依赖:version(name) 拿版本,缺失抛 PackageNotFoundError——探测一律 try 包住;metadata(name) 返回 email.Message 风格对象,Summary、Author 等字段用 .get 取;entry_points 看注册的入口(3.9 与 3.10+ 的 API 形态不同,兼容代码要先判 hasattr),packages_distributions 给出「顶层导入名到发行版」的反查(3.10+ 才有)。demo 探测 setuptools/pip/wheel 等常见发行版并容错不存在者。应用场景:依赖诊断与能力检测、启动日志里写版本、插件系统读第三方包声明的入口点;与 Q507 的 zipapp 打包、Q521 的配置读取同属「包工程」基础设施。

```python
# file: code/01_语言核心与底层/q1823_pkg_metadata.py
"""importlib.metadata:已安装发行版的版本与元数据探测。"""
import importlib.metadata as md


def probe(dists):
    found = []
    for name in dists:
        try:
            found.append((name, md.version(name)))
        except md.PackageNotFoundError:
            continue
    return found


def show_first(found):
    if not found:
        print("纯标准库环境,没有可探测的第三方发行版")
        return
    name, ver = found[0]
    meta = md.metadata(name)
    print("首个发行版:", name, ver)
    print("Summary:", (meta.get("Summary") or "")[:56])
    if hasattr(md, "packages_distributions"):     # 3.10+ 才有该 API
        mapping = md.packages_distributions().get(name, [])
        print("顶层模块映射:", sorted(mapping)[:3] or "无")


if __name__ == "__main__":
    found = probe(["setuptools", "pip", "wheel", "six", "nonexistent-xyz"])
    print("探测到:", found)
    show_first(found)
```

**追问**:1) 为什么查版本用 metadata 而不是 import 后读 __version__?——不是所有包都有 __version__,且那查的是「导入单元」而 metadata 查的是「安装单元」,多模块发行版下两者不一一对应。2) metadata 的能力面?——version/Requires/entry_points;3.10+ entry_points(group=...) 返回可 select 的对象;插件发现走 entry points 是发行级标准(比目录扫描更解耦)。3) 与运行环境的关系?——查的是当前解释器 site-packages 里的安装记录;editable 安装与离线环境可能没有 metadata(PackageNotFoundError);依赖检查要 catch。4) 生产陷阱?——把 __version__ 当真值做依赖仲裁;在冻结/打包环境假设 metadata 可查;entry points 解析老 API(group 参数前返回 dict)。
