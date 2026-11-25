---
title: [RBL-903] 综合深水：构建器与边缘计算的职责再划分——什么该构建期做、什么该边缘做
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-903：综合深水：构建器与边缘计算的职责再划分——构建期 vs 边缘期

**答**:
- 职责划分的原则：**确定性优先在构建期，个性化优先在边缘期**——1) 构建期（确定性）：格式转换/代码裁剪/内容 hash/预推清单——同输入同输出，缓存友好；2) 边缘期（个性化/动态）：地域路由（RBL-14 目录）、A/B manifest 选择（RBL-888）、动态图片格式协商（CDN 边缘转格式兜底 RBL-719）、实时 CSP nonce（RBL-791）。
- 越界反模式：构建期做个性化（多区域全量构建爆炸 RBL-775 的反面——能用运行时注入的别编译 N 份）；边缘做确定性计算（每请求重复付同样的计算成本——边缘缓存可缓解但浪费）。
- 判定清单：该计算是否依赖请求上下文？（依赖 → 边缘）；结果是否可枚举缓存？（可枚举 → 构建期预生成 + 边缘查表）；失败的成本？（确定性计算失败在构建期暴露更便宜）。
- 边缘的「查表优先」：边缘计算的最好形态是「查预生成的表」（构建期算好所有可能结果 → 边缘按请求维度查）——把「计算问题」转成「存储问题」——与构建期 precompute（modulepreload 清单/能力清单 RBL-751）同一哲学。
- 追问钩子：为什么「构建期预生成 + 边缘查表」是边缘计算的黄金形态？——边缘的约束是 CPU 时间与冷启动（RBL-787），计算越少越好；构建期无此约束且产物可审计可缓存；查表让边缘的逻辑退化为「路由选择」——计算与存储的转换遵循两者的成本结构：构建期 CPU 免费且一次性，边缘 CPU 每请求付费。

```javascript
// 职责划分判定器
function classifyTask(task) {
  if (task.dependsOnRequestContext && !task.enumerable)
    return { place: 'edge', reason: '请求上下文依赖且不可枚举预生成' };
  if (task.enumerable && task.resultCount < 10_000)
    return { place: 'build-time', reason: '可预生成，边缘查表' };
  if (task.deterministic && !task.dependsOnRequestContext)
    return { place: 'build-time', reason: '确定性计算，构建期一次付清' };
  return { place: 'edge', reason: '动态个性化' };
}
// 场景归类
const ASSIGNMENTS = {
  '图片 webp 转换': 'build-time（主格式）+ edge（格式协商兜底）',
  'A/B manifest 选择': 'edge（用户维度分流 RBL-888）',
  '地域路由': 'edge',
  '内容 hash': 'build-time',
  'CSP nonce': 'edge（每响应唯一）',
};
```
