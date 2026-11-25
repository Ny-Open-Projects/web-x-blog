---
title: [AGT-475] 笔试题——实现任务验收断言器（多类型断言+部分得分+证据校验）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-475：手写验收断言器：文件/状态/内容/证据四类断言、分级计分、拒答加分

**需求与边界**：
- 输入：任务（含 asserts 数组）、执行结果；输出：分数与明细。
- 边界要求：① 断言类型：文件存在/状态变更/内容含关键要素/证据真实；② 分级计分（全对 1.0/部分按子目标/正确拒答 0.5）；③ 证据校验（引用的文件与数据必须真实存在——防"声称完成"）；④ 断言失败明细可定位。

**答**：
```javascript
async function grade(task, result, { fs, db }) {
  const details = [];
  for (const a of task.asserts ?? []) {
    let ok = false, detail = '';
    if (a.type === 'file_exists') {
      ok = await fs.exists(a.path);
      detail = ok ? '' : `文件不存在: ${a.path}`;
    } else if (a.type === 'state') {
      const v = await db.get(a.field);
      ok = v === a.expected;
      detail = ok ? '' : `状态 ${a.field}=${v}，期望 ${a.expected}`;
    } else if (a.type === 'content') {
      const text = await fs.read(a.path);
      ok = a.mustAll.every(k => text.includes(k)) &&
        !a.mustNot?.some(k => text.includes(k));
      detail = ok ? '' : '内容要素缺失或含禁用项';
    } else if (a.type === 'evidence') {          // 证据真实性
      ok = await fs.exists(a.claimedPath) &&
        (await fs.read(a.claimedPath)).includes(a.mustContain);
      detail = ok ? '' : '引用的证据不存在或不匹配（疑似声称完成）';
    }
    details.push({ assert: a, ok, detail });
  }
  const passed = details.filter(d => d.ok).length;
  if (passed === details.length) return { score: 1.0, details };
  if (result.refusedProperly && passed === 0)
    return { score: 0.5, details,
      note: '正确拒答优于编造' };                // 有效拒答
  return { score: passed / details.length, details,
    failed: details.filter(d => !d.ok).map(d => d.detail) };
}
// 拒答有效性判定：refusedProperly 由拒答生成器（AGT-454）标记。
```

**评分点**:
- 四类断言齐全，evidence 断言验证"声称完成"的真实性（防 Agent 报喜不报忧）。
- 分级计分含正确拒答 0.5 的激励设计。
- 失败明细可定位（具体字段/期望值）。
- 拒答标记来自拒答生成器（组件协同）。
