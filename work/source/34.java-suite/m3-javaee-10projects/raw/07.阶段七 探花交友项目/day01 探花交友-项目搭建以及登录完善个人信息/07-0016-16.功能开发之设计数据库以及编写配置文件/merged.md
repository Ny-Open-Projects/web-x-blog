# 16.功能开发之设计数据库以及编写配置文件

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\16.功能开发之设计数据库以及编写配置文件_【海量资源尽在 666java.com】.mp4
- 时长 7分17秒（音频 433s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来把我们的数据库啊创建出来那么以及我们编写我们的配置文件啊那么我们数据库呢使用的是mycircle数据库那么我们呃暂时呢先用到两张表那我们把这两张表呢先创建出来那么这两张表呢我们就放到这个位置吧这是之前所创建的一个表那我再来一个吧再来一个数据库比如说我叫my什么呢看花
[00:26] 然后呢制服级呢我们采用的是这个U8然后呢我们来找到这个麦炭花在这里好然后呢我们把这个打开然后呢我们把它呢把这两个吧拷贝过来我们来看一下那我们有两张表那么一张表呢叫做什么呢TB user那么这张表里面有什么呢有ID组件
[00:55] 有我们手机号有密码其实这个密码其实没有也可以的因为我们是直接通过验证码去做一个登录但是为了扩展我们后续的业务的话我们还是预留一个密码的制段当然了密码的存储都是需要进行加密的比如说可以使用MD5在那个加密那么有create和update两个通用性的一个制段
[01:20] 那么其中呢我们这个主键是我们的ID然后呢我们给我们的这个Mobile然后呢去设置一个我们的一个索引那么因为根据手机号查询会比较多好那么这个是用户表那么下面还有所对应的就是一个用户的一个信息表那么这个表中呢我们可以看到有很多的一些字段包括有这个昵称用户的头像性别年龄学历居住的城市
[01:50] 生日等等一些这个字段好嘞那么其中我们给我们的这个表的这个UID去创建一个这个索引好那我们来执行一下那么这两张表就应该就创建好了来刷新一下那么可以看到是不是两张表已经就OK了对吧但是现在并没有数据并没有数据那么到目前为止我们这个表结构是不是就已经搞定了那么接下来我们就来编写
[02:20] 我们的这个SSO系统的一个配置文件那么我们需要在我们的这工程中呢去创建一个application啊publish这样的一个配置文件那我们来找到我们这个工程那么这工程呢是在这找到src下面有一个resource然后呢我们在这个下面去创建一个文件叫做applicationpublish文件那么这个呢就是submit boot啊呃标准的一个配置文件了
[02:47] 那么我们把一些配置项呢丢在这个里面来那我们来看一下啊那么这两个呢属于Spring Boot的一个标准的一个配置对吧好那么这个就不做过多的这个解释了那么这个叫什么呢Mai ID Cast应该叫ID Cast这样吧那我们就要看花吧不加那个Mai了啊然后呢下面这个配置呢其实是我们的什么呢连接池的一个配置数据源那个配置
[03:16] 那么要注意的是在这个位置呢我们所连接的我们的数据库呢加一个什么呢mine探花啊然后呢下面的是用户名和密码是rootroot好嘞好这个是我们的数据库的连接信息的配置然后呢下面这个配置呢是mybetis啊plus插件的一些配置那我们可以配置这个美举的扫描包啊以及我们这个表明的一个前缀tb那么刚才我们这个表其实可以看到
[03:45] 表明都是以tb下滑线是不是开头的所以说我们在这个位置指定它的一个表明的前缀就是一个tb下滑线然后我们设置我们 id的一个自增的一个策略是一个auto就自增长ok好我们把这个也拷贝过来那么往这一丢这都是一些常规的一些配置那么这个包目前我们是不是还没有我们先把这个包给它创建出来
[04:14] 就创建到这这是我们去放我们这个美举美举用在哪里呢大家可以看一下比如说我们像我们这个性别是不是就可以用美举这样的一种类型比如说在这个下面是不是有一个这个性别对吧那么就可以用美举了OK好那么接下来呢我们来配置我们的redis相关的一些这个配置项那我们把这个也拷贝过来然后呢我们把它
[04:42] 丢在这个位置那么在这个配置中其实我们配置了redis的一些集群的配置那么比如说我们配置的cluster nodes是不是就是我们所配置的一些节点什么6379,6380,6381等等三个节点是不是前面我们所搭建的redis的集群然后下面这个是指定集群的一个最大跳转速是5ok好那么
[05:08] 这个呢就是也是一个常规的一个配置那么下面呢我们再来配置我们的RocketMQ的一个配置那么来看一下那么在这个位置是不是我们所配置的是一个Nameserver就是我们的9876就是31.81这个机器的9876然后呢我们的这个就是提供者对吧它的一个分组呢叫探花这样的一个配置OK这两个配置也是一个比较常规的配置了
[05:36] 然后在下面的这个是怎么配置呢这个是我们在生成我们token的时候我们是不是要用到JWT我们去设置了我们的一个字幕创那么secret或者说我们这个是生成我们的一个token的一个盐对吧但是要注意这个字幕创一定要保护好不能把它泄露出去如果把它泄露出去了那么你的那个token的生成那么别人很容易得到一个伪造了这一定要注意这个不可以泄
[06:05] 进入出去的那么这个字幕创是怎么来的呢其实我们就是这个上面这个itcast下滑线探花做一个MD5加密之后的这样的一个字幕创那么大家可以根据你项目的一些这个需求去改变这个字幕创大家别跟我都写的一样那么当然你学这个项目就可以的但如果你真正以后做自己的项目的话那么这个是不能够这样去写的ok好那么下面我们把它也拷贝过来这个是什么配置
[06:34] 这个是我们这个关于这个红软相关的一些配置那么这个我们在后面会讲到我们的人脸识别那么这几个配置会用到当前这个里面都是信息这个没关系到后面呢我告诉大家怎么样能够找到具体这个信息那么后面我们再把它填回来就可以了那么OK那么到这里呢我们是不是基本的一些这个外围的一些服务包括我们的一些这个配置呢都已经写好了那么接下来是不是就可以动手去写代码了
[07:03] OK好那么关于这个数据库的一个这个设计以及我们的一个这个配置文件的编写那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个 Spring Boot 项目（itcast-tanhua-ss0）的数据库表结构设计、配置文件编写及基础代码编写过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示 Typora 文档，内容为“3.3. 数据库表”，展示创建用户表 `tb_user` 的 SQL 语句。
- SQL 语句：
  ```sql
  CREATE TABLE `tb_user` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `mobile` varchar(15) DEFAULT NULL COMMENT '手机号',
    `password` varchar(32) DEFAULT NULL COMMENT '密码，需要加密',
    `created` datetime DEFAULT NULL,
    `updated` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `mobile` (`mobile`) USING BTREE
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';
  ```

画面 2：
- 显示 Navicat Premium 连接数据库的界面，左侧树状结构中选中了数据库 `mytanhua`。
- 数据库连接地址为 `127.0.0.1:3306`。

画面 3：
- 在 Navicat Premium 中，选中了 `mytanhua` 数据库下的 `tb_user` 和 `tb_user_info` 两个表。
- 表信息显示：`tb_user` 和 `tb_user_info` 均为 InnoDB 引擎，占用空间 16 KB。

画面 4：
- 显示 Typora 文档，内容为“3.4. 编写配置”，展示 `application.properties` 文件的开头部分。
- 配置内容：
  ```properties
  spring.application.name = itcast-tanhua-ss0
  server.port = 18080
  ```

画面 5：
- 显示 IntelliJ IDEA 的项目结构，右键点击 `src/main/java`，弹出创建新文件的菜单。
- 菜单中包含 Kotlin、Java、XML、YAML 等多种文件类型选项。

画面 6：
- 显示 IntelliJ IDEA 中 `application.properties` 文件的内容，包含数据库连接配置。
- 配置内容：
  ```properties
  spring.application.name = itcast-tanhua-ss0
  server.port = 18080
  spring.datasource.driver-class-name=com.mysql.jdbc.Driver
  spring.datasource.url=jdbc:mysql://127.0.0.1:3306/mytanhua?useUnicode=true&characterEncoding=utf8&autoReconnect=true&multiQueries=true&useSSL=false
  spring.datasource.username=root
  spring.datasource.password=root
  ```

画面 7：
- 显示 IntelliJ IDEA 中 `application.properties` 文件内容，下方有一个 Typora 文档的缩略图预览。
- 预览图中包含多个视频画面，其中一张显示了 `application.properties` 文件。

画面 8：
- 显示 IntelliJ IDEA 中 `application.properties` 文件内容，选中了 MyBatis-Plus 的配置项。
- 配置内容：
  ```properties
  # 表名前缀
  mybatis-plus.type-enums-package=com.tanhua.sso.enums
  mybatis-plus.global-config.db-config.table-prefix-th_
  # id策略为自增
  mybatis-plus.global-config.db-config.id-type-auto
  ```

画面 9：
- 显示 Typora 文档，内容为“3.4. 编写配置”，展示 `application.properties` 文件中 Redis 和 RocketMQ 的配置。
- 配置内容：
  ```properties
  # Redis相关配置
  spring.redis.jedis.pool.max-wait = 5000ms
  spring.redis.jedis.pool.maxIdle = 100
  spring.redis.jedis.pool.minIdle = 10
  spring.redis.timeout = 10s
  spring.redis.cluster.nodes = 192.168.31.81:6379,192.168.31.81:6380,192.168.31.81:6381
  spring.redis.cluster.max-redirects=5

  # RocketMQ相关配置
  spring.RocketMQ.nameServer=192.168.31.81:9876
  spring.RocketMQ.producer.group=tanhua
  ```

画面 10：
- 显示 IntelliJ IDEA 中 `application.properties` 文件内容，选中了 Redis 配置部分。
- 配置内容：
  ```properties
  # Redis相关配置
  spring.redis.jedis.pool.max-wait = 5000ms
  spring.redis.jedis.pool.maxIdle = 100
  spring.redis.jedis.pool.minIdle = 10
  spring.redis.timeout = 10s
  spring.redis.cluster.nodes = 192.168.31.81:6379,192.168.31.81:6380,192.168.31.81:6381
  spring.redis.cluster.max-redirects=5
  ```

画面 11：
- 显示 Navicat Premium 中 `mytanhua` 数据库的表结构，下方有一个 Typora 文档的缩略图预览。
- 预览图中包含多个视频画面，其中一张显示了 `application.properties` 文件。

画面 12：
- 显示 IntelliJ IDEA 中 `application.properties` 文件内容，选中了 RocketMQ 配置部分。
- 配置内容：
  ```properties
  # RocketMQ相关配置
  spring.RocketMQ.nameServer=192.168.31.81:9876
  spring.RocketMQ.producer.group=tanhua
  ```

画面 13：
- 显示 IntelliJ IDEA 中 `application.properties` 文件内容，选中了 JWT 密钥配置。
- 配置内容：
  ```properties
  jwt.secret=76bd425b6f29f7fcc2e0bfc286043df1
  ```

画面 14：
- 显示 Typora 文档，内容为“3.5. 编写基础代码”，展示 `SexEnum` 的 Java 类代码。
- Java 代码：
  ```java
  package com.tanhua.sso.enums;

  public enum SexEnum {
      MALE(1, "男"),
      FEMALE(2, "女"),
      UNKNOW(3, "未知");
  }
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
见上文第 2 点中各画面的要点。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- 画面 1、4、6、7、9、10、12、13、14 中的 Typora 文档标题分别为：
  - 画面 1：3.3. 数据库表
  - 画面 4：3.4. 编写配置
  - 画面 9：3.4. 编写配置
  - 画面 14：3.5. 编写基础代码
- 画面 1 中的架构图：
  - 上层：`注册登录`
  - 中层：`状态变更`
  - 下层：`RocketMQ`
  - 无明确指向关系，但结构上是自上而下的流程。

5) 不要评价画面美观，不要输出与课程无关的内容。
- 无。

