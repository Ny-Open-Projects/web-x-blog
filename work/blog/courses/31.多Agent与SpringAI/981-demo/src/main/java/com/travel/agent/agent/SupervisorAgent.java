package com.travel.agent.agent;

import com.travel.agent.common.LlmTokenBudget;
import com.travel.agent.config.AgentProperties;
import com.travel.agent.model.OfflineChatModel;
import com.travel.agent.model.TokenBudgetModel;
import io.agentscope.core.ReActAgent;
import io.agentscope.core.message.Msg;
import io.agentscope.core.model.ChatResponse;
import io.agentscope.core.tool.Toolkit;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * 主管 Agent（课程 11-1 旅游规划整体架构、13-2 暴露给用户的交互入口）：
 * 不亲自干活，负责发现团队成员、拆解任务、分发、汇总。
 *
 * <p>离线模式的决策规则（与 ReAct 循环同构）：
 * 第一轮按任务关键词选择要调用的成员工具；拿到成员返回后第二轮汇总。
 * 真实模式下由大模型自主决策（{@code app.agent.model-name}）。
 *
 * <p>maxIters 显式声明（默认 10）：自主循环的预算/停止条件必须在代码里可见，
 * 生产按 token 成本经 {@code app.agent.max-iters} 收紧。</p>
 */
@Configuration
public class SupervisorAgent {

    private static final Logger log = LoggerFactory.getLogger(SupervisorAgent.class);

    public static final String TRAVEL_MANAGER_AGENT = "TravelManagerAgent";

    @Bean
    public ReActAgent travelManagerAgent(SupervisorTools supervisorTools, AgentProperties props, LlmTokenBudget budget) {
        Toolkit toolkit = new Toolkit();
        toolkit.registerTool(supervisorTools);

        ReActAgent.Builder builder = ReActAgent.builder()
                .name(TRAVEL_MANAGER_AGENT)
                .description("主管Agent：统筹团队成员完成旅行规划")
                .maxIters(props.getMaxIters())
                .sysPrompt(""
                        + "你是旅行规划主管。根据用户需求把子任务分发给合适的团队成员："
                        + "涉及路线、交通、通勤交给 ask_route_making_agent；"
                        + "涉及景点、游玩交给 ask_attraction_agent。"
                        + "如需两类信息，先调用其中一个，再调用另一个，最后汇总成完整行程。")
                .toolkit(toolkit);

        // 不论离线还是真实模型，都用 TokenBudgetModel 装饰，把每次 LLM 调用的 usage 累计进预算
        if (props.isOffline()) {
            builder.model(new TokenBudgetModel(
                    new OfflineChatModel("offline-supervisor", supervisorDecider()), budget));
        } else {
            builder.model(new TokenBudgetModel(
                    io.agentscope.core.model.ModelRegistry.resolve(props.getModelName()), budget));
        }
        return builder.build();
    }

    /**
     * 主管决策：按用户需求里的关键词路由到对应成员工具；结果回来后汇总。
     */
    public static Function<List<Msg>, List<ChatResponse>> supervisorDecider() {
        return OfflineChatModel.singleToolThenAnswer(
                SupervisorAgent::pickTool,
                messages -> Map.of("task", promptOf(messages)),
                messages -> "行程规划已完成（离线演示）："
                        + "路线由路线制定专员产出、景点由景点推荐 SubAgent 产出，"
                        + "主管已汇总； prod 模式下该汇总由真实大模型生成。");
    }

    private static String pickTool(List<Msg> messages) {
        String prompt = promptOf(messages);
        boolean route = prompt.contains("路线") || prompt.contains("交通") || prompt.contains("通勤");
        boolean attraction = prompt.contains("景点") || prompt.contains("游玩") || prompt.contains("推荐");
        if (route && !attraction) {
            return "ask_route_making_agent";
        }
        if (attraction && !route) {
            return "ask_attraction_agent";
        }
        return "ask_route_making_agent";
    }

    private static String promptOf(List<Msg> messages) {
        try {
            if (!messages.isEmpty()) {
                return messages.get(0).getTextContent();
            }
        } catch (Exception e) {
            // 离线兜底：记 trace 级日志，排查时能区分「数据没到」和「代码路径错」
            log.trace("离线兜底：取首条消息失败", e);
        }
        return "";
    }
}
