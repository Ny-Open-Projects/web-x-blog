---
title: [MP-212] Taro 的 setData 链路怎么量化分析？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-212：Taro 的 setData 链路怎么量化分析？
**答**：
- 链路：setState → React 重渲染 → Taro diff → payload 序列化 → 跨线程传输 → 渲染层 diff 渲染。
- 量化工具：wx.getPerformance（setData 耗时）、Taro DevTools 面板（单次数据量）、console.time 包 setState。
- 优化核对清单：单次数据量（<256KB）、调用频率（合并/节流）、深层路径 patch（避免数组全量）、大列表虚拟化。
- 高频场景专项：输入框（controlled input 在 Taro 下的受控回显延迟）——用非受控或 IME 事件优化。
- 度量即预算：把「页面关键交互 setData 量」写入性能门禁。
