# 题 1：ReAct 执行循环

## 题目（20 分钟）

给定两个接口（不可修改）：

```java
interface ModelClient {
    /** 返回模型响应：content（最终答案）或 toolCalls（工具调用意图列表），二者互斥 */
    ModelResponse chat(List<Message> messages, List<ToolSpec> tools);
}
interface ToolRegistry {
    ToolResult execute(String toolName, Map<String, Object> args); // 未注册工具抛 UnknownToolException
    List<ToolSpec> specs(); // 工具描述列表（给模型）
}
```

实现 `AgentExecutor.run(String task)`：循环调用模型、解析响应、执行工具、结果回填，直到模型输出最终答案或步数达上限（默认 10）。要求：① 消息序列顺序正确（user/assistant/tool 成组）② 三类终止（完成/步数/模型声明无法完成）③ 返回最终输出。

## 评分细则（四维可勾选）

| 维度 | 得分点 | 分值 |
|------|--------|------|
| 功能正确 40% | 消息序列成组追加（assistant+tool 成对）✓｜终止三条件（完成/步数/放弃）✓｜最终答案提取 ✓ | 40 |
| 边界处理 20% | 步数上限优雅收尾（返回当前进度而非报错）✓｜模型声明无法完成时透传 ✓ | 20 |
| 工程质量 20% | 类结构（Executor 独立/消息构建封装）✓｜命名与轨迹点 ✓ | 20 |
| 并发与安全 20% | 单线程正确性（消息序列无竞态假设）✓｜task 内容进入 user 消息（非拼接 system）✓ | 20 |

## 参考实现

```java
public class AgentExecutor {
    private final ModelClient model;
    private final ToolRegistry tools;
    private final int maxSteps;

    public AgentExecutor(ModelClient model, ToolRegistry tools, int maxSteps) {
        this.model = model; this.tools = tools; this.maxSteps = maxSteps;
    }

    public String run(String task) {
        List<Message> messages = new ArrayList<>();
        messages.add(Message.system("你是任务执行 Agent，完成任务或声明无法完成。"));
        messages.add(Message.user(task));
        for (int step = 0; step < maxSteps; step++) {
            ModelResponse resp = model.chat(messages, tools.specs());
            messages.add(Message.assistant(resp));
            if (resp.hasToolCalls()) {
                for (ToolCall call : resp.toolCalls()) {
                    ToolResult result = tools.execute(call.name(), call.args()); // 未知工具在 registry 内抛错→见题 2
                    messages.add(Message.tool(call.id(), result.content()));
                }
            } else {
                return resp.content(); // 最终答案
            }
        }
        return "已达最大步数，当前进度：" + lastAssistantText(messages); // 优雅收尾
    }
}
```

## 追问清单

1. 模型谎报完成（实际任务没完成）怎么办？→ 验证器（AD-502）+ 完成声明需带证据（AD-676 证据链）
2. 模型调用了不存在的工具？→ 错误反馈回喂（题 2），不终止
3. 上下文超窗怎么办？→ 裁剪策略族（AD-023），本地估算（AD-067）
4. 为什么每轮要重发全量上下文？→ 模型无状态协议（AD-024 成本模型），累积成本陷阱（AD-025）
5. 步数上限触发后返回进度还是报错？→ 优雅收尾（AD-005），报错丢上下文

## 常见错误（AD-200 清单）

工具结果未追加到消息序列（循环空转）｜assistant 消息漏追加（协议断裂）｜终止条件漏"模型放弃"｜步数上限直接抛异常（应优雅收尾）。
