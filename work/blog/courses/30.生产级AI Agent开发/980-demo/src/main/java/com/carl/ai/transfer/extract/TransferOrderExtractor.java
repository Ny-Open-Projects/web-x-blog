package com.carl.ai.transfer.extract;

import com.carl.ai.transfer.common.LlmTokenBudget;
import com.carl.ai.transfer.domain.param.TransferOrderParam;
import io.github.resilience4j.circuitbreaker.CircuitBreaker;
import io.github.resilience4j.retry.Retry;
import java.util.function.Supplier;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.client.ResponseEntity;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.stereotype.Component;

/**
 * 结构化抽取（复刻 5-16「状态机 JSON 数据解析与入库节点」的前半段）。
 * <p>
 * 课程里 LLM 先生成调拨建议文本，再「提取 JSON 串」。本工程用 Spring AI 2.0.1 的
 * {@code ChatClient.prompt().user(...).call().responseEntity(TransferOrderParam.class)} —— 底层即
 * {@code BeanOutputConverter}：把模型输出（或 OfflineChatModel 的固定 JSON）直接绑定到 POJO。
 * 字段名与 {@link TransferOrderParam} 一致即可，无需手写 Jackson 解析。
 *
 * <p>生产加固（按加固优先级从外到内）：
 * <ol>
 *   <li>Token 预算：调用前检查，耗尽直接 400 明确拒绝，不把账单打爆；</li>
 *   <li>重试（指数退避限次）：兜住瞬时网络抖动 / 限流 429；</li>
 *   <li>熔断：模型持续故障时快速失败，降级返回空 param 由上层决定业务异常；</li>
 *   <li>用量记账：responseEntity 单次访问器同时拿 entity 与 usage（Spring AI 2.0.1
 *       的 advisor 链一次性，chatResponse() 之后再调 entity() 会抛
 *       "No CallAdvisors available to execute"）。</li>
 * </ol>
 */
@Component
public class TransferOrderExtractor {

    private static final Logger log = LoggerFactory.getLogger(TransferOrderExtractor.class);

    private final ChatClient chatClient;
    private final CircuitBreaker circuitBreaker = CircuitBreaker.ofDefaults("transferLlm");
    private final Retry retry;
    private final LlmTokenBudget tokenBudget;

    public TransferOrderExtractor(ChatClient.Builder builder,
                                  Retry transferLlmRetry,
                                  LlmTokenBudget tokenBudget) {
        this.chatClient = builder.build();
        this.retry = transferLlmRetry;
        this.tokenBudget = tokenBudget;
    }

    /**
     * LLM 抽取用 resilience4j 包裹（手动 core API，跨 Boot 版本安全，规避 spring-boot3 starter 在 Boot 4 下的兼容问题）。
     * 包裹顺序：重试在外、熔断在内（resilience4j 推荐顺序）——每次重试仍过熔断，
     * 熔断打开后后续重试快速失败，不再真的打模型。
     * 模型/网络异常时降级返回空 param，由上层决定是否抛业务异常。
     */
    public TransferOrderParam extract(String naturalLanguage) {
        // 预算检查在重试/熔断之外：配额耗尽重试没有意义，直接以 400 明确拒绝
        tokenBudget.checkBudget();
        Supplier<TransferOrderParam> guarded = Retry.decorateSupplier(retry,
                CircuitBreaker.decorateSupplier(circuitBreaker, () -> doExtract(naturalLanguage)));
        try {
            return guarded.get();
        } catch (Exception e) {
            // 关键：异常必须可见，不能静默吞掉（否则上游只能靠空字段猜失败）。
            // 传异常对象而非 getMessage()：排查时需要看是熔断 Open 还是绑定失败
            log.warn("LLM 抽取失败，降级返回空 param", e);
            return extractFallback();
        }
    }

    private TransferOrderParam doExtract(String naturalLanguage) {
        // 单次访问器 responseEntity：同时拿到绑定结果与 usage 元数据
        ResponseEntity<ChatResponse, TransferOrderParam> response = chatClient.prompt()
                .user(u -> u.text("""
                        你是库存调拨助手。请把用户的自然语言需求转成调拨单 JSON，字段：
                        sourceWarehouseId, targetWarehouseId, status, transferType,
                        transferDate(格式 yyyy-MM-dd), comment, createdBy,
                        items: [{sku, qty}]。
                        只输出 JSON。
                        需求：%s
                        """.formatted(naturalLanguage)))
                .call()
                .responseEntity(TransferOrderParam.class);
        tokenBudget.record(response.getResponse().getMetadata().getUsage());
        return response.getEntity();
    }

    /** 熔断/超时降级：返回空 param，由上层决定是否抛业务异常。 */
    private TransferOrderParam extractFallback() {
        return new TransferOrderParam();
    }
}
