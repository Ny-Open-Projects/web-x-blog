---
title: [AIC-792] 笔试：实现 IDP 中 AI 能力的目录服务
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-792：笔试：实现 IDP 中 AI 能力的目录服务

**需求**：实现 `createCatalog()`，返回 `{ upsert(cap), search(query), detail(name), tag(name, tags) }`。`cap`: `{ name, description, owner, tags: string[], score }`。规则：1) upsert：按 name 覆盖更新；2) search：`query` 为 `{ tags?: string[], keyword?: string, minScore?: number }`，tags 为「包含全部」（AND）；keyword 在 name/description 中不区分大小写匹配；minScore 过滤低于分数的；结果按 score 降序、name 字典序；3) detail：不存在返回 null；4) tag：给指定能力追加 tags（去重），不存在抛 NOT_FOUND；5) 返回的对象均为浅拷贝（外部修改不影响内部）。边界：search 无匹配返回 []；cap 缺 tags 按 []；score 缺按 0。

**答**：
- 结论先行：目录服务是 IDP 能力可发现的基础；tags 用 AND 匹配才能精确收窄，OR 匹配会返回太多噪声。
- 浅拷贝返回是「防御性编程」——调用方修改返回对象不应污染目录内部状态，否则会出现难以追踪的数据篡改。
- 追问钩子：为什么结果要按 score 降序再 name 兜底？——高分优先符合「先看到最好的」直觉，name 兜底保证同分结果稳定可复现。

```javascript
function createCatalog() {
  const store = {};
  const copy = c => c ? { ...c, tags: [...(c.tags ?? [])] } : null;
  return {
    upsert(cap) { store[cap.name] = { ...cap, tags: cap.tags ?? [], score: cap.score ?? 0 }; },
    search(query = {}) {
      const kw = (query.keyword ?? '').toLowerCase();
      return Object.values(store)
        .filter(c => (query.tags ?? []).every(t => c.tags.includes(t)))
        .filter(c => !kw || (c.name + ' ' + c.description).toLowerCase().includes(kw))
        .filter(c => c.score >= (query.minScore ?? 0))
        .sort((a, b) => b.score - a.score || a.name.localeCompare(b.name))
        .map(copy);
    },
    detail(name) { return copy(store[name]); },
    tag(name, tags = []) {
      if (!store[name]) throw { code: 'NOT_FOUND' };
      store[name].tags = [...new Set([...store[name].tags, ...tags])];
    },
  };
}
const cat = createCatalog();
cat.upsert({ name: 'review', description: 'Code Review', owner: 'platform', tags: ['quality'], score: 9 });
cat.upsert({ name: 'complete', description: '代码补全', owner: 'platform', tags: ['speed'], score: 7 });
cat.tag('review', ['ai']);
console.log(cat.search({ tags: ['quality'], keyword: 'review' }).map(c => c.name)); // ['review']
console.log(cat.search({ minScore: 8 }).length === 1);
const d = cat.detail('review'); d.tags.push('x');
console.log(cat.detail('review').tags.includes('x')); // false —— 浅拷贝隔离
```


**评分点**：
- tags AND 匹配、keyword 不区分大小写
- score 降序 + name 字典序兜底
- 浅拷贝隔离防外部篡改
- 边界（无匹配 / 缺字段按默认）
