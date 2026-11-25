---
title: [WCN-948] 微前端多 bundle 场景 source map 的 sources 命名冲突与隔离
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-948：微前端多 bundle 场景 source map 的 sources 命名冲突与隔离

**答**：
- 结论先行：多个子应用各自上传 map 时，sources 里都叫 `src/index.ts` 会互相覆盖，监控平台按文件名索引就串味——要给 sources 加全局唯一前缀（场景名/版本）。
- 做法：构建时给每个 bundle 的 sources 加前缀（如 `app1:/src/index.ts`），或在上传时按 release + 子应用名做命名空间，平台索引键 = 前缀 + 路径。
- 同名 chunk 哈希碰撞：两应用都产出 `chunk-vendor.js` 时 map 归属错乱，用 contenthash 或加应用名前缀区分。
- 隔离策略：监控平台按子应用/tenant 分区存储 map，上报栈里带 app 标识，反查时限定分区，避免跨应用误匹配。
- 追问钩子：面试官问「共享依赖的 map 归谁」——答：共享 chunk 单独命名空间，多个应用引用同一份 map，按 release 关联而非复制。

```javascript
// 给 sources 加命名空间前缀，避免多 bundle 冲突
function prefixSources(map, appName) {
  return { ...map,
    sources: map.sources.map(s => `${appName}:${s}`) };
}
const mapA = { file: 'index.js', sources: ['src/index.ts'], mappings: 'AAAA' };
const mapB = { file: 'index.js', sources: ['src/index.ts'], mappings: 'AACA' };
console.log(prefixSources(mapA, 'app1').sources); // ['app1:src/index.ts']
console.log(prefixSources(mapB, 'app2').sources); // ['app2:src/index.ts']
// 平台索引键 = app + release + 路径，互不覆盖
```
