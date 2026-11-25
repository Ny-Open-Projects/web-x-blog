---
title: [AIC-596] AI 代码敏感数据泄露检测
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-596：AI 代码敏感数据泄露

**答**:
- AI 生成代码的敏感数据泄露模式（RBL-762 扩展到 AI 特有）：1) **环境变量硬编码**（AI 生成 `const key = "sk-abc123"`——训练数据中的示例 key 被复现（AI 记住了训练数据中的 API key 格式）；2) **连接字符串泄露**（AI 生成的 DB 连接串包含真实密码（`postgres://admin:password123@host/db`——AI 从训练数据复制了连接模式；3) **JWT secret 硬编码**（`jwt.sign(payload, "secret123")`——AI 使用了"看起来合理"的 secret（但任何人都能猜到——JWT 的 secret 必须来自环境变量）；4) **PII 硬编码**（AI 生成测试数据含真实 PII（训练数据中的个人信息被复现——GDPR 违规 RBL-601）。
- AI 特有的泄露原因：AI 不区分"示例"与"真实值"（训练数据中的 API key 示例被 AI 当作"标准做法"复现——人写代码会意识到"这是示例要换成真实的"，AI 不做这个区分）。
- 追问钩子：为什么「AI 生成的硬编码密钥」比「人写的硬编码密钥」更危险？——人写硬编码密钥 = 开发者知道这是临时的（会替换——但可能忘）；AI 硬编码密钥 = AI 不知道这是敏感数据（LLM 把训练数据中的密钥模式当作"正确做法"复现——开发者可能没注意到 AI 嵌入了密钥）；「AI 的密钥泄露的隐蔽性」：人写的 `password123` 容易被发现（明显的占位符）；AI 写的 `sk-proj-abc123def456`（看起来像真实 key——开发者和安全扫描都可能漏过——AI 的输出"看起来合理"反而是安全隐患 RBL-507 幻觉的反面：太合理了反而危险）。

```typescript
// AI 代码敏感数据泄露检测
const SENSITIVE_PATTERNS = [
  { type: 'api-key', re: /(?:sk-|pk-|api[_-]?key|apikey)\s*[:=]\s*['"][A-Za-z0-9_\-]{20,}['"]/i },
  { type: 'db-connection', re: /(?:postgres|mysql|mongodb):\/\/\w+:\w+@/i },
  { type: 'jwt-secret', re: /jwt\.sign\(\s*\w+\s*,\s*['"][^'"]{8,}['"]/i },
  { type: 'aws-key', re: /AKIA[0-9A-Z]{16}/ },
  { type: 'private-key', re: /-----BEGIN\s+(?:RSA\s+)?PRIVATE\s+KEY-----/ },
  { type: 'pii-email', re: /['"][\w.+-]+@[\w-]+\.\w{2,}['"]/ },
  { type: 'pii-phone', re: /['"]1[3-9]\d{9}['"]/ },
];
function detectSensitiveData(code: string) {
  const findings: { type: string; line: number; severity: 'error' }[] = [];
  code.split('\n').forEach((line, i) => {
    if (line.trim().startsWith('//')) return;            // 注释跳过
    for (const p of SENSITIVE_PATTERNS) {
      if (p.re.test(line))
        findings.push({ type: p.type, line: i + 1, severity: 'error' });
    }
  });
  return { findings, ok: findings.length === 0 };
}
```
