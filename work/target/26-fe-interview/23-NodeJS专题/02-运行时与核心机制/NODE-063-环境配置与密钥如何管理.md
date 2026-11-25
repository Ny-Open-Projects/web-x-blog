---
title: [NODE-063] 环境配置与密钥如何管理？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-063：环境配置与密钥如何管理？
**答**：
- 层级：**默认值 < 环境变量 < 运行时覆盖**。配置对象按环境（dev/test/prod）分层合并，启动时**校验完整性**（zod/joi），配置错误 fail-fast 而不是运行中 NPE。
- 密钥红线：`.env` 不进 git（`.gitignore`）；生产密钥走 K8s Secret/Vault/云 KMS，不落代码仓；日志与错误上报 redact 敏感字段。
- 高频坑：`process.env` 全是字符串；config 模块被多处 require 时缓存不一致（应单例导出冻结对象）；动态配置（限流阈值等）走配置中心热更新，避免重启。

```javascript
// config/index.js：分层合并 + zod 校验 + 单例冻结
const { z } = require('zod');

const schema = z.object({
  NODE_ENV: z.enum(['development', 'test', 'production']).default('development'),
  PORT: z.coerce.number().default(3000),                 // '3000' → 3000
  DB_HOST: z.string(),
  DB_PASSWORD: z.string().min(1),
  REDIS_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),                        // 密钥强度约束
  RATE_LIMIT_QPS: z.coerce.number().default(100),
  LOG_LEVEL: z.enum(['debug', 'info', 'warn', 'error']).default('info'),
});

const parsed = schema.safeParse(process.env);
if (!parsed.success) {
  // fail-fast：启动期报出全部缺失配置，而不是运行时逐个炸
  console.error('配置校验失败:', JSON.stringify(parsed.error.flatten().fieldErrors));
  process.exit(1);
}

const config = Object.freeze({ ...parsed.data, isProd: parsed.data.NODE_ENV === 'production' });
module.exports = config;
```

```yaml
# .gitignore（红线）
# .env
# .env.local
# .env.*.key

# k8s：密钥走 Secret，不进镜像不进环境文件
apiVersion: v1
kind: Secret
metadata:
  name: bff-secrets
type: Opaque
stringData:
  DB_PASSWORD: "prod-password-from-vault"
  JWT_SECRET: "at-least-32-chars-random-secret-value"
---
# deployment 引用
containers:
  - name: bff
    envFrom:
      - secretRef: { name: bff-secrets }
      - configMapRef: { name: bff-config }
```
