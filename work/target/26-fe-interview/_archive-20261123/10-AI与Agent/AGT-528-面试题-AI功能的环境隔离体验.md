---
title: [AGT-528] 企业 AI 应用里个人助手与共享空间（团队知识库问答）如何做界面与权限隔离？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-528：企业 AI 应用里个人助手与共享空间（团队知识库问答）如何做界面与权限隔离

**答**：
- 域分离：个人会话（可带个人文件）与团队空间（仅团队知识库）在 UI 上明确分域（tab/侧栏分区），跨域引用要显式声明"引用了个人文件 X"。
- 权限可视化：团队空间的回答只引用当前用户有权限的文档，引用卡带权限标识；无权限命中时不展示内容只提示"有 N 篇相关文档你无权限查看"。
- 分享边界：个人会话分享到团队空间时要过一遍敏感扫描 + 资产转存（个人文件→团队空间副本），避免链接失效或越权。

```javascript
function renderCitation(c, space) {
  if (c.denied)  // 无权限命中：数量提示而非内容
    return <div className="cite-denied">有 {c.deniedCount} 篇相关文档无权限查看</div>;
  return <CiteCard src={c} scope={space} />;   // 带 scope 权限标识
}
async function shareToTeam(msgIds) {
  const risk = await scanSensitive(msgIds);
  if (risk.hits) return confirm('含敏感内容：' + risk.summary);
  await api.share({ msgIds, copyAssets: true });  // 资产转存团队空间
}
```

