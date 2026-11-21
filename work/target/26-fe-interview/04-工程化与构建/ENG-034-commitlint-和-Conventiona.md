---
title: [ENG-034] commitlint 和 Conventional Commits 是什么？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-034：commitlint 和 Conventional Commits 是什么？
**答**：
- Conventional Commits 规定提交格式：type(scope): subject，如 feat(order): 支持批量导出。
- 常用 type：feat、fix、docs、style、refactor、perf、test、build、ci、chore。
- commitlint 校验提交信息合法性，挂在 commit-msg 钩子，不合格直接拒绝。
- 收益：提交历史结构化，可自动生成 changelog、自动判断 semver 升级级别。

```bash
npm install --save-dev @commitlint/cli @commitlint/config-conventional

# commitlint.config.js 内容
cat > commitlint.config.js << 'EOF'
module.exports = { extends: ['@commitlint/config-conventional'] };
EOF

# 挂到 commit-msg 钩子
echo "npx --no -- commitlint --edit \$1" > .husky/commit-msg

# 合规提交示例
git commit -m "feat(order): 支持批量导出订单"
git commit -m "fix: 修复登录页在窄屏下的溢出"
```

---

## 第七章 Git 工作流（ENG-035 ~ ENG-039）
