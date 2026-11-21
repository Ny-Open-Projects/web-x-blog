# 05_数据迁移_common模块整合hbase

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\05_数据迁移_common模块整合hbase【海量资源尽在 666java.com】.mp4
- 时长 7分19秒（音频 439s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就在项目中去集成一下HBase和MongoDB首先咱们先去说一下当前的HBase因为想去加上HBase你要在common中去集成咱们都是在common中去集成那这集成的方式也要比较简单首先你要去准备一个HBase的progress把这两项输进去当然这一下要根据你自己的环境和自己的这种什么HBase的地址去设置
[00:30] 行那这个加上之后你可以看一下我这边已经加完了你可以看一下当前的它这有一个它好这两项加进来是吧然后你需要在当前的这种资料中资料资料中有一个叫HBase你把它统一拷贝一下拷到哪呢拷到当前的这个在当前的common下边创建一个HBase然后你把这些类的统一都拷过来
[00:58] 那拷贝之后呢就有那么多类啊就有那么多类啊那咱们可以简单去看一下当前的这些类啊首先呢咱们可以看一下这当前这个什么HBaseClient打开那这个呢其实就比较简单了啊它就是一个配置类对吧然后呢然后它是去往当前的Spring中去注入了一个东西就是谁呢就是当前的什么HBaseClient这个加了个SB
[01:22] 是吧咱们最主要的其实就是拿到当前HBase Client然后去操作当前的HBase好吧行这几项其实都是去注册地址还有超时时间的设置行其他的话就没有太多东西咱们可以再往下看那就说完之后这里边还有一个叫做HBase Client这个类比较大这里边有几十个有什么有700多行代码
[01:51] 没有800行将近800行代码这个代码其实都是当前的HBase Client然后你可以看一下这里边其实就是去调用或者说去连接了当前的这种HBase首先你看这是一个连接是吧然后然后他就会去设置一些方法那这些方法咱们可以简单看几个首先是检查这个表是否存在这个表然后往下
[02:20] 往下的话就是你可以去创建表但是创建表的时候你可以看一下它最终都是会去调用一个叫做找找这是表名是吧这是列足咱们可以看一下它到底是到底是去调哪个方法这有一个叫做correct看到了吗等一下这个其实就是去创建的表这个底层它咱们看不着了叫咱们主要是封装了这么一个类但是你这个东西你要知道就可以了
[02:53] 然后再往下看呢是有一个这种预分区的创建表这也是创建表啊然后再往下看啊看还有啥嗯这是获取所有的表获取所有的表信息啊然后还有吗看看啊还有没有这是查询数据库中所有的表名对吧当然这个根据这个表名去查询它的其他的表名啊然后呢是什么便利查询指定表中的所有数据啊这是
[03:26] 根据表明去查询所有的数据啊咱们也可以去查询还有呢就是咱们找一个有用的啊咱们一会会用到的啊往下找找嗯这是查询看到了吗这是查询当前的根据过滤条件还有表呢去查询当前的数据然后再往下看啊这是精确查询这个咱们会用啊一个是啥呢根据当前的
[03:53] 你表和rooting key和rokey去查询咱们的数据好吧这个咱们会用得着然后的话再往下看看看就这个这个是不是这个咱们会有一个新增找下新增有一个put date这个其实你看一下第一个是表名第二个是rokey第三个是列组第四个是列组里边的这种列然后还有什么呢列所对应的值
[04:26] OK啊那这个咱们也会一会呢也会用到好吧一会也会用到啊那行那这个就说到这啊你也可以去自己去看一看用到哪个的时候呢你可以去调用哪个方法你大概知道哪个方法是什么意思或者有什么作用就可以了好吧那行那这是一个比较原生的啊咱们比较原生的一个封装当然那你说真正用的时候呢其实咱们咱们也可以不用它用谁呢
[04:49] 用当前那个HBaseStorageClient用第二个Client这Client呢他呢咱们也是去封装了那封装完之后呢是结合咱们的项目或者说结合咱们的迁移的方案呢是做了一个再一次的封装你看这里边是注入了当前的HBaseClient就是他就是刚才咱们看这个列啊然后呢他就去封装了一些东西比如说咱们去添加数据是吧你只要去传这些就可以了那这是啥呢
[05:18] 咱们一手在说好吧还有什么呢还有也是添加是吧这也是添加下面还有应该还有一个获取是吧根据什么什么获取咱们也可以去获取这咱们用到用的比较多的呢其实就是一个添加一个获取像修改和删除呢咱们一般也是不用的啊像HB4的数据呢咱们一般也不会去删除好吧那行那这几个了呀你知道像是有什么作用
[05:43] 咱们一会用的时候你有印象然后是咱们能够调用API去存储或者去获取数据就可以好吧大家里边还有一些东西比如说这有个constance这个是一个HBase咱们定义的一个这种那么长量就是一个表面刚才说了咱们整个天衣方案就只有一张表就是这个表咱们这个表面已经写好了然后下面还有一些东西这是真正存储数据的
[06:10] 这个数据是这样主要是存两个第一个是当前的周期然后第二个是当前的列足你要获取列足这个就是刚刚咱们说的又再一次封装的client类他用到的一个东西你可以看一下你看他这个什么HBase storage是不是这里边又再次去封装了这里边封装的东西刚才说了其实就是啥呢一个是rokey
[06:35] 嗯一个什么呢一个是列足啊主要是这东西啊当然你也可以去设置一些毁掉它去做用于增强当前这个类的一个效果好吧嗯那行那这个呢就是咱们这个整合之后啊整合之后所有的东西当然我再去说一下啊你需要去做的事就是把当前的这些东西准备一下然后呢然后就是你需要把这几个类给考过来给考过来啊知道大概这几个类是什么意思就可以好吧
[07:02] 但是里边有一个一直没有说就是当前的pop文件里边其实发给你们的pop文件已经包含了当前的什么hbase相关的jar 包这东西咱们就不用再讲了行咱们关于整合咱们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 HBase 的 Java 项目中，如何通过配置文件初始化客户端、创建表、删除列族、查询数据以及封装存储对象的代码实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示项目结构，选中 `HBaseConfig.java` 文件。
画面 2: 选中 `HBaseConstants` 类，准备查看其内容。
画面 3: 展示 `HBaseConfig.java` 代码，包含 HBase 配置项如 `ZooKeeper.quorum` 和 `client.keyvalue.maxsize`，以及创建 `HBaseClient` 的方法。
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
@Value("${hbase.ZooKeeper.quorum}")
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
    org.apache.Hadoop.hbase.client.HBaseConfiguration hBaseConfiguration = getHBaseConfiguration();
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

