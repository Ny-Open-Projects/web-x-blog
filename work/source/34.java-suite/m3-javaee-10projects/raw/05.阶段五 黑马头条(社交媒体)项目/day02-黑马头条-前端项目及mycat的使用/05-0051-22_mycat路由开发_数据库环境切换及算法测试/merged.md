# 22_mycat路由开发_数据库环境切换及算法测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\22_mycat路由开发_数据库环境切换及算法测试【海量资源尽在 666java.com】.mp4
- 时长 6分59秒（音频 420s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好各位那咱们下面的就来去测试一下当前写完的这个算法啊那测试之前的首先的我要把这个环境稍微调整一下目前的咱们买色口是安装到了本地的买色口上面是吧所以说呢你这块内容的我稍微做了调整就是我本地用的是5.5的所以说这个呢可能到后期可能会出问题所以说呢咱们在这块啊
[00:25] 直接就改了改成5.7的啊买色口5.7的版本各位如果说不是的话呢不是5.7的版本你需要去把它重新安装一下啊当然这个安装的方式有很多种是吧你可以装到嗯windows上你也可以装到linux上当然我这块用的是一个win linux并且是用DAO口安装的啊这个DAO口咱们之前都都学过啊你只需要去拉一些镜像然后直接去把这个容器给启动起来就完事了啊你看我这块呢已经
[00:55] 在当前的Nux上安装了Docker安装上了当前的一个容器这个容器就是当前的一个MySQL它的装备号是333.6那这个安装完之后这会儿内容是要去改一些东西改哪呢改咱们的当前的MyCat因为这个MyCat你启动的时候还是连着之前的本地的系统那肯定是不行的所以说你需要在当前的Skymer的配置文件中打开
[01:26] 最下边最下边呢这有一个地址是吧这个地址的话我目前的地址就是我Linux上的一个地址或者说你到你门公司的某一台服务器上的地址我的段号是33306用户名和密码都是root和12346这个你的是啥那就写啥好吧行这个再强调一下用的是mycircle5.7以上的都可以OK行啊那这个改完之后啊那这时候咱们就可以启动当前的谁呀
[01:57] 当前的mycat好双击它那启动完之后呢咱们可以用narrowcat去连接一下那连接的方式其实跟之前差不多点一下比如说我起个名字叫什么呢叫mycat145好吧mycat-145然后这个还是logo host让mycat去连接咱们的Docker的145的mycircle所以说这块是端口多少8066后面是root密码是
[02:32] 123456这个对应上啊这个是不是也是在当前的某一个位置文件上去对应上啊咱们刚才是不是讲过了行这个这有个server啊主要是跟当前的server里边的你自己定义的当前的这种内容去定义上就可以了好吧这是呃用名这是密码行那这个咱们设置完之后可以测一下连接成功好点确定双击再双击
[03:02] 好这时候咱们所有的表啊都已经定义出来了这一共是117张表当然啊我刚才有个事忘了说就是说你换了数据库之后啊比如说这是我的145z的啊买色够的啊服务器是吧这时候呢你需要去重新去运行一下啊当前今天资料中的有个bak.sql你要把这个搜索链重新执行一下啊
[03:27] 这一下之后呢他创建了那么多库之后你再用麦凯特去连接啊这样的话你才能真正去查比如说咱们查一个article好稍等你看这个数据是不是查出来了行啊那咱们下面呢就来去测试啊刚才把这个环境简单说一说啊稍微去切换了环境啊那这个测试的话咱们分两种第一种的是工具测试第二种是呃有一个工具类去生成
[03:53] 那生成的话咱们一会再说先说工具啊那工具的话呢就是说咱们可以去查看某一些数据它到底是保存到了哪个节点上面保存到了哪个节点上啊咱们可以随便查怎么查呢你可以在这写啊比如说咱们就找一个嗯啊看他啊behave entry啊当前的一个行为实体类啊这个行为实体表啊这个表里边呢是有一个birth是吧
[04:22] 然后这里边有个1-1 2-1 3-2 4-2是啥意思刚才咱们讲什么意思就是前面这些是不是它的主件的后边这些就是它的分片的某一块是吧哪个分片哪个分片上这是第一个是吧这是第二个是吧行那咱们可以查一下咱们可以用那个Explan直接去查这个你可以在这写Explan然后后边是跟上你的搜索语句slot
[04:52] ID吧plum谁呢vpweirfirst比如咱们查两个第一个呢是1-1第二个呢3-2这时候呢他就能去查出来当前这个语句中的数据到底是存到了哪个节点上面你可以运行一下运用之后的效果其实在这已经写出来了大家看好啊这呢是有一个
[05:30] data not分别是在DNB11上一个是在2上看到了吧OK也就是说1-1呢其实咱们都知道是在1上3-2呢其实是在2上对吧那这样的话呢就能用explan直接去查找当前的数据到底是在哪个节点上面或者在哪个分片上面好吧行那这是一种方式啊咱们再来看第二种打开笔记
[06:01] 第二种说是咱们是有一个工具类叫BossUtils这个Utils其实已经在这了比如说你看这在你的Utils这个这个工程下边有一个common里边有一个BossUtils这里边是有两个方法一个是拼接当前的一个servePlan拼接的方式就是用杠ok下面是默认第一组咱们也可以去默认去第一组其实也是拼接也是去拼接当前的某一个东西这个东西
[06:31] 咱们到后期真正应用的时候咱们再去讲好吧目前的话咱们现在还暂时要用着你可以去再去设置一个Burst设置一个这样的字段并且你可以用着工具类去生成或者说去组成当前的某一个Burst字段到底是存在什么样的情况OK这个咱们后期用到的时候咱们再讲好吧行关于当前的这种Map文件咱们也不再说了因为它这个是对应上的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Mycat 分库分表中间件的配置文件结构、SQL 测试工具使用、Burst 字段处理逻辑及数据插入查询的实现方式。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 Mycat 的配置文件目录结构，包括 server.xml、schema.xml、rule.xml 等。
- 文档内容为“4.7 算法测试”章节，其中“4.7.1 工具测试”部分提到可通过 explain 关键字查询 burst 字段。
- 展示了在 MySQL 客户端执行的 SQL 示例：explain select id from ap_collection where burst in ('1-5','6-9')。

画面 2：
- 展示了 Windows 资源管理器中“conf”目录下的文件列表，选中了“schema.xml”文件。
- 右键菜单显示“编辑”选项，准备用 Notepad++ 打开。

画面 3：
- 展示了 Windows 资源管理器中“mycatWin”文件夹，路径为“C:\develop\mycatWin\conf”。

画面 4：
- 展示了“bin”目录下的文件，包括 dataMigrate.bat、mycat.bat、startup-windows-x86-32.exe 等。
- 展示了“wrapper-windows-x86-32.exe”文件的详细信息。

画面 5：
- 展示了“conf”目录下的文件列表，选中了“server.xml”文件。
- 文件列表中包含多个配置文件，如 schema.xml、rule.xml、sequence_db_conf.properties 等。

画面 6：
- 展示了 Navicat for MySQL 的界面，连接了名为“mycat-145”的数据库实例。
- 界面为空白，准备进行数据库操作。

画面 7：
- 展示了 Navicat for MySQL 中“mycat-145”数据库下的“day02”文件夹，选中了“bak.sql”文件。
- 弹出“打开”对话框，准备导入 SQL 文件。

画面 8：
- 展示了 Navicat for MySQL 中“mycat-145”数据库下的“heima-news”数据库的表数据。
- 表名为“ap_article”，显示了多条记录，包括 title、author_id、author_name、channel_id 等字段。

画面 9：
- 展示了 Navicat for MySQL 中“mycat-145”数据库下的“heima-news”数据库的表结构。
- 展示了“ap_article”表的 DDL 语句，包括字段定义和约束。

画面 10：
- 展示了 Navicat for MySQL 中“mycat-145”数据库下的“heima-news”数据库的表结构。
- 界面为空白，准备进行数据库操作。

画面 11：
- 展示了 Mycat 的配置文件目录结构，包括 server.xml、schema.xml、rule.xml 等。
- 文档内容为“4.7 算法测试”章节，其中“4.7.1 工具测试”部分提到可通过 explain 关键字查询 burst 字段。
- 展示了在 MySQL 客户端执行的 SQL 示例：explain select id from ap_collection where burst in ('1-5','6-9')。

画面 12：
- 展示了 IntelliJ IDEA 中“BurstUtils.java”文件的内容。
- 代码中定义了“split”方法，用于将数组拼接成字符串。

画面 13：
- 展示了 IntelliJ IDEA 中“BurstUtils.java”文件的内容。
- 代码中定义了“groupOne”方法，用于将数组拼接成字符串。

画面 14：
- 展示了 Mycat 的配置文件目录结构，包括 server.xml、schema.xml、rule.xml 等。
- 文档内容为“4.7 算法测试”章节，其中“4.7.3 程序-数据插入”部分提到在程序中要给对应表的 burst 字段赋值。
- 展示了 Mapper.xml 中的 SQL 语句，用于插入数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
- SQL 示例：
  explain select id from ap_collection where burst in ('1-5','6-9')

画面 4：
- 文件列表：
  dataMigrate.bat
  init_ok_data.bat
  mycat.bat
  startup-windows-x86-32.exe
  wrapper-windows-x86-32.exe

画面 5：
- 文件列表：
  server.xml

画面 9：
- DDL 语句：
  CREATE TABLE `ap_article` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '标题',
  `author_id` int(11) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章作者ID',
  `author_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '作者姓名',
  `channel_id` int(11) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '频道ID',
  `layout` tinyint(4) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章所属栏目',
  `flag` tinyint(4) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章状态',
  `label` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '标签',
  `collection` int(11) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '文章数量',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `idx_author_id` (`author_id`),
  KEY `idx_channel_id` (`channel_id`),
  KEY `idx_create_time` (`create_time`),
  KEY `idx_update_time` (`update_time`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

画面 12：
- Java 代码：
  public static String split(Object... fields) {
      StringBuffer sb = new StringBuffer();
      if (fields != null && fields.length > 0) {
          for (int i = 0; i < fields.length; i++) {
              sb.append(SPLIT_CHAR).append(fields[i]);
          }
      }
      return sb.toString();
  }

画面 13：
- Java 代码：
  public static String groupOne(Object... fields) {
      StringBuffer sb = new StringBuffer();
      if (fields != null && fields.length > 0) {
          sb.append("0");
          for (int i = 0; i < fields.length; i++) {
              sb.append(SPLIT_CHAR).append(fields[i]);
          }
      }
      return sb.toString();
  }

画面 14：
- Mapper.xml 中的 SQL 语句：
  <Insert id="insert"
          parameterType="com.heima.article.mysql.core.pojos.app.AppliesBehavior">
      insert into ap_likes_behavior (id, behavior_entry_id, entry_id, type, operation,
      create_time, burst)
      values
      (#(id), #(behaviorEntryId), #(entryId), #(type), #(operation),
      #(createTime), #(burst))
  </Insert>

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：
- PPT 标题：“4.7 算法测试”
- 子标题：“4.7.1 工具测试”
- 内容：“在mysql客户端工具中我们可以通过explain关键字查询sql会在哪些DN节点上执行。例：explain select id from ap_collection where burst in ('1-5','6-9')”

画面 14：
- PPT 标题：“4.7.3 程序-数据插入”
- 内容：“在程序中要给对应表的burst字段赋值，并在程序中拼接字段值，同时表主键的值需要在程序中生成（该项目中使用ZKSEQUENCE方式生成）。例：alb.setId(sequences.sequenceApplies()); //设置主键
alb.setBurst(BurstUtils.encrypt(alb.getId(),alb.getBehaviorEntryId())); //设置分片”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

