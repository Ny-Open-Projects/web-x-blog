package com.travel.agent.tool;

import com.travel.agent.config.BaiduMapProperties;
import io.agentscope.core.tool.Tool;
import io.agentscope.core.tool.ToolParam;
import java.util.Map;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

/**
 * 路线制定专员的工具箱（对应课程 11-5 / 11-6：百度地图 MCP 服务端暴露的工具列表）。
 *
 * <p>真实环境里这些工具由百度地图 MCP Server 提供（map_geocode / map_directions 等），
 * 通过 {@code Toolkit.registerMcpClient(...)} 挂载到智能体；离线演示用本地桩返回同构数据，
 * 保证「工具挂载 → 工具调用 → 结果回传」的链路形态与生产一致。
 *
 * <p>凭证管理：百度地图 AK 通过 {@link BaiduMapProperties} 从环境变量 {@code BAIDU_MAP_API_KEY}
 * 注入，<b>不硬编码</b>；未配置时仅打告警、继续走离线桩（优雅降级），不会因缺 Key 启动失败。
 * 真实接入时由该 Key 构造签名请求，离线桩仍是默认安全行为。</p>
 *
 * <p>注意：@ToolParam 的 required 只参与生成 JSON Schema，框架调用时不做强校验——
 * 真实模型漏传参数会以 null 进入方法体，入口必须自行判空（否则 NPE 被包装成
 * 工具错误回灌模型，白白烧一轮迭代）。</p>
 */
@Component
public class RouteMakingTools {

    private static final Logger log = LoggerFactory.getLogger(RouteMakingTools.class);

    private final BaiduMapProperties baiduMapProperties;

    public RouteMakingTools(BaiduMapProperties baiduMapProperties) {
        this.baiduMapProperties = baiduMapProperties;
        if (baiduMapProperties.isKeyConfigured()) {
            log.info("[百度地图] 已检测到 BAIDU_MAP_API_KEY，可接入真实地图 MCP（当前默认仍走离线桩）");
        } else {
            log.warn("[百度地图] 未配置 BAIDU_MAP_API_KEY，离线桩返回演示数据；"
                    + "prod 接入真实地图 MCP 时需通过环境变量注入该 Key");
        }
    }

    /** 是否已配置真实百度地图 Key（观测/测试用，也可作为「是否切换真实地图」的开关依据）。 */
    public boolean isBaiduMapKeyConfigured() {
        return baiduMapProperties.isKeyConfigured();
    }

    /** 对应百度地图 MCP 的 map_geocode：地理编码。 */
    @Tool(name = "map_geocode", description = "把地址转换为经纬度坐标")
    public String geocode(@ToolParam(name = "address", description = "地址，如 杭州西湖") String address) {
        requireText(address, "address");
        return "{\"lng\":120.155070,\"lat\":30.274084,\"precise\":1,\"confidence\":90,\"level\":\"兴趣点\"}";
    }

    /** 对应百度地图 MCP 的 map_directions_matrix：路线/通勤方案。 */
    @Tool(name = "map_directions", description = "查询两点之间的通行方案，返回路线摘要")
    public String directions(
            @ToolParam(name = "origin", description = "起点") String origin,
            @ToolParam(name = "destination", description = "终点") String destination) {
        requireText(origin, "origin");
        requireText(destination, "destination");
        double minutes = 25 + (origin.length() + destination.length()) % 30;
        return String.format(
                "{\"origin\":\"%s\",\"destination\":\"%s\",\"distance_km\":%.1f,\"duration_min\":%.0f,"
                        + "\"route\":\"地铁+步行\",\"taxi_estimate_cny\":%.0f}",
                origin, destination, minutes * 0.4, minutes, minutes * 2.5);
    }

    /** 对应百度地图 MCP 的 map_weather：目的地天气（行程决策输入）。 */
    @Tool(name = "map_weather", description = "查询目的地天气")
    public String weather(@ToolParam(name = "city", description = "城市，如 杭州") String city) {
        requireText(city, "city");
        return String.format("{\"city\":\"%s\",\"forecasts\":[{\"date\":\"D1\",\"high\":28,\"low\":20,\"text_day\":\"多云\"}]}", city);
    }

    /** 暴露本 Agent 的工具清单（课程 11-6 用 toolkit.getToolNames() 验证挂载）。 */
    public Map<String, String> toolNames() {
        return Map.of(
                "map_geocode", "地理编码",
                "map_directions", "路线规划",
                "map_weather", "天气查询");
    }

    /** 工具入参统一非空校验：非法时抛 IllegalArgumentException，由框架回灌模型自我修正。 */
    private static void requireText(String value, String name) {
        if (value == null || value.isBlank()) {
            throw new IllegalArgumentException(name + " 不能为空");
        }
    }
}
