---
title: [AIC-686] 平台化的 Prompt 资产库怎么管版本和复用？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-686：平台化的 Prompt 资产库怎么管版本和复用？

**答**：
- 结论先行：**Prompt 是资产不是文本——要像代码一样「版本化、可评测、可追溯、可复用」**。散落在各人笔记里的 prompt 是不可管理的；平台化就是把它们收进统一资产库（AIC-141 SOP 库 / AIC-358 Agent 技能）。
- 资产库要素：1) **结构化元数据**：每个 prompt 有 id、版本、适用场景、作者、依赖变量、关联评测集；2) **版本管理**：改 prompt 要像改代码一样走 git，保留历史版本，支持回滚（AIC-101 规则版本化）；3) **评测绑定**：每个 prompt 关联一组评测用例，修改后跑评测确认没退化（AIC-204 规则验证）；4) **复用机制**：按场景检索复用，而非每人重写——「写 PR 描述的 prompt」全团队用同一份经过验证的。
- 平台能力：提供 prompt 的 CRUD、搜索、版本 diff、评测跑分、灰度发布（AIC-696）——让 prompt 从「个人技巧」变成「团队基建」。
- 关键区分：**prompt 模板（带变量的骨架）vs 具体 prompt（填充后）**——资产库存模板，运行时填变量渲染（AIC-414 模板渲染器）。
- 追问钩子：为什么 prompt 修改必须「跑评测」而不能「凭感觉更好」？——因为 prompt 的改动效果反直觉：加一句约束可能提升 A 场景却搞砸 B 场景；没有评测集，你不知道改动是全方面提升还是「拆东墙补西墙」——评测是 prompt 版本管理的灵魂。

```typescript
type PromptAsset = { id: string; version: number; template: string; variables: string[]; evalPassRate: number };

class PromptRegistry {
  private assets = new Map<string, PromptAsset[]>();
  publish(asset: PromptAsset) {
    const versions = this.assets.get(asset.id) || [];
    versions.push(asset); // 追加版本，不覆盖历史
    this.assets.set(asset.id, versions);
  }
  render(id: string, vars: Record<string, string>, version?: number): string {
    const versions = this.assets.get(id) || [];
    const asset = version
      ? versions.find(a => a.version === version)
      : versions[versions.length - 1];
    if (!asset) throw new Error('prompt not found');
    return asset.template.replace(/\{(\w+)\}/g, (_, k) => vars[k] ?? `{${k}}`);
  }
}

const reg = new PromptRegistry();
reg.publish({ id: 'pr-desc', version: 1, template: '根据 {commits} 写PR描述', variables: ['commits'], evalPassRate: 0.7 });
reg.publish({ id: 'pr-desc', version: 2, template: '根据 {commits} 和 {issue} 写PR描述', variables: ['commits','issue'], evalPassRate: 0.85 });
console.log(reg.render('pr-desc', { commits: 'c1', issue: 'i1' }).includes('i1'));
console.log(reg.render('pr-desc', { commits: 'c1', issue: 'i1' }, 1).includes('i1') === false); // 旧版无issue
```
