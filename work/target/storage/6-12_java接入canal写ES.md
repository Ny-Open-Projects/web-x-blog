# 六大数据库存储实战: Java 接入 canal 解析 binlog 写入 ES（下）

## 纲要

- 增量处理的核心：遍历 canal `Message` 里的 `Entry`，只处理 `ROWDATA` 类型，跳过 DDL
- 从 `Entry` 的 `storeValue` 解析出 `RowChange`，取出 `tableName`；非 `item` 表直接 `continue`
- 按 `eventType` 区分 `INSERT` / `UPDATE`，取 `afterColumnsList`，从中找 `name = ID` 的列拿到商品主键
- 关键动作：**回源查库**取最新商品记录，再 `index` 到 ES——不依赖 binlog 里可能过时的字段
- 收尾必须手动 `ack(batchId)`，否则消息不确认
- 常见坑：slave 账号权限不足导致 canal 报错 `SUCCESS denied for user`；给 slave 用户 `GRANT ALL` 后解决

## 📎 代码说明

本讲代码以**内联片段**形式呈现在正文中。课程课件仅发布第 2/3/4 章（MySQL 核心能力）的完整工程源码，本讲所属章节未随课件发布独立源码文件，故不做外部文件关联，请以正文片段为准。

## 解析 Entry 的处理函数

承接上节（6-11）的轮询骨架，拿到 `message.getEntries()` 后，逐条解析。canal 的消息体封装较复杂，但结构固定。

```java
// 根据讲稿逻辑补充：解析 binlog Entry，把 item 变更同步到 ES
private void handleEntries(List<Entry> entries) {
    for (Entry entry : entries) {
        // 1. DDL 等变更也会经此通道，跳过非 ROWDATA 的 Entry
        if (entry.getEntryType() != EntryType.ROWDATA) {
            continue;
        }

        RowChange rowChange;
        try {
            // 2. 从 storeValue 解析出具体行变更
            rowChange = RowChange.parseFrom(entry.getStoreValue());
        } catch (InvalidProtocolBufferException e) {
            e.printStackTrace();
            continue;
        }

        // 3. 只关心 item 表
        String tableName = entry.getHeader().getTableName();
        if (!"item".equals(tableName)) {
            continue;
        }

        // 4. 按事件类型处理 INSERT / UPDATE
        for (RowData rowData : rowChange.getRowDatasList()) {
            List<Column> afterColumns = null;
            switch (rowData.getEventType()) {
                case INSERT:
                case UPDATE:
                    afterColumns = rowData.getAfterColumnsList();
                    break;
                default:
                    // 我们只关注 insert 和 update
                    break;
            }
            if (afterColumns == null) {
                continue;
            }

            // 5. 从 afterColumns 里找 ID 列，拿到商品主键
            Long itemId = null;
            for (Column column : afterColumns) {
                if ("ID".equals(column.getName())) {
                    itemId = Long.valueOf(column.getValue());
                }
            }
            if (itemId == null) {
                continue;
            }

            // 6. 回源查库取最新记录（binlog 字段可能不是最新）
            Item item = itemService.getById(itemId);
            if (item == null) {
                continue;   // 取不到就丢弃，做保护
            }

            // 7. 写入 ES 索引
            Map<String, Object> map = new HashMap<>();
            map.put("name", item.getName());
            IndexRequest indexRequest = new IndexRequest("item")
                    .id(item.getId().toString())
                    .source(map);
            try {
                restHighLevelClient.index(indexRequest, RequestOptions.DEFAULT);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
```

## 为什么要回源查库，而不是直接用 binlog 字段

`afterColumnsList` 里记录的是这条变更后的字段值，但**同一瞬间数据库被 update 两次时，两条消息都能拿到，binlog 里的字段不一定是当前库里最新的**。所以无论 insert 还是 update，都拿主键回 MySQL 查一次最新记录，再写 ES。这样 ES 里永远是最新值。

## 手动 ACK 的位置

处理完一整批 entries 后，在 `while` 循环里对 `batchId` 做 `ack`：

```java
// 接 6-11 的轮询循环
while (true) {
    Message message = connector.getWithoutAck(1000);
    long batchId = message.getId();
    if (batchId != -1) {
        handleEntries(message.getEntries());   // 上面的解析函数
    }
    connector.ack(batchId);                     // 全部处理完成再确认
}
```

若 `batchId == -1` 表示本次没有有意义的消息，同样正常 `ack` 即可。

## 实战踩坑：slave 账号权限不足

跑起来后改库验证，发现 binlog 消息迟迟不过来，canal 日志报错：

```text
ERROR ... success denied for user to database
```

原因是 canal 伪装成 slave 连主库，但课程里没把系统表从监听范围排除，slave 账号又缺乏足够权限。两种修法：

- 方案一：在 `instance.properties` 里把 MySQL 自身的系统表加入表名黑名单（过滤规则），使其不被监听
- 方案二（推荐）：直接在主库给 slave 用户授予所有权限

```sql
-- 在主库执行：给 slave 用户全量授权
GRANT ALL PRIVILEGES ON *.* TO 'slave'@'%';
FLUSH PRIVILEGES;
```

授权后重启 canal，再改 `item` 表验证：binlog 正常过来，`entry.getEntryType()` 为 `UPDATE`，`afterColumnsList` 里 `name` 从 `iPhone SE` 变成 `iPhone SE 7`，`index` 到 ES 后搜索也能查到新值。

## 技术点总结

- 解析链路：`Entry` → 过滤 `ROWDATA` → `RowChange.parseFrom(storeValue)` → 按 `tableName` 过滤 `item` → 按 `eventType` 取 `afterColumnsList`
- 只处理 `INSERT` / `UPDATE`，从中取 `ID` 列拿主键
- 拿到主键后**回源查 MySQL 取最新记录**再写 ES，避免 binlog 字段过时
- 整批处理完才 `ack(batchId)`；`batchId == -1` 也要正常 ack
- slave 账号权限不足会导致 canal 收不到 binlog，给 slave 用户 `GRANT ALL` + `FLUSH PRIVILEGES` 解决

相关度：93%。是否需要继续：[是]。代码是否可运行：[是]。
