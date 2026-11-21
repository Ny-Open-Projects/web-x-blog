package com.travel.agent.agent;

import com.travel.agent.a2a.AgentCard;
import com.travel.agent.common.LlmTokenBudget;
import com.travel.agent.config.AgentProperties;
import com.travel.agent.model.OfflineChatModel;
import com.travel.agent.model.TokenBudgetModel;
import com.travel.agent.tool.AttractionTools;
import com.travel.agent.tool.RouteMakingTools;
import io.agentscope.core.ReActAgent;
import io.agentscope.core.message.Msg;
import io.agentscope.core.tool.Toolkit;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * 团队成员（课程 10-1 SubAgent、11-1 旅游规划架构、12-5 景点推荐 SubAgent）：
 * 每个成员是一个挂载了 Toolkit 的 ReActAgent。
 *
 * <p>离线模式下每个成员配备一枚规则模型（{@link OfflineChatModel}）：
 * 第一轮调用自己的 MCP 风格工具、第二轮汇总，行为与真实 ReAct 循环同构；
 * 真实模式下改用 {@code AgentProperties.modelName} 解析出的模型（如 dashscope:qwen-plus）。
 *
 * <p>maxIters 显式声明：与 {@link SupervisorAgent} 同一预算口径，见 app.agent.max-iters。</p>
 */
@Configuration
public class TeamMembers {

    private static final Logger log = LoggerFactory.getLogger(TeamMembers.class);

    public static final String ROUTE_MAKING_AGENT = "RouteMakingAgent";
    public static final String ATTRACTION_AGENT = "AttractionAgent";

    /** 路线制定专员（课程 11-6）：挂载百度地图 MCP 风格工具。 */
    @Bean
    public ReActAgent routeMakingAgent(RouteMakingTools routeTools, AgentProperties props, LlmTokenBudget budget) {
        Toolkit toolkit = new Toolkit();
        toolkit.registerTool(routeTools);
        ReActAgent.Builder builder = ReActAgent.builder()
                .name(ROUTE_MAKING_AGENT)
                .description("路线制定Agent：调用百度地图 MCP 规划路线与通勤方案")
                .maxIters(props.getMaxIters())
                .sysPrompt("你是路线制定专员，调用地图工具完成路线规划。")
                .toolkit(toolkit);
        applyModel(builder, props, budget, "offline-route-making", offlineRouteDecider());
        return builder.build();
    }

    /** 景点推荐 SubAgent（课程 12-5）：挂载景点检索工具。 */
    @Bean
    public ReActAgent attractionAgent(AttractionTools attractionTools, AgentProperties props, LlmTokenBudget budget) {
        Toolkit toolkit = new Toolkit();
        toolkit.registerTool(attractionTools);
        ReActAgent.Builder builder = ReActAgent.builder()
                .name(ATTRACTION_AGENT)
                .description("景点推荐Agent：按城市与偏好推荐景点")
                .maxIters(props.getMaxIters())
                .sysPrompt("你是景点推荐专员，调用工具检索景点并给出推荐。")
                .toolkit(toolkit);
        applyModel(builder, props, budget, "offline-attraction", offlineAttractionDecider());
        return builder.build();
    }

    /** 成员名片（A2A Agent Card，课程 11-2 注册用）。 */
    public static AgentCard routeCard(String baseUrl) {
        return new AgentCard(ROUTE_MAKING_AGENT, "路线制定Agent：调用百度地图 MCP 规划路线", baseUrl);
    }

    public static AgentCard attractionCard(String baseUrl) {
        return new AgentCard(ATTRACTION_AGENT, "景点推荐Agent：按城市与偏好推荐景点", baseUrl);
    }

    // ---------- 离线规则模型 ----------

    /**
     * 离线模式注入规则模型；真实模式把字符串 id 交给 ModelRegistry 解析
     * （agentscope-extensions-model-dashscope 等扩展通过 SPI 提供）。
     *
     * <p>两种模式都套 {@link TokenBudgetModel} 装饰：它是 ReAct 循环内部的「模型」，
     * 能看到每次 LLM 响应的 usage 并累计进预算，绕开 AgentScope 内部循环不向应用层
     * 暴露 usage 的限制。</p>
     */
    private static void applyModel(
            ReActAgent.Builder builder,
            AgentProperties props,
            LlmTokenBudget budget,
            String offlineName,
            Function<List<Msg>, List<io.agentscope.core.model.ChatResponse>> decider) {
        if (props.isOffline()) {
            builder.model(new TokenBudgetModel(new OfflineChatModel(offlineName, decider), budget));
        } else {
            builder.model(new TokenBudgetModel(
                    io.agentscope.core.model.ModelRegistry.resolve(props.getModelName()), budget));
        }
    }

    /**
     * 路线成员决策：先调 map_directions，再汇总。
     */
    public static Function<List<Msg>, List<io.agentscope.core.model.ChatResponse>> offlineRouteDecider() {
        return OfflineChatModel.singleToolThenAnswer(
                messages -> "map_directions",
                messages -> Map.of("origin", "杭州东站", "destination", "西湖风景区"),
                messages -> "路线方案已生成：杭州东站 → 西湖风景区，地铁+步行约 "
                        + minutesOf(messages)
                        + " 分钟（离线演示数据；prod 模式由真实地图 MCP 返回）。");
    }

    /**
     * 景点成员决策：先调 search_attractions，再汇总。
     */
    public static Function<List<Msg>, List<io.agentscope.core.model.ChatResponse>> offlineAttractionDecider() {
        return OfflineChatModel.singleToolThenAnswer(
                messages -> "search_attractions",
                messages -> Map.of("city", "杭州", "preference", "自然风光"),
                messages -> "景点推荐完成：西湖、灵隐寺、西溪湿地（自然风光向，联票约 150 元；离线演示数据）。");
    }

    private static long minutesOf(List<Msg> messages) {
        try {
            String last = messages.get(messages.size() - 1).getTextContent();
            int idx = last == null ? -1 : last.indexOf("duration_min");
            if (idx >= 0) {
                String digits = last.substring(idx).replaceAll("[^0-9]", " ").trim().split(" ")[0];
                return Long.parseLong(digits);
            }
        } catch (Exception e) {
            // 离线汇总兜底：记 trace 级日志，与 SupervisorAgent.promptOf 同口径
            log.trace("离线汇总兜底：解析时长失败", e);
        }
        return 28L;
    }
}
