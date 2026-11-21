package com.travel.agent.tool;

import io.agentscope.core.tool.Tool;
import io.agentscope.core.tool.ToolParam;
import org.springframework.stereotype.Component;

/**
 * 景点推荐 SubAgent 的工具箱（对应课程 12-5：景点推荐 SubAgent 执行景点推荐任务）。
 *
 * <p>@ToolParam 的 required 只生成 JSON Schema，调用时不做强校验，
 * 真实模型漏参会以 null 进方法体，入口必须自行判空。</p>
 */
@Component
public class AttractionTools {

    @Tool(name = "search_attractions", description = "按城市与偏好搜索景点")
    public String search(
            @ToolParam(name = "city", description = "城市") String city,
            @ToolParam(name = "preference", description = "偏好，如 自然风光/历史人文") String preference) {
        if (city == null || city.isBlank()) {
            throw new IllegalArgumentException("city 不能为空");
        }
        if (preference == null || preference.isBlank()) {
            throw new IllegalArgumentException("preference 不能为空");
        }
        return String.format(
                "{\"city\":\"%s\",\"preference\":\"%s\",\"attractions\":[\"西湖\",\"灵隐寺\",\"西溪湿地\"],"
                        + "\"ticket_total_cny\":150}",
                city, preference);
    }
}
