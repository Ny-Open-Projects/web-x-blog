---
title: [HW-195] 手写幂等键生成——crypto.randomUUID 优先 + 时间戳熵补充降级 + 碰撞概率分析
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：幂等键生成的完整降级链：crypto.randomUUID（原生，安全随机）→ getRandomValues 拼 UUID v4 → 时间戳+计数器+随机熵（老环境）——每级都保证"同一会话内唯一"。碰撞概率分析：UUID v4 122 位随机，10 亿次/秒需 100 年才 50% 碰撞；降级版熵 ≈ 60 位（毫秒时间戳 40 位 + 计数器 + 随机 16 位），单设备内安全。

```javascript
function idempotencyKey() {
  if (globalThis.crypto?.randomUUID) return crypto.randomUUID();            // 原生
  const buf = new Uint8Array(16);
  if (globalThis.crypto?.getRandomValues) {
    crypto.getRandomValues(buf);                                            // 拼.UUID v4
    buf[6] = (buf[6] & 0x0f) | 0x40; buf[8] = (buf[8] & 0x3f) | 0x80;       // 版本/变体位
    const hex = [...buf].map((b) => b.toString(16).padStart(2, '0')).join('');
    return `${hex.slice(0, 8)}-${hex.slice(8, 12)}-${hex.slice(12, 16)}-${hex.slice(16, 20)}-${hex.slice(20)}`;
  }
  // 老环境：时间戳 + 自增计数 + Math.random 熵（单设备会话内唯一够用）
  let counter = (idempotencyKey._c = (idempotencyKey._c ?? 0) + 1);
  return `${Date.now().toString(36)}-${counter.toString(36)}-${Math.random().toString(36).slice(2, 8)}`;
}
// 唯一性要求分级：
// 幂等键（服务端按 key 去重）：单用户内唯一即可 —— 降级版够用
// 数据库主键（全局唯一）：必须原生 randomUUID —— 降级版碰撞风险不可接受
// 碰撞概率：UUID v4 122 位 → 生日攻击 50% 需 ~2^61 个键（10 亿/秒 × 100 年）—— 实际唯一
```

**评分点**：
- 三级降级链（randomUUID → getRandomValues 拼 v4 → 时间戳+计数+熵）。
- UUID v4 版本/变体位设置正确（buf[6]/buf[8] 掩码）。
- 唯一性要求分级（幂等键 vs 主键）与碰撞概率量级分析——本题核心。
- 计数器防同毫秒碰撞。
