package com.riskbot.controller;

import com.riskbot.agent.RiskQueryAgent;
import com.riskbot.common.BizException;
import com.riskbot.domain.RiskAlert;
import com.riskbot.service.RiskEvaluationService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.regex.Pattern;

@RestController
@RequestMapping("/api/risk")
public class RiskController {

    /** A股 6 位数字代码（600519/000001/300001）或美股代码（AAPL/BRK.B 带点后缀）。 */
    private static final Pattern SYMBOL_PATTERN =
            Pattern.compile("^(\\d{6}|[A-Za-z]{1,5}(\\.[A-Za-z]{1,2})?)$");

    private static final int MAX_QUESTION_LENGTH = 2000;

    private final RiskEvaluationService evaluationService;
    private final RiskQueryAgent agent;

    public RiskController(RiskEvaluationService evaluationService, RiskQueryAgent agent) {
        this.evaluationService = evaluationService;
        this.agent = agent;
    }

    /**
     * 主动评估某代码。
     * required=false：缺参放行为 null，由下方校验统一收敛 400。
     */
    @PostMapping("/evaluate")
    public List<RiskAlert> evaluate(@RequestParam(required = false) String symbol) {
        if (symbol == null || symbol.isBlank() || !SYMBOL_PATTERN.matcher(symbol.trim()).matches()) {
            throw new BizException("symbol 需为 A股 6 位数字（如 600519）或美股代码（如 AAPL、BRK.B）");
        }
        return evaluationService.evaluate(symbol.trim().toUpperCase());
    }

    /** 扫描全市场当前告警。 */
    @GetMapping("/scan")
    public List<RiskAlert> scan() {
        return evaluationService.scanAll();
    }

    /**
     * Agent 自然语言问答（prod 下可触发工具调用）。
     * required=false：缺参放行为 null，由下方校验统一收敛 400。
     */
    @GetMapping("/query")
    public String query(@RequestParam(required = false) String q) {
        if (q == null || q.isBlank() || q.length() > MAX_QUESTION_LENGTH) {
            throw new BizException("q 不能为空且长度不超过 " + MAX_QUESTION_LENGTH);
        }
        return agent.ask(q);
    }
}
