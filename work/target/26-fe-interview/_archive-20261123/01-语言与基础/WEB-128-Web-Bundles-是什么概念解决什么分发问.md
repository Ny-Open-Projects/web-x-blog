---
title: [WEB-128] Web Bundles 是什么概念？解决什么分发问题？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-128：Web Bundles 是什么概念？解决什么分发问题？
**答**：
- Web Bundles（.wbn）把一个站点的 HTML/CSS/JS/图片打包成单个二进制文件，内含资源清单与完整内容，可离线分发或离线打开。
- 场景：弱网/无网区域整站分发（P2P、U 盘、邮件）、内容可离线自校验（bundle 内签名证明出处）、微前端把子应用作为 bundle 交付。
- 与 SW 预缓存的区别：SW 缓存依赖首次在线访问，bundle 天生完整可离线且自带完整性声明。
- 现状：Chrome 有实验性支持（webbundle/wbn 格式），尚未成为普适标准，面试按概念与动机答即可。

```bash
# 用 webbundle CLI 工具打包静态站点
# npm i -g wbn（gen-bundle 命令）
gen-bundle \
  -url https://app.example.com/ \   # 主 URL，作为 bundle 的入口标识
  -dir ./dist \                     # 构建产物目录整体打入
  -primaryURL https://app.example.com/ \
  -o app.wbn

# 校验与预览
# Chrome 启动参数：--enable-blink-features=WebBundles
# 打开 file:///path/to/app.wbn 即可离线浏览整站
ls -lh app.wbn   # 单文件包含整站，可任意渠道分发
```
