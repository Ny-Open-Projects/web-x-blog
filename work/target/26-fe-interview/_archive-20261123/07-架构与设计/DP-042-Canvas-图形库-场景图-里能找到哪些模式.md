---
title: [DP-042] Canvas 图形库（场景图）里能找到哪些模式？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-042：Canvas 图形库（场景图）里能找到哪些模式？
**答**：
- 场景图（SceneGraph）：Canvas 上层封装的对象树——组合模式（Group/Shape 统一 render）+ 模板方法（基类定义绘制骨架，子类实现 draw）+ 享元（样式对象/画笔共享）。
- 典型库：Konva、Fabric.js、ECharts 的 ZRender 都是"场景图 + 渲染循环"。
- 其他模式：命令模式（undo/redo 栈）、备忘录（快照）、职责链（事件冒泡命中检测）。
- 面试价值：能在一个具体库里指认多模式，说明真正理解了"模式是组合使用的"。

```javascript
// 场景图最小骨架：组合 + 模板方法 + 命令
class Shape { // 模板方法：基类固定绘制流程
  constructor(props) { Object.assign(this, { x: 0, y: 0, ...props }); this.children = []; }
  render(ctx) {                       // 骨架：save -> 变换 -> draw -> restore
    ctx.save();
    ctx.translate(this.x, this.y);
    this.draw(ctx);                   // 变化点下放给子类（钩子）
    this.children.forEach((c) => c.render(ctx));
    ctx.restore();
  }
  add(shape) { this.children.push(shape); return this; }
  draw() {}
}
class Circle extends Shape {
  draw(ctx) {
    ctx.beginPath();
    ctx.arc(0, 0, this.r, 0, Math.PI * 2);
    ctx.fillStyle = this.fill;
    ctx.fill();
  }
}
class Group extends Shape {} // 纯容器：骨架中的 children 遍历已覆盖

// 命令模式：绘制历史 undo/redo
class History {
  constructor() { this.undoStack = []; this.redoStack = []; }
  execute(cmd) { cmd.do(); this.undoStack.push(cmd); this.redoStack = []; }
  undo() { const c = this.undoStack.pop(); c?.undo(); c && this.redoStack.push(c); }
}
const canvas = document.createElement('canvas');
const ctx = canvas.getContext('2d');
const stage = new Group();
const circle = new Circle({ r: 30, fill: 'red', x: 100, y: 100 });
const addCmd = {
  do() { stage.add(circle); },        // 命令封装"动作 + 逆动作"
  undo() { stage.children = stage.children.filter((c) => c !== circle); },
};
const history = new History();
history.execute(addCmd);
stage.render(ctx);
history.undo();
console.log(stage.children.length); // 0 —— 可撤销
```

---

## 七、行为型：观察者与发布订阅
