---
title: [SOFT-889] 手写 intelProfile：公司档案的三源交叉（面经/社媒/内部朋友）、可信度标注、时效检查？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-889：手写 intelProfile：公司档案的三源交叉（面经/社媒/内部朋友）、可信度标注、时效检查

**需求与边界**：
- 实现 intelProfile(company, sources)。
- 边界要求：① sources 三源 { jingyan, social, insider }——各源条目带 { text, date }；② 交叉验证：三源都提的信息标 HIGH_CONF，单源标 LOW_CONF（SOFT-750 多源验证）；③ 时效检查：>6 个月的情报标 STALE（团队与薪酬半年一变 SOFT-867）；④ 合规过滤：标记疑似内部违规信息（未公开财务/薪酬明细）为 DO_NOT_USE；⑤ 输出档案 markdown。

**答**：
```javascript
function intelProfile(company, sources) {
  const all = [
    ...sources.jingyan.map(t => ({ ...t, src: '面经' })),
    ...sources.social.map(t => ({ ...t, src: '社媒' })),
    ...sources.insider.map(t => ({ ...t, src: '内线' })),
  ];
  const rows = all.map(item => {
    const cross = all.filter(x => x.text === item.text).length;
    const conf = cross >= 2 ? 'HIGH_CONF' : 'LOW_CONF';
    const stale = (Date.now() - item.date) > 183 * 864e5;
    const violate = /未公开|具体薪资明细|内部数据/.test(item.text)
      ? 'DO_NOT_USE：疑似违规内部信息（SOFT-867合规线）' : null;
    return { text: item.text, src: item.src, conf,
      stale: stale ? 'STALE：>6个月——用前验证（SOFT-867）' : null,
      violate };
  });
  const usable = rows.filter(r => !r.violate);
  return { company,
    profile: usable.map(r =>
      `- [${r.conf}${r.stale ? '/STALE' : ''}]（${r.src}）${r.text}`)
      .join('\n'),
    violations: rows.filter(r => r.violate),
    highConf: usable.filter(r => r.conf === 'HIGH_CONF').length,
    note: '单源信息不当决策依据（SOFT-750多源验证）' };
}
```

**评分点**:
- 三源交叉可信度（HIGH/LOW_CONF——SOFT-750 落地）。
- 时效检查（>6 月 STALE——情报半衰期纪律）。
- 合规过滤（违规内部信息 DO_NOT_USE——道德底线工具化）。

