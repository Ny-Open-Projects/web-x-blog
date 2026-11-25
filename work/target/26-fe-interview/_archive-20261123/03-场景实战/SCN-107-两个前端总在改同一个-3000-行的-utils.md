---
title: [SCN-107] 两个前端总在改同一个 3000 行的 utils.js，git 冲突不断，如何从工程上收敛？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-107：两个前端总在改同一个 3000 行的 utils.js，git 冲突不断，如何从工程上收敛？
**答**：
- 冲突根因是模块边界缺失：按领域拆分（utils/date、utils/money、utils/validate），依赖显式化，改不同域就不再碰同一个文件。
- 迁移期保留聚合层 re-export 兼容老引用，配合 lint 规则禁止新代码从聚合层引入，调用方渐进迁移。
- 组织配套：CODEOWNERS 指定模块责任人，跨域修改强制评审；大改动提前沟通拆小 PR。

```bash
# 1) 按领域拆模块，git mv 保留文件历史
mkdir -p src/utils/date src/utils/money
git mv src/utils.js src/utils/date/core.ts

# 2) 兼容层：老路径 re-export，调用方渐进迁移
cat > src/utils/index.js <<'EOF'
export { formatDate, formatRange } from './date';
export { fen2yuan, thousandSeparator } from './money';
EOF

# 3) CODEOWNERS：指定模块责任人，跨域修改强制评审
echo "src/utils/  @zhangsan @lisi" >> .github/CODEOWNERS

# 4) ESLint：新代码禁止从聚合层引入，防止再次发散
npx eslint src --rule '{"no-restricted-imports": ["error", {"patterns": ["@/utils"]}]}' --fix-dry-run
```
