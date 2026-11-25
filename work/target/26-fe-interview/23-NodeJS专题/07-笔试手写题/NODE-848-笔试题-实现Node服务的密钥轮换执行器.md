---
title: [NODE-848] 笔试题——实现密钥轮换执行器（kid 双密钥窗口）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-848：手写密钥轮换

**需求与边界**：
- 需求：密钥轮换（SCN-FIN-567/649）——① 双密钥窗口（新密钥签名 + 新旧双验证——过渡期，SCN-NODE-649）；② kid 路由（验证按 kid 选密钥）；③ 轮换审计与紧急轮换（泄露应急——SCN-ENG-229）；④ 轮换计划（定期自动——30 天）。
- 边界：① 过渡期窗口（旧密钥 TTL——签发的旧 token 自然过期）；② 轮换的零停机（双验证窗口——无中断）；③ 紧急轮换的连接清理（SCN-NODE-649 撤销链）。

**答**：
```javascript
const keys = new Map();                                // kid → 密钥（双窗口：new + old）
function sign(payload) {
  payload.kid = currentKid;
  return jwt.sign(payload, keys.get(currentKid), { algorithm: 'RS256' });   // 新密钥签（SCN-FIN-567）
}
function verify(token) {
  const { kid } = jwt.decode(token) ?? {};
  const key = keys.get(kid) ?? keys.get(prevKid);      // 双验证窗口（过渡期——SCN-NODE-649）
  if (!key) throw new Error('UNKNOWN_KID');
  return jwt.verify(token, key, { algorithms: ['RS256'] });
}
// 轮换执行
async function rotate({ emergency = false } = {}) {
  const newKid = crypto.randomUUID();
  keys.set(newKid, await generateKey());               // 1. 生成新密钥
  prevKid = currentKid; currentKid = newKid;           // 2. 双窗口（旧验证保留）
  schedule(() => keys.delete(prevKid), 30 * 60_000);   // 3. 过渡期后删旧（旧 token 自然过期）
  audit({ action: emergency ? 'EMERGENCY_ROTATE' : 'ROTATE', kid: newKid });   // 审计（SCN-ENG-229）
  if (emergency) await revokeAllSessions();            // 紧急：全量撤销（SCN-NODE-649）
}
cron('0 0 */30 * *', () => rotate());                  // 定期自动轮换
```

**评分点**:
- 双密钥窗口（零停机轮换——过渡期旧验证保留）。
- kid 路由验证（SCN-FIN-567）。
- 紧急轮换 + 全量撤销（SCN-ENG-229 应急）。
- 定期自动轮换 + 审计。
