---
title: "题 2：工具错误反馈与自修复"
date: 2026-11-18
categories: [Java面试, Agent笔试]
tags: [Java面试, 手写题, 33]
type: 手写题
disableNunjucks: true
---

## 题 2：工具错误反馈与自修复

### 题目（20 分钟）

在题 1 的 AgentExecutor 基础上实现工具执行容错层 `SafeToolExecutor`，处理三类失败：
① 幻觉工具（模型调用了未注册的工具名）
② 参数缺失（schema required 字段缺失）
③ 执行异常（工具运行时抛异常）
三类失败都要包装为**模型可读的错误反馈消息**回喂（模型可修正重试），**连续 3 次工具失败则终止**（防循环）。失败要计入轨迹。

### 评分细则

| 维度 | 得分点 | 分值 |
|------|--------|------|
| 功能正确 40% | 三类失败分别捕获并反馈 ✓｜错误消息含"原因+修正建议"（模型可读）✓｜连续失败计数与终止 ✓ | 40 |
| 边界处理 20% | 连续失败终止时输出已收集信息 ✓｜成功后失败计数清零 ✓ | 20 |
| 工程质量 20% | SafeToolExecutor 独立类（装饰器模式）✓｜错误消息模板化 ✓ | 20 |
| 并发与安全 20% | 工具异常不泄漏堆栈给模型（脱敏）✓｜失败计数线程安全意识 ✓ | 20 |

### 参考实现

```java
public class SafeToolExecutor {
    private final ToolRegistry delegate;
    private final TrajectoryRecorder recorder;
    private int consecutiveFailures = 0;
    private static final int MAX_CONSECUTIVE = 3;

    /** @return 工具消息内容；抛 TooManyFailuresException 时由循环终止收尾 */
    public String execute(ToolCall call) throws TooManyFailuresException {
        String feedback;
        try {
            ToolSpec spec = delegate.spec(call.name()); // 未注册抛 UnknownToolException
            if (spec == null) {
                feedback = "错误：工具 " + call.name() + " 不存在。可用工具："
                         + delegate.specs().stream().map(ToolSpec::name).toList()
                         + "。请改用上述工具之一或直接回答。";
            } else {
                String missing = spec.validateRequired(call.args()); // schema 必填校验
                if (missing != null) {
                    feedback = "错误：缺少必填参数 " + missing + "（描述：" + spec.paramDesc(missing) + "）。请补全后重试。";
                } else {
                    ToolResult r = delegate.execute(call.name(), call.args());
                    consecutiveFailures = 0; // 成功清零
                    recorder.record(call, r, "OK");
                    return r.content();
                }
            }
        } catch (UnknownToolException e) {
            feedback = "错误：工具 " + call.name() + " 不存在。";
        } catch (Exception e) {
            // 脱敏：不给模型堆栈（可能含敏感路径），给可读原因
            feedback = "错误：工具执行失败（" + safeReason(e) + "）。请检查参数后重试或换方案。";
        }
        recorder.record(call, null, feedback);
        if (++consecutiveFailures >= MAX_CONSECUTIVE) {
            throw new TooManyFailuresException("连续 " + MAX_CONSECUTIVE + " 次工具失败");
        }
        return feedback; // 错误反馈回喂，模型可自修复（AD-016）
    }
}
```

### 追问清单

1. 为什么错误消息要"模型可读"而非直接给堆栈？→ 模型读得懂才能自修复（AD-016），堆栈含敏感路径（脱敏 AD-054）
2. 连续失败为什么是 3 次而不是 1 次或无限？→ 1 次太脆弱（偶发失败），无限=成本失控（AD-017），3 是权衡
3. 成功后为什么清零计数？→ 计数语义是"连续失败"（间歇性失败不应终止）
4. 工具失败的错误会进上下文占用 token，如何治理？→ 错误消息精简+历史裁剪（AD-023）
5. 如果工具是支付类（不可重试）怎么办？→ 幂等键+人工确认（AD-218/080），禁自动重试（JA-056）

### 常见错误

堆栈直接回喂模型（敏感泄露+模型读不懂）｜失败终止不返回已收集信息｜计数不清零（间歇失败误杀）｜三类失败混在一个 catch。
