---
title: [AGT-495] 笔试题——实现会话隐私脱敏展示（界面掩码+完整数据权限分离）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-495：手写展示脱敏：界面掩码渲染、揭示权限、导出全量、屏幕共享检测

**需求与边界**：
- 输入：会话消息（含敏感字段）、查看者权限；输出：渲染视图。
- 边界要求：① 敏感字段界面掩码（默认打码）；② 揭示需权限+操作留痕（谁揭示了什么）；③ 屏幕共享/录屏时的提示（敏感内容外泄通道）；④ 导出全量需二次确认。

**答**：
```javascript
function renderView(messages, viewer, { audit, screenState }) {
  const canReveal = viewer.role === 'owner';
  const items = messages.map(m => ({
    ...m,
    content: maskSensitive(m.content, {
      // 默认掩码：手机号/身份证/卡号
      mask: (s) => s.slice(0, 3) + '****' + s.slice(-2),
    }),
    revealable: canReveal && hasSensitive(m.content),
  }));
  return {
    items,
    // 揭示操作：权限+留痕
    reveal(itemId) {
      if (!canReveal) return { ok: false, reason: '无权限' };
      audit.log({ viewer: viewer.id, itemId, action: 'reveal' });
      return { ok: true };                        // 前端替换为明文
    },
    // 屏幕共享检测：共享中默认全掩码
    screenSharing: screenState.sharing
      ? { warning: '检测到屏幕共享，敏感内容已强制掩码',
          forceMask: true }
      : null,
    export: {                                     // 导出全量需确认
      requiresConfirm: true,
      confirmText: '导出将包含完整敏感信息，确认继续？',
    },
  };
}
// 掩码渲染在前端组件层：mask 属性 → <MaskedText reveal={fn}/>
// 揭示状态不持久（刷新恢复掩码——默认安全）。
```

**评分点**:
- 默认掩码+按权限揭示+揭示审计三件套。
- 屏幕共享强制掩码（外泄通道感知）。
- 导出全量二次确认；揭示状态不持久（刷新回默认安全态）。
- canReveal 由角色而非前端开关（权限服务端校验意识）。
