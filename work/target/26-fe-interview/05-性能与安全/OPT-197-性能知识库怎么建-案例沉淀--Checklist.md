---
title: [OPT-197] 性能知识库怎么建（案例沉淀 + Checklist 固化）？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-197：性能知识库怎么建（案例沉淀 + Checklist 固化）？

**答**：
- 知识库解决"经验随人走"：每个专项结束沉淀三件套——案例卡（问题/根因/手段/实测收益/适用边界）、Checklist（评审与上线自查）、弹性系数（手段→指标收益的量化表，服务 OPT-184 排序）。
- Checklist 分场景固化：新页面上线 Checklist、发布 Checklist、大促 Checklist；形式用结构化 YAML 存仓库（可被 CI/机器人引用），文档站只做渲染。
- 案例卡模板强制字段：实测前后数据 + 样本量，没有数据不准入库（防止"据说有效"的经验污染）。
- 运营机制：案例卡关联到代码库 tag（可一键看示例实现）；季度盘点把高频 Checklist 项做成自动化（能进 CI 的进 CI，见 OPT-187）。

```yaml
# 一一对应：结构化案例卡 + Checklist（存 perf-knowledge/ 目录，CI 与文档站共用）
# perf-knowledge/cases/lcp-hero-preload.yaml
case:
  id: CASE-014
  title: LCP 首图 preload 与 fetchpriority
  symptom: 首页 LCP P75 3.8s，LCP 元素为轮播首帧大图
  root_cause: 图片在 CSS 渲染后才被发现，且与轮播逻辑竞争带宽
  action:
    - head preload + fetchpriority=high
    - 轮播首帧改静态直出，去掉接口依赖
    - AVIF 双源
  measured:
    before: { lcp_p75: 3800ms, sample: 142000 }
    after:  { lcp_p75: 2600ms, sample: 138000 }   # 无实测数据不准入库
  applicability: LCP 元素为图片的所有页面；SSR 需把 URL 注入 head
  ref_code: src/components/Hero/index.tsx
  author: perf-owner
  verified_by: ab-exp-042

# perf-knowledge/checklists/release.yaml
release_checklist:
  - id: rc-01
    item: 产物体积 diff 未见超预算新增（CI size-limit 通过）
    auto: true
  - id: rc-02
    item: 新增第三方脚本已过审批并 async 化
    auto: false
  - id: rc-03
    item: 新增图片均有宽高或 aspect-ratio
    auto: true
  - id: rc-04
    item: 关键接口有降级兜底与超时配置
    auto: false
  - id: rc-05
    item: 性能埋点覆盖新页面路由
    auto: true
```
