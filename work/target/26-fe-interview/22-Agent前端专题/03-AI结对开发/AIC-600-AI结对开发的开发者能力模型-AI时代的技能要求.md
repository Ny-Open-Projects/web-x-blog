---
title: [AIC-600] AI 时代的开发者技能要求
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-600：AI 时代的开发者技能要求

**答**:
- AI 时代开发者的技能转变：1) **从"写代码"到"审代码"**（RBL-501 Driver→Navigator——核心技能从编码速度变为审查精度；2) **从"记住 API"到"描述意图"**（RBL-506 Prompt 工程——精确描述需求比记住 API 签名更重要；3) **从"实现逻辑"到"设计架构"**（AI 处理实现细节，人处理架构决策（RBL-522 规范设计）；4) **从"调试代码"到"调试 AI"**（RBL-509 迭代收敛——诊断 AI 为什么生成错误的代码（prompt 问题/上下文不足/模型限制）。
- AI 时代的新增技能：1) **Prompt 工程**（精确描述意图 RBL-506；2) **AI 代码审查**（RBL-532 检查点体系；3) **上下文管理**（RBL-502 裁剪策略；4) **AI 安全**（RBL-546 注入检测 RBL-584 防御体系；5) **AI 成本管理**（RBL-524 Token 预算；6) **Agent 编排**（RBL-518 任务分解 RBL-520 工具注册表）。
- 不变的技能：1) **领域知识**（业务规则的理解——AI 无法替代 RBL-938 归因）；2) **架构思维**（系统的整体设计——AI 只能局部优化）；3) **安全意识**（注入/越权/数据泄露——人的安全直觉超越模式匹配 RBL-546）；4) **沟通能力**（与团队协作——AI 不替代人的沟通）。
- 追问钩子：为什么「领域知识」和「安全意识」是 AI 时代不可替代的技能？——AI 可以生成代码但不知道"这个业务为什么这么设计"（领域知识在人脑中——AI 只有训练数据中的通用模式）；安全意识 = 人的直觉超越 AI 的模式匹配（AI 检测"已知的安全模式"——新型攻击 AI 不认识）；「不可替代性 = AI 无法从训练数据推断的知识」：业务上下文/团队历史/安全直觉/架构权衡——这些是"人的独有价值"（RBL-600 的能力模型核心）。

```typescript
// AI 时代开发者能力模型
const SKILL_MODEL = {
  evolved: {  // 演化的技能（原有技能的新形态）
    'write-code': 'review-code (RBL-501)',
    'remember-api': 'prompt-engineering (RBL-506)',
    'implement-logic': 'design-architecture (RBL-522)',
    'debug-code': 'debug-ai (RBL-509)',
  },
  new: {  // 全新技能
    'prompt-engineering': 'RBL-506',
    'ai-code-review': 'RBL-532',
    'context-management': 'RBL-502',
    'ai-security': 'RBL-546/584',
    'ai-cost-management': 'RBL-524',
    'agent-orchestration': 'RBL-518/520',
  },
  irreplaceable: [  // 不可替代的技能
    'domain-knowledge (业务规则理解)',
    'architecture-thinking (系统设计)',
    'security-intuition (安全直觉)',
    'communication (团队协作)',
  ],
};
```
