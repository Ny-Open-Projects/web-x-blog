---
title: [WCN-921] Islands 粒度怎么定：用「交互密度阈值」决定哪些区域值得水合
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-921：Islands 粒度怎么定：用「交互密度阈值」决定哪些区域值得水合

**答**：
- 结论先行：island 不是切得越碎越好——每个岛有独立水合成本（JS chunk + 依赖重建），粒度由「交互价值密度」决定：高频交互 × 用户可达性 ÷ 水合成本。
- 量化思路：给每个区域打「交互概率」（如加购按钮 0.8、商品详情文本 0.05）× 「水合字节数」，只水合密度超过阈值的岛（大促详情页典型：SKU 选择/加购水合，图文详情静态）。
- 边界：纯展示但含动态数据（库存倒计时）要单独切小岛，避免为一行数字水合整个商品卡。
- 过度切分的代价：岛之间状态同步变难、chunk 请求数增多（HTTP/2 下仍需解析执行），要用构建期合批把相邻小岛合并。
- 追问钩子：面试官问「阈值随设备变化吗」——答：应结合设备能力（navigator.hardwareConcurrency、save-data）动态调整，低端机降低水合量。

```javascript
// 交互密度评分 → 决定是否水合为 island
function shouldHydrate(region) {
  const density = region.interactProb * region.businessWeight /
                  Math.max(1, region.hydrateKB);
  return density >= region.threshold;
}
const regions = [
  { name: 'sku-select', interactProb: 0.8, businessWeight: 10, hydrateKB: 20, threshold: 0.2 },
  { name: 'desc-text',  interactProb: 0.05, businessWeight: 2,  hydrateKB: 8,  threshold: 0.2 },
];
regions.forEach(r => console.log(r.name, shouldHydrate(r)));
// sku-select true；desc-text false（保持静态 HTML）
```
