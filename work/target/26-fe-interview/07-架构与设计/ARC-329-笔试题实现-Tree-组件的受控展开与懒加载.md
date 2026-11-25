---
title: [ARC-329] 笔试题：实现 Tree 组件的受控展开与懒加载？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-329：笔试题：实现 Tree 组件的受控展开与懒加载？
**答**：实现 Tree 组件核心：1) 受控 expandedKeys + 非受控 defaultExpandedKeys 双模式；2) 节点懒加载（无 children 且 hasChildren → 展开时触发 loadData）；3) 加载态与失败重试；4) 选中受控（selectedKeys 单选）。
**评分点**：
- 受控/非受控双模式合并逻辑正确（expanded 集合运算）。
- 懒加载触发时机正确（首次展开才触发，缓存不重复请求），loading 态渲染。
- 失败重试（点击重试重新加载）与展开状态一致性（失败时收起或保留 loading 可重试）。
- key 使用正确（列表渲染 key 稳定）。
```tsx
function Tree({ data, expandedKeys: ek, defaultExpandedKeys = [], selectedKeys, onSelect, loadData }) {
  const [inner, setInner] = useState(new Set(defaultExpandedKeys));       // 1) 双模式
  const expanded = ek ? new Set(ek) : inner;
  const [loading, setLoading] = useState(new Map());                      // key → attempt
  const toggle = async (node) => {
    const next = new Set(expanded);
    if (next.has(node.key)) { next.delete(node.key); ek ? onSelectChange() : setInner(next); return; }
    next.add(node.key);
    if (node.hasChildren && !node.children) {                             // 2) 懒加载
      const attempt = (loading.get(node.key) ?? 0) + 1;
      setLoading(m => new Map(m).set(node.key, attempt));
      try {
        const kids = await loadData(node);                                // 3) 失败重试：attempt 供显示
        node.children = kids;                                             // 缓存挂回（或上抛更新）
        setLoading(m => { const n = new Map(m); n.delete(node.key); return n; });
      } catch { /* 保留 loading，UI 显示"加载失败，点击重试" */ }
    }
    ek ? undefined : setInner(next);
  };
  return <ul role="tree">{data.map(n =>
    <li key={n.key} role="treeitem" aria-expanded={expanded.has(n.key)}>
      <span onClick={() => { toggle(n); selectedKeys !== undefined && onSelect?.(n.key); }}
        aria-selected={selectedKeys === n.key}>{n.title}</span>
      {loading.has(n.key) && <Spinner attempt={loading.get(n.key)}/>}
      {expanded.has(n.key) && n.children && <Tree data={n.children} {...passDown}/>}
    </li>)}</ul>;
}
```
