---
title: [DP-092] 组件库源码（element-plus/antd）里有哪些模式？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-092：组件库源码（element-plus/antd）里有哪些模式？
**答**：
- **外观**：`ElMessage/ElNotification` 把"创建实例→挂载→动画→销毁"封装成一行调用。
- **模板方法**：Form 组件基类骨架（注册字段→校验→提交→反馈），字段组件只填钩子。
- **策略 + 工厂**：`type="primary/success/danger"` 的样式策略；`ElButton` 内部按 type 查表取 class。
- **单例 + 中介**：ConfigProvider 全局配置注入；**组合**：`<Form><FormItem><Input/></FormItem></Form>` 上下文协同。

```jsx
// 组件库模式速览（对照 element-plus / antd 源码结构）
// 1. 外观：ElMessage 的完整生命周期被收拢
function Message(options) {
  const { content, duration = 3000, type = 'info' } = typeof options === 'string' ? { content: options } : options;
  const host = document.createElement('div');
  host.className = `el-message el-message--${type}`; // 策略：类型查表
  host.textContent = content;
  document.body.appendChild(host);
  const timer = setTimeout(() => {                    // 模板骨架：定时 -> 动画 -> 卸载
    host.style.opacity = '0';
    setTimeout(() => host.remove(), 300);
  }, duration);
  return { close: () => { clearTimeout(timer); host.remove(); } }; // 返回控制句柄
}
Message.success = (c) => Message({ content: c, type: 'success' }); // 便捷方法（外观语义化）
Message.success('已保存'); // 一行完成创建-挂载-自毁

// 2. 模板方法 + 中介：Form 校验骨架，FormItem 经 Context 协同
const FormContext = React.createContext(null);
function Form({ children, onFinish }) {                     // 骨架持有者
  const fieldsRef = React.useRef([]);                       // 中介：收集所有字段
  const api = React.useMemo(() => ({
    register: (field) => { fieldsRef.current.push(field); return () => {
      fieldsRef.current = fieldsRef.current.filter((f) => f !== field); }; },
    validateAll: async () => {                              // 固定校验流程（模板方法）
      const results = await Promise.all(fieldsRef.current.map((f) => f.validate()));
      return results.every(Boolean);
    },
  }), []);
  return (
    <FormContext.Provider value={api}>
      <form onSubmit={async (e) => { e.preventDefault(); if (await api.validateAll()) onFinish?.(); }}>
        {children}
      </form>
    </FormContext.Provider>
  );
}
function FormItem({ name, rules, children }) {              // 字段钩子
  const form = React.useContext(FormContext);
  const valueRef = React.useRef('');
  React.useEffect(() => form.register({
    name,
    validate: async () => {                                 // 钩子：具体校验策略由 rules 决定
      for (const rule of rules) if (!(await rule(valueRef.current))) return false;
      return true;
    },
  }), [name, rules]);
  return <div>{React.cloneElement(children, {
    onChange: (e) => { valueRef.current = e.target.value; },
  })}</div>;
}
// <Form onFinish={save}><FormItem name="phone" rules={[mustPhone]}><Input/></FormItem></Form>
```
