---
title: [WCN-887] 设计系统的「弃用（deprecation）流程」完整怎么设计？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-887：设计系统的「弃用（deprecation）流程」完整怎么设计？

**答**：
- 结论先行：弃用不是「删掉代码」，而是一个有明确阶段、给消费方足够迁移时间的流程——核心是「先标记、再告警、最后才移除」，全程可追踪、可回退。
- 阶段一标记：给组件/API 打 `@deprecated` 标记与弃用原因、替代方案、计划移除版本；文档站显著标注，registry 元数据里记录。
- 阶段二告警：消费方使用时通过 lint 规则、构建警告、运行时 console.warn（开发态）提示；提供 codemod 自动迁移；看板展示「还有多少页面在用旧 API」。
- 阶段三等待：保留至少一个 major 周期（如 6~12 个月），期间只修 bug 不加功能；定期通知仍在使用方，提供迁移支持。
- 阶段四移除：使用量降到接近零后，在新主版本移除；移除前最后确认无关键消费方；移除后更新文档与迁移指南。
- 追问钩子：面试官会问「到期了还有团队在用怎么办」——答：不要硬删——评估其迁移成本与价值，可延长过渡期或提供兼容层再保一版；弃用的目的是收敛而非惩罚，必要时升级为跨团队项目推动迁移。

```javascript
// 弃用管理器：标记 → 告警 → 统计使用量 → 判定能否移除
function deprecationManager(registry) {
  const deprecated = new Map(); // api -> { since, removeIn, replacement }
  function mark(api, { removeIn, replacement }) {
    deprecated.set(api, { since: new Date().toISOString(), removeIn, replacement });
  }
  function warnIfUsed(code) {
    for (const [api, info] of deprecated) {
      if (code.includes(api)) console.warn(`${api} 已弃用，请改用 ${info.replacement}，将于 ${info.removeIn} 移除`);
    }
  }
  function canRemove(api, usageCount) {
    return deprecated.has(api) && usageCount === 0; // 无使用方可移除
  }
  return { mark, warnIfUsed, canRemove, deprecated };
}
const dm = deprecationManager({});
dm.mark('ds-button.oldType', { removeIn: 'v4.0', replacement: 'ds-button.variant' });
dm.warnIfUsed('<ds-button oldType="primary">');
console.log(dm.canRemove('ds-button.oldType', 3)); // false，还有 3 处在用
```
