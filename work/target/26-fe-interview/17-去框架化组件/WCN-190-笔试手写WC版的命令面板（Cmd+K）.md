---
title: [WCN-190] 笔试：手写 Cmd+K 命令面板 WC（快捷键 + 模糊搜索 + 键盘导航）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-190：笔试：手写 Cmd+K 命令面板 WC

**题目**：实现 `<wc-cmdk>`：① 全局监听 Cmd/Ctrl+K 打开（影子树内 popover）；② 输入过滤命令列表（拼音/关键字 contains，大小写不敏感）；③ 上下键选择 + Enter 执行 + Esc 关闭；④ 执行派发 `cmd-run`（detail: {id, args}）；⑤ 选中项滚动到可视区；⑥ 关闭后焦点还原到触发前的元素。

**答**：

```javascript
class WcCmdk extends HTMLElement {
  #commands = []; #active = 0; #lastFocus = null;
  connectedCallback() {
    if (!this.shadowRoot) {
      this.attachShadow({ mode: 'open' }).innerHTML = `
        <style>
          [popover] { inset: 10% auto auto 50%; transform: translateX(-50%);
            border: 1px solid #e5e7eb; border-radius: 12px; padding: 8px; width: 480px; }
          input { width: 100%; box-sizing: border-box; padding: 8px; border: 0; border-bottom: 1px solid #f3f4f6; }
          ul { list-style: none; margin: 4px 0 0; padding: 0; max-height: 300px; overflow: auto; }
          li { padding: 8px; border-radius: 8px; cursor: pointer; }
          li.active { background: #eff6ff; }
        </style>
        <div popover id="p"><input placeholder="输入命令…" part="input"><ul></ul></div>`;
      this.#panel = this.shadowRoot.getElementById('p');
      // 全局快捷键（document 级，disconnected 清理）
      this.#onKey = (e) => {
        if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
          e.preventDefault();
          this.open();
        }
      };
      document.addEventListener('keydown', this.#onKey);
      const input = this.shadowRoot.querySelector('input');
      input.addEventListener('input', () => this.#filter(input.value));
      this.shadowRoot.addEventListener('keydown', (e) => this.#nav(e));
    }
  }
  #panel; #onKey;
  disconnectedCallback() { document.removeEventListener('keydown', this.#onKey); }
  set commands(list) { this.#commands = list; this.#filter(''); }
  open() {
    this.#lastFocus = document.activeElement;
    this.#panel.showPopover();
    this.shadowRoot.querySelector('input').focus();
    this.#filter('');
  }
  close() { this.#panel.hidePopover(); this.#lastFocus?.focus?.(); }
  #filter(q) {
    const ul = this.shadowRoot.querySelector('ul');
    const norm = (s) => s.toLowerCase();
    this.#view = this.#commands.filter((c) => norm(c.title).includes(norm(q)));
    this.#active = 0;
    ul.innerHTML = this.#view.map((c, i) =>
      `<li data-id="${c.id}" class="${i === 0 ? 'active' : ''}">${c.title}</li>`).join('');
  }
  #nav(e) {
    const ul = this.shadowRoot.querySelector('ul');
    const items = [...ul.children];
    if (e.key === 'Escape') return this.close();
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      this.#active = Math.max(0, Math.min(this.#view.length - 1,
        this.#active + (e.key === 'ArrowDown' ? 1 : -1)));
      items.forEach((li, i) => li.classList.toggle('active', i === this.#active));
      items[this.#active]?.scrollIntoView({ block: 'nearest' });   // 选中项滚入视区
    }
    if (e.key === 'Enter') {
      const c = this.#view[this.#active];
      if (c) { this.close();
        this.dispatchEvent(new CustomEvent('cmd-run',
          { bubbles: true, composed: true, detail: { id: c.id, args: c.args } }));
      }
    }
  }
}
customElements.define('wc-cmdk', WcCmdk);
```

**评分点**：
- 全局快捷键 preventDefault + popover top layer（不受 z-index/裁剪影响）。
- 键盘导航：循环边界 clamp、选中项 scrollIntoView nearest。
- 焦点还原（#lastFocus.focus）——可达性细节。
- 大小写不敏感过滤、事件 detail 结构（id+args）。
