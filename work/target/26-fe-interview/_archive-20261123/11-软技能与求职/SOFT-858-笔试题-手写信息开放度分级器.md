---
title: [SOFT-858] 手写 infoOpenness：信息项的开放度分级（默认开放/分级保留/草稿标注）、守门与囤积检测？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-858：手写 infoOpenness：信息项的开放度分级（默认开放/分级保留/草稿标注）、守门与囤积检测

**需求与边界**：
- 实现 infoOpenness(info)。
- 边界要求：① info 每条 { name, kind, draft?, sensitive? }；② 分级规则：sensitive→受限保留（SOFT-569）；draft→开放但标注状态（防被当结论 SOFT-569）；其他→默认开放；③ 囤积检测：kind=core 且开放度=restricted 且无合规理由（合规字段缺失）→囤积告警（SOFT-849 反模式）；④ 输出分级清单与制度建议（开放度入公约 SOFT-811）。

**答**：
```javascript
function infoOpenness(info) {
  const rows = info.map(i => {
    let level, note;
    if (i.sensitive) { level = '受限保留';
      note = 'SOFT-569分级——访问需申请+审计'; }
    else if (i.draft) { level = '开放+标注';
      note = '必须带状态声明："草稿仅供参考未定稿"'; }
    else { level = '默认开放';
      note = '透明=协作地基（SOFT-818）'; }
    const hoarding = i.kind === 'core' && level === '受限保留'
      && !i.compliance;
    return { name: i.name, level, note,
      hoardingAlarm: hoarding
        ? '囤积告警：核心信息无合规理由受限——组织毒瘤（SOFT-849）' : null };
  });
  return { rows,
    hoardings: rows.filter(r => r.hoardingAlarm).length,
    advice: '开放度规则入团队公约（SOFT-811信息域）' };
}
```

**评分点**:
- 三级开放度规则（默认开放/受限/草稿标注——SOFT-849 落地）。
- 囤积检测（核心信息无合规理由受限=组织毒瘤告警）。
- 草稿状态标注强制（防被当结论引用）。

