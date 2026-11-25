---
title: [H5-062] checkValidity、reportValidity 与 validityState 如何组合成完整校验工具箱？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-062：checkValidity、reportValidity 与 validityState 如何组合成完整校验工具箱？
**答**：
- `checkValidity()`：**静默**检查并触发 `invalid` 事件，返回布尔值，不弹任何 UI；适合程序化预检。
- `reportValidity()`：检查**并**展示浏览器原生提示（气泡 + 聚焦第一个非法字段）；想借原生 UI 就用它。
- `element.validity` 是 11 个布尔位的"体检报告"：`valueMissing/badInput/typeMismatch/patternMismatch/tooLong/tooShort/rangeOverflow/rangeUnderflow/stepMismatch/tooLong 之外还有 customError/valid`。
- `setCustomValidity(msg)` 设置非空即视为非法（`customError` 为 true），传空串清除——这是把业务错误挂进原生体系的唯一入口。
- 组合拳：`setCustomValidity` 挂业务错误 → `reportValidity()` 展示 → `validity.customError` 区分"格式错"与"业务错"。

```html
<form id="pay">
  <label>提现金额
    <input name="amount" type="number" required min="1" max="5000" step="0.01">
  </label>
  <p id="biz-err" hidden>该金额超出今日剩余额度</p>
  <button>申请提现</button>
</form>

<script>
  const form = document.getElementById('pay');
  const amount = form.elements.amount;
  let quotaLeft = 800; // 模拟接口返回的剩余额度

  // 业务校验挂在原生体系上
  amount.addEventListener('input', () => {
    const v = Number(amount.value);
    amount.setCustomValidity(
      v > quotaLeft ? `超出今日剩余额度 ${quotaLeft} 元` : ''
    );
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    // 1) 静默预检：不发 UI
    if (!form.checkValidity()) {
      // 2) 需要提示时再交给原生气泡，自动聚焦第一个非法字段
      form.reportValidity();
      return;
    }

    // 3) 用 validityState 区分错误类型，做精细化 UI
    if (amount.validity.customError) {
      document.getElementById('biz-err').hidden = false;
    } else {
      document.getElementById('biz-err').hidden = true;
      fetch('/api/withdraw', { method: 'POST', body: new FormData(form) });
    }
  });

  // 附：常见 validity 位速查
  amount.value = '';
  console.log(amount.validity.valueMissing); // true
  amount.value = '99999';
  console.log(amount.validity.rangeOverflow, amount.validity.customError); // true true
</script>
```
