---
title: [PER-1222] 如何设计"性能问题速查手册"（值班 CD 手册）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1222：如何设计"性能问题速查手册"（值班 CD 手册）

**答**：
- 结构：症状→可能原因→验证命令→修复动作→升级路径，一页一个症状。
- 症状库：白屏、慢 3 秒以上、滚动卡、点击延迟、内存增长、CDN 404……
- 维护：每次值班处理的新症状补充入库，季度评审删除过时项。
- 使用场景：值班不用从零推理，按手册 15 分钟内完成初步定位。

```javascript
// 症状手册条目
const RUNBOOK = {
  'blank-screen': { causes: ['JS 错误', 'CSS 阻塞', '路由未命中'],
    check: ['console 错误?', '资源 404?', '路由表 diff?'],
    fix: '回滚/热修', escalate: 'P0 走应急' },
  'slow-lcp': { causes: ['LCP 资源慢', 'TTFB 高', '阻塞 JS'],
    check: ['resource timing 分解', 'Early Hints 是否生效'],
    fix: 'preconnect/优先级/CDN', escalate: '>1h 未定位找平台' },
};
function runbookFor(symptom) {
  return RUNBOOK[symptom] ?? { causes: ['未收录，处理后请回填'], escalate: '平台' };
}
```
