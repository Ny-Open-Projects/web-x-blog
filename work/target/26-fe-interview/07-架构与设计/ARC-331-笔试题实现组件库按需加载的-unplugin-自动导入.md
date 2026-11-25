---
title: [ARC-331] 笔试题：实现组件库按需加载的自动导入插件？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-331：笔试题：实现组件库按需加载的自动导入插件？
**答**：实现一个构建插件（unplugin 风格）：1) 识别源码中使用的 `<ElButton>`/`ElMessage` 并自动注入 `import { ElButton } from 'ui'` 与对应样式 `import 'ui/es/button/style/index.css'`；2) 不重复注入；3) 支持解析配置（组件→样式路径映射表）。
**评分点**：
- transform 钩子里正确扫描模板/script 中的组件引用（正则或 AST）。
- 注入去重（分析已有 import 声明，合并具名导入而非重复行）。
- 样式映射表驱动（resolver 配置），组件名 kebab-case 转换正确。
- 只处理目标库引用，不污染用户自己的组件。
```javascript
// unplugin-auto-import 风格
function createUiResolver({ components } /* components: { ElButton: 'button', ElMessage: 'message' } */) {
  const kebab = s => s.replace(/([A-Z])/g, '-$1').toLowerCase().replace(/^-/, '').replace(/^el-/, '');
  return {
    transform(code, id) {
      if (!/\.(vue|tsx?|jsx)$/.test(id) || id.includes('node_modules')) return null;
      const used = new Set();
      for (const name of Object.keys(components)) {
        if (new RegExp(`<${name}[\\s/>]`).test(code) || new RegExp(`\\b${name}\\.`).test(code)) used.add(name);
      }
      if (!used.size) return null;
      let out = code;
      for (const name of used) {
        if (new RegExp(`import\\s*{[^}]*${name}[^}]*}\\s*from\\s*['"]ui['"]`).test(out)) continue; // 2) 去重
        out = `import { ${name} } from 'ui';\nimport 'ui/es/${kebab(name)}/style/index.css';\n` + out;
      }
      return { code: out, map: null };
    },
  };
}
```
