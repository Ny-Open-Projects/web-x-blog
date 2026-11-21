---
title: [PER-100] 错误如何聚合成指纹并与版本关联？sourcemap 还原流水线怎么搭？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-100：错误如何聚合成指纹并与版本关联？sourcemap 还原流水线怎么搭？

**答**：
- 错误指纹（fingerprint）：用“错误类型 + 归一化后的堆栈前三帧（去文件 hash、去行号抖动）”哈希生成，同一 bug 聚成一个 issue 而不是一万条日志。
- 版本关联：每条上报带 `appVersion`（构建号）与 `sourceMapId`，服务端按版本拉对应 sourcemap 还原；发版后 sourcemap 必须先上传再放量。
- 流水线：CI 构建 -> 产物与 sourcemap 上传符号服务器 -> sourcemap 不随站点发布（`hidden-source-maps`）-> 错误平台按版本还原堆栈。
- 聚合后还要做**回归检测**：新版本出现旧版本没有的指纹即“新增错误”告警，旧指纹在新版本上复现则是回归。

```yaml
# CI：构建后上传 sourcemap 到符号服务器，再发布站点
name: release
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run build   # webpack 配 hidden-source-maps：sourcemap 不进产物目录
      - name: upload sourcemaps
        run: |
          VERSION="${GITHUB_SHA::8}"
          for f in dist/assets/*.map; do
            curl -sS -X POST "$SYMBOL_SERVER/upload" \
              -H "Authorization: Bearer $SYMBOL_TOKEN" \
              -F "app=web-app" -F "version=$VERSION" -F "map=@$f"
          done
          echo "APP_VERSION=$VERSION" >> "$GITHUB_ENV"
      - name: deploy only js bundles
        run: rsync -a --exclude='*.map' dist/ deploy@prod:/var/www/app/
```

```javascript
// 服务端还原：按版本拉 sourcemap，把压缩堆栈映射回源码位置
const { SourceMapConsumer } = require('source-map');

async function resolveStack(errorReport) {
  const maps = await symbolServer.load(errorReport.appVersion, errorReport.stackFiles); // 按版本号取
  const consumers = new Map(maps.map((m) => [m.file, new SourceMapConsumer(m.content)]));
  const resolved = errorReport.frames.map((f) => {
    const smc = consumers.get(f.file);
    if (!smc) return f;
    const pos = smc.originalPositionFor({
      line: f.line, column: f.column,
    });
    return { ...f, source: pos.source, line: pos.line, column: pos.column, name: pos.name }; // 还原到源码
  });
  // 指纹用还原后的堆栈算，保证跨版本同名 bug 聚合到同一 issue
  const fingerprint = sha256(resolved.slice(0, 3).map((f) => `${f.source}:${f.name ?? ''}`).join('|'));
  return { resolved, fingerprint, appVersion: errorReport.appVersion };
}
```
