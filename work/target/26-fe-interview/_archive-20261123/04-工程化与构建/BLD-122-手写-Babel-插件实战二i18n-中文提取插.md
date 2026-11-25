---
title: [BLD-122] 手写 Babel 插件实战二：i18n 中文提取插件（扫描 + 生成语言包）。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 笔试题, 18]
type: 笔试题
---

## BLD-122：手写 Babel 插件实战二：i18n 中文提取插件（扫描 + 生成语言包）。
**答**：
- 需求：扫描所有 JSX/字符串字面量里的中文，替换为 `t('key')`，并把"原文→key"写入抽出的 JSON 语言包——国际化改造的自动化工具。
- 实现要点：visitor 命中 `StringLiteral / JSXText / TemplateLiteral`，用 `/[\u4e00-\u9fa5]/` 判断含中文；key 用**原文 md5 前 8 位**或"模块名_序号"保证稳定（同一原文全局同 key）；替换为 `t('key')` 调用并按需注入 import。
- 工程细节：排除注释与 console 日志（可用 comments 判断）；`t` 若未导入需在 Program 层 `path.unshiftContainer('body', importDeclaration)`；语言包按文件增量 merge 写盘（插件里用 `state.filename` 定位）。
- 配套：`state.opts.output` 支持命令行传语言包路径，插件内 `fs.writeFileSync` 落盘（插件是 Node 环境，可直接 IO）。

```javascript
// babel-plugin-extract-i18n.js：中文提取与 t() 替换
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const t = require('@babel/types');

const CJK = /[\u4e00-\u9fa5]+/;
const pack = {}; // 全局累计（babel 进程内），构建结束统一落盘

module.exports = function ({ types }) {
  return {
    name: 'extract-i18n',
    visitor: {
      Program: {
        enter(programPath, state) {
          state.set('needT', false); // 标记本文件是否用到 t()
        },
        exit(programPath, state) {
          if (state.get('needT')) {
            // 已有 import { t } 则不重复注入
            const has = programPath.node.body.some(
              (n) => t.isImportDeclaration(n) && n.source.value === '@/locale'
            );
            if (!has) {
              programPath.unshiftContainer('body',
                t.importDeclaration(
                  [t.importSpecifier(t.identifier('t'), t.identifier('t'))],
                  t.stringLiteral('@/locale')
                )
              );
            }
          }
        },
      },
      StringLiteral(path, state) {
        const raw = path.node.value;
        if (!CJK.test(raw)) return;
        if (path.findParent((p) => p.isConsoleStatement?.())) return; // 排除日志
        const key = 'k' + crypto.createHash('md5').update(raw).digest('hex').slice(0, 8);
        pack[key] = raw;                                   // 收录语言包
        path.replaceWith(
          t.callExpression(t.identifier('t'), [t.stringLiteral(key)])
        );
        state.set('needT', true);
      },
      JSXText(path, state) {
        const raw = path.node.value.trim();
        if (!CJK.test(raw)) return;
        const key = 'k' + crypto.createHash('md5').update(raw).digest('hex').slice(0, 8);
        pack[key] = raw;
        path.replaceWith(
          t.jsxExpressionContainer(t.callExpression(t.identifier('t'), [t.stringLiteral(key)]))
        );
        state.set('needT', true);
      },
    },
    post() { // post 在整个 babel 转换结束后调用一次/文件
      // 简化：直接覆盖 zh-CN.json；生产应 merge 且加 lint 防手工编辑丢失
      fs.writeFileSync(
        path.resolve(process.cwd(), 'locales/zh-CN.json'),
        JSON.stringify(pack, null, 2)
      );
    },
  };
};
// 输入： <Button>提交订单</Button>   输出： <Button>{t("k3f2a9c1d")}</Button>
```
