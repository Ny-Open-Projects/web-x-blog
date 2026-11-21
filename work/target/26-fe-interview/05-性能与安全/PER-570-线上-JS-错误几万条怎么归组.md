---
title: [PER-570] 线上 JS 错误几万条怎么归组？错误指纹聚类算法怎么才能稳定？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-570：线上 JS 错误几万条怎么归组？错误指纹聚类算法怎么才能稳定？

**答**：
- 聚类的目标是同一根因的报错归为一组，稳定的关键是**指纹只保留语义不变的部分**：堆栈前三帧的函数名、剥离行号列号（bundle 变化漂移）、剥离动态参数与消息中的变量值（用正则把数字/URL/UUID 替换成占位符）。
- 聚合层级：指纹分组 -> 组内聚合同版本 -> 跨版本追踪（通过函数名+文件名 hash 归并，处理 sourcemap 前后的映射）。
- 追加维度：错误发生时的路由、组件树、用户操作序列（最近 5 步）作为组的上下文属性，帮助判断哪类页面哪类操作触发。
- 长尾治理：Top 组修复（占 80% 量），长尾用新增指纹告警机制——从未见过的指纹出现即通知，抓新事故。

```javascript

function stableFingerprint(err, meta) {
  const norm = (s) => s
    .replace(/:\d+:\d+/g, '')                            // 剥行列号
    .replace(/\b\d+\b/g, 'N')                            // 数字 -> N
    .replace(/https?:\/\/[^\s]+/g, 'URL')                // URL -> 占位
    .replace(/[0-9a-f]{8}-[0-9a-f]{4}/gi, 'UUID');
  const frames = (err.stack ?? '')
    .split('\n').slice(1, 4)                              // 前 3 帧
    .map(l => norm(l)).join('|');
  const msg = norm(err.message ?? '');
  return { fp: `${frames}#${msg}`,                          // 稳定指纹
    context: { route: meta.route, version: meta.version,   // 组上下文
      lastActions: meta.actions?.slice(-5) } };
}
// 分组策略：fp 完全相同归一组；topN 修复 + 新指纹出现即告警（抓新事故）
```
