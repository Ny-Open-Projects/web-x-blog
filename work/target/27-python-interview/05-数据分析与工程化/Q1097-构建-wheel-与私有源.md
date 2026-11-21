---
title: [Q1097] 构建 wheel 与私有源
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1097 · 构建 wheel 与私有源

> 难度:★★★☆ | 标签:打包, wheel

**问**:公司内部包要发给多个团队,发 git 仓库链接好还是私有 PyPI 好?wheel 里到底有什么?

**答**:私有 PyPI + wheel 是正解:wheel 是已构建的发行格式(代码 + 元数据 + 入口点),安装不触发构建、快且可离线;版本化发布让依赖方锁定确定的产物,配合语义化版本与变更日志。构建用 `python -m build`(产出 sdist + wheel),上传到私有源(如 devpi/Nexus/Artifactory)用 twine;消费端 `--index-url` 指向私有源并回退公共源。包名、版本、平台标签都编码在 wheel 文件名里,解析规则要能说清。

```python
# file: code/05_数据分析与工程化/q1097_wheel_private_index.py
import re

WHEEL_RE = re.compile(r"^(?P<name>[^-]+)-(?P<version>[^-]+)-(?P<py>[^-]+)-(?P<abi>[^-]+)-(?P<platform>[^-]+)\.whl$")

def parse_wheel(filename):
    m = WHEEL_RE.match(filename)
    if not m:
        raise ValueError("非法 wheel 文件名")
    return m.groupdict()

if __name__ == "__main__":
    name = "my_pkg-1.2.0-cp312-cp312-manylinux_2_17_x86_64.whl"
    print(parse_wheel(name))
    # 构建:python -m build -> dist/*.whl + *.tar.gz
    # 上传:twine upload --repository-url https://pypi.example.com/simple/ dist/*
    # 安装:uv pip install my-pkg --index-url https://pypi.example.com/simple/
```

**追问**:
- 追问 1:sdist 和 wheel 都发布还是只发 wheel?—— 两者都发,sdist 兜底特殊平台从源码构建,wheel 覆盖主流平台加速安装。
- 追问 2:纯 Python 包的平台标签是什么?—— py3-none-any,无 C 扩展全平台通用;含扩展则绑定解释器与平台。
