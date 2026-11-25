---
title: [R19-440] 笔试：手写 useImmer（不可变更新的 proxy 草稿）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 状态管理]
type: 笔试题
---

## R19-440：笔试：手写 useImmer

**答**：实现简化 useImmer：① `update(recipe)`：recipe 接收「草稿」（Proxy）可直接 mutate——内部收集变更生成新对象（copy-on-write）；② 浅层实现：Proxy 拦截 set/delete 生成浅拷贝新对象；③ 嵌套：访问子对象时也包 Proxy（惰性）；④ hasChanged 判定（无变更不触发渲染）；⑤ 与手写展开运算符的成本对比说明。写出实现。

```javascript
function produce(base, recipe) {
  const copies = new Map();               // 原对象 → 浅拷贝
  const changed = { v: false };

  function proxy(obj) {
    return new Proxy(obj, {
      get(t, k) {
        const v = t[k];
        return (typeof v === 'object' && v !== null) ? proxy(v) : v;   // 惰性嵌套
      },
      set(t, k, nv) {
        if (Object.is(t[k], nv)) return true;
        if (!copies.has(t)) { copies.set(t, { ...t }); changed.v = true; }
        copies.get(t)[k] = nv;
        return true;
      },
      deleteProperty(t, k) {
        if (!copies.has(t)) { copies.set(t, { ...t }); changed.v = true; }
        delete copies.get(t)[k];
        return true;
      },
    });
  }
  const draft = proxy(base);
  recipe(draft);
  if (!changed.v) return base;                    // 无变更: 返回原引用(bailout 友好)
  // 重建树: 沿 copies 替换父级引用(简化: 顶层替换)
  return copies.get(base) ?? base;
}

export function useImmer(initial) {
  const [state, setState] = useState(initial);
  const update = useCallback((recipe) => {
    setState((s) => produce(s, recipe));          // 不可变更新进 setState
  }, []);
  return [state, update];
}
// 用法
const [user, updateUser] = useImmer({ name: 'a', tags: ['x'] });
updateUser((d) => { d.tags.push('y'); });         // 直接 mutate 草稿
```

**评分点**：
- copy-on-write 的 Proxy 拦截（浅拷贝 + 变更收集）
- 无变更返回原引用（bailout 兼容）
- 惰性嵌套 Proxy
- 顶层重建的简化局限（完整实现要沿路径替换父引用）
