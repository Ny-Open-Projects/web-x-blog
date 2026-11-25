---
title: [BLD-305] 笔试题——实现 chunk 加载失败自愈（版本对齐刷新）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-305：手写 chunk 自愈

**需求与边界**：
- 需求：灰度期 chunk 404 自愈（SCN-OPS-218）——① 捕获 script/link 动态加载失败；② 版本对齐判断（当前版本 vs 服务端期望版本）；③ 自愈刷新（带会话状态保存——表单不丢）；④ 自愈频率保护（同一会话最多 2 次——防刷新循环）。
- 边界：① 刷新前保存状态（sessionStorage 快照——路由/表单恢复）；② 非版本问题（真 404/网络断）不无限刷新（区分错误类型）；③ 自愈事件上报（频率监控——SCN-OPS-218 残留率联动）。

**答**：
```javascript
window.addEventListener('error', async (e) => {
  const src = e.target?.src ?? e.target?.href;
  if (!src || !/\/assets\//.test(src)) return;         // 只处理产物资源
  e.preventDefault();
  report({ type: 'CHUNK_FAIL', src, version: window.__BUILD__.commit });
  if (healCount >= 2) return showManualReload();       // 频率保护：2 次后人工
  const expected = await fetch('/api/expected-version').then(r => r.text()).catch(() => null);
  if (expected && expected !== window.__BUILD__.commit) {   // 版本过期 → 自愈刷新
    healCount++;
    sessionStorage.setItem('route-snapshot', JSON.stringify({
      path: location.pathname + location.search,
      form: snapshotForms(),                           // 表单状态保存
    }));
    location.reload();                                 // 版本对齐
  } else if (!expected) {
    retryWithBackoff(src);                             // 网络问题：退避重试不刷新
  } else {
    showManualReload();                                // 真版本一致仍 404——人工处理
  }
}, true);
// 恢复：路由回位 + 表单回填
const snap = JSON.parse(sessionStorage.getItem('route-snapshot') ?? 'null');
if (snap) { history.replaceState(null, '', snap.path); restoreForms(snap.form); }
```

**评分点**:
- 版本对齐判断（版本过期才刷新——非版本问题不无限刷）。
- 频率保护（2 次后人工——防刷新循环）。
- 会话状态保存恢复（表单不丢——SCN-OPS-218 体验）。
- 三分支（自愈/退避重试/人工）错误类型区分。
