---
title: [SCN-1245] AI 对话的模型服务健康探测与降级路由
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1245：AI 对话的模型服务健康探测与降级路由

**答**：
- 探测：多模型服务健康探测（TTFT/错误率），自动路由到健康模型。
- 降级：主模型故障切备用（用户可见提示"已切换备用模型"）。
- 恢复：主模型恢复自动切回（灰度验证）。

```javascript
// 健康路由
class ModelRouter {
  constructor(models) { this.models = models; this.health = new Map(); }
  async pick(payload) {
    const healthy = this.models.filter(m =>
      (this.health.get(m.id)?.ok ?? true));
    const chosen = healthy.sort((a, b) => a.cost - b.cost)[0];
    return { model: chosen,
      note: chosen.id !== this.models[0].id ? '已切换备用模型' : null };
  }
  probe() {
    this.models.forEach(async m => {
      const r = await probeModel(m.id);
      this.health.set(m.id, r);
    });
  }
}
async function probeModel(id) { return { ok: true, ttft: 800 }; }
```
