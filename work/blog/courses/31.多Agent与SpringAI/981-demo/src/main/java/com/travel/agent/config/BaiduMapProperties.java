package com.travel.agent.config;

import org.springframework.boot.context.properties.ConfigurationProperties;

/**
 * 百度地图开放平台凭证配置。
 *
 * <p>生产务必通过环境变量 {@code BAIDU_MAP_API_KEY} 注入，<b>严禁在代码或配置里硬编码 AK</b>；
 * 缺省（未配置）时 {@link #isKeyConfigured()} 返回 false，调用方走离线桩并打告警，
 * 不会因缺 Key 直接启动失败（优雅降级）。</p>
 */
@ConfigurationProperties(prefix = "baidu.map")
public class BaiduMapProperties {

    /** 百度地图 API Key；默认从环境变量 BAIDU_MAP_API_KEY 取，空串表示未配置。 */
    private String apiKey = "";

    public String getApiKey() {
        return apiKey;
    }

    public void setApiKey(String apiKey) {
        this.apiKey = apiKey == null ? "" : apiKey;
    }

    public boolean isKeyConfigured() {
        return apiKey != null && !apiKey.isBlank();
    }
}
