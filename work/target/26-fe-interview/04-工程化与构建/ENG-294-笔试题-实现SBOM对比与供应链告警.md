---
title: [ENG-294] 笔试题——实现 SBOM 对比与供应链告警（新依赖引入检测）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-294：手写 SBOM 对比

**需求与边界**：
- 输入：基线 SBOM 与当前 SBOM（CycloneDX 简化：[{name, version, hashes}]）；输出：新增包（进白名单校验）/hash 变化（同版本不同内容 = 疑似投毒）/删除包。
- 边界：① 同版本 hash 变化是最高危信号（上游重发或缓存污染）；② 新增包查白名单 + 维护活跃度评分；③ 输出按风险排序（hash 变化 > 未白名单新增 > 常规新增）。

**答**：
```javascript
function sbomDiff(base, current, { whitelist } = {}) {
  const alerts = [];
  const bMap = new Map(base.map(b => [`${b.name}@${b.version}`, b]));
  const cMap = new Map(current.map(c => [`${c.name}@${c.version}`, c]));
  for (const [key, cur] of cMap) {
    const prev = bMap.get(key);
    if (!prev) {
      const risk = !whitelist.has(cur.name) ? 'UNLISTED_NEW' : 'NEW';
      alerts.push({ level: risk === 'UNLISTED_NEW' ? 1 : 2, type: risk,
        name: cur.name, version: cur.version,
        score: packageHealth(cur.name) });           // 活跃度/下载量评分
    } else if (prev.hash !== cur.hash)
      alerts.push({ level: 0, type: 'HASH_CHANGED', name: cur.name,   // 同版本内容变化：最高危
        version: cur.version, note: '疑似上游重发/缓存污染' });
  }
  for (const [key] of bMap)
    if (!cMap.has(key)) alerts.push({ type: 'REMOVED', name: key.split('@')[0] });
  return alerts.sort((a, b) => (a.level ?? 9) - (b.level ?? 9));
}
function packageHealth(name) {                       // 新增依赖健康度
  return { maintained: lastCommitAge(name) < 365, downloads: weeklyDl(name), license: licenseOf(name) };
}
```

**评分点**:
- 同版本 hash 变化识别为最高危（供应链投毒核心信号）。
- 新增包白名单 + 健康度评分（入库前评审数据）。
- 风险排序输出（hash 变化置顶）。
- REMOVED 包记录（依赖面收缩可见）。
