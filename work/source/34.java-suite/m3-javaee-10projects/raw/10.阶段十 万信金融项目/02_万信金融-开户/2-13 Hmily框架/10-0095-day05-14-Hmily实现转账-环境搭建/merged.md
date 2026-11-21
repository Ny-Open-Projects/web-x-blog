# day05-14-Hmily实现转账-环境搭建

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-13 Hmily框架
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-13 Hmily框架\day05-14-Hmily实现转账-环境搭建_【海量资源尽在 666java.com】.mp4
- 时长 9分1秒（音频 541s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们整体上了解了一下Harmony这个框架那接下来咱就要来一个快速入门的一个案例来用一用这个什么呀Harmony那这个案例呢也是大家最熟悉的一个案例就是咱们前面提到的过的这个谁啊对银行转账啊还是这个银行转账因为这个大家比较熟悉嘛那咱先把这个案例的这个业务我们再给大家明确一下啊虽然大家都非常熟悉了
[00:24] 让我再明确明确因为咱这个入门案例呢跟前面咱们提到过的那个转账稍微有点不太一样我们做了简化啊这个还是两个账户进行转账啊比如一个张三一个李四啊张三呢是在Bank1银行开的户啊李四呢是在Bank2这个银行开的户那当然了在我们这个案例当中呢Bank1和Bank2就是两个独立的什么呀微服然后这两个微服各自操作各自的数据库那么张三呢要给李四
[00:54] 转账那这里边是否涉及到分布式事务的问题呢这大家应该都清楚是不是肯定涉及到分布式事务的问题因为半颗一和半颗二是两个相互独立的什么呀微服务各自操作各自的数据库对不对当然我们最终的目的也是要保证这个转账这个里边涉及到每个操作要么都成功要么都什么呀都失败这是我们最终的目的那这个案例呢我们自然是要用
[01:24] Hemery这个框架来实现那么具体的话我们看看这个图这个时候咱前面见过吧对我们在讲TC的时候呢也是以这个图为例了但是呢我们接下来再用Hemery框架实现这个入门案例的时候我们做了简化大家看一下你像这个A这边检查这个余额啊包括冻结啊解冻啊等等我们就不再实现了
[01:52] B账户这边检查这个账户状态等等我们也不再实现因为咱这就是一个注门案例嘛我们的重点是研究这个Harmony这个框架是具体怎么使用的所以说咱业务上就简化了A这边就是扣钱B这边就是干什么呀对增加相对应的金额就行所以说呢这个例子还是咱之前一直提到过的那个转账的例子就是我们稍微做了一些简化这个大家给大家提一提你知道就行那这个
[02:21] 有需求我们搞清楚之后呢我们接下来首先要做的事就是进行环境搭建那环境搭建咱首先了解一下这个环境上的一些要求吧数据库JDK的版本我就不再说了大家自己看你重点要看的就是下面这一块我们这个引入了一些依赖都有哪些以及他们的什么呀这个版本这个你要重点看一看这是环境的一些要求吧那接下来咱首先要做的事就是把数据库环境给搭建好
[02:51] 数据库环境大家知道我们刚才这个业务场景里面是这样子的就是A和B或者就是张三和李四吧他是不是在分别在两个银行开头户那也就是说半可一和半可二是两个微服务嘛他们是不是各自操作各自的什么呀数据库是不是也就是半可一操作一个数据库半可二也要操作一个数据库所以说我们得把库还有库里边的什么呀表以及甚至一些测试数据对不对我们要提前给他准备一下
[03:21] 那这样呢有脚本啊大家直接粘到你的搜索项里边一执行就OK了你看我们这创建了一个Bank1然后Bank1里边呢创建了一个表就是账户信息表那你看我们这还创建了一个什么呀Bank2然后里边呢也有一个什么呀用户信息表那Bank1里边这是谁呀插入了一个测试数据张三然后呢Bank2里边是谁呀对是李四那这呢时间关系我就不再
[03:52] 给大家挨个执行了我这已经提前执行好了好你看这是半个一这是半个二两个数据库然后这个表里边你看这有一个我看的音负你看这里边我们插入一条初始数据张三的余额是多少钱对1万块钱万元户对不对1万块钱这是他的id number1然后半个二这个数据库里边也是一样的有一个表也叫康的音负这里边有一条初始数据叫李四对吧这个number是2
[04:23] 这个余额是零这个有点穷是不是这是大概的一个内容数据库里边的一些内容然后呢这呢特别提示大家我们前面在介绍Harmony的时候说过Harmony它在运行的时候是不是需要存储日志对不对这个日志呢对于Harmony它在运行的时候呢来说至关重要就这个地方不知道你还有没有印象这个日志对于Harmony来说非常关键那它呢支持各种方式来存储这个什么呀日志
[04:55] 你看redis也支持这个文件也可以对不对非关于营收据库关于营收据库都支持那我们这呢就用什么呀mycircle但是呢这个库呢不需要我们去建是由Harmony它自动就可以创建了其实刚才大家细心的话你应该能看到你看这这俩库其实这俩库不是咱创建的一会你就会发现不是咱创建的或者你下去自己再测试的时候你也会发现这两个表这两个表
[05:26] 不是库是这两个表其实他不需要我们去创建我们创建自己的库自己的表然后在咱的库里边呢他会自动创建这个存储日志的这个表每个这个库这边都会有这么一个存储日志的这个表我这个你不用管将来你可以观察一下这里面的内容这是数据库这一块我们需要做的一个准备工作然后接下来就是工程对不对我们的没问工程
[05:56] 这个没有工程的这一块是这样呃我就时间关系我就不再从头搭建从头把这个代码一行一行给大家敲了呃这呢我是代码已经写好了我就直接导进来大家看这这是我们整体的一个副工程啊副工程里边呢你看他主要是管理依赖了其实跟咱p2p那个整个结构是一样的大家看这这里边呢你重点看看那几个依赖就行了比如说黑美里对不对最重要的啊spin cloud啊
[06:27] 这都不用说了能不可是咱们以前都见过了其他的一些最基本的APIMySQL啊MyBallis啊因为咱这里边是不是涉及到操作数据库涉及到吗当然涉及到你转账嘛不都是要要进行增删改良的哪一种转账这大家应该比较熟了增删改良的都是修改是不是一边是加钱一边减钱嘛对不对所以你看这里边数据库操作相关的MySQL驱动MyBallis啊
[06:58] 这个数据库廉价值啊对不对等等这些都有说这是复工厂然后呢这个里边呢包含三个模块对不对我们虽然只是一个小小的转账功能但是咱说了这个麻雀虽小无脏巨险对不对我们这里边还是按照很规范的这个做法去做了啊你看我们这里边还有一个这是啥你看名字一看能猜出来这是啥玩意儿这是什么东西对这就是我们说的什么呀注册中心对我们说了嘛
[07:27] 虽然我们只是一个转账功能但是我们还是要搞一个注册中心这俩我就不用给大家过多介绍了吧一个Bank1的微服一个是什么呀Bank2的微服Bank1肯定是操作张三的那个余额了对不对Bank2肯定是操作李四的余额了那这呢我还想问大家一个问题这两个微服之间有没有调用关系就是有没有远程调用的关系他俩之间有没有业务上的联系
[08:01] 转账这个业务有吗我刚才说了这是操作张三的余额的这是操作什么呀李四的余额的这两位服之间有关系没有有啊那张三这边应该怎么着减钱是吧扣钱然后呢去远程调用Bank2让李四这边干什么呀对增加相应的金额所以说他们之间会通过Fain来实现一个远程调用只不过在整个过程当中呢我们加入了什么呀Hemily
[08:32] 来实现分布式的一个事务管理事务控制所以说这是这个咱这几个微服务它的整体的一个结构以及每个工程他们都负责实现相应的什么功能以及他们之间的具体关系这是咱们快速的把这个转账这个案例它的一些环境整体给搭建了一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Hmily 框架实现 TCC 分布式事务，通过创建两个银行账户（张三和李四）的转账业务来说明事务管理机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示 PPT 页面“3.3.1 业务说明”，内容为：本案例通过 Hmily 框架实现 TCC 分布式事务，模拟两个账户的转账交易过程。两个账户分别在不同的银行（张三在 bank1、李四在 bank2），bank1、bank2 是两个微服务。对于交易过程中的每个操作，要么都成功，要么都失败。
- 展示架构图：张三（bank1）→ 转账100元 → 李四（bank2），下方有“事务管理器（协调管理）”，并有箭头分别指向 A账户和 B账户。

画面2：
- 与画面1内容相同，PPT 页面“3.3.1 业务说明”和架构图完全一致。

画面3：
- 展示 PPT 页面“3.3.2.2 数据库”，内容为：创建 bank1 库，并导入以下表结构和数据：
- 代码块：
  CREATE DATABASE 'bank1' CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';

画面4：
- 展示 PPT 页面“3.3.2.2 数据库”，内容为：创建 bank1 库，并导入以下表结构和数据：
- 代码块：
  USE bank1;
  DROP TABLE IF EXISTS 'account_info';
  CREATE TABLE 'account_info' (
    'id' bigint(20) NOT NULL AUTO_INCREMENT,
    'account_name' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '户主姓名',
    'account_no' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '银行卡号',
    'account_password' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '账户密码',
    'account_balance' double NULL DEFAULT NULL COMMENT '账户余额',
    PRIMARY KEY ('id') USING BTREE
  ) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;
  INSERT INTO 'account_info' VALUES ('1', '张三', '1', '10000');

画面5：
- 展示 PPT 页面“3.3.2.2 数据库”，内容为：创建 bank2 库，并导入以下表结构和数据：
- 代码块：
  CREATE DATABASE 'bank2' CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
  USE bank2;
  DROP TABLE IF EXISTS 'account_info';
  CREATE TABLE 'account_info' (
    'id' bigint(20) NOT NULL AUTO_INCREMENT,
    'account_name' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '户主姓名',
    'account_no' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '银行卡号',
    'account_password' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '账户密码',
    'account_balance' double NULL DEFAULT NULL COMMENT '账户余额',
    PRIMARY KEY ('id') USING BTREE
  ) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;
  INSERT INTO 'account_info' VALUES ('2', '李四', '2', NULL, '0');

画面6：
- 展示数据库管理工具（DBeaver）中 bank2 数据库的 account_info 表，显示数据：
  - account_name: 张三
  - account_no: 1
  - account_password: 1
  - account_balance: 10000

画面7：
- 展示数据库管理工具（DBeaver）中 bank1 数据库的 account_info 表，显示数据：
  - account_name: 李四
  - account_no: 2
  - account_password: 2
  - account_balance: 0

画面8：
- 展示 PPT 页面“3.3.1 业务说明”，内容为：本案例通过 Hmily 框架实现 TCC 分布式事务，模拟两个账户的转账交易过程。两个账户分别在不同的银行（张三在 bank1、李四在 bank2），bank1、bank2 是两个微服务。对于交易过程中的每个操作，要么都成功，要么都失败。
- 展示“黑马程序员”官网信息及链接。

画面9：
- 展示 IntelliJ IDEA 中的项目结构，当前选中 pom.xml 文件。
- 代码块：
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <version>2.0.0</version>
  </dependency>

画面10：
- 展示 IntelliJ IDEA 中的项目结构，当前选中 pom.xml 文件。
- 代码块：
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <version>2.0.0</version>
  </dependency>

画面11：
- 展示 IntelliJ IDEA 中的项目结构，当前选中 pom.xml 文件。
- 代码块：
  <dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>hmily-spring-boot-starter</artifactId>
    <version>1.1.16</version>
  </dependency>

画面12：
- 展示 IntelliJ IDEA 中的项目结构，当前选中 pom.xml 文件。
- 代码块：
  <dependency>
    <groupId>commons-lang</groupId>
    <artifactId>commons-lang</artifactId>
    <version>2.6</version>
  </dependency>

画面13：
- 展示 PPT 页面“3.3.2.3 Maven 工程”，内容为：
  (1) 搭建 maven 工程，以 tcc-hmily-demo 为父工程，进行依赖管理，hmily-demo-bank1 负责张三账户操作，hmily-demo-bank2 负责李四账户操作，hmily-demo-discover-server 是服务注册中心。
  (2) pom.xml 导入 hmyl 相关依赖，这里不再详述。
- 展示项目结构：
  tcc-hmily-demo
  ├── idea
  ├── hmily-demo-bank1
  ├── hmily-demo-bank2
  ├── hmily-demo-discover-server
  └── logs
  └── tcc-hmily-demo.iml

画面14：
- 展示 PPT 页面“3.3.2.2 数据库”，内容为：创建 bank1 库，并导入以下表结构和数据：
- 代码块：
  CREATE DATABASE 'bank1' CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
  USE bank1;
  DROP TABLE IF EXISTS 'account_info';
  CREATE TABLE 'account_info' (
    'id' bigint(20) NOT NULL AUTO_INCREMENT,
    'account_name' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '户主姓名',
    'account_no' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '银行卡号',
    'account_password' varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL COMMENT '账户密码',
    'account_balance' double NULL DEFAULT NULL COMMENT '账户余额',
    PRIMARY KEY ('id') USING BTREE
  ) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;
  INSERT INTO 'account_info' VALUES ('1', '张三', '1', '1', '10000');

