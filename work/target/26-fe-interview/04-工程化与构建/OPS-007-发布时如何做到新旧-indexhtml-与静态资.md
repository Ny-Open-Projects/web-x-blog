---
title: [OPS-007] 发布时如何做到新旧 index.html 与静态资源多版本并存？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-007：发布时如何做到新旧 index.html 与静态资源多版本并存？
**答**：
- 原理：每次构建产出一个带版本号的独立目录（releases/{version}/），index.html 只通过 current 符号链接指向当前版本；历史目录保留不删。
- 只要 JS/CSS 的文件名带 content hash，旧 index.html 引用的旧 chunk 仍然存在，正在浏览旧页面的用户不会 404——这是前端发布安全的地基。
- 切换 = 重建 symlink，原子且瞬时；回滚 = 把 symlink 指回上一版本。
- 定期清理 N 版之前的目录（且要保守，留足"最长停留会话"的时间）。

```bash
#!/usr/bin/env bash
# deploy.sh：版本化目录发布，支持多版本并存与秒级回滚
set -euo pipefail

APP_DIR="/data/web/mall"
RELEASES="$APP_DIR/releases"
VERSION="$(date +%Y%m%d%H%M%S)-$(git -C /tmp/build rev-parse --short HEAD)"
TARGET="$RELEASES/$VERSION"

# 1. 上传新版本目录（目录名含版本号，永不覆盖旧目录）
rsync -az --delete /tmp/build/dist/ "deploy@web01:$TARGET/"
rsync -az --delete /tmp/build/dist/ "deploy@web02:$TARGET/"

# 2. 原子切换：先生成临时链接再 mv，避免出现 symlink 不存在的瞬间
ssh deploy@web01 "ln -sfn $TARGET $APP_DIR/current.tmp && mv -Tf $APP_DIR/current.tmp $APP_DIR/current"
ssh deploy@web02 "ln -sfn $TARGET $APP_DIR/current.tmp && mv -Tf $APP_DIR/current.tmp $APP_DIR/current"

# 3. 只保留最近 10 个版本，且至少保留 24 小时内的全部版本（防止老会话 404）
ssh deploy@web01 "
  cd $RELEASES
  ls -1t | tail -n +11 | while read v; do
    [ \$(find \"\$v\" -maxdepth 0 -mtime +1 2>/dev/null | wc -l) -eq 1 ] && rm -rf \"\$v\"
  done"

echo "deployed $VERSION, rollback: ln -sfn $RELEASES/<old> $APP_DIR/current"
```
