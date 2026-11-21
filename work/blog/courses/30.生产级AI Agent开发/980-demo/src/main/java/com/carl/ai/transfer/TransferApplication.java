package com.carl.ai.transfer;

import com.carl.ai.transfer.agent.TransferAgent;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * 980-demo 启动类（复刻 mksz980 第5章：LLM 生成 → 结构化抽取 → MapStruct 转换 → 入库）。
 * <p>
 * default profile（{@code transfer.offline=true}）启动即跑通一次完整闭环：离线 MockChatModel
 * 返回固定调拨单 JSON → {@link com.carl.ai.transfer.extract.TransferOrderExtractor} 用
 * {@code call().entity()} 提取 → MapStruct 转换 → H2 入库。无需联网、无需 Key。
 */
@SpringBootApplication
public class TransferApplication implements CommandLineRunner {

    private static final Logger log = LoggerFactory.getLogger(TransferApplication.class);

    private final TransferAgent transferAgent;
    private final boolean offline;

    public TransferApplication(TransferAgent transferAgent,
                               @Value("${transfer.offline:true}") boolean offline) {
        this.transferAgent = transferAgent;
        this.offline = offline;
    }

    public static void main(String[] args) {
        SpringApplication.run(TransferApplication.class, args);
    }

    @Override
    public void run(String... args) {
        if (!offline) {
            log.info("prod profile：跳过启动演示调用（避免无 Key 调真实模型）");
            return;
        }
        String result = transferAgent.createTransferFromText(
                "把华北仓的 10 件 SKU-A 调拨到华东仓，日期 2026-10-20", null);
        log.info("【离线演示闭环】{}", result);
    }
}
