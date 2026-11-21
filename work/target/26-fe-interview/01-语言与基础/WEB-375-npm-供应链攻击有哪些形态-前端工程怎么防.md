---
title: [WEB-375] npm 供应链攻击有哪些形态？前端工程怎么防？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 笔试题
---

## WEB-375：npm 供应链攻击有哪些形态？前端工程怎么防？
**答**：
- 形态：恶意包投毒（typosquatting 名字仿冒）、已维护包被卖号推送恶意版本、install/postinstall 脚本执行、镜像源被污染。
- 工程防线：lockfile 锁版本 + CI 校验（npm ci）、audit 与依赖扫描（socket/snyk）、禁止未知来源 postinstall、npm provenance/签名校验。
- 底线操作：新包引入先看周下载量、仓库、维护者与发布时间；重要项目开启 dependabot/renovate + 审查升级 diff。

```javascript
// .npmrc 与 CI 防线
// audit=true, engine-strict=true
// ignore-scripts=true            ← 阻断 postinstall（按需放行）
const gate = (pkg) => {
  if (!registryOfficial(pkg.name)) throw '仅允许官方源';
  if (pkg.age < 14) throw '新包冷却期，人工审查';
  return 'ok';
};
console.log('lockfile + ignore-scripts + 冷却审查');
```

**评分点**：
- 结论先行，机制一句话讲透
- 覆盖攻击面/异常分支与边界条件
- 代码可运行、命名清晰、有防御性处理
- 主动给出工程取舍与常见坑
