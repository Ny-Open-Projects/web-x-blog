---
title: 组件批量开发范式：新增一个组件的五步清单
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 实战, 组件开发, share]
---

## 组件批量开发范式：新增一个组件的五步清单

课程 15 种组件（titleText/swiper/list/image/video/card/split/richText/qrcode/alert/input/textArea/radio/checkbox/empty）全部沿用同一范式，新增组件五步：
1. **share 放视图组件** + 类型 + 默认值（编辑页与发布页共用）；
2. **client 放属性配置组件**（视图映射在 share、配置映射只在 client）；
3. **必改三处**：组件 index.ts 导出、types.ts 加类型、componentExport 注册（漏一处触发遍历断链 + TS 警告）；
4. **改 share 必须 `pnpm build:share`**，别处才能引入新内容；
5. 数据流：右侧表单改值 → store action → 视图 useMemo/observer 刷新。

**通用配置形态** = value/defaultValue/isHidden 三件套。列表型组件（轮播/列表/单选多选）复用 `FormContainerWithList`（keyName/id/value 数组/newItemDefaultValue 四参），非列表用 `FormContainer`。

**采集型组件**（问卷）额外要求：视图组件必须预留 `onChange/onUpdate` 回调把用户输入抛给发布页，收集成 `{id,value}` 数组提交。文本域 = 复用输入框配置面板只把 Input 换成 `Input.TextArea`——零成本复用的示范。

**踩坑集**：Tailwind base 重置了 h1~h6/ol/ul 默认样式，富文本须全局样式补回且放在 Tailwind 之后；ColorPicker 回调返回颜色对象需 `toHex()`；函数被当 type 导入的坑。

出处「课程25 · 15-1~16-7」
