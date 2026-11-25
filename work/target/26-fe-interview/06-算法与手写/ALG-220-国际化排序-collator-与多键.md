---
title: [ALG-220] 国际化列表排序：中文按拼音、多语言混合按区域排序（Intl.Collator，O(n log n)）
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-220：国际化列表排序：中文按拼音、多语言混合按区域排序（Intl.Collator，O(n log n)）
**答**：通讯录要按中文拼音排序（'张三' 在 '李四' 前后取决于拼音），混合英文/数字按区域规则。`localeCompare` 每次调用慢（内部构造 collator），用 `Intl.Collator` 实例复用，性能差 10 倍以上。

**思路**：`new Intl.Collator('zh', { sensitivity: 'base', numeric: true })` 复用比较器；多键排序（先姓氏后名字）用比较器链；稳定排序与 null 容错。

```javascript
const zhCollator = new Intl.Collator('zh-Hans-CN', { numeric: true, sensitivity: 'base' });
const enCollator = new Intl.Collator('en', { numeric: true });

function sortContacts(list, locale = 'zh') {
  const c = locale.startsWith('zh') ? zhCollator : enCollator;
  return [...list].sort((a, b) => {                    // 浅拷贝不改原数组
    // 多键：先按 sortKey（姓氏拼音），同则按 name，null 兜底排最后
    if (a.sortKey == null && b.sortKey == null) return 0;
    if (a.sortKey == null) return 1;
    if (b.sortKey == null) return -1;
    return c.compare(a.sortKey, b.sortKey) || c.compare(a.name, b.name);
  });
}
sortContacts([{ name: '张三', sortKey: 'zhang' }, { name: '李四', sortKey: 'li' }, { name: 'apple', sortKey: 'apple' }]);
// zh 排序 => apple, 李四(li), 张三(zhang)（拼音序）
// 性能要点：Collator 实例化昂贵（初始化区域规则），必须模块级复用；
// 10 万条排序 + 每次 localeCompare ≈ 3s；复用 Collator ≈ 200ms
// numeric: true 让 'v2' 排在 'v10' 前（自然数字序）
```

**评分点**：
- Intl.Collator 实例复用（模块级）——性能核心点，能说出 localeCompare 每次实例化的开销。
- 多键比较链 + null 容错；浅拷贝不改原数组。
- numeric/sensitivity 选项语义。
- 能对应场景：通讯录/国际化列表的本地化排序。
