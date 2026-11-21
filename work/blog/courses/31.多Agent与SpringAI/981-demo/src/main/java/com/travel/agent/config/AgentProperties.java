package com.travel.agent.config;

import org.springframework.boot.context.properties.ConfigurationProperties;

/**
 * Agent 团队配置（application.yml 的 {@code app.agent.*}）。
 */
@ConfigurationProperties(prefix = "app.agent")
public class AgentProperties {

    /** offline：离线规则模型（默认，可无 Key 跑通全链路）；dashscope：真实模型。 */
    private String modelMode = "offline";

    /** 真实模式的模型 id，ModelRegistry 可解析，如 dashscope:qwen-plus。 */
    private String modelName = "dashscope:qwen-plus";

    /** in-process：进程内注册表；nacos：Nacos 注册中心（课程 11-2）。 */
    private String discovery = "in-process";

    private String nacosServerAddr = "127.0.0.1:8848";

    /**
     * 注册到 Nacos 时对外暴露的 IP（容器 / 多网卡场景必须显式配置，
     * 否则回退 InetAddress.getLocalHost()，DNS 异常时可能拿到 127.0.0.1）。
     */
    private String advertiseIp = "";

    /** ReAct 循环最大迭代轮数（AgentScope 默认 10；收紧可控制 token 成本）。 */
    private int maxIters = 10;

    public String getModelMode() {
        return modelMode;
    }

    public void setModelMode(String modelMode) {
        this.modelMode = modelMode;
    }

    public String getModelName() {
        return modelName;
    }

    public void setModelName(String modelName) {
        this.modelName = modelName;
    }

    public String getDiscovery() {
        return discovery;
    }

    public void setDiscovery(String discovery) {
        this.discovery = discovery;
    }

    public String getNacosServerAddr() {
        return nacosServerAddr;
    }

    public void setNacosServerAddr(String nacosServerAddr) {
        this.nacosServerAddr = nacosServerAddr;
    }

    public String getAdvertiseIp() {
        return advertiseIp;
    }

    public void setAdvertiseIp(String advertiseIp) {
        this.advertiseIp = advertiseIp;
    }

    public int getMaxIters() {
        return maxIters;
    }

    public void setMaxIters(int maxIters) {
        this.maxIters = maxIters;
    }

    public boolean isOffline() {
        return "offline".equalsIgnoreCase(modelMode);
    }

    public boolean isNacos() {
        return "nacos".equalsIgnoreCase(discovery);
    }
}
