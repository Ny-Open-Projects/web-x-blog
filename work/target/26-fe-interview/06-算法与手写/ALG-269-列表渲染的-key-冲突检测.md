---
title: [ALG-269] 列表 key 冲突检测：重复 id 的检测与稳定化（服务端数据异常的防御性处理）？
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-269：列表 key 冲突检测：重复 id 的检测与稳定化（服务端数据异常的防御性处理）？
**答**：服务端偶发返回重复 id（分页重叠/bug）——React key 冲突导致渲染错乱。防御：渲染前检测重复 id → 稳定化（重复项加后缀 or 过滤 + 上报），开发期报错、生产期静默降级。

**思路**：单遍 Set 检测 → 冲突处理策略（dev: throw 让测试发现；prod: 附加唯一后缀保留数据 + 上报缺陷）。

```javascript
function stabilizeKeys(items, { env = 'prod' } = {}) {
  const seen = new Map();                                 // id -> 出现次数
  const out = items.map((item) => {
    const c = seen.get(item.id) ?? 0;
    seen.set(item.id, c + 1);
    return c === 0 ? item : { ...item, __dupIndex: c, key: `${item.id}#${c}` };   // 重复项加序号后缀
  });
  const dupes = [...seen].filter(([, c]) => c > 1);
  if (dupes.length) {
    report?.({ type: 'dup-ids', ids: dupes.map(([id]) => id), count: dupes.length });   // 缺陷上报
    if (env === 'dev') console.error('重复 id（key 冲突）:', dupes);   // dev 期显式暴露
  }
  return out;
}
// 渲染：items.map((item) => <Row key={item.key ?? item.id} .../>)
// 策略分级：
// dev: throw/console.error —— 测试期发现服务端 bug
// prod: 后缀稳定化（#0 #1）—— 用户看到数据（重复可见），渲染不炸
// 上报：dup-ids 事件 → 服务端侧修根因（前端是防御不是修复）
```

**评分点**：
- 单遍检测 + 稳定化策略分级（dev 报错/prod 降级）——本题核心。
- 后缀 key 保持数据可见（不是静默丢数据）。
- 缺陷上报闭环（前端防御、服务端修根因）。
- Map 计数（不只 Set——需要知道第几次重复以生成稳定后缀）。
