package com.travel.agent.model;

import io.agentscope.core.message.Msg;
import io.agentscope.core.message.TextBlock;
import io.agentscope.core.message.ToolUseBlock;
import io.agentscope.core.model.ChatResponse;
import io.agentscope.core.model.ChatUsage;
import io.agentscope.core.model.GenerateOptions;
import io.agentscope.core.model.Model;
import io.agentscope.core.model.ToolSchema;
import io.agentscope.core.util.JsonUtils;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import reactor.core.publisher.Flux;

/**
 * 离线规则模型：不调用任何外部 LLM，按规则模拟 ReAct 循环的「决策」。
 *
 * <p>决策函数 {@code decider} 每次收到消息列表时返回一组 {@link ChatResponse}：
 * <ul>
 *   <li>第一轮（消息列表只有用户输入）→ 返回 {@link ToolUseBlock}，触发工具调用；</li>
 *   <li>后续轮（工具结果已回到消息列表，长度 ≥ 3）→ 返回 {@link TextBlock} 总结，收敛 ReAct 循环。</li>
 * </ul>
 * 这样整个「主管 Agent → 远程成员 Agent → MCP 风格工具」的链路在 default profile
 * 不联网、不填 API Key 也能完整跑通；prod profile 换成真实模型（见 {@code AgentConfig}）。
 */
public class OfflineChatModel implements Model {

    private final String name;
    private final Function<List<Msg>, List<ChatResponse>> decider;

    public OfflineChatModel(String name, Function<List<Msg>, List<ChatResponse>> decider) {
        this.name = name;
        this.decider = decider;
    }

    @Override
    public Flux<ChatResponse> stream(List<Msg> messages, List<ToolSchema> tools, GenerateOptions options) {
        List<ChatResponse> responses = decider.apply(messages);
        return Flux.fromIterable(responses.isEmpty() ? List.of(text("（离线模型无可用决策）")) : responses);
    }

    @Override
    public String getModelName() {
        return name;
    }

    @Override
    public boolean supportsNativeStructuredOutput() {
        return false;
    }

    @Override
    public int getContextWindowSize() {
        return 32768;
    }

    // ---------- 快速构造：官方 MockModel 同款响应构造 ----------

    public static ChatResponse text(String content) {
        return ChatResponse.builder()
                .id("msg_" + content.hashCode())
                .content(List.of(TextBlock.builder().text(content).build()))
                .usage(new ChatUsage(10, 20, 30))
                .build();
    }

    public static ChatResponse toolCall(String toolName, String toolCallId, Map<String, Object> arguments) {
        Map<String, Object> args = arguments == null ? new LinkedHashMap<>() : new LinkedHashMap<>(arguments);
        String json = JsonUtils.getJsonCodec().toJson(args);
        return ChatResponse.builder()
                .id("msg_" + toolName.hashCode())
                .content(List.of(ToolUseBlock.builder()
                        .name(toolName)
                        .id(toolCallId == null ? "call_" + toolName : toolCallId)
                        .input(args)
                        .content(json)
                        .build()))
                .usage(new ChatUsage(8, 15, 23))
                .build();
    }

    /** 便捷：多轮响应（先工具调用、后总结），与 ReActAgent 循环节奏对应。 */
    public static Function<List<Msg>, List<ChatResponse>> singleToolThenAnswer(
            Function<List<Msg>, String> toolPicker,
            Function<List<Msg>, Map<String, Object>> argsBuilder,
            Function<List<Msg>, String> answerBuilder) {
        return messages -> {
            // 第一轮：用户提问，尚未发生工具调用
            if (!hasToolRound(messages)) {
                String toolName = toolPicker.apply(messages);
                return new ArrayList<>(List.of(toolCall(toolName, "call_1", argsBuilder.apply(messages))));
            }
            // 第二轮：工具结果已在消息列表中，收敛为最终回答
            return new ArrayList<>(List.of(text(answerBuilder.apply(messages))));
        };
    }

    private static boolean hasToolRound(List<Msg> messages) {
        // 不依赖内部 Block 类型，用消息长度判定：首轮=[user]，工具结果回来后=[user, assistant, tool]
        return messages.size() >= 3;
    }
}
