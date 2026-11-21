---
title: [MP-127] UGC 内容安全如何做（msgSecCheck/imgSecCheck）？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-127：UGC 内容安全如何做（msgSecCheck/imgSecCheck）？
**答**：
- 用户产生内容（昵称/评论/图文/分享文案）**先审后发**：文本走 `msgSecCheck`（服务端 API，2.0 版支持输出命中标签与风险概率），图片走 `imgSecCheck`（1M 内）或异步 `mediaCheckAsync` 回调。
- 命中风险：阻断发布并给友好提示；边缘样本（概率中等）进人工审核队列，先发后审需标记可见范围。
- 服务端对接需要 access_token 管理（中控 token 服务，避免各处刷新互相顶掉）。
- 保留内容与审核结果日志（监管要求可追溯）；昵称头像变更同样要过检。

```javascript
// 服务端内容安全中间件
const tokenCenter = require('./token-center') // 中控 access_token
async function secCheckText(content, openid) {
  const token = await tokenCenter.get()
  const r = await fetchJSON(`https://api.weixin.qq.com/wxa/msg_sec_check?access_token=${token}`, {
    method: 'POST', body: JSON.stringify({ version: 2, scene: 2, openid, content })
  })
  if (r.errcode !== 0) throw new Error('sec-check-fail')
  const d = r.result.suggest      // pass / risky / review
  if (d === 'risky') throw new BizError('内容包含违规信息，请修改后重试')
  return d === 'review' ? 'MANUAL' : 'PASS'   // review 进人工队列
}
app.post('/api/comment', auth, async (req, res) => {
  const verdict = await secCheckText(req.body.content, req.auth.openid)
  await db.comment.create({ ...req.body, verdict })   // 先审后发或标记待审
  res.json({ code: 0, verdict })
})
```
