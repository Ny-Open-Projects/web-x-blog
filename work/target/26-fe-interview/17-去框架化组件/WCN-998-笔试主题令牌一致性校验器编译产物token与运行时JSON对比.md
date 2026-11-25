---
title: [WCN-998] 手写主题令牌一致性校验器：编译产物 token 与运行时 JSON 对比
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-998：手写主题令牌一致性校验器：编译产物 token 与运行时 JSON 对比

**题目**：实现 `checkTokenSync(compiled, runtime)`，compiled 为编译期注入 token 的字符串（形如 `--primary:#1677ff;--radius:4px;`），runtime 为运行时 token 对象（ `{ primary:'#1677ff', radius:'8px' }` ）。要求：① 解析 compiled 的 CSS 变量声明为 `{ key: value }`；② 找出 runtime 中存在但 compiled 缺失或值不同的 key，记入 `drifts:[{key, compiled, runtime}]`；③ compiled 中有但 runtime 无的 key 记入 `orphans:[...]`；④ 返回 `{ drifts, orphans, synced }`，synced 为无 drift 且无 orphan；⑤ 输入非字符串/非对象时按空处理，不抛异常。请自足实现并给出可运行示例。

**答**：

```javascript
function checkTokenSync(compiled, runtime) {
  const c = {};
  if (typeof compiled === 'string') {
    compiled.split(';').forEach(decl => {
      const i = decl.indexOf(':');
      if (decl.startsWith('--') && i > 0) c[decl.slice(2, i).trim()] = decl.slice(i+1).trim();
    });
  }
  const r = (runtime && typeof runtime === 'object') ? runtime : {};
  const drifts = [], orphans = [];
  for (const [k, v] of Object.entries(r))
    if (!(k in c) || c[k] !== v) drifts.push({ key:k, compiled: c[k] || null, runtime: v });
  for (const k of Object.keys(c)) if (!(k in r)) orphans.push(k);
  return { drifts, orphans, synced: drifts.length===0 && orphans.length===0 };
}
console.log(checkTokenSync('--primary:#1677ff;--radius:4px;', { primary:'#f00', radius:'4px' }));
// drifts:[{key:'primary',compiled:'#1677ff',runtime:'#f00'}], orphans:[]
```

**评分点**：
- CSS 变量声明解析正确（--key:value）。
- drifts 检测缺失与值不同，记录 compiled/runtime 值。
- orphans 检测编译有运行时无的 key。
- 非字符串/非对象输入健壮、synced 判定正确。
- 示例可运行、输出正确。
