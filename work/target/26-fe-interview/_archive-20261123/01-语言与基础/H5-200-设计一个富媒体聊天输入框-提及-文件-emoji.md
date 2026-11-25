---
title: [H5-200] 设计一个富媒体聊天输入框（@提及/文件/emoji/语音混合输入）
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-200：设计一个富媒体聊天输入框（@提及/文件/emoji/语音混合输入）
**答**：
- 核心：`contenteditable` 混排（文本 + @提及 chip + emoji）；提及节点 `contentEditable='false'` 保证整体删除不被拆散，`data-uid` 携带身份。
- 文件/图片：粘贴（截图高频）与拖拽统一走 addFiles → 预览卡条（可删除）→ 发送时上传；语音按住说话（H5-196），上滑取消。
- 序列化协议：发送时把 contenteditable 内容序列化为 `[{type:'text'|'mention', ...}]`，纯文本等价物用于搜索/推送预览。
- 交互细节：Enter 发送 Shift+Enter 换行（移动端相反）、草稿本地暂存、超长折叠、@弹出候选人面板（keyup 检测 '@'）。

```html
<div class="composer">
  <div id="attachments"></div>       <!-- 已选文件/图片预览条 -->
  <div id="editor" contenteditable="true"></div>
  <button id="emoji">😀</button>
  <button id="file">📎</button>
  <button id="voice">按住说话</button>
</div>
<style>
  .composer { border: 1px solid #e5e7eb; border-radius: 8px; padding: 8px; }
  #editor { min-height: 40px; outline: none; }
  .mention { background: #dbeafe; border-radius: 4px; padding: 0 4px; color: #2563eb; }
  #attachments img { width: 64px; height: 64px; object-fit: cover; margin-right: 4px; }
</style>
<script>
const ed = document.getElementById('editor');

// 1) @提及：keyup 检测 '@' 弹面板；插入不可拆分的提及 chip
ed.addEventListener('keyup', (e) => {
  const sel = document.getSelection();
  if (e.key === '@' && sel.isCollapsed) openMentionPopup(insertMention);
});
function insertMention(user) {
  const chip = document.createElement('span');
  chip.contentEditable = 'false';          // 整体删除/不可内部编辑
  chip.className = 'mention';
  chip.dataset.uid = user.id;
  chip.textContent = '@' + user.name;
  const sel = document.getSelection();
  sel.getRangeAt(0).insertNode(chip);
  const sp = document.createTextNode('\u00A0');   // chip 后留空格继续打字
  chip.after(sp);
  sel.collapse(sp, 1);
}
function openMentionPopup(cb) { cb({ id: 'u1', name: '张三' }); }

// 2) 文件/图片：粘贴与拖拽统一走 addFiles（截图粘贴高频）
async function addFiles(files) {
  for (const f of files) {
    const item = f.type.startsWith('image/')
      ? makeImageCard(f) : makeFileCard(f);   // 预览卡带删除按钮
    document.getElementById('attachments').append(item);
  }
}
function makeImageCard(f) {
  const img = new Image();
  img.src = URL.createObjectURL(f);
  return img;
}
function makeFileCard(f) {
  const d = document.createElement('span');
  d.textContent = f.name;
  return d;
}
ed.addEventListener('paste', (e) => {
  const img = [...e.clipboardData.items].find((i) => i.type.startsWith('image/'));
  if (img) { e.preventDefault(); addFiles([img.getAsFile()]); }
});

// 3) emoji：插入文本节点，保持光标
document.getElementById('emoji').onclick = () => {
  const r = document.getSelection().getRangeAt(0);
  r.insertNode(document.createTextNode('😀'));
  document.getSelection().collapseToEnd();
};

// 4) 语音：按住说话（方案见 H5-196），上滑取消，松开生成语音条 + 转文字预览

// 5) 发送序列化：contenteditable 内容 → 消息协议
function serialize() {
  return [...ed.childNodes].map((n) =>
    n.nodeType === 3 ? { type: 'text', text: n.textContent }
    : n.classList?.contains('mention')
      ? { type: 'mention', uid: n.dataset.uid }
      : { type: 'text', text: n.textContent });
}
// Enter 发送 Shift+Enter 换行（移动端相反）；草稿 localStorage 暂存；
// 发送时拼装 { text: serialize(), attachments: [...pendingFiles] }
</script>
```
