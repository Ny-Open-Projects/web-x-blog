# 画面线理解：06_数据迁移_hbase原生client测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\06_数据迁移_hbase原生client测试【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:24, 01:01, 01:37, 01:57, 02:28, 02:50, 02:59, 03:50, 04:02, 04:17, 06:09, 06:32, 07:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:03:14

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的 Java 项目如何通过单元测试对 HBase 数据库进行表的创建、删除、数据写入和查询操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，选中 `src/main/java/com/heima/migration/config/InitConfig.java` 文件。
画面2：显示 `InitConfig.java` 文件内容，包含 `@Configuration` 和 `@EnableScheduling` 注解，以及 `@ComponentScan` 指定扫描包。
画面3：显示 `HBaseTest.java` 文件，包含 `testCreateTable()`、`testDeleteTable()`、`testSaveData()` 和 `testFindRowKey()` 四个测试方法。
画面4：展示在 SecureCRT 中执行 HBase 命令的终端输出，显示了表的创建、删除和数据操作结果。
画面5：显示 `HBaseTest.java` 文件，光标位于 `testCreateTable()` 方法中。
画面6：显示 `HBaseTest.java` 文件，光标位于 `testDeleteTable()` 方法中，下方终端显示测试通过日志。
画面7：展示在 SecureCRT 中执行 HBase 命令的终端输出，显示了表的创建、删除和数据操作结果。
画面8：显示 `HBaseTest.java` 文件，光标位于 `testCreateTable()` 方法中，下方终端显示测试通过日志。
画面9：显示 `HBaseTest.java` 文件，光标位于 `testCreateTable()` 方法中，下方终端显示测试通过日志。
画面10：显示 `HBaseTest.java` 文件，光标位于 `testDeleteTable()` 方法中，下方终端显示测试通过日志。
画面11：显示 `HBaseTest.java` 文件，光标位于 `testSaveData()` 方法中，下方终端显示测试通过日志。
画面12：显示 `HBaseTest.java` 文件，光标位于 `testSaveData()` 方法中，下方终端显示测试通过日志。
画面13：显示 `HBaseTest.java` 文件，光标位于 `testFindRowKey()` 方法中，下方终端显示测试通过日志。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
package com.heima.migration.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@ComponentScan({"com.heima.common.common.init","com.heima.common.mysql.core", "com.heima.common.hbase"})
@EnableScheduling
public class InitConfig {
}
```

画面3：
```java
columnFamily.add("test_cloum_family1");
columnFamily.add("test_cloum_family2");
boolean ret = hBaseClient.createTable(tableName: "hbase_test_table_name", columnFamily);
```

画面5：
```java
public void testCreateTable() {
    List<String> columnFamily = new ArrayList<>();
    columnFamily.add("test_cloum_family1");
    columnFamily.add("test_cloum_family2");
    boolean ret = hBaseClient.createTable(tableName: "hbase_test_table_name", columnFamily);
}
```

画面6：
```java
@Test
public void testDeleteTable() {
    hBaseClient.deleteTable(tableName: "hbase_test_table_name");
}
```

画面7：
```java
String []columns = {"name","age"};
String []values = {"shangsan","28"};
hBaseClient.putData(tableName: "hbase_test_table_name", rowKey: "test_row_key_001", familyName: "test_cloum_family1", columns, values);
```

画面10：
```java
@Test
public void testDeleteTable() {
    hBaseClient.deleteTable(tableName: "hbase_test_table_name");
}
```

画面11：
```java
@Test
public void testSaveData() {
    //String tableName, String rowKey, String familyName, String[] columns, String[] values
    String []columns = {"name","age"};
    String []values = {"shangsan","28"};
    hBaseClient.putData(tableName: "hbase_test_table_name", rowKey: "test_row_key_001", familyName: "test_cloum_family1", columns, values);
}
```

画面12：
```java
@Test
public void testSaveData() {
    //String tableName, String rowKey, String familyName, String[] columns, String[] values
    String []columns = {"name","age"};
    String []values = {"shangsan","28"};
    hBaseClient.putData(tableName: "hbase_test_table_name", rowKey: "test_row_key_001", familyName: "test_cloum_family1", columns, values);
}
```

画面13：
```java
@Test
public void testFindRowKey() {
    Result hbaseResult = hBaseClient.getHbaseResult(tableName: "hbase_test_table_name", rowKey: "test_row_key_001");
    System.out.println(hbaseResult);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
