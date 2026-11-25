---
title: [DP-099] 重构实战：if-else 巨型分支 → 策略；类继承 → 函数式组合，怎么落地？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-099：重构实战：if-else 巨型分支 → 策略；类继承 → 函数式组合，怎么落地？
**答**：
- 坏味道→模式映射表：巨型条件→策略/状态；重复 switch→多态/查表；长参数列表→options/建造者；深层继承→组合；临时字段泛滥→命令/备忘录。
- 重构纪律：先补测试锁定现状 → 小步提取函数 → 再引模式；"闻到坏味道"是信号，模式是工具不是目的。
- OO→函数式重构方向：类层次（模板方法）→ 高阶函数注入；setter 状态修改 → 纯函数 + 不可变数据；命令对象 → 闭包/函数值。

```javascript
// 实战1：巨型条件 -> 策略表（先测试，后重构）
// 重构前：审批流 if-else 泥潭（每加审批类型都要改此函数）
function calcApproverLegacy(ticket) {
  if (ticket.type === 'expense' && ticket.amount > 10000) return 'CFO';
  else if (ticket.type === 'expense') return 'manager';
  else if (ticket.type === 'leave' && ticket.days > 3) return 'director';
  else if (ticket.type === 'leave') return 'leader';
  return 'HR';
}
// 重构后：规则表（数据化），每条规则 = 条件 + 审批人（可配置、可测试）
const approvalRules = [
  { when: (t) => t.type === 'expense' && t.amount > 10000, approver: 'CFO' },
  { when: (t) => t.type === 'expense', approver: 'manager' },
  { when: (t) => t.type === 'leave' && t.days > 3, approver: 'director' },
  { when: (t) => t.type === 'leave', approver: 'leader' },
];
const calcApprover = (ticket) => approvalRules.find((r) => r.when(ticket))?.approver ?? 'HR';
// 回归验证：与旧实现结果一致（重构安全性来源）
[
  [{ type: 'expense', amount: 20000 }, 'CFO'],
  [{ type: 'expense', amount: 100 }, 'manager'],
  [{ type: 'leave', days: 5 }, 'director'],
  [{ type: 'leave', days: 1 }, 'leader'],
  [{ type: 'other' }, 'HR'],
].forEach(([t, expect]) => console.log(calcApprover(t) === expect, calcApprover(t)));

// 实战2：模板方法类层次 -> 函数式组合（OO -> FP）
// 重构前：类层次固定骨架（见 DP-060 BaseChart）
// 重构后：骨架 = 函数，步骤 = 可注入参数
const createChartV2 = ({ container, process = (d) => d, draw, after }) => (data) => {
  const el = document.createElement('canvas');       // 骨架步骤1：固定
  container.appendChild(el);
  const processed = process(data);                   // 骨架步骤2：注入
  draw(el, processed);                               // 骨架步骤3：注入
  after?.(el);                                       // 骨架步骤4：可选注入
  return () => el.remove();                          // 返回清理函数（ RAII ）
};
const lineChart = createChartV2({
  container: document.body,
  process: (d) => d.map((p) => ({ ...p, smooth: true })),       // 策略注入
  draw: (el, data) => console.log('画折线', data.length, '点'),
});
const destroy = lineChart([{ x: 1 }]);               // 画折线 1 点 —— 无类层次，自由组合
destroy();
// 对比：继承版新增图表要写子类；函数版新增图表 = 换一组参数（组合优于继承的落地）
```
