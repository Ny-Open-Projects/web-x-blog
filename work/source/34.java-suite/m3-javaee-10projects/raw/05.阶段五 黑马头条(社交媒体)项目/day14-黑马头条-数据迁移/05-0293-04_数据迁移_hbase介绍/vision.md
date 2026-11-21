# 画面线理解：04_数据迁移_hbase介绍

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\04_数据迁移_hbase介绍【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 02:39, 03:23, 05:08, 06:33, 06:55, 07:15, 07:41, 08:50, 09:01, 09:11, 09:25, 09:33, 09:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:01:51

1) 这一组画面整体在讲什么（一句话）：
讲解 HBase 基础概念、集群搭建、命令行操作及 Java API 开发。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示文件资源管理器，当前目录为“day14”，包含 HBase 相关文档和安装包。
画面 2: PDF 文档第 1 页，介绍 HBase 是建立在 HDFS 上的高可用、高性能、列存储、可伸缩、实时写入的数据库系统。
画面 3: PDF 文档第 2 页，展示 HBase 表结构示意图，说明 Row Key 用于索引记录，数据按 Row Key 排序。
画面 4: PDF 文档第 3 页，讲解 HBase 表的列族（column family）概念，强调列名以列族作为前缀。
画面 5: PDF 文档第 4 页，介绍 HBase 中的“时间戳”概念，说明每个 cell 都包含时间戳。
画面 6: PDF 文档第 5 页，讲解 HBase 集群搭建步骤，包括上传 zookeeper 包、配置 hbase-env.sh 和 hbase-site.xml。
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
        <name>hbase.zookeeper.quorum</name>
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
    conf.set("hbase.zookeeper.quorum", "weekend5,weekend6,weekend7");
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
