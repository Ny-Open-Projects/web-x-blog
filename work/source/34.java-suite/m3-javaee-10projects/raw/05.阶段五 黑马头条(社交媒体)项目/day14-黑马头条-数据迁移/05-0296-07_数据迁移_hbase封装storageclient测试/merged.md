# 07_数据迁移_hbase封装storageclient测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\07_数据迁移_hbase封装storageclient测试【海量资源尽在 666java.com】.mp4
- 时长 12分46秒（音频 766s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就继续讲刚才咱们是把这个HBase的一些方法大概说了说但是刚才也说了咱们在封装的时候其实咱们用它的时候并不多不要用的是HBaseStorageClient所以说咱们下面咱们就用一下它去创建一个表然后是数据然后还有咱们再去做一个查询好吧来咱们
[00:26] 首先呢你要想用它你得先去把它给注入进来hbhb storage client然后先注入下面你在这啊就可以去创建一个方法void然后是teststoragestor.de啊就是这么叫save date好下面呢咱们就可以去在这去加一个test然后呢你就可以去调用了啊说咱们调用里边的一个方法
[01:01] 爱的咱们就用第一个吧好吧第一个值呢就是一个表名这个表名咱们就叫叫他啊这个表咱们可以改一改啊说怎么叫什么space了叫什么来着前面再加一个吧好吧嗯这边加一个啊storage好加这么一个表面啊第二个呢二个的话是一个对象对象是谁呢这个对象啊是一个叫做嗯可以看一看啊看一看
[01:36] 是这么个对象叫HBaseStorage好,翻译出来等于你有一个HBaseStorage那它需要啥呢咱们可以看一下里边咱们可以去set首先有一个RowKey这个RowKey其实跟你之前离的RowKey是一样的名字你可以随便起比如说怎么叫StorageStoward然后是trow
[02:07] -0001无所谓随便写然后下面还有storage.有一个set做一个你不用管主要是设置一个datalist这个datalist是啥是一个集合好把它给创建出来创建出来之后你就可以把它给装进去但是这个数据你得去准备了准备什么数据把storage也放到这
[02:40] 准备什么数据看一看啊主要的是里边装的是storage date我们叫storage date,new一个storage date好这里边数据有一个非常关键啊来看一下,点有一个set有一个叫做arget class name这个这个你不能随便设咱们用的时候就不能随便设了用的它呢就是你这个的返回值这个的返回值,当然你查询的返回值啊
[03:09] 查询的时候管理值又说你需要往当前的某一个class里边某一个实体类里边去设置那怎么设置呢咱们一会再说但这个类啊咱们先去确定一下比如说我想往里边去存一个AP article我们可以把它的全类名按一下啊全类名跑进来然后呢看一下然后看他还有什么属性storage date.set一个叫做country list
[03:39] 好那这个Entry List可以看一下这个又是一个集合好吧来拷贝一下拷贝完之后可以再再再往下看这个Entry List它很显然就是需要去创建一个Storage Entry然后是Entry等于New一个Storage Entry然后你看Entry里边需要去做啥set一个key和value这个key value我跟你说一下set value这个key和value
[04:12] 就应该这是你的什么这是你的属性名称然后呢这是你的值也就是说咱们应该对应列组里边的这是它的列这是它的值好吧这是列组这是它的列这是它的值那它的列有啥呢当然你可以随便领引无所谓但最终咱们要去返回正常返回的话呢你最好是跟你的AP article这个列要对应上你看比如说我设一个title设一个title
[04:44] 这个title这个文章的名称是啥呢比如说咱们叫数据迁移然后呢然后咱们可以再再设一个再设一个的话你需要去再拷贝一个比如说咱们设置一个ID这个ID然后这个是ID的话123456是2错了2行那这样的话咱们就设置完了设置完之后你得去把它给装进来
[05:13] 当然你装它的时候呢你别忘了entry list.add你把它两个entry装进来entry list.add entry好吧行那这样的话就可以了啊那里边还少一个东西还少一个啊这个date list里边呢你也要去装进去.add当前的哪个呢是storage我看啊应该是storage date行那这样的话咱们就
[05:48] 但是安装完了应该是组装完了组装完之后你说这个表没有你是不是得先创建表OK你看这个方法里边它就会先去检查表这个里边是有一个create table是吧其实这个里边你可以看一下封装的时候会去先去判断这个表到底有没有没有的话就会创建有的话就不会创建了
[06:12] 明白意思吧所以说这个表即使是没有也没事他也会帮你创建并且他会告诉当前表的列足就是这个东西再说一遍这是列足然后这个是rokey这是表名他的key和value就是当前的看到了吗这只是一个对象一个对象的追击出来的现在咱们下面就可以去测试一下在这打断点咱们看一下servit里边的值全不全好吧右键走debug
[06:44] 我稍等一下啊在加载环境好马上结束啊看一下看看这个能不能存进去或者说咱们打断点了啊咱们看一下这个sourcet的数据全不全你把手标放到这也行啊好看一下你看这个是rokey然后呢往下看啊这里边呢是有一个这叫什么ap article是吧这是他叫什么列足是吧列足里边呢是有两个字段分别是key是title还有一个是id是123456
[07:14] 没问题吧好那咱们就直接放行好看一看放行完之后呢看看是不是保存成功了对吧没问题啊这时候呢你就可以在这去查看一下list这时候是不是又有一个新的这种列这叫保名啊好没问题啊那这时候呢你就可以去查看了那你可以在这查看啊你可以在这查看你也可以用代码去查看咱们一般情况都用代码去查看是吧你就是去查找当前的数据那怎么查呢来
[07:45] public void teststoragegetget的话首先在里边再去再一个test你就可以调用当前的方法有一个点有一个getget的话我们是用当前的第一个第一个就是你的表还是这个表然后第二个是谁
[08:22] 这个的话就是你的LoadingT就是Lookie写完了吗这是引号这里边还有一个参数这个参数是谁呢是一个class这class就是APArticle的classAPArticle.CRclass它最终返回的就是一个APArticle好对象拿到之后咱们可以打印一下APArticle
[08:53] 那行咱们先看结果一会咱们再去分析那为什么这么着可以可以去直接获取到当前那个类型好吧好直接去执行底bug往下走好看一下能不能把这个数据给打印出来来看一看好结束了钻点我这之前加的放行好来看一看最终的数据有没有你看第一个是什么123456
[09:29] 另外一个是数据迁移是不是把article toString打进去了是不是数据拿到了这个其实就是从哪拿的从当前的HBase中去拿的这个为什么会这么做其实咱们只是在这去做了一个微型的封装一个简单的封装那这封装的方式也可以看一下比如说开它然后你传入的其实就是个class
[09:54] 它会去强转成这么一个类型去返回也就是说你传入啥它就是什么类型但是这样的话呢你得去往里边去设值怎么设呢你可以看啊中式到这可以看关键代码啊首先呢它会往里边去设个class然后呢它就会一个一个属性的去往里边去设置好吧但这个代码其实还不是最关键的最关键的是在这啊往下走主要呢是这一段啊
[10:28] 这段其实是用到了反射首先是通过反射是把你的class给new出来new出来之后它就会往里边去设值这里边有个工具类这个工具类叫defect是吧这里有个usus这个工具类咱们之前是用过的往里边去设值那设什么值就是往这个对象就是你new出来的对象里边有一个key和value这个key和value其实就是从哪里查的
[10:54] 就是从HBase中去查的然后拿到你的属性然后是给你的属性复值你看这里边虽然这两个是有值但其他的属性是不是也有是吧但是其他属性都是那没有值看到了吧好了那这个咱们就做完了刚才的一个是算是一个新增一个新增一个是啥呢一个是查询那这个新增再去说一下这个新增的一个关键点其实这里边就要去设置它的什么它的一个列足这个列足要对应上你的一个实体类
[11:24] 就是你接收的实体类也就是说你往里边去设置的时候你不能随便设必须干嘛呢必须给你的当前的这个实体类的字段一定要对应上如果对应不上的话那你是吧那你以后再去获取数据的时候这一块获取数据的时候那还能封装吗肯定就封装不上了好吧那行那这个咱们就这个保存就说到这当然这个保存还有一个功能它呢这个表别管存在不存在
[11:50] 他都会去执行成功因为呢有的话他就会用没有的话他就会创建这个表好吧当然这个下面这个方法呢就是查询那查询的话呢里边呢就是根据当前的表名入key还有你的class一块去查询就可以了好吧这里边其实还有一个方法啊咱们可以看一下啊按它开里边呢是有一个叫做他是吧你可以去传入一个list咱们刚才用的这个啊你也可以传入多个class
[12:20] 多个class它也会返回多个class好吧你看下面去获取的时候你可以往下看往下翻往下翻这是获取一个是吧他们下面也有一个获取多个的也是返回的是一个list集合好吧也就是说查询单个或插入插入单个还有多个都会都有对应的方法好吧那行那这个就是storage client

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

