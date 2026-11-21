---
title: [Q1826] zipfile:压缩包的读取、校验与流式解压
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1826 · zipfile:压缩包的读取、校验与流式解压

> 难度:★★★☆☆ | 标签:zipfile, 数据管道, 校验

**问**:拿到大 zip 包,怎么只解压需要的成员、怎么确认整个包没坏?

**答**:zipfile 的三个层级:① namelist/getinfo 只读中央目录,不碰数据;② zf.open(member) 返回流式文件对象,按成员解压、支持 read(n) 分块——处理大包里的单个成员不需要落盘整个包;③ testzip() 逐成员读一遍做 CRC 校验,返回第一个坏成员名,全好返回 None。写侧 writestr/直接写 ZipFile 配 ZIP_DEFLATED。安全要点:解包外部 zip 前先逐个 getinfo 校验目标路径——成员名里的绝对路径与 .. 逃逸是真实攻击面,不允许解到目标目录之外;大成员用流式 copy 而不是 read() 全量进内存。CRC 失败抛 BadZipFile,管道上游要区分「包整体损坏」与「单成员损坏」给出不同告警。

```python
# file: code/01_语言核心与底层/q1826_zipfile_read.py
"""zipfile:压缩包的读取、校验与流式解压。"""
import os
import tempfile
import zipfile


def build_archive(path):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("docs/readme.txt", "第一版内容,足够长以便压缩生效")
        zf.writestr("docs/api.txt", "接口说明")
        zf.writestr("data/rows.csv", "id,name\n1,ada\n")


def inspect_archive(path):
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        info = zf.getinfo("docs/readme.txt")
        crc_ok = zf.testzip() is None          # None 表示全部成员 CRC 通过
        return names, info.file_size, info.compress_size, crc_ok


def stream_member(path, member, nbytes=12):
    with zipfile.ZipFile(path) as zf:
        with zf.open(member) as fh:            # 按成员流式读,不解压整个包
            return fh.read(nbytes).decode("utf-8")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as root:
        path = os.path.join(root, "demo.zip")
        build_archive(path)
        names, raw, comp, ok = inspect_archive(path)
        print("成员列表:", names)
        print("readme 原始/压缩字节:", raw, comp, "| CRC 全通过:", ok)
        print("流式读前 12 字节:", stream_member(path, "docs/readme.txt"))
```

**追问**:1) testzip 对大包太慢,有折中吗?——只校验关键成员或抽样;zip 读成员时本就会校验 CRC、失败即抛,所以「实际用到的成员自然被校验过」。2) 流式解压的要点?——zf.open(member) 逐块读,内存 O(块);读取时 CRC 校验内建;ZIP64 支持大包(member > 4GB);坏包 BadZipFile 在打开或读取时抛。3) 安全三查?——zip 炸弹(解压后大小超限,读前查 file_size 累计);路径穿越(成员名含 / 或绝对路径,提取前规范化);重名成员。4) 生产陷阱?——extractall 直接解到目标目录(炸弹+穿越双风险);大包整包读内存;密码 zip 要 pwd 参数且算法弱。
