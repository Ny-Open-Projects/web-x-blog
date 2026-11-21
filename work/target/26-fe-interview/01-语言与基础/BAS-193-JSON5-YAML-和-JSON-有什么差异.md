---
title: [BAS-193] JSON5、YAML 和 JSON 有什么差异？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-193：JSON5、YAML 和 JSON 有什么差异？
**答**：
- JSON：键必须双引号、不许注释、不许尾逗号——机器友好但人不友好。
- JSON5：允许单引号、无引号键、注释、尾逗号、十六进制数，是"给配置用的 JSON"。
- YAML：缩进表达层级、标量可不加引号，还支持锚点引用与多文档；代价是缩进错一位就语义错，且有莫明安全坑（非字符串类型隐式转换）。

```yaml
# JSON：键必须双引号、无注释、无尾逗号
# JSON5：单引号、注释、尾逗号、十六进制都允许
# YAML：缩进即层级，标量可不加引号
version: 2
jobs:
  build:
    steps: [checkout, run-tests]   # 流式写法等价于列表
    retries: 3                     # 数字不加引号，解析为 number
```
