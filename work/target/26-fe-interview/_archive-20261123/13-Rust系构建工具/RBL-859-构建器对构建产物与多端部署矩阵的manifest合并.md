---
title: [RBL-859] 场景题：多端部署矩阵的 manifest 合并——多目标产物的聚合与冲突消解
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-859：场景题：多端部署矩阵的 manifest 合并——多目标产物聚合与冲突消解

**答**:
- 多端部署（web 应用 + CDN 静态 + SSR 服务 + 边缘函数）各自构建产出独立 manifest——聚合为一个「部署视图」：1) **冲突消解规则**（同文件名多端产出：优先级序 SSR > edge > CDN > web——或显式声明归属）；2) 引用完整性（web manifest 引用的 chunk 在聚合视图中存在——跨端引用校验 RBL-656 的多 manifest 版）；3) 部署计划的生成（聚合视图 → 按端分组的部署步骤）。
- 冲突的预防优于消解：文件名空间分端隔离（web: /assets/**、edge: /edge/**）——命名约定让冲突天然消失；聚合器只处理「历史遗留的重名」。
- 聚合的一致性校验：所有端的 buildId 记录（跨端引用的版本对齐——web html 引用的 SSR api 版本必须一致部署——原子性跨端扩展 RBL-700）；「部分端发布」的校验（只发 web 不发 SSR → 引用错配门禁）。
- 合并的确定性：聚合结果可复现（输入 manifest 相同输出相同——部署审计 RBL-773 的输入），合并顺序显式化（按优先级排序处理）。
- 追问钩子：为什么「文件名空间隔离」比「冲突消解规则」更值得投入？——消解规则依赖「谁记得住优先级」（隐性知识，改错一顺序全盘错），隔离是结构性预防（规则写进目录约定，新人零学习成本）；工程上的冲突最好在设计层消灭而不是在执行层仲裁——这也是「约定优于配置」的深层逻辑。

```javascript
// 多端 manifest 聚合
const PRECEDENCE = ['ssr', 'edge', 'cdn', 'web'];
function mergeManifests(manifests) {
  const merged = { version: '1.0', outputs: {}, deployments: [] };
  for (const end of PRECEDENCE) {                        // 优先级序处理：后写不覆盖先写
    for (const f of manifests[end]?.files ?? []) {
      if (merged.outputs[f.name])
        warn(`重名冲突: ${f.name} 同时属于 ${merged.outputs[f.name].end} 与 ${end}——按优先级保留`);
      else merged.outputs[f.name] = { ...f, end };
    }
    merged.deployments.push({ end, buildId: manifests[end]?.buildId });
  }
  // 跨端引用校验
  for (const [name, o] of Object.entries(merged.outputs))
    for (const ref of o.refs ?? [])
      if (!merged.outputs[ref]) fail(`跨端引用缺失: ${name} -> ${ref}`);
  return merged;
}
```
