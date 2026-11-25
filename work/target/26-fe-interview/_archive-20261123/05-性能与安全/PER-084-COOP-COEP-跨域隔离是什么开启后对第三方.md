---
title: [PER-084] COOP/COEP 跨域隔离是什么？开启后对第三方资源有什么影响？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-084：COOP/COEP 跨域隔离是什么？开启后对第三方资源有什么影响？

**答**：
- 三个头：**COOP**（Cross-Origin-Opener-Policy）隔离 window.opener，防标签页反向标签攻击与跨窗泄漏；**COEP**（require-corp）要求所有子资源声明可被跨域嵌入；**CORP**（Cross-Origin-Resource-Policy）声明自身允许被谁嵌入。
- 终极收益：COOP+COEP 开启后进入**跨域隔离状态**，才能使用 SharedArrayBuffer、高精度计时等强大 API（这些曾被 Spectre 攻击封禁）。
- 代价：COEP 生效后，未带 `Cross-Origin-Resource-Policy` 或 CORS 头的第三方图片/脚本/iframe 全部加载失败——接第三方资源前必须对方配合或走代理。
- 渐进迁移：用 COEP `credentialless`（Chrome 支持）先放开无 Cookie 资源，逐步推动第三方补 CORP 头。

```nginx
# nginx：跨域隔离三件套
server {
    listen 443 ssl;
    server_name app.example.com;

    add_header Cross-Origin-Opener-Policy "same-origin" always;                 # COOP：弹窗与 opener 隔离
    add_header Cross-Origin-Embedder-Policy "require-corp" always;              # COEP：子资源必须声明 CORP 或 CORS
    add_header Cross-Origin-Resource-Policy "same-origin" always;               # 自身资源默认只许同源嵌入

    # 跨域隔离生效后 SharedArrayBuffer 可用（音视频处理等场景）
    location / {
        proxy_pass http://app;
    }
}
```

```html
<!-- COEP 开启后：第三方资源必须显式声明可嵌入 -->
<!-- 1) 支持 CORS 的资源：加 crossorigin 即可通过 COEP 校验 -->
<img src="https://img.partner.com/pic.png" crossorigin="anonymous" alt="">
<!-- 2) 对方已加 CORP 声明的资源：无需改动 -->
<img src="https://cdn.example.com/logo.png" alt="">
<!-- 3) 不配合的第三方：走自家代理补头 -->
<img src="/api/proxy?url=https%3A%2F%2Flegacy-embed.com%2Fchart.png" alt="">
<script>
// 检测跨域隔离是否生效
console.log('crossOriginIsolated:', self.crossOriginIsolated); // true 才能用 SharedArrayBuffer
</script>
```

## 十四、加载策略深水区
