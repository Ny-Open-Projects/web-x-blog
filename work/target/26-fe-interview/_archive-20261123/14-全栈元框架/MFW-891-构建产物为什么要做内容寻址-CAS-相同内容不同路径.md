---
title: [MFW-891] 构建产物为什么要做内容寻址（CAS），相同内容不同路径怎么去重
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-891：构建产物为什么要做内容寻址（CAS），相同内容不同路径怎么去重

**答**：
- 结论：内容寻址存储用产物内容的哈希作为标识与文件名，相同内容无论来自哪个路径/哪次构建都只存一份，天然去重且缓存可跨部署复用。
- 落地：产物文件名带内容哈希（如 app.[hash].js），存储层按哈希索引；部署只需比对哈希决定是否上传。
- 追问钩子：内容寻址与「确定性构建」什么关系？——确定性是可复现的前提，内容寻址是结果：只有产物确定，哈希才能稳定复用。

```javascript
const store = new Map();   // hash -> content
function contentKey(content) {
  return 'sha256:' + hash(content);
}
async function put(path, content) {
  const key = contentKey(content);                    // 按内容，不按路径
  if (!store.has(key)) store.set(key, content);      // 相同内容只存一份
  return { path, key };
}
// 两个不同路径、相同内容 → 同一 key，去重
put('/a/logo.png', IMG).then(r1 =>
put('/b/logo.png', IMG).then(r2 =>
  console.log(r1.key === r2.key && store.size === 1))); // true
// 部署：哈希已存在则跳过上传
```
