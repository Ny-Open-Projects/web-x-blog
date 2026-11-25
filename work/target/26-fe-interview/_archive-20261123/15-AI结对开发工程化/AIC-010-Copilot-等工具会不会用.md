---
title: [AIC-010] 团队里有人担心 Copilot 类工具会把公司代码上传泄漏，隐私模式与合规要点有哪些？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-010：团队里有人担心 Copilot 类工具会把公司代码上传泄漏，隐私模式与合规要点有哪些？
**答**：
- 技术层面：Copilot Business/Enterprise 有不训练承诺与零数据保留选项；Cursor 有 Privacy Mode（请求不留存）。关键是确认「启用的到底是什么版本」——个人免费版与企业版的隐私条款完全不同。
- 合规层面：先查公司安全政策与客户合同（很多 B 端合同明确禁止代码出境/交第三方），工具白名单由安全团队审批，而不是个人装了就用。
- 分级策略：核心仓库（支付、鉴权）禁用或走私有化部署模型；一般业务仓库可用云端工具但关闭遥测；开源/脚手架仓库不限制。
- 技术兜底：仓库级 pre-commit 扫描敏感信息（密钥、手机号），即使误传也在本地拦截。
- 追问钩子：面试官可能追问「私有化部署的代价」——算力成本、模型能力弱于顶级云端模型、运维投入。

```yaml
# .github/copilot/config.yml 示意：仓库级关闭内容使用 + 敏感文件排除
policy:
  exclude:
    - "**/*.env*"
    - "server/keys/**"
    - "**/secrets.yaml"
```

```bash
# pre-commit 本地兜底：扫描疑似密钥
git secrets --scan || gitleaks detect --source . -v
```
