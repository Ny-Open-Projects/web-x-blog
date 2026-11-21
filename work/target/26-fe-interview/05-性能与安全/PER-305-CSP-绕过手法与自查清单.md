---
title: [PER-305] 常见的 CSP 绕过手法有哪些？如何给自己的站点做 CSP 自查？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-305：常见的 CSP 绕过手法有哪些？如何给自己的站点做 CSP 自查？

**答**：
- 白名单域即"通行证"：白名单里任何域开了 JSONP/开放重定向/任意文件托管（如 CDN 上传区），攻击者就能拼出 script-src 合法 URL 执行 XSS——所以白名单收敛到"只跑自己代码的域"是根本，这也让 strict-dynamic 成为首选。
- base 标签劫持：相对路径 script 会被 `<base href>` 重定向——必须配 `base-uri 'self'`。表单提交劫持同理需 `form-action 'self'`。
- 内联事件与 javascript: URI：`onclick=` 与 `href="javascript:..."` 不受 script-src 管，需 `script-src-attr`（或干脆禁内联事件改造）；默认的 `default-src` 忘配子指令会留洞（如 object/worker-src/frame-ancestors）。
- 其他洞：`object-src` 忘禁（Flash 时代 legacy，仍可能 embed HTML）、`worker-src` 未配回落 script-src 之外的 default、CSP 只在 HTTP 头配了但页面有 `<meta http-equiv>` 旧策略叠加、report-uri 泄漏策略信息给三方。
- 自查清单：白名单域逐个验证"是否只承载可信脚本"；base-uri/form-action/object-src/frame-ancestors 齐全；nonce 全覆盖动态脚本；report 数据周期审计；用 CSP Evaluator 等工具扫一遍策略文本。

```text
自查清单（逐项勾选）：
[ ] 白名单每个域验证：无 JSONP 端点、无开放重定向、非用户可控上传域
[ ] base-uri 'self' 与 form-action 'self' 已配置
[ ] object-src 'none'、frame-ancestors 'none'（无嵌入需求时）
[ ] worker-src 显式配置（不依赖 default-src 意外回落）
[ ] script-src-attr 'none'（禁内联事件 handler）
[ ] nonce 每响应随机（缓存页面注意：静态 HTML 缓存会让 nonce 复用！）
[ ] report-uri 持续监控，拦截样本人工复核
工具：csp-evaluator.withgoogle.com 扫策略文本
```
