---
title: [SOFT-697] 手写 evidencePack：主张↔证据映射、附录编号、缺失检测、打印清单？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-697：手写 evidencePack：主张↔证据映射、附录编号、缺失检测、打印清单

**需求与边界**：
- 实现 genPack(claims, evidences)。
- 边界要求：① 每条主张（claim）至少 1 条证据（无证据的主张标 UNPROVEN——答辩主张必须有据）；② 证据分配附录编号（A1/A2/B1…按主张分组）；③ 索引页输出（编号+一句话说明+主张映射）；④ 打印清单：关键证据（数据类）前 6 份；⑤ 证据类型配比检查（数据类占比 ≥50% 警告否则）。

**答**：
```javascript
function genPack(claims, evidences) {
  const index = []; let seq = {}; const proven = new Set();
  for (const e of evidences) {
    const claim = claims.find(c => c.id === e.claimId);
    if (!claim) continue;
    seq[claim.id] = (seq[claim.id] ?? 0) + 1;
    const no = `${claim.tag}${seq[claim.id]}`;
    index.push({ no, claim: claim.tag, desc: e.desc,
      type: e.type });                               // 数据/文档/证言
    proven.add(claim.id);
  }
  const unproven = claims.filter(c => !proven.has(c.id))
    .map(c => c.text);                               // 无据主张
  const dataShare = index.filter(i => i.type === 'data').length
    / Math.max(index.length, 1);
  return {
    index, unproven,
    printList: index.filter(i => i.type === 'data')
      .slice(0, 6).map(i => i.no),                   // 打印前6
    warn: dataShare < 0.5 ? '数据类证据占比<50%——硬度不足' : null,
  };
}
```

**评分点**:
- 无证据主张显式标 UNPROVEN（答辩主张必须有据可查）。
- 附录编号按主张分组（评委问到哪条主张 10 秒翻到）。
- 数据类配比 ≥50% 检查（证据硬度）+ 打印清单（设备兜底）。

