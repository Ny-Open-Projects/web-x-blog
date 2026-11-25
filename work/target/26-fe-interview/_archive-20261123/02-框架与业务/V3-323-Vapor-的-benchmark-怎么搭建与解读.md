---
title: [V3-323] Vapor 的 benchmark 怎么搭建与解读？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-323：Vapor 的 benchmark 怎么搭建与解读？
**答**：
- 参照 js-framework-benchmark 思路：建 1000/10000 行表格，测「创建、部分更新、替换全部、随机选中、清空」五类操作耗时。
- 用 CDP（Chrome DevTools Protocol）脚本自动化点击 + performance API 计时，多轮取中位数，排除 GC 抖动（触发前 gc 或加大样本）。
- 对照组：同一组件的 VDOM 版、Solid 版、原生 JS 版；记录版本号与机器环境保证可比。
- 解读重点：高频小更新（选中一行）Vapor 优势最明显，因为更新路径是单点 setText；大结构替换两者接近（都是重建 DOM）。
- 报告要写「操作语义 + 数据规模 + 版本」，避免裸数字。
