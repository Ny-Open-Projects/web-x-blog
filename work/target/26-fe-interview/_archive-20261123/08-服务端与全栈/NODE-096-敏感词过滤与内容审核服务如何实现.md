---
title: [NODE-096] 敏感词过滤与内容审核服务如何实现？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-096：敏感词过滤与内容审核服务如何实现？
**答**：
- 两级方案：① **本地敏感词库**：DFA（确定有限自动机）/双数组 Trie 树，微秒级，挡住明确违禁词（支持变体字：`微`→`W微` 归一化后匹配）；② **机器审核**：调用内容安全 API（图片/文本），异步回调结果，用于语义级风险（辱骂、广告、涉政变体）。
- 服务端设计：`POST /moderation/text` 同步快速过滤（DFA）+ 异步机器审核（先发后审或先审后发按业务定）；词库热更新；命中记录审计（封禁依据）。
- 性能：DFA 构建一次常驻内存（10 万词条约几十 MB）；归一化（繁简、全半角、插入符号）在匹配前统一处理。

```javascript
// DFA 敏感词过滤（生产可用 aho-corasick 库，此处手写 Trie 版）
class WordFilter {
  constructor() {
    this.root = {};
  }
  addWord(word) {
    let node = this.root;
    for (const ch of word) node = (node[ch] ||= {});
    node.__end = true;
  }
  // 归一化：全角半角、变体符号剥离
  normalize(text) {
    return text.toLowerCase()
      .replace(/[ａ-ｚＡ-Ｚ０-９]/g, (c) => String.fromCharCode(c.charCodeAt(0) - 0xfee0))
      .replace(/[\s\*·•_.\-]/g, '');            // 去插入符：'微-信' → '微信'
  }
  filter(text) {
    const s = this.normalize(text);
    const hits = [];
    for (let i = 0; i < s.length; i++) {
      let node = this.root;
      for (let j = i; j < s.length; j++) {
        node = node[s[j]];
        if (!node) break;
        if (node.__end) hits.push(s.slice(i, j + 1));   // 命中：最长匹配继续尝试
      }
    }
    return [...new Set(hits)];
  }
}

const filter = new WordFilter();
SENSITIVE_WORDS.forEach((w) => filter.addWord(w));       // 词库启动加载，配置中心热更新

// 审核接口：DFA 同步 + 机器审核异步
router.post('/moderation/text', async (ctx) => {
  const { content } = ctx.request.body;
  const localHits = filter.filter(content);
  if (localHits.length) {                                 // 一级：明确违禁，直接拒绝
    await db.query('INSERT INTO moderation_log (uid, content, hits, action) VALUES (?, ?, ?, ?)',
      [ctx.state.user.uid, content, JSON.stringify(localHits), 'reject']);
    ctx.throw(422, '内容包含违禁词');
  }
  // 二级：机器审核（先发后审场景异步）
  const task = await contentSafety.submit(content);       // 厂商 API
  await db.query('UPDATE comments SET audit_status = ? WHERE id = ?', ['pending', ctx.request.body.commentId]);
  ctx.body = { status: 'accepted_pending_audit', taskId: task.id }; // 先展示，机器判定违规后下架+通知
});

// 机器审核回调
router.post('/moderation/callback', async (ctx) => {
  const { taskId, verdict } = ctx.request.body;
  const record = await db.query('SELECT * FROM moderation_tasks WHERE id = ?', [taskId]);
  if (verdict === 'risky') {
    await db.query('UPDATE comments SET audit_status = ? WHERE id = ?', ['blocked', record.comment_id]);
    await notifyUser(record.uid, 'content_blocked', { reason: '涉嫌违规' });
  }
  ctx.body = 'ok';
});
```
