# 画面线理解：05_数据迁移_common模块整合hbase

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\05_数据迁移_common模块整合hbase【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:33, 00:58, 01:32, 01:50, 02:24, 02:53, 03:13, 03:38, 04:09, 04:55, 05:22, 05:54, 06:50, 07:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:02:42

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 HBase 的 Java 项目中，如何通过配置文件初始化客户端、创建表、删除列族、查询数据以及封装存储对象的代码实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示项目结构，选中 `HBaseConfig.java` 文件。
画面 2: 选中 `HBaseConstants` 类，准备查看其内容。
画面 3: 展示 `HBaseConfig.java` 代码，包含 HBase 配置项如 `zookeeper.quorum` 和 `client.keyvalue.maxsize`，以及创建 `HBaseClient` 的方法。
画面 4: 展示 `HBaseClient.java` 中的 `deleteColumnFamily` 方法，用于删除表的列族。
画面 5: 展示 `HBaseClient.java` 中的 `createTable` 方法，用于创建 HBase 表，包含 `TableDescriptor` 和 `ColumnFamilyDescriptor` 的构建逻辑。
画面 6: 展示 `HBaseClient.java` 中 `createTable` 方法的完整实现，包含表存在性判断和异常处理。
画面 7: 展示 `HBaseClient.java` 中的 `getFamilyNames` 方法，用于获取表的所有列族名称。
画面 8: 展示 `HBaseClient.java` 中的 `queryData` 方法，用于通过 Scan 查询数据，使用 `ResultScanner` 和 `HashMap`。
画面 9: 展示 `HBaseClient.java` 中的 `getColumnValuesByVersion` 方法，用于根据版本号查询单元格数据。
画面 10: 展示 `HBaseStorageClient.java` 中的 `getStorageDataEntity` 方法，用于根据表名、行键和类获取存储数据。
画面 11: 展示 `HBaseStorageClient.java` 中的 `addRaceStorage` 方法，用于添加存储数据，包含创建表、获取数据列表和写入操作。
画面 12: 展示 `HBaseConstants.java` 文件，定义常量 `APARTICLE_QUANTITY_TABLE_NAME`。
画面 13: 展示 `HBaseStorage.java` 文件，定义 `HBaseStorage` 类，继承 `StorageEntry`，包含 `rowKey` 和 `hBaseInvok` 字段。
画面 14: 展示 `pom.xml` 文件，列出项目依赖，包括 Spring Boot 各模块和 `reflections`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3 代码：
```java
//HBase 让带先生
//
@Value("${hbase.zookeeper.quorum}")
private String zookeeper_quorum;
//
//超时时间
//
@Value("${hbase.client.keyvalue.maxsize}")
private String maxsize;
//
//创建HBaseClient
//
@Bean
public HBaseClient getHBaseClient() {
    org.apache.hadoop.hbase.client.HBaseConfiguration hBaseConfiguration = getHBaseConfiguration();
    return new HBaseClient(hBaseConfiguration);
}
```

画面 4 代码：
```java
//根据columnFamily删除指定的列族
*
* @param tableName 表名
* @param columnFamily 列族
* @return boolean
* @since 1.0.0
public boolean deleteColumnFamily(String tableName, String columnFamily) {
    Admin admin = null;
    try {
        admin = connection.getAdmin();
        admin.deleteColumnFamily(tableName, columnFamily);
        return true;
    } catch (IOException e) {
        log.error(MessageFormat.format("删除列族失败，tableName:{0}, columnFamily:{1}", tableName, columnFamily), e);
        return false;
    } finally {
        close(admin, null, null);
    }
    return true;
}
```

画面 5 代码：
```java
//创建表
*
* @param tableName 表名
* @param columnFamily 列族
* @return boolean
* @since 1.0.0
public boolean createTable(String tableName, List<String> columnFamily) {
    Admin admin = null;
    try {
        admin = connection.getAdmin();
        List<ColumnFamilyDescriptor> familyDescriptors = new ArrayList<>(columnFamily.size());
        columnFamily.forEach(cf -> {
            familyDescriptors.add(ColumnFamilyDescriptor.newBuilder(Bytes.toBytes(cf)).build());
        });
        TableDescriptor tableDescriptor = TableDescriptorBuilder.newBuilder(tableName)
                .setColumnFamilies(familyDescriptors)
                .build();
        if (admin.tableExists(TableNames.valueOf(tableName))) {
            log.debug("table Exists!");
        } else {
            admin.createTable(tableDescriptor);
            log.debug("create table Success!");
        }
    } catch (IOException e) {
        log.error(MessageFormat.format("创建表失败，tableName:{0}", tableName), e);
        return false;
    } finally {
        close(admin, null, null);
    }
    return true;
}
```

画面 6 代码：
```java
//创建表
*
* @param tableName 表名
* @param columnFamily 列族
* @return boolean
* @since 1.0.0
public boolean createTable(String tableName, List<String> columnFamily) {
    Admin admin = null;
    try {
        admin = connection.getAdmin();
        List<ColumnFamilyDescriptor> familyDescriptors = new ArrayList<>(columnFamily.size());
        columnFamily.forEach(cf -> {
            familyDescriptors.add(ColumnFamilyDescriptor.newBuilder(Bytes.toBytes(cf)).build());
        });
        TableDescriptor tableDescriptor = TableDescriptorBuilder.newBuilder(tableName)
                .setColumnFamilies(familyDescriptors)
                .build();
        if (admin.tableExists(TableNames.valueOf(tableName))) {
            log.debug("table Exists!");
        } else {
            admin.createTable(tableDescriptor);
            log.debug("create table Success!");
        }
    } catch (IOException e) {
        log.error(MessageFormat.format("创建表失败，tableName:{0}", tableName), e);
        return false;
    } finally {
        close(admin, null, null);
    }
    return true;
}
```

画面 7 代码：
```java
//获取表所有的列族
*
* @param tableName 表名
* @return List<String> 所有列族名称
* @since 1.0.0
public List<String> getFamilyNames(String tableName) {
    ColumnFamilyDescriptor[] familyDescriptorList = null;
    List<String> familyNameList = new ArrayList<>();
    try {
        Table table = getTable(tableName);
        familyDescriptorList = table.getDescriptor().getColumnFamilies();
    } catch (IOException e) {
        log.error("获取表的所有列族失败", e);
    } finally {
        if (null != familyDescriptorList && familyDescriptorList.length > 0) {
            familyNameList = Arrays.stream(familyDescriptorList).map(ColumnFamilyDescriptor::getFamilyName).collect(Collectors.toList());
        }
    }
    return familyNameList;
}
```

画面 8 代码：
```java
//通过表名以及过滤条件查询数据
*
* @param tableName 表名
* @param scan 查询条件
* @return Map<String, Map<String, String>> 查询结果
* @since 1.0.0
private Map<String, Map<String, String>> queryData(String tableName, Scan scan) {
    ResultScanner rs = null;
    Table table = null;
    try {
        table = getTable(tableName);
        rs = table.getScanner(scan);
        for (Result r : rs) {
            Map<String, String> columnMap = new HashMap<>();
            for (Cell cell : r.listCells()) {
                columnMap.put(Bytes.toString(CellUtil.cloneFamily(cell)), Bytes.toString(CellUtil.cloneQualifier(cell)));
            }
            result.put(Bytes.toString(CellUtil.cloneRow(cell)), columnMap);
        }
    } catch (IOException e) {
        log.error("查询数据失败", e);
    } finally {
        if (rs != null) {
            rs.close();
        }
        if (table != null) {
            table.close();
        }
    }
    return result;
}
```

画面 9 代码：
```java
//根据表名、rowKey、familyName、columnFamily 查询指定单元格的数据
*
* @param tableName 表名
* @param rowKey 行键
* @param familyName 列族
* @param columnName 列名
* @param versions 需要查询的版本数
* @return List<String> 查询结果
* @since 1.0.0
public List<String> getColumnValuesByVersion(String tableName, String rowKey, String familyName, String columnName, int versions) {
    //获取表
    Table table = null;
    try {
        table = getTable(tableName);
        Result result = table.get(new Get(Bytes.toBytes(rowKey)).addColumn(Bytes.toBytes(familyName), Bytes.toBytes(columnName)).setVersions(versions));
        List<String> values = new ArrayList<>();
        for (Cell cell : result.listCells()) {
            values.add(Bytes.toString(CellUtil.cloneValue(cell)));
        }
        return values;
    } catch (IOException e) {
        log.error("查询数据失败", e);
    } finally {
        if (table != null) {
            table.close();
        }
    }
    return null;
}
```

画面 10 代码：
```java
//根据表名以及 rowKey 获取一个对象
*
* @param tableName 表名
* @param rowKey 主键
* @param tClass 需要
