---
title: [DP-212] 源码识别：Ant Design Form 源码中的发布订阅与注册器？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-212：源码识别：Ant Design Form 源码中的发布订阅与注册器？
**答**：
- 发布订阅：FieldEntity 注册进 formStore（registerField），值变化 notify 指定 path 的观察者——和全局 pub-sub 的区别是**按字段路径精确通知**（性能关键）。
- 注册器模式：Form.Item 挂载时向 store 注册自己（namePath、校验规则），卸载注销——"组件即观察者"的注册器实现。
- 命令+状态机：validateFields 返回 Promise（成功/失败聚合），校验任务有状态（pending/resolved），resetFields 是命令式状态复位。
- 识别要点：性能题答案在这——`notifyObservers(watchList, changedFields)` 只通知依赖变化字段的 Item，避免整表单重渲染。

```javascript
// AntD Form store 简化
class FormStore {
  entities = [];                    // FieldEntity 注册表（观察者）
  values = {};
  registerField(entity) { this.entities.push(entity); return () => {
    this.entities = this.entities.filter(e => e !== entity); }; }      // 注销
  updateValue(namePath, value) {
    set(this.values, namePath, value);
    const watchList = this.entities.filter(e => dependsOn(e.namePath, namePath)); // 精确匹配依赖
    watchList.forEach(e => e.reRender());        // 只重渲染受影响字段
    this.validateField(namePath);                // 触发该字段校验（命令）
  }
  async validateFields(nameList) {
    const tasks = this.entities.filter(e => !nameList || matchPath(e.namePath, nameList))
      .map(e => e.validateRules());              // 并行校验
    return Promise.all(tasks).then(rs => rs.reduce((acc, r) => ({ ...acc, ...r }), {}));
  }
}
```
