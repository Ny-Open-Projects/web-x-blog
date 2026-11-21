package com.carl.ai.transfer.config;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * 幂等唯一索引兜底初始化。
 * <p>
 * default（create-drop）模式下索引由 Hibernate 按 {@code @Column(unique=true)} 自动创建；
 * prod（ddl-auto=update）模式下 Hibernate 只加列、<b>不会给已有表补唯一约束</b>，
 * 导致幂等只剩预查一道防线。启动时 best-effort 执行 DDL 补齐：
 * H2 支持 {@code IF NOT EXISTS} 直接通过；MySQL 不支持，索引已存在时报 1061，
 * 捕获后视为就绪。库里有历史重复 requestId 时建索引会失败，只告警不阻断启动
 * （运维按 DEPLOY.md 的清理 SQL 处理后重启即可）。
 */
@Component
public class IdempotencyIndexInitializer implements ApplicationRunner {

    private static final Logger log = LoggerFactory.getLogger(IdempotencyIndexInitializer.class);

    private static final String DDL =
            "CREATE UNIQUE INDEX IF NOT EXISTS uk_bb_transfer_order_request_id ON bb_transfer_order(request_id)";

    private final DataSource dataSource;

    public IdempotencyIndexInitializer(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @Override
    public void run(ApplicationArguments args) {
        try (Connection conn = dataSource.getConnection();
             Statement stmt = conn.createStatement()) {
            stmt.execute(DDL);
            log.info("幂等唯一索引就绪：uk_bb_transfer_order_request_id");
        } catch (SQLException e) {
            log.warn("幂等唯一索引未自动创建（可能已存在或存在历史重复数据）：{}", e.getMessage());
        }
    }
}
