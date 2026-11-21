package com.travel.agent;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * 981-demo：多 Agent 自主决策旅游规划。
 *
 * <p>复刻课程第 10~13 章的形态：主管 Agent（Supervisor）通过 A2A 协议发现并调度
 * 远程团队成员 Agent，成员 Agent 通过 Toolkit 挂载 MCP 风格工具。
 * 详见 README.md 与课程 11-2 / 11-3 / 11-4 / 11-6 / 11-7 篇。
 */
@SpringBootApplication
public class TravelAgentApplication {

    public static void main(String[] args) {
        SpringApplication.run(TravelAgentApplication.class, args);
    }
}
