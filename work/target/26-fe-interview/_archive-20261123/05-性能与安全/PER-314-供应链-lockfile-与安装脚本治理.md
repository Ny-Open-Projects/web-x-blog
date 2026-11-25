---
title: [PER-314] 供应链安全：lockfile 策略、install 脚本治理与私有源如何形成纵深？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-314：供应链安全：lockfile 策略、install 脚本治理与私有源如何形成纵深？

**答**：
- lockfile 是"已审计状态"的快照：CI 一律 `npm ci`（按 lock 精确安装），本地也不许 `npm install <pkg>` 直接改 lock 后未审计合入；lockfile 变更进 code review 必看 diff（新增了哪些包/脚本）。
- install 脚本治理：`.npmrc` 设 `ignore-scripts=true`（默认不执行任何包的 install 脚本），确需脚本的包（如 node-sass 过渡）单独白名单放行——这直接废掉"npm 投毒最常见Payload：install 脚本执行任意命令"这条主路。
- 私有源/镜像：公司级 registry（代理 npmjs + 白名单 + 漏洞过滤 + 内部包），`publishConfig` 禁止误发布（`private: true`）；npm 包名抢注监控（新包与内部包名近似即告警）。
- 移动端/桌面端同理：CocoaPods/Gradle 同样有 lock 与仓库白名单思维。
- 组合纵深：lockfile 锁内容、ignore-scripts 锁执行、私有源锁来源、SBOM 锁清单、CI audit 锁漏洞——五层各挡一类攻击，缺一层就有一条路。

```ini
; .npmrc（仓库级提交）
audit=true
ignore-scripts=true
registry=https://registry.npmmirror.example.com/   ; 公司私有代理源
save-exact=true                                     ; 固定版本，防 ^ 漂移
```
```json
// package.json 关键字段
{ "private": true,
  "scripts": { "preinstall": "node scripts/check-lockfile.js" } }  // 校验 lock 与清单一致性
// CI: npm ci --ignore-scripts && npm audit --audit-level=high && npm run build
```
