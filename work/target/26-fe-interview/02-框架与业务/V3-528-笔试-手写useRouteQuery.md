---
title: [V3-528] 笔试：手写 useRouteQuery（URL 参数双向绑定）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 路由]
type: 笔试题
---

## V3-528：笔试：手写 useRouteQuery

**答**：实现 `useRouteQuery(key, { mode = 'replace', transform })`：① 返回可写 ref：读 = route.query[key]，写 = router 替换 URL；② mode: replace（历史不堆栈，适合筛选器）/ push（分页场景保留后退）；③ 类型转换：数字/布尔/数组（?ids=1,2,3 ↔ [1,2,3]）双向；④ 多实例同 key 同步（路由是唯一真源，各实例 watch route）；⑤ 与组件卸载无关（URL 状态天然持久）。写出实现。

```javascript
import { ref, watch, customRef } from 'vue';
import { useRoute, useRouter } from 'vue-router';

export function useRouteQuery(key, { mode = 'replace', type = String, default: dflt } = {}) {
  const route = useRoute(), router = useRouter();
  const parse = (v) => {
    if (v == null) return dflt;
    if (type === Number) return +v;
    if (type === Boolean) return v !== 'false' && v !== '0';
    if (Array.isArray(type)) return String(v).split(',');
    return v;
  };
  const serialize = (v) => Array.isArray(v) ? v.join(',') : String(v);

  return customRef((track, trigger) => ({
    get() {
      track();
      return parse(route.query[key]);           // route 是响应式真源
    },
    set(v) {
      const q = { ...route.query };
      if (v == null || v === '' || v === dflt) delete q[key];
      else q[key] = serialize(v);
      router.push({ query: q }).catch(() => {});   // 重复导航 ignore
    },
  }));
}
// 用法: 筛选状态存 URL, 刷新/分享不丢
const page = useRouteQuery('page', { type: Number, default: 1 });
const tags = useRouteQuery('tags', { type: [String] });
page.value = 3;   // URL → ?page=3
```

**评分点**：
- customRef 双向读写直通路由（route 为真源，多实例天然同步）
- replace/push 模式的历史语义
- 类型双向转换（number/boolean/array）
- 删除语义（回默认值清 query）与重复导航容错
