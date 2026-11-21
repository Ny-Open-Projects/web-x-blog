# 04_数据迁移_hbase介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\04_数据迁移_hbase介绍【海量资源尽在 666java.com】.mp4
- 时长 9分51秒（音频 591s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就继续往下讲然后下面咱们要讲啥咱们讲的是一个这种HBase的一个东西咱们可以简单介绍一下你可以打开今天资料中有一个叫做HBase的PDF我打开了就是它然后这里边是去介绍了一下HBase咱们可以简单去读一读说是HBase是一个Bigtable开源的driver版本是建立在HDFS之上的提供高可靠
[00:27] 高性能列存处可伸缩实时读取的No Circle的数据库系统它是一个No Circle的数据库系统好吧它是介于什么No Circle和RD-RD BMS之间仅能通过主键Low Key和主键的Linge来检索数据其实咱们大部分时间都是在通过主键去检索好吧当然这个里面是还有仅支持单行数可通过Hive
[00:54] 支持来实现多表招引等复杂查询咱这个Hive咱们没有学过这是大数据相关的东西但是这个HBase它是一个数据库这你知道了它就是一个No Circle的数据库好吧当然咱们再往下看它还有什么特点可以往下看说主要用来存储结构化和半结构化的松散数据松散数据然后HBase查询功能很简单不支持招引等复杂查询不支持复杂的事物它只是行级的事物
[01:22] 好那它存储的类型呢OK啊你可以看一下它只有一种叫Bite数组它只能存这个Bite数组好吧它呢是与Hardware一样HBase目标主要是依靠横向扩展这个就是它横向扩展的意思呢就是说我可以不断的去增加服务器来去增加我的这种储存的容量是吧那这个呢其实呢它是可以存储很多东西啊很大的容量啊咱们可以看一下下面的特点说大
[01:50] 第一个是大一个表可以有上十亿行上百万列这个数量还是挺大的还有是面向列这里边有一个列组的概念它是可以面向列组的存储和权限控制主要是列组列组是独立检索的还有一个是稀疏这个其实说你可以对于为空的就是为浪的列并不占用存储空间因此表可以设计的非常稀疏
[02:19] 这是它的一个特点特点的话其实你记住一个就是一个表可以存可以有上十亿行或上百万列其实咱们今天的黑马头条里边做迁移咱们一共就创了一张表一共就创了一张表咱们所有的数据都是从这一张表中去查询或者叫查入好吧那行那这个咱们就HBase大概做个了解好吧然后接着往下看里边其实还有一些这种什么呢
[02:48] 有一些这种算是概念咱们就要去听一听首先是有一个表结构逻辑视图它也有表这个表跟咱们之前的页的表是差不多它也有行和列但是这里边是有一个若干个列足列足叫column family是吧families是吧ok就它这个就是
[03:12] 就是什么有很多个列组这个列组咱们一会会去大概去说说下这个概念下面会去讲到这是你首先要知道它是有表的有表然后有表的话就有行就有行这个行你看这叫rokeyrokey的话意思就是当下怎么其实这不是这不是行这是什么这是一个主件ok这是rokey是用来检索基度的什么主件主件
[03:39] 行这个你就知道就可以了咱们一会去在黑马头条里边去检索的时候主要用的就是当前的周期当然你保存数据的时候也要去指定他的rookie是啥好吧这个概念你要知道ok然后再往下看这有个列足这列足是这样你再去创建表的时候在一生前表的时候你要去指定当前的表有什么列这个列的话有可能会有多个因为他要列足所以说你要你可以去指定多个列
[04:09] 也可以说指定多个列组都是可以的好吧这个列组呢你必须在创建表的时候必须指定但是你查数据的时候呢你可以每次查数据去指定当前的rook因为它可以检索某一条数据是吧但是你创建表的时候你必须告诉他他有什么列那他有什么列啊这个列列组啊你看可以读一下啊说被此表中的每一个列都归属于什么某个列组列组是表的scammer的一部分
[04:36] 而列不是列族里边包含了多个列可以包含多个列好吧那必须是干嘛呢必须在使用表之前定义也就是说你创建表的时候必须定义出来你说我后边再定义吧不行好吧这个你要知道列名都可以列族作为前备你看前面这个就是列族它里边有啥呢有当前黑色是吧还有什么Mars是吧像那些都属于什么Cost这个列族
[05:05] OK这个你要能够明白行再往下看好一个时间戳这个时间戳咱们也可以读一读说HBase中通过Row和Columns确定为一个什么的存储单元为SERV每个SERV都保存着某同一份数据的多个版本比如说你去指定了某一个Rowkey和某一个列组里边的数据但是你这个数据已经插入了很多条但是很多条的话
[05:35] 也没事啊咱买色够多你多条可能不行是吧但这个拆多条也没事用啥呢因为他时间圈是不一样的哎时间圈是不一样的每插入一条数据呢他都会有一个自己的时间圈好吧那并且你看啊那每一个sales中啊不同版本的数据呢是按照时间倒序进行排序的哎既既然呢最新的数据排在最前边好吧
[05:59] 那行那这当然这个这里边也有一个最大的时间和最小的时间就是说他这个你可以设置这个时间中的次数好吧行那这是一个还有一个sale这就是单元格是吧你可以去去你可以按照这个列把rokey什么column是吧你的列你的你的你的rokey什么好你的列好你的版本来确定一个什么单元好吧那这个单元的话你看这个单元数据是没有类型的全部是字节码形式
[06:27] 全部是自解码行这个概念咱们就说到这按照下面还有一些东西咱们可以往下看里边有一个集群是吧集群的话就告诉你你该怎么去安装当前的什么当前的HBase当然你要想去安装HBase你首先得有一个Zoho Keyboard环境然后还得有一个叫做Hadoop环境然后这时候有这两个环境之后你就可以去安装HBase安装起来非常简单直接解压就可以
[06:55] 当然这里边文档都可以看一下我这边已经弄完了我也不再去讲了你可以参考一下文档或者在百度上去找一找都可以好吧然后下面还有一些东西就是你安装完之后这里边会有一些命令你就可以去在命令行上去操作当前的什么这种HBase比如说这里边有list你可以去查看所有的这种表是吧你可以打开你看我这然后咱们可以去拷贝一下这个东西
[07:26] 叫点HBaseShare点我这操作不了了是吧连不上了连不上就不连了就好像是断了没事我把这个网线给插上稍等好网线插上就好了你可以点H什么Base然后这有一个叫做Share好吧对吗我看看点HBase
[08:11] 你得先去到当前的目录usr有一个local到当前的Hadoop然后当前的什么cd是base里边然后是找到当前的hbase然后到里边之后你到目录到这个b目录然后是点hbase然后是干嘛然后是这个就能去连上了这算是客户端
[08:42] 放在联想之后你就可以去跳一个命令这个命令是叫做list你就可以去查看所有的你看目前我这里边存在的表就是几个第一个是他然后第二个是他三个是他好吧一共是四个一共是四个当然这里边还有一些东西比如说你可以去创建表是吧创建表的语法你还可以干嘛你还可以往里边去查数据你还可以干嘛你还可以去获取数据
[09:07] 是吧当然下面还有些删除还有些删除你都可以去看一看你看还有查找这些他都有好呗但这个咱们用的不多用的并不多这也只是在这种命令行上去执行是吧用的不多哪个用的比较多下面会有一些这种加入代码可以往下看往下翻翻到最后往下翻这边是有一个这种加入代码的开发里边会去介绍当前的什么增伤改查
[09:34] 增长改查你也可以去瞧一瞧也可以去看一看好吧那行那这个关于HBase这块咱们就不多说了关于这个增长改查咱们也一会儿也会在黑马头条里边咱们的项目里边也会去简单的去演示一下好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 HBase 基础概念、集群搭建、命令行操作及 Java API 开发。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示文件资源管理器，当前目录为“day14”，包含 HBase 相关文档和安装包。
画面 2: PDF 文档第 1 页，介绍 HBase 是建立在 HDFS 上的高可用、高性能、列存储、可伸缩、实时写入的数据库系统。
画面 3: PDF 文档第 2 页，展示 HBase 表结构示意图，说明 Row Key 用于索引记录，数据按 Row Key 排序。
画面 4: PDF 文档第 3 页，讲解 HBase 表的列族（column family）概念，强调列名以列族作为前缀。
画面 5: PDF 文档第 4 页，介绍 HBase 中的“时间戳”概念，说明每个 cell 都包含时间戳。
画面 6: PDF 文档第 5 页，讲解 HBase 集群搭建步骤，包括上传 ZooKeeper 包、配置 hbase-env.sh 和 hbase-site.xml。
画面 7: PDF 文档第 6 页，介绍 HBase 命令行基本操作，如进入 shell、列出表、创建表、插入数据。
画面 8: SecureCRT 窗口显示 hosts 文件内容，包含多个主机的 IP 地址和域名。
画面 9: SecureCRT 窗口显示在 HBase 环境下执行命令，列出表并创建测试表。
画面 10: PDF 文档第 6 页，再次展示 HBase 命令行基本操作，如创建表、插入数据。
画面 11: PDF 文档第 7 页，展示 HBase 命令行中获取、插入、扫描数据的命令。
画面 12: PDF 文档第 8 页，展示 HBase 命令行中扫描数据的更多命令，如按列族、时间戳、前缀过滤。
画面 13: PDF 文档第 9 页，展示 HBase Java API 示例代码，用于创建连接、删除表、插入数据。
画面 14: PDF 文档第 10 页，介绍 HBase 过滤器，列出比较运算符和过滤器类型。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6:
(1) 上传 hbase 安装包
(2) 解压
(3) 配置 hbase 集群，要修改 3 个文件
注意：要修改 hbase-env.sh 和 core-site.xml 及 hbase-site.xml
(3.1) 修改 hbase-env.sh
export JAVA_HOME=/usr/java/jdk1.7.0_55
//配置 hbase 使用外部的 zk
export HBASE_MANAGES_ZK=false
(3.2) 修改 hbase-site.xml
<configuration>
    <!-- 指定 hbase 在 HDFS 上存储的路径 -->
    <property>
        <name>hbase.rootdir</name>
        <value>hdfs://hbase</value>
    </property>
    <!-- 指定 hbase 集群分布式 -->
    <property>
        <name>hbase.cluster.distributed</name>
        <value>true</value>
    </property>
    <!-- 指定 zk 的地址，多个用 “,” 分别 -->
    <property>
        <name>hbase.ZooKeeper.quorum</name>
        <value>master01,master02,slave01</value>
    </property>
</configuration>

画面 7:
进入 hbase 命令行
./hbase shell
显示 hbase 中的表
list
创建 user 表，包含 info、data 两个列族
create 'user', 'info', 'data'
向 user 表中插入人信息，row key 为 r0001，列族 info 中添加 name 列标识符，值为 zhangsan
put 'user', 'r0001', 'info:name', 'zhangsan'
向 user 表中插入人信息，row key 为 r0001，列族 info 中添加 gender 列标识符，值为 female
put 'user', 'r0001', 'info:gender', 'female'
向 user 表中插入人信息，row key 为 r0001，列族 info 中添加 age 列标识符，值为 20
put 'user', 'r0001', 'info:age', '20'

画面 11:
get 'user', 'r0001', (COLUMN => 'info:name', VERSIONS => 5, TIMERANGE => [15923878398, 15923878398184])
获取 user 表中 row key 为 r0001，cell 为 zhangsan 的信息
get 'people', 'r0001', (FILTER => 'ValueFilter', 'binary:{"name": "zhangsan"}')
获取 user 表中 row key 为 r0001，列标识符中含有 a 的信息
get 'user', 'r0001', (FILTER => 'QualifierFilter', 'substring', 'a')
put 'user', 'r0002', 'info:name', 'zhangs'
put 'user', 'r0002', 'info:gender', 'female'
put 'user', 'r0002', 'info:nationality', '中国'
get 'user', 'r0002', (FILTER => 'ValueFilter', 'binary:{"中国"}')
查询 user 表中所有信息
scan 'user'
直接获取 user 表中列族为 info 的信息
scan 'user', (COLUMNS => 'info')
scan 'user', (COLUMNS => 'info', VERSIONS => 5)
查询 user 表中列族为 info 的数据
scan 'user', (COLUMNS => 'info', RAW => true, VERSIONS => 3)
查询 user 表中列族为 info 中标识符为 name 的信息
scan 'user', (COLUMNS => 'info:name')
查询 user 表中列族为 info，列标识符为 name 的数据
scan 'user', (COLUMNS => 'info:name', VERSIONS => 5)
查询 user 表中列族为 info，列标识符中含有 a 的信息
scan 'user', (COLUMNS => 'info', FILTER => 'QualifierFilter', 'substring', 'a')
查询 user 表中列族为 info，rk 范围是 [r0001, r0003] 的数据
scan 'user', (COLUMNS => 'info', STARTROW => 'r0001', ENDROW => 'r0003')
查询 user 表中列族为 info 中标识符为 name 的数据
scan 'user', (FILTER => 'PrefixFilter', 'name')

画面 13:
@Before
public void init() throws Exception {
    conf = HBaseConfiguration.create();
    conf.set("hbase.ZooKeeper.quorum", "weekend5,weekend6,weekend7");
}
@Test
public void testDrop() throws Exception {
    HBaseAdmin admin = new HBaseAdmin(conf);
    admin.disableTable("account");
    admin.deleteTable("account");
    admin.close();
}
@Test
public void testPut() throws Exception {
    HTable table = new HTable(conf, "person_info");
    Put p = new Put(Bytes.toBytes("person_id_000001"));
    p.add(Bytes.toBytes("name"), Bytes.toBytes("zhangwu"), Bytes.toBytes("zhangwu"));
    table.put(p);
    table.close();
}

画面 14:
引言：过滤器的类型很多，但可以分为两大类——比较过滤器、专用过滤器
过滤器的作用是在查询端判断数据是否满足条件，然后只将满足条件的数据返回给客户端。
HBase 过滤器的比较运算符：
LESS <
LESS_OR_EQUAL <=
EQUAL =
NOT_EQUAL !=
GREATER >
GREATER_OR_EQUAL >=
NO_OP 目录所有
HBase 过滤器的比较器（指定比较规则）：
BinaryComparator 按字节顺序比较指定字节数组
BinaryPrefixComparator 按前缀比较数据是否相同
NullComparator 判断数据是否为空
BitComparator 按位比较
RegexStringComparator 提取一个正则的比较，仅支持 EQUAL 和不相等
SubstringComparator 判断数据的子串是否包含 value 值

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: 标题为“1. HBase 基础”，子标题“1.1 Hbase 数据库介绍”，内容包括 HBase 的定义、特点、数据模型。
画面 3: 标题为“3. Row Key”，内容包括 Row Key 的三种访问方式、排序规则。
画面

