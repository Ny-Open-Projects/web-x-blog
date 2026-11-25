---
title: [OPS-047] 前端镜像的 CI 构建 push 流程怎么设计？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-047：前端镜像的 CI 构建 push 流程怎么设计？
**答**：
- 关键点：镜像 tag 要可追溯——用 git sha + 语义版本双 tag；latest 永不用于生产部署。
- 构建加速：BuildKit 层缓存（cache-from/cache-to gha）+ 依赖缓存，把"冷构建 10 分钟"压到"热构建 2 分钟"。
- 安全卡点：镜像扫描（trivy）高危漏洞阻断推送；推完后用 cosign 签名，部署侧只信签名镜像（可选进阶）。
- 推送后把镜像摘要（digest）写入部署产物，K8s 部署用 digest 而非浮动 tag，保证部署的不可变性。

```yaml
# .github/workflows/docker.yml：构建、扫描、推送、输出 digest
name: docker
on:
  push:
    branches: [main]

jobs:
  build-push:
    runs-on: ubuntu-latest
    permissions: { contents: read, packages: write }
    steps:
      - uses: actions/checkout@v4

      - uses: docker/setup-buildx-action@v3

      - name: Login registry
        uses: docker/login-action@v3
        with:
          registry: registry.example.com
          username: ${{ secrets.REG_USER }}
          password: ${{ secrets.REG_TOKEN }}

      - name: Build and push
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: |
            registry.example.com/web-mall:${{ github.sha }}
            registry.example.com/web-mall:v2026.11.01
          cache-from: type=gha          # 复用 GH Actions 层缓存
          cache-to: type=gha,mode=max

      - name: Scan image
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: registry.example.com/web-mall:${{ github.sha }}
          severity: CRITICAL,HIGH
          exit-code: "1"                # 高危漏洞阻断流水线

      - name: Export digest for deploy
        run: |
          DIGEST=$(docker buildx imagetools inspect \
            registry.example.com/web-mall:${{ github.sha }} \
            --format '{{json .Manifest.Digest}}')
          echo "digest=$DIGEST" >> $GITHUB_OUTPUT
```
