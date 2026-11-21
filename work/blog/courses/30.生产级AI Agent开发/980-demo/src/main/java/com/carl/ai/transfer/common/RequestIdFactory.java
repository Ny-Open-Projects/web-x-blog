package com.carl.ai.transfer.common;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

/**
 * 幂等键（requestId）工厂。
 * <p>
 * 两个来源：
 * <ul>
 *   <li>客户端显式 {@code Idempotency-Key} 头（优先）：调用方自己保证键的全局唯一语义；</li>
 *   <li>无显式键时按需求文本派生 SHA-256：同一句自然语言重复提交天然同键，
 *       挡住「用户连点 / 前端重试 / 工作流重投」造成的重复调拨单。</li>
 * </ul>
 * 键长统一收敛到 64 字符（SHA-256 hex 恰好 64），与 bb_transfer_order.request_id 列宽一致。
 */
public final class RequestIdFactory {

    private static final String SHA_256 = "SHA-256";
    private static final int KEY_MAX_LENGTH = 64;

    private RequestIdFactory() {
    }

    /**
     * 归一化客户端幂等键：trim + 超长截断；空白 / null 视为「未提供」。
     */
    public static String normalizeClientKey(String clientKey) {
        if (clientKey == null || clientKey.isBlank()) {
            return null;
        }
        String trimmed = clientKey.trim();
        return trimmed.length() > KEY_MAX_LENGTH ? trimmed.substring(0, KEY_MAX_LENGTH) : trimmed;
    }

    /**
     * 自然语言需求文本 → SHA-256 hex（64 字符）。
     * trim 后哈希：首尾空白差异不产生不同键。
     */
    public static String fromText(String requirement) {
        return sha256Hex(requirement.trim());
    }

    /**
     * 从 param 关键字段派生内容哈希：服务层被单独调用（未经过 Agent 派生）时的兜底键。
     * 明细先排序再拼接，避免 items 顺序波动导致同语义不同键。
     */
    public static String fromFields(Integer sourceWarehouseId, Integer targetWarehouseId,
                                    String transferDate, List<String[]> items) {
        String itemPart = items == null ? "" : items.stream()
                .map(it -> Objects.toString(it[0], "") + ":" + Objects.toString(it[1], ""))
                .sorted()
                .collect(Collectors.joining(";"));
        String raw = Objects.toString(sourceWarehouseId, "") + "|"
                + Objects.toString(targetWarehouseId, "") + "|"
                + Objects.toString(transferDate, "") + "|" + itemPart;
        return sha256Hex(raw);
    }

    private static String sha256Hex(String raw) {
        try {
            MessageDigest md = MessageDigest.getInstance(SHA_256);
            byte[] digest = md.digest(raw.getBytes(StandardCharsets.UTF_8));
            StringBuilder sb = new StringBuilder(digest.length * 2);
            for (byte b : digest) {
                sb.append(Character.forDigit((b >> 4) & 0xF, 16));
                sb.append(Character.forDigit(b & 0xF, 16));
            }
            return sb.toString();
        } catch (NoSuchAlgorithmException e) {
            // SHA-256 是 JDK 强制算法，走到这里说明 JDK 被裁剪，直接快速失败
            throw new IllegalStateException("JDK 缺少 SHA-256，无法派生幂等键", e);
        }
    }
}
