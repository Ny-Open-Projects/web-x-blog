---
title: [NODE-805] 笔试题——实现页面缓存键生成器（全维度 + 校验）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-805：手写缓存键

**需求与边界**：
- 需求：页面缓存键（SCN-NODE-718）——① 键维度声明（url/profile/gray/locale/user 类型——漏维度串数据防御）；② 键生成（hash 稳定排序——SCN-BLD-254 确定性）；③ 键维度完整性校验（CI 校验——影响响应的维度全在键里，SCN-NODE-692 Vary 联动）；④ 缓存键碰撞测试（哈希碰撞概率——键空间评估）。
- 边界：① 键的稳定排序（维度顺序无关——SCN-BLD-254）；② 用户级键的谨慎（命中低+泄露——只对高价值页面启用，SCN-NODE-718）；③ 键长度（hash 截断——碰撞概率评估）。

**答**：
```javascript
const KEY_DIMS = ['url', 'profile', 'gray', 'locale', 'userTier'];   // 声明维度（CI 校验清单）
function pageCacheKey(req) {
  const dims = {
    url: req.url, profile: req.profile ?? 'default',
    gray: req.grayBucket ?? 'stable', locale: req.locale ?? 'zh',
    userTier: req.user?.tier ?? 'anon',                // 全维度（SCN-NODE-718）
  };
  return sha256(KEY_DIMS.sort().map(k => `${k}=${dims[k]}`).join('|')).slice(0, 24);   // 稳定排序（SCN-BLD-254）
}
// CI 校验：响应依赖维度 ⊆ 键维度（SCN-NODE-692 Vary 联动）
test('缓存键维度完整性', () => {
  const responseDeps = collectResponseDims('/home');   // 响应依赖的请求维度
  responseDeps.forEach(d => assert(KEY_DIMS.includes(d), `缓存键漏维度 ${d}`));
});
// 碰撞评估
const keyspace = 1e12, hashes = 24 * 4;                // 24 hex 位
assert(collisionProb(keyspace, hashes) < 1e-9);
```

**评分点**:
- 键维度声明化 + CI 完整性校验（漏维度防御——SCN-NODE-718）。
- 稳定排序 hash（SCN-BLD-254 确定性）。
- 碰撞概率评估（键空间工程化）。
- userTier 分级（谨慎的用户级缓存——SCN-NODE-718）。
