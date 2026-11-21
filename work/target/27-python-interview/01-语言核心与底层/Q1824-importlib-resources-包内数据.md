---
title: [Q1824] importlib.resources:包内数据文件的规范访问
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1824 · importlib.resources:包内数据文件的规范访问

> 难度:★★★☆☆ | 标签:importlib.resources, 数据文件, 打包

**问**:包里带了模板与配置数据,为什么 open("pkg/data.txt") 是错的,规范姿势是什么?

**答**:按字符串路径 open 绑定了「包已被解压到文件系统」这个假设,zip 安装、frozen 二进制、自定义 loader 下都会碎。importlib.resources 提供按包定位的 Traversable 抽象:3.9+ 用 files(pkg).joinpath("greeting.txt").read_text(encoding=...),拿到的是与加载器配套的资源视图,zipapp 里照样读(Q507 场景);3.8 及更早是 read_text/read_binary 函数式 API,写兼容层用 hasattr 判断。demo 在临时目录造出带资源的包并读回中文内容。约定:资源放包目录内、按数据名管理;写资源文件是反模式——资源应当只读,可变状态进用户数据目录。资源路径不是文件路径,不能直接拼接后 open,一切读写经 Traversable。

```python
# file: code/01_语言核心与底层/q1824_pkg_resources.py
"""importlib.resources:包内数据文件的规范访问。"""
import importlib.resources
import os
import sys
import tempfile


def build_pkg(root):
    pkg = os.path.join(root, "resx")
    os.makedirs(pkg)
    with open(os.path.join(pkg, "__init__.py"), "w") as f:
        f.write("")
    with open(os.path.join(pkg, "greeting.txt"), "w", encoding="utf-8") as f:
        f.write("你好,资源文件")
    return "resx"


def read_via_api(pkg_name, pkg_root):
    sys.path.insert(0, pkg_root)
    try:
        mod = importlib.import_module(pkg_name)
        if hasattr(importlib.resources, "files"):         # 3.9+ Traversable
            res = importlib.resources.files(mod).joinpath("greeting.txt")
            return res.read_text(encoding="utf-8")
        return importlib.resources.read_text(mod, "greeting.txt")
    finally:
        sys.path.pop(0)


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as root:
        pkg_name = build_pkg(root)
        print("读到:", read_via_api(pkg_name, root))
```

**追问**:1) 想列出包里全部资源怎么办?——files(pkg).iterdir() 返回 Traversable 迭代,可递归;它走加载器抽象,不依赖文件系统语义,与 glob 不同。2) 规范访问的意义?——open_text/open_binary(files(pkg).joinpath(...)) 在 zipapp/打包环境同样工作;__file__ 拼 path 假设真实文件,打包后崩(Q507)。3) 版本与迁移?——3.9+ importlib.resources.files 新 API;3.7/3.8 旧函数(path/read_text 模块级)已弃用;wheel 要把数据文件打进包目录(package_data)。4) 生产陷阱?——用 os.path 直接拼 __file__;数据文件没进打包配置;对 Traversable 做文件系统专有操作(要 importlib.resources.as_file)。
