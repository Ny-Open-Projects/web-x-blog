# 画面线理解：07_数据迁移_hbase封装storageclient测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\07_数据迁移_hbase封装storageclient测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:39, 02:26, 03:27, 04:04, 05:21, 06:14, 07:00, 07:39, 08:38, 09:21, 10:20, 11:37, 12:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:03:56

1) 这一组画面整体在讲如何通过 Java 代码实现对 HBase 表的增删改查操作，重点演示了如何封装存储数据并批量写入 HBase。

2) 按时间顺序列出每张画面的要点：
画面1：展示 HBase 测试类 HBaseTest.java 中的 testSaveData() 方法，用于向 HBase 表 hbase_test_table_name 写入数据，代码中设置了列名和值。
画面2：展示 testStorageSaveData() 方法，准备调用 HBaseStorageClient 的 addBaseStorage 方法写入数据。
画面3：在 testStorageSaveData() 方法中，实例化 HBaseStorage 对象 storage，并设置其 rowKey 和 tableName。
画面4：展示 Article.java 实体类，定义了文章的属性，如 id、title、authorId 等。
画面5：在 testStorageSaveData() 方法中，创建 StorageEntry 对象并设置其 key 和 value，然后添加到 StorageData 的 entryList 中。
画面6：展示 StorageData 的 setEntryList 方法，用于设置存储数据的 entry 列表。
画面7：继续编写 testStorageSaveData() 方法，将 StorageData 对象添加到 dataList，并调用 storageClient 的 addBaseStorage 方法。
画面8：调试模式下，展示 HBaseStorage 对象的结构，包含 rowKey、hbaseLook、dataList 等属性。
画面9：测试通过，控制台输出测试结果。
画面10：测试通过，控制台输出测试结果。
画面11：展示 HBaseStorageClient 类中的 getStorageDataEntity 方法，用于根据 rowKey 获取存储数据。
画面12：展示 getStorageDataEntity 方法的实现，通过 HBaseClient 获取 StorageData 并返回。
画面13：展示 testStorageSaveData() 方法中设置 StorageEntry 的 key 和 value。
画面14：展示 getStorageDataEntity 方法的注释，说明其参数和返回值。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1：
```java
@Test
public void testSaveData() {
    //String tableName, String rowKey, String[] columns, String[] values
    String [] columns = {"name", "age"};
    String [] values = {"zhangsan", "28"};
    HBaseClient.putData( tableName: "hbase_test_table_name", rowKey: "test_row_key_001", family: "info", columns: columns, values: values);
}
```

画面2：
```java
@Test
public void testStorageSaveData() {
    storageClient.addBaseStorage( tableName: "hbase_storage_test_table_name");
}
```

画面3：
```java
@Test
public void testStorageSaveData() {
    HBaseStorage storage = new HBaseStorage();
    storage.setRowKey("storage_row_key_00001");
    storage.setTableName("hbase_storage_test_table_name");
    storageClient.addBaseStorage( tableName: "hbase_storage_test_table_name", storage);
}
```

画面4：
```java
package com.heima.model.article.pojos;

import ...

@Data
public class AArticle {
    private Integer id;
    private String title;
    private Long authorId;
    private String authorName;
    private Integer channelId;
    private String channelName;
    private Short layout;
    private Extra flag;
    private String images;
    private String labels;
    private Integer likes;
    private Integer collection;
}
```

画面5：
```java
StorageEntry entry = new StorageEntry();
entry.setKey("title");
entry.setValue("数据迁移");
StorageEntry entry2 = new StorageEntry();
entry2.setKey("id");
entry2.setValue("123456");
entryList.add(entry);
entryList.add(entry2);
storageData.setEntryList(entryList);
```

画面6：
```java
storageData.setEntryList(entryList);
```

画面7：
```java
StorageEntry entry = new StorageEntry();
entry.setKey("title");
entry.setValue("数据迁移");
StorageEntry entry2 = new StorageEntry();
entry2.setKey("id");
entry2.setValue("123456");
entryList.add(entry);
entryList.add(entry2);
storageData.setEntryList(entryList);
```

画面8：
```java
storageClient.addBaseStorage( tableName: "hbase_storage_test_table_name", storage);
```

画面9：
```java
@Test
public void testStorageSaveData() {
    HBaseStorage storage = new HBaseStorage();
    storage.setRowKey("storage_row_key_00001");
    storage.setTableName("hbase_storage_test_table_name");
    storageClient.addBaseStorage( tableName: "hbase_storage_test_table_name", storage);
}
```

画面10：
```java
@Test
public void testStorageSaveData() {
    HBaseStorage storage = new HBaseStorage();
    storage.setRowKey("storage_row_key_00001");
    storage.setTableName("hbase_storage_test_table_name");
    storageClient.addBaseStorage( tableName: "hbase_storage_test_table_name", storage);
}
```

画面11：
```java
public <T> T getStorageDataEntity(String tableName, String rowKey, Class<T> tClass) {
    if (StringUtils.isEmpty(tableName)) {
        StorageData storageData = hBaseClient.getStorageData(tableName, rowKey, tClass.getName());
        if (null != storageData) {
            tValue = (T) storageData.getObjectValue();
        }
    }
    return tValue;
}
```

画面12：
```java
public <T> T getStorageDataEntity(String tableName, String rowKey, Class<T> tClass) {
    if (StringUtils.isEmpty(tableName)) {
        StorageData storageData = hBaseClient.getStorageData(tableName, rowKey, tClass.getName());
        if (null != storageData) {
            tValue = (T) storageData.getObjectValue();
        }
    }
    return tValue;
}
```

画面13：
```java
StorageEntry entry = new StorageEntry();
entry.setKey("title");
entry.setValue("数据迁移");
StorageEntry entry2 = new StorageEntry();
entry2.setKey("id");
entry2.setValue("123456");
entryList.add(entry);
entryList.add(entry2);
storageData.setEntryList(entryList);
```

画面14：
```java
public <T> T getStorageDataEntity(String tableName, String rowKey, Class<T> tClass) {
    if (StringUtils.isEmpty(tableName)) {
        StorageData storageData = hBaseClient.getStorageData(tableName, rowKey, tClass.getName());
        if (null != storageData) {
            tValue = (T) storageData.getObjectValue();
        }
    }
    return tValue;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
