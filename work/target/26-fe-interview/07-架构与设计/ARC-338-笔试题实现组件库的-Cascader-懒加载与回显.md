---
title: [ARC-338] 笔试题：实现组件库的 Cascader 懒加载与回显？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-338：笔试题：实现组件库的 Cascader 懒加载与回显？
**题目**：实现级联选择器：1) 逐级懒加载（loadData(options, level)）；2) 根据已选值数组回显路径（异步数据未加载时先占位再加载）；3) 搜索模式：任意层级匹配过滤；4) 单选回填 value 路径数组。
**评分点**：
- 懒加载状态管理正确（loading 子级、加载后渲染下一列）。
- 回显逻辑正确：逐级按 value 找到节点并触发其 loadData。
- 搜索过滤保留完整路径（祖先可见性继承）。
- 键盘/点击选中后 onChange 抛出完整路径数组。
```tsx
function Cascader({ loadData, value = [], onChange }) {
  const [cols, setCols] = useState<Record<number, Option[]>>({ 0: initialOptions });
  const [loading, setLoading] = useState<number | null>(null);
  const [activePath, setActivePath] = useState<number[]>([]);
  // 2) 回显：初始挂载时按 value 逐级展开
  useEffect(() => {
    (async () => {
      for (let lv = 0; lv < value.length; lv++) {
        setLoading(lv);
        const opts = lv === 0 ? cols[0] : await loadData(parentAt(lv - 1), lv);
        setCols(c => ({ ...c, [lv + 1]: opts }));
        setLoading(null);
        setActivePath(p => [...p, opts.findIndex(o => o.value === value[lv])]);
      }
    })();
  }, []);
  const pick = async (lv: number, idx: number) => {
    const opt = cols[lv][idx];
    setActivePath(p => [...p.slice(0, lv), idx]);
    if (!opt.isLeaf && !cols[lv + 1]) {
      setLoading(lv + 1);
      const kids = await loadData(opt, lv + 1);                             // 1) 懒加载
      setCols(c => ({ ...c, [lv + 1]: kids }));
      setLoading(null);
    }
    if (opt.isLeaf) {
      const path = activePath.concat(idx).map((i, level) => cols[level][i].value);
      onChange(path);                                                       // 4) 完整路径
    }
  };
  const filter = (kw: string) =>                                            // 3) 搜索
    deepFilter(cols[0], o => o.label.includes(kw));                         // 保留祖先链
  return <Columns cols={cols} activePath={activePath} onPick={pick} loading={loading} search={filter}/>;
}
```
