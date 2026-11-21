package com.travel.agent;

import static org.assertj.core.api.Assertions.assertThat;

import com.travel.agent.config.BaiduMapProperties;
import com.travel.agent.tool.RouteMakingTools;
import org.junit.jupiter.api.Test;

/**
 * 百度地图凭证管理单测（#542）：
 * ① Key 从外部（环境变量/配置）注入，绝不硬编码；
 * ② 缺失时 {@link RouteMakingTools#isBaiduMapKeyConfigured()} 返回 false（优雅降级，不启动失败）；
 * ③ 工具本身离线仍可用，与 Key 是否配置无关。
 */
class RouteMakingToolsTest {

    @Test
    void keyConfigured_trueWhenApiKeyPresent() {
        BaiduMapProperties props = new BaiduMapProperties();
        props.setApiKey("AK-from-env-123");
        RouteMakingTools tools = new RouteMakingTools(props);
        assertThat(tools.isBaiduMapKeyConfigured()).isTrue();
    }

    @Test
    void keyConfigured_falseWhenAbsent() {
        BaiduMapProperties props = new BaiduMapProperties(); // 默认空串
        RouteMakingTools tools = new RouteMakingTools(props);
        assertThat(tools.isBaiduMapKeyConfigured()).isFalse();
    }

    @Test
    void setApiKey_nullSafe_noHardcode() {
        BaiduMapProperties props = new BaiduMapProperties();
        props.setApiKey(null); // 防御：外部注入 null 等同未配置
        assertThat(props.isKeyConfigured()).isFalse();
    }

    @Test
    void toolsWorkOfflineRegardlessOfKey() {
        RouteMakingTools tools = new RouteMakingTools(new BaiduMapProperties());
        assertThat(tools.geocode("杭州西湖")).contains("lng");
        assertThat(tools.directions("杭州东站", "西湖")).contains("duration_min");
        assertThat(tools.weather("杭州")).contains("forecasts");
        assertThat(tools.toolNames()).containsKeys("map_geocode", "map_directions", "map_weather");
    }

    @Test
    void toolsRejectBlankInput() {
        RouteMakingTools tools = new RouteMakingTools(new BaiduMapProperties());
        try {
            tools.geocode("   ");
            assertThat(false).as("空地址应抛异常").isTrue();
        } catch (IllegalArgumentException e) {
            assertThat(e.getMessage()).contains("不能为空");
        }
    }
}
