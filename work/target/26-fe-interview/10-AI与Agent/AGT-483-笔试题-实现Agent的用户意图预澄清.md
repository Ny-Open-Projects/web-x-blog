---
title: [AGT-483] 笔试题——实现输入预澄清（提交前歧义提示+智能补全建议）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-483：手写预澄清：提交前歧义检测、内联建议、可选修正（不打断主流程）

**需求与边界**：
- 输入：输入框文本（防抖后）、歧义检测器；输出：非阻塞建议 UI。
- 边界要求：① 非阻塞：建议不拦截提交（用户可忽略）；② 防抖检测（输入停顿才触发，省调用）；③ 建议类型（歧义选项/缺失信息提示/改写建议）；④ 建议采纳率统计（低采纳建议下线）。

**答**：
```javascript
function createPreflight({ detect, debounceMs = 600 }) {
  let timer = null, lastSig = '';
  return {
    onInput(text, cb) {
      clearTimeout(timer);
      timer = setTimeout(async () => {
        // 签名去重（同内容不重复检测）
        const sig = text.trim();
        if (sig === lastSig || sig.length < 8) return;
        lastSig = sig;
        const issues = await detect(sig);       // [{type, msg, options}]
        // 非阻塞建议：不拦截提交，仅提示
        cb(sig, issues.map(i => ({
          type: i.type,                        // ambiguity/missing/rewrite
          msg: i.msg,
          quickFixes: i.options?.slice(0, 3),  // 一键替换候选
          dismissible: true,                   // 可忽略
        })));
      }, debounceMs);
    },
    // 采纳率统计：低采纳建议类型下线（避免噪音）
    track(type, accepted) {
      stats.inc(`preflight.${type}.${accepted ? 'used' : 'ignored'}`);
      if (stats.rate(`preflight.${type}.used`) < 0.05
          && stats.count(`preflight.${type}`) > 100)
        featureFlags.off(`preflight.${type}`); // 自动下线
    },
  };
}
// 提交时不校验建议（预澄清是助力不是门禁）；
// 强歧义在提交后由 ClarifyManager（AGT-431）兜底。
```

**评分点**:
- 非阻塞定位正确：预澄清是建议不是门禁，强歧义由提交后澄清兜底（分层）。
- 防抖+签名去重（省调用）。
- 建议三类型带一键修正（quickFixes）与可忽略标记。
- 采纳率统计与低采纳自动下线（噪音治理闭环）。
