---
title: [ENG-069] create-vite 的源码设计有什么值得借鉴的思想？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-069：create-vite 的源码设计有什么值得借鉴的思想？
**答**：
- 模板不是远程下载，而是 npm 包内自带的 template-* 目录，安装即用、离线可用、发版即更新。
- 交互极简：只问框架与变体（ts/js），按目录组织模板而不是运行时大量分支拼装。
- 变量注入最少化：只改 package.json 的 name，其余保持模板原样，降低模板维护成本。
- 对自研脚手架的启示：模板越"静态"越好，动态逻辑放在交互与后置脚本里。

```typescript
// create-vite 核心思路（简化）
import prompts from 'prompts';

const { framework, variant } = await prompts([
  { type: 'select', name: 'framework', message: '选择框架', choices: [
    { title: 'Vue', value: 'vue' }, { title: 'React', value: 'react' },
  ] },
  { type: (prev) => (prev ? 'select' : null), name: 'variant', message: '变体', choices: [
    { title: 'TypeScript', value: 'ts' }, { title: 'JavaScript', value: 'js' },
  ] },
]);

// 模板在包内 template-vue-ts 目录，直接拷贝，零网络依赖
const templateDir = path.join(__dirname, `template-${framework}-${variant}`);
copyDir(templateDir, targetDir); // 之后只改 package.json 中的 name 字段
```
