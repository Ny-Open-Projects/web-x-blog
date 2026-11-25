---
title: [RBL-817] 场景题：组件库发布与文档站联动——版本化产物与文档的同步发布
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-817：场景题：组件库发布与文档站联动——版本化产物与文档同步

**答**:
- 组件库发布的三件套必须同版本：npm 包 + 文档站版本快照 + d.ts/类型——「文档站展示最新版但 npm 还是旧版」是高频事故（用户照文档用新 API 报错）。构建器/发布流程的联动：release 时文档站构建绑定 release 版本（URL 带 /v1.2.3/ 快照 + latest 重定向）。
- 版本快照的成本：每版本一份全量文档（构建产物膨胀）——策略：仅 major/里程碑做全量快照，minor 增量更新 latest（快照树保留关键版本）；「版本切换器」的数据来自发布记录。
- 类型文档的自动生成：API 文档（props 表格）从 d.ts 生成——构建期校验「文档示例可运行」（RBL-590 doctest 模式）；示例代码与实际 API 的漂移检测（示例引用的 props 已改名 → 文档构建失败）。
- deprecate 的联动：废弃 API 在文档站标注（从 registry.deprecated 读取）+ 运行时 console.warn（构建器注入 deprecation banner）——「废弃要三处同步：类型标记/文档/运行时警告」。
- 追问钩子：为什么文档站要「版本快照」而不是「永远最新」？——团队升级有节奏：老版本用户查文档需要老 API 语义（latest 文档可能已删掉他们用的 API）；快照是「时间旅行」能力，成本可控（关键版本）——文档的版本化与代码的版本化同构。

```javascript
// 发布联动
async function releaseWithDocs(pkg, version, { snapshot = false } = {}) {
  await build(pkg);                                      // 产物 + d.ts
  await npmPublish(pkg, version);
  const docBuild = await buildDocs({ version, apiExtract: true });
  await doctest(docBuild);                               // 示例可运行校验（RBL-590）
  if (snapshot || isMajor(version))
    await deployDocsSnapshot({ version, files: docBuild.files });   // 全量快照
  else
    await deployDocsLatest(docBuild);                    // 增量更新 latest
  await updateVersionsSwitcher(version);
}
// 废弃联动
function deprecate(api, { since, removal }) {
  registry.mark(api, { status: 'deprecated', since, removal });
  injectRuntimeWarning(api, `已废弃，${removal} 移除，替代: ${registry.replacement(api)}`);
  docsBadge(api, 'deprecated');                          // 文档标注
}
```
