---
title: [AGT-447] 笔试题——实现技能包版本发布器（评测门禁+灰度+回滚）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-447：手写技能包发布：schema 校验、专属评测门禁、灰度指针、秒级回滚

**需求与边界**：
- 输入：技能包定义 {id, prompt, tools, schema, evalSuite}、变更说明；输出：发布结果。
- 边界要求：① 定义完整性校验（prompt/tools/schema/eval 缺一不可）；② 专属评测集跑过门禁才可发布；③ 灰度按流量比例推进（版本指针）；④ 回滚=指针切回，秒级生效；⑤ 弃用流程（低使用率下线前通知）。

**答**：
```javascript
class SkillPublisher {
  constructor({ registry, evaluator }) {
    this.registry = registry; this.evaluator = evaluator;
  }
  async publish(skill, change) {
    // 1. 完整性校验
    const required = ['prompt', 'tools', 'schema', 'evalSuite'];
    const missing = required.filter(k => !skill[k]);
    if (missing.length)
      throw new Error(`技能定义缺失: ${missing.join(',')}`);
    // 2. 工具白名单校验（引用的工具必须存在且授权）
    for (const t of skill.tools)
      if (!this.registry.toolExists(t))
        throw new Error(`工具不存在: ${t}`);
    // 3. 专属评测门禁
    const r = await this.evaluator.run(skill.evalSuite, skill);
    if (r.score < 0.85 || r.hardFails > 0)
      return { published: false, reason: 'eval_gate_failed', r };
    // 4. 版本入库 + 灰度指针（默认 0% 全量前灰度）
    const ver = await this.registry.save(skill,
      { change: change.desc, rationale: change.whyGeneralizes });
    await this.registry.setTraffic(skill.id, ver, 0);
    return { published: true, version: ver,
      next: 'setTraffic 逐步放量，护栏指标异常 rollback' };
  }
  async rollout(skillId, pct) {
    return this.registry.setTraffic(skillId, 'latest', pct);
  }
  async rollback(skillId) {
    const prev = this.registry.previousVersion(skillId);
    await this.registry.setTraffic(skillId, prev, 100);  // 指针切回
    return { rolledBackTo: prev, effective: 'immediate' };
  }
  async deprecate(skillId) {                       // 弃用流程
    const usage = await this.registry.usage(skillId);
    if (usage.dailyCalls > 100)
      return { done: false, reason: '仍有使用，先通知用户' };
    await this.registry.notify(skillId);           // 提前 30 天通知
    return { done: true, effectiveAt: plusDays(30) };
  }
}
```

**评分点**:
- 发布四关卡：完整性→工具引用校验→评测门禁→灰度指针，缺一不可。
- 泛化理由归档随版本存（AGT-443 联动）。
- 回滚=版本指针切换秒级生效（不重部署）。
- 弃用有使用率检查与提前通知期。
