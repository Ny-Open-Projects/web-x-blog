package com.riskbot.agent;

import com.riskbot.common.LlmTokenBudget;
import com.riskbot.common.TokenBudgetExceededException;
import com.riskbot.domain.RiskAlert;
import com.riskbot.service.RiskEvaluationService;
import io.github.resilience4j.retry.Retry;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.tool.annotation.Tool;
import org.springframework.ai.tool.annotation.ToolParam;
import org.springframework.stereotype.Component;
import org.springframework.util.StringUtils;

import java.util.List;
import java.util.function.Supplier;
import java.util.regex.Pattern;

/**
 * 风控问答 Agent（执行层.ai）：基于 Spring AI 2.0.1 ChatClient，把
 * RiskEvaluationService 挂成 @Tool，让大模型能「查某票风险」。
 * 工具循环由 2.0 的 ToolCallingAdvisor 在 Advisor 链统一驱动（见 v3 §3.2）。
 *
 * <p>生产加固（问答入口三重防线）：
 * <ol>
 *   <li>Token 预算：调用前检查、调用后记账，超限返回明确文案而不是把账单打爆；</li>
 *   <li>重试：指数退避限次，兜住瞬时网络抖动 / Provider 限流；</li>
 *   <li>降级：重试耗尽或其它异常仍返回固定文案，/api/risk/query 恒不 500。</li>
 * </ol>
 */
@Component
public class RiskQueryAgent {

    private static final Logger log = LoggerFactory.getLogger(RiskQueryAgent.class);

    /** 与 RiskController 同一套符号语义：A股 6 位数字或美股代码。 */
    private static final Pattern SYMBOL_PATTERN =
            Pattern.compile("^(\\d{6}|[A-Za-z]{1,5}(\\.[A-Za-z]{1,2})?)$");

    /** LLM 通道故障时的降级文案：不给 500，也不给空体，引导调用方走结构化端点。 */
    public static final String FALLBACK_ANSWER =
            "模型暂不可用，请稍后重试；也可直接调用 /api/risk/evaluate 或 /api/risk/scan 获取结构化风控结果";

    /** Token 预算耗尽时的文案：与通道故障区分，让调用方知道是配额问题。 */
    public static final String BUDGET_FALLBACK_ANSWER =
            "今日模型调用额度已用完（token 预算耗尽），请稍后重试或调高风险预算配置";

    private final ChatClient chatClient;
    private final RiskEvaluationService evaluationService;
    private final LlmTokenBudget tokenBudget;
    private final Retry retry;

    public RiskQueryAgent(ChatClient.Builder builder,
                          RiskEvaluationService evaluationService,
                          LlmTokenBudget tokenBudget,
                          Retry riskLlmRetry) {
        this.evaluationService = evaluationService;
        this.tokenBudget = tokenBudget;
        this.retry = riskLlmRetry;
        // defaultTools(this)：把本类的 @Tool 方法注册给 ChatClient
        this.chatClient = builder.defaultTools(this).build();
    }

    @Tool(description = "查询指定股票代码当前的风险评估结果（异动告警列表），支持 A股/美股")
    public List<RiskAlert> queryRisk(@ToolParam(description = "股票代码，如 600519 或 AAPL") String symbol) {
        // LLM 生成的工具参数同样不可信：与 Controller 同标准校验，非法直接抛，
        // Spring AI 会把异常回灌模型让其自我修正，而不是把脏代码带进查询
        if (symbol == null || !SYMBOL_PATTERN.matcher(symbol.trim()).matches()) {
            throw new IllegalArgumentException("symbol 需为 A股 6 位数字（如 600519）或美股代码（如 AAPL）");
        }
        return evaluationService.evaluate(symbol.trim().toUpperCase());
    }

    /** 自然语言问答入口（prod profile 下大模型可触发 queryRisk 工具）。 */
    public String ask(String question) {
        try {
            // 预算检查放在 try 内：预算耗尽也要走降级文案而不是把异常抛给调用方
            tokenBudget.checkBudget();
            // 注意：chatClient.call() 是懒执行（只造 spec），真正的模型调用发生在
            // chatResponse() 访问器里。重试必须包住访问器，否则瞬时故障全部漏出重试圈
            Supplier<ChatResponse> guarded = Retry.decorateSupplier(retry,
                    () -> chatClient.prompt().user(question).call().chatResponse());
            // 关键（Spring AI 2.0.1 实测坑）：CallResponseSpec 的 advisor 链一次性，
            // chatResponse() 之后再调 content() 会抛 "No CallAdvisors available to execute"。
            // 因此只触发 chatResponse() 一个访问器，正文与 usage 都从 ChatResponse 里取
            ChatResponse chatResponse = guarded.get();
            tokenBudget.record(chatResponse.getMetadata().getUsage());
            String content = chatResponse.getResult() != null && chatResponse.getResult().getOutput() != null
                    ? chatResponse.getResult().getOutput().getText()
                    : null;
            // 模型仅返回工具调用无正文时 content 为 null：给固定文案，别对外吐 200 空体
            return StringUtils.hasText(content) ? content : "（模型未返回文本内容）";
        } catch (TokenBudgetExceededException e) {
            // 并发问答下可能调用后才超限：同样按预算耗尽处理
            log.warn("[问答降级] token 预算耗尽: {}", e.getMessage());
            return BUDGET_FALLBACK_ANSWER;
        } catch (Exception e) {
            // LLM 调用异常（网络抖动 / 限流 429 / 超时 / Provider 5xx）不向上抛：
            // /api/risk/query 恒返回 200 文案，prod 通道故障不打成 500
            log.warn("[问答降级] LLM 调用失败，question={}", truncate(question), e);
            return FALLBACK_ANSWER;
        }
    }

    /** 日志防膨胀：用户原文只留前 100 字符。 */
    private static String truncate(String s) {
        if (s == null) {
            return null;
        }
        return s.length() <= 100 ? s : s.substring(0, 100) + "...";
    }
}
