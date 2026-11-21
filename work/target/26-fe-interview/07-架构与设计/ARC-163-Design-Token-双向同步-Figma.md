---
title: [ARC-163] Design Token 双向同步（Figma → 代码）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-163：Design Token 双向同步（Figma → 代码）如何设计？
**答**：
- 单向数据流为主：Figma Variables/Styles 是 token 唯一源头，导出流水线 Figma → tokens.json → 多平台产物（CSS vars/iOS/Android/SVG 主题），代码侧不手写颜色与间距——双向自由编辑必然分叉。
- 双向的合理范围：代码侧需要新增 token 时走"提案流程"（提 PR 修改 tokens.json + 同步回 Figma 侧建变量，设计师评审），即"受控的双向"而不是"双向自动同步"。
- 语义层分层：primitive（原始色板）→ semantic（语义别名：color-bg-primary）→ component（组件级引用），Figma 侧只暴露 semantic 层给设计师使用，改语义不影响原语层稳定。
- 落地关键：导出自动化（Figma API 定时/事件触发）、产物带版本与 diff 报告（设计侧改了什么一目了然）、未同步告警（Figma 与 tokens.json 哈希比对）。

```yaml
# Design Token 同步流水线
token_pipeline:
  source: figma-variables            # 唯一源头
  layers:
    primitive:  { example: "blue-500 #1E6FFF" }     # 原语层：设计师不可直接引用
    semantic:   { example: "color-action-primary → {primitive.blue-500}" }  # 设计师使用层
    component:  { example: "button-primary-bg → {semantic.color-action-primary}" }
  export_flow:
    - trigger: [figma webhook 变更事件, 每日定时]
    - pull: figma API 拉取 variables → tokens.json（入仓 PR，自动生成 diff 报告）
    - build: style-dictionary 产物
      outputs:
        - packages/tokens/css/variables.css
        - packages/tokens/ios/Tokens.swift
        - packages/tokens/android/tokens.xml
    - verify: 与 Figma 线上哈希比对，不一致告警（防手动改产物）
  reverse_proposal:                  # 受控反向：代码侧新增 token
    flow: 改 tokens.json PR → 设计师评审 → 合入后机器人同步建 Figma 变量
  governance:
    - 产物文件禁止手改（CI 校验 generated 标记）
    - semantic 层重命名需走 ADR（影响全站主题）
```
