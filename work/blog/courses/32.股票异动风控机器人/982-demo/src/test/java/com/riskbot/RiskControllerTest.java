package com.riskbot;

import com.riskbot.agent.RiskQueryAgent;
import com.riskbot.common.BizException;
import com.riskbot.domain.RiskAlert;
import com.riskbot.service.RiskEvaluationService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.when;

/**
 * 控制器入参校验单元测试（不依赖 Spring 上下文）：验证非法 symbol / 空 q
 * 必须抛 BizException，合法输入正确委托下层。
 */
@ExtendWith(MockitoExtension.class)
class RiskControllerTest {

    @Mock
    private RiskEvaluationService evaluationService;

    @Mock
    private RiskQueryAgent agent;

    private com.riskbot.controller.RiskController controller;

    @BeforeEach
    void setUp() {
        controller = new com.riskbot.controller.RiskController(evaluationService, agent);
    }

    @Test
    void evaluate_rejectsBlankSymbol() {
        assertThrows(BizException.class, () -> controller.evaluate("  "));
    }

    @Test
    void evaluate_rejectsMalformedSymbol() {
        assertThrows(BizException.class, () -> controller.evaluate("AAPL@!"));
    }

    @Test
    void evaluate_delegatesValidSymbol() {
        RiskAlert alert = new RiskAlert("600519", "A股", "HIGH", List.of("涨跌幅异动"), null, null);
        when(evaluationService.evaluate("600519")).thenReturn(List.of(alert));
        List<RiskAlert> result = controller.evaluate("600519");
        assertEquals(1, result.size());
        assertEquals("600519", result.get(0).symbol());
    }

    @Test
    void query_rejectsBlank() {
        assertThrows(BizException.class, () -> controller.query(""));
    }

    @Test
    void query_rejectsOversized() {
        assertThrows(BizException.class, () -> controller.query("x".repeat(2001)));
    }

    @Test
    void query_delegatesValidQ() {
        when(agent.ask(anyString())).thenReturn("离线应答");
        assertEquals("离线应答", controller.query("茅台今天有异动吗"));
    }
}
