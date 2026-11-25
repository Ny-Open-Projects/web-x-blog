---
title: [HW-343] 手写一个 Canvas 图层系统：离屏 canvas 分层与合成
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-343：手写一个 Canvas 图层系统：离屏 canvas 分层与合成

**答**：
- 需求：实现 LayerSystem：分层（背景层/内容层/交互层），每层一个离屏 canvas；节点归属层（静态节点入背景层，动节点入内容层）；重绘只重绘所属层，最后 drawImage 合成到主 canvas；层可见性/透明度控制。
- 边界：合成时全局透明度（globalAlpha）；层重绘仍可嵌套脏区；主 canvas 尺寸变化时全部层 resize。
- 评分点：分层重绘减少全量；drawImage 合成；层 resize。

```javascript
class LayerSystem {
  constructor(mainCanvas, layers = ['bg', 'content', 'ui']) {
    this.main = mainCanvas.getContext('2d');
    this.layers = new Map(layers.map(name => [name, this.makeLayer(mainCanvas)]));
  }
  makeLayer(src) {
    const c = document.createElement('canvas');
    c.width = src.width; c.height = src.height;
    return { canvas: c, ctx: c.getContext('2d'), dirty: true, alpha: 1, visible: true };
  }
  renderLayer(name, nodes) {                                 // 只重绘脏层
    const layer = this.layers.get(name);
    if (!layer.dirty) return;
    layer.ctx.clearRect(0, 0, layer.canvas.width, layer.canvas.height);
    nodes.filter(n => n.layer === name).forEach(n => n.draw(layer.ctx));
    layer.dirty = false;
  }
  composite() {                                              // 合成到主 canvas
    this.main.clearRect(0, 0, this.main.canvas.width, this.main.canvas.height);
    for (const layer of this.layers.values()) {
      if (!layer.visible) continue;
      this.main.globalAlpha = layer.alpha;
      this.main.drawImage(layer.canvas, 0, 0);               // drawImage 合成
      this.main.globalAlpha = 1;
    }
  }
  frame(scene) {                                             // 一帧流程
    for (const name of this.layers.keys()) this.renderLayer(name, scene.nodes);
    this.composite();
  }
  resize(w, h) { for (const l of this.layers.values()) { l.canvas.width = w; l.canvas.height = h; l.dirty = true; } }
}
```
