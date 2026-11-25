---
title: [PER-126] 如何制定一份可落地的前端安全编码 Checklist（输入/输出/存储/通信四层）？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-126：如何制定一份可落地的前端安全编码 Checklist（输入/输出/存储/通信四层）？

**答**：
- 规范必须按数据流向分层：**输入层**（白名单校验类型/长度/格式）、**输出层**（按 HTML/属性/URL/JS 四种上下文分别编码）、**存储层**（localStorage 不放凭证与 PII、Cookie 全量 HttpOnly/Secure/SameSite）、**通信层**（全站 HTTPS、postMessage 校验 origin、错误响应不带堆栈）。
- 核心口诀：输入做"校验"，输出做"编码"，两者不可互相替代——校验挡格式错误，编码挡上下文逃逸。
- Checklist 要可机检：每条对应一条 Semgrep/ESLint 规则或 CI 卡口，纯文档规范等于没有规范。
- 落地机制：CR 模板挂 Checklist、CI 扫描强制项、每季度人工抽查，违规项进安全债台账限期修复。

```json
{
  "frontend_security_checklist": {
    "input": {
      "rules": ["所有外部输入按类型白名单校验", "富文本只允许白名单标签与属性", "文件上传校验扩展名 MIME 与魔数", "数字与日期在入口统一转换"],
      "ci_rule": "semgrep: input-validation-required"
    },
    "output": {
      "rules": ["HTML 上下文依赖框架默认转义", "URL 输出前校验协议与域名白名单", "style 与事件属性禁止字符串拼接", "富文本输出前过 DOMPurify"],
      "ci_rule": "eslint: no-innerhtml-string-concat"
    },
    "storage": {
      "rules": ["localStorage 禁止存 token 与 PII", "sessionStorage 只放会话级非敏感数据", "Cookie 一律 HttpOnly Secure SameSite", "加密密钥不落前端"]
    },
    "comm": {
      "rules": ["接口全站 HTTPS 并开启 HSTS", "postMessage 双向校验 origin", "敏感字段传输前脱敏", "错误响应不回传堆栈与 SQL"]
    }
  }
}
```
