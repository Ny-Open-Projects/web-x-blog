---
title: [ZSM-631] queryKey 的 hashKey 规范：对象键序无关是怎么实现的
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-631：queryKey 的 hashKey 规范：对象键序无关是怎么实现的

**答**：
- QueryCache 用 `hashKey(queryKey)` 序列化成字符串做 Map 的 key。规则：数组递归逐位、对象**键排序后**序列化、数字/布尔/字符串原样、undefined 转空、日期转 ISO——所以 `{ page: 1, size: 2 }` 与 `{ size: 2, page: 1 }` 是同一缓存条目（不会因为字面量书写顺序不同而缓存分裂）。
- 序列化陷阱：1) Date 转字符串——写 Date 进 key 和读出来比较要注意时区；2) **值为函数/Symbol 直接丢弃**（JSON 不支持）——带函数的 key 是反模式；3) 大对象进 key（整个表单 draft）会撑爆 hash 成本与缓存空间——key 应是「查询身份的最小标识」（id + 页码 + 排序），不是数据本身。
- 自定义序列化：`queryKeyHashFn` 可替换（比如忽略某些字段：`({ todo }) => todo.id`），用于「key 里带无关字段但要共享缓存」的场景。
- 结构化 key 分层设计：`['domain', 'resource', id, scope, params]`——第 0 位是域（方便大前缀 invalidate），中间是资源与 id，最后是参数。团队规范固化这个模板，invalidate 才有确定性。
- 追问钩子：`queryKey` 数组的**可变对象引用**——组件每次渲染 new 一个对象进 key 会导致 hash 每次不同（对象键序无关救不了「值不同」），key 必须引用稳定。

```javascript
// hashKey 源码骨架
function hashKey(queryKey) {
  return JSON.stringify(queryKey, (_, val) =>
    isPlainObject(val)
      ? Object.keys(val).sort().reduce((acc, k) => {   // 键排序
          acc[k] = val[k]
          return acc
        }, {})
      : val
  )
}

// 序列化等价性
hashKey(['todos', { page: 1, size: 2 }])   // ["todos",{"page":1,"size":2}]
hashKey(['todos', { size: 2, page: 1 }])   // 完全相同字符串 → 同一缓存

// 分层 key 模板
const qk = {
  all: ['todos'],
  lists: () => [...qk.all, 'list'],
  list: (filters) => [...qk.lists(), filters],       // ['todos','list',{page,sort}]
  details: () => [...qk.all, 'detail'],
  detail: (id) => [...qk.details(), id],
}
queryClient.invalidateQueries({ queryKey: qk.lists() })  // 删改后失效所有列表视图

// queryKeyHashFn：忽略无关字段
useQuery({
  queryKey: ['detail', id, { traceId }],        // traceId 用于日志不想分裂缓存
  queryKeyHashFn: (key) => JSON.stringify([key[0], key[1]]),   // 只 hash 前两位
})
```
