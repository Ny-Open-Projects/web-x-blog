---
title: [RBL-396] 产物 sourcemap 的安全与私有化策略
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-396：产物 sourcemap 的安全与私有化策略

**答**:
- 泄露面：sourcemap 完整还原源码（业务逻辑/注释甚至 secret 引用）——公开产物目录带 map = 源码公开
- 策略分级：产物目录不含 map（隐藏 sourceMappingURL 或剥离）+ map 私有存储（监控平台/S3 内部）→ 错误上报时按需符号化
- 实现链：构建产出 map（用于分析/监控上传）→ 发布剥离（产物目录只留 js）→ 监控平台按 release 版本匹配 map 还原堆栈
- 校验：线上探测（产物目录不应可访问 .map）进发布检查清单——map 泄露是常见安全事故

```text
策略：产物剥离 map + 私有存储 + 按版本符号化
链路：构建产 map → 上传监控 → 发布剥离 → 线上探测不可访问
```
