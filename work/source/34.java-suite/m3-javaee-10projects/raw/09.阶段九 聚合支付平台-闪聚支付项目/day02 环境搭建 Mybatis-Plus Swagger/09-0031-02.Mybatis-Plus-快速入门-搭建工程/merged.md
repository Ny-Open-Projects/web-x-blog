# 02.Mybatis-Plus-快速入门-搭建工程

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\02.Mybatis-Plus-快速入门-搭建工程【海量资源尽在 666java.com】.mp4
- 时长 8分24秒（音频 505s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面呢我们来进行MyBetis Plus的快速入门通过快速入门呢我们大家掌握MyBetis Plus的一个基本的一个使用方法好 我们来看啊首先我们要准备一个开发环境那这个开发环境呢大家看到有四项JDK 1.8 Maven 3.3.9 IDEA我们用IDEA开发然后呢MyCircle 5.7好 那这些环境呢这里面我就
[00:26] 不再说了你可以参考我们项目的一个开发工具配置的一个视频来学习一下好那么这里边呢我们来看首先呢是需要去创建一个数据库因为我们要使用Meptis Plus来访问我们的数据库来我们创建一个数据库啊来执行一下这个脚本这个脚本呢大家可以看到是不是创建一个数据库叫MP的数据库那当然首先你是不是需要用你的这个数据库的客户端连上你的数据库的服务器是吧
[00:55] 好你把它拷到这然后呢执行这里边执行完成之后刷新MP的数据库是不是就创建好了创建好了之后呢这里边呢还没有表我们是需要干嘛呀去创建一张表的这是创建表的这个脚本大家可以看到它有几个字段IDID字段是组件自增的然后呢有usernamepassword等等啊这是一个用户的一个一张表里边可以导入一些数字化数据
[01:24] 那我们把这个脚本呢一块复制到客户端那么当然你这时候你要选中这个数据库啊左侧选中数据库然后呢执行好这时候执行完了之后呢我们刷新好这张表呢大家可以看到是不是就创建出来了这里边初始化了一些用户啊好那么这个数据库创建好了之后接下来我们是不是要写一个Meptis Plus的这个程序啊那我们是不是就必须创建一个工程对不对所以这里边呢
[01:53] 好来我们创建一个工程这里边我们就用Maven的方式Maven的方式来打开idea然后这里边我新建好下一步这里边我们是看一下这个工程的坐标是CNN IDCAST MP好我们跟讲义保持一致CNN IDCAST MP好它的模块名是它好这里边我们来看我们就在这个位置这个位置是我们的什么
[02:26] 代码啊将来我们课程的代码好然后下一步点击OK好那大家看这个工程是不是就创建好了这个工程创建好了之后我们要用MyBetisPlus各位我们是不是需要把MyBetisPlus的这个依赖加进去是吧另外还有一点就是我们是基于Spring Boot来开发因为后边我们的微服务都是基于Spring Boot开发是吧所以这里边呢我们就基于Spring Boot所以我们在我们的依赖当中去把这个
[02:56] parent当中来指定Spring Boot的依赖好那这个Spring Boot的依赖呢大家可以看到是不是就是2.1.3版本啊好这里边呢我们把这个maven呢给它设置一个自动导入啊好勾上去把这个勾上去好OK好那另外呢还有这是Spring Boot的另外还有就是mybatesplus本身的是吧大家可以看到啊这里边我们要嗯
[03:26] 这里面有一些依赖我们把这个依赖考过去我给大家说一下都是哪些这里面有哪些依赖你看这是Spring Boot的依赖对吧这是Spring Boot的一个Test包将来我们进行单元测试这是LongBulk的方便我们创建模型类的MyBitX Plus自己的MyBitX Plus和Spring Boot的一个包启动类这个是数据库的驱动数据库的驱动包好这就搞定了那么
[03:53] 一会儿呢我们是不是就可以在这个里边呢去写代码呀好那这里边呢各位我们是不是就可以去配置一些配置文件配置配置文件然后呢这里边呢我们就参考讲义来配吧你这配置文件里边的内容是啥呀你要连接数据库你肯定是数据库的连接参数是不是啊所以这里边呢各位我们来看我们把它拷过去啊配置文件呢我不建议大家手动去输入啊来这是数据库的驱动是吧
[04:22] 这个是我的本地的MySQL服务器然后MP数据库那这里边你要把根据你的这个账号密码数据库的账号密码你写正确好然后接下来还有怎么呢接下来还有的就是我们需要做什么事那就是要编写PUGO编写Mapper其实这个过程和我们之前说的这个MyBatis的开发过程是不是差不多也是
[04:51] 添加MapTest的依赖对不对然后呢写这个PUGO然后呢写MAP好因为我们现在要做的事是什么呢是不是就是要操作这个哪一张表啊是不是就是TB user这张表对吧所以你这里边呢各位我们是不是就需要去创建一个这个TB user对应的这个模型类啊那所以说这里边呢各位我们是不是就可以
[05:20] 按照这个步骤来创建一个对吧好那么接下来我们这样我们把这个模型类创建一下它的包名对吧包名好然后呢这里边呢我们要创建它的这个什么user当然这个这个这个这个类名这个类名无所谓啊关键的是你要在这儿指定一个什么你的这个对应的表
[05:47] 所以这个注解其实就是Mavetis的注解了看见吗就是这个类它所对应的表是哪一张表对于哪张表是不是就是TPU的所以你把它拷到这大家看到了吗然后呢这里边还有你要写它的一些字段嘛所以说你看它的组件呢是不是就是ID啊ID是不是你看它的是不是bigint所以这里边我们用langID这就是组件当然对于组件的话你需要用什么呀
[06:16] 用mybattlesplus的这个注解就是叫table id来指定它的组件名这个id其实就指定谁啊是不是就指定它的一个组件名啊组件名组件的这个字段名对吧好那么当然它还有很多的这个什么这个属性嘛所以你需要一个一个的来配置一个一个的配置
[06:47] 那这里边呢我们要配置的是个什么呀这个user name是吧user name你看有个下滑线通常我们都用驼峰方式嘛对吧user name你看user name是不是大写呀当然你这里边要指定的就是什么它所对应的列名了这个注意啊这个注解可变了看好这个组件用的是table id是吧这里边要指定什么指定所对应的字段名就是列名
[07:15] 好其他的方法其实都是按照这样一种方式呢来写就可以了嗯然后呢我们其实你把我password啊name啊这些东西是不是都我就拷贝了啊好然后最后一个是不是就是一个日期类型啊日期类型日期类型它是一个叫birthday看见吗哎它的这个数据库里边的类型叫date time那它呢这里边有点特殊啊哎我们准备用一个类型叫local哎local date time
[07:46] Local Date Time然后呢他最好他的名字和我们数据库的名字你看字段名保持一致大家理解吗然后当然这个我建议你也来指定他所对应的字段名看这个POGO是不是就搞定了然后呢POGO搞定之后呢一会儿我们是不是就可以写Mapper然后呢包括写测试类对不对到这儿其实我们这个快速入门的一个
[08:16] 工程结构其实准备工作我就做完了稍后呢我们去写mypl呢写它的测试类好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 MyBatis-Plus 框架快速搭建一个 Spring Boot 项目，包括环境准备、数据库创建、工程结构搭建、配置文件编写和实体类 POJO 的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前位于“2.1 准备环境”，列出所需环境：JDK 8+、Maven 3.3.9、IDEA 2018.2、MySQL 5.7。
画面2：展示创建数据库和表的 SQL 语句，包括创建数据库 `mp`（字符集 utf8，排序规则 utf8_general_ci）和创建表 `tb_user` 的结构。
画面3：展示在 MySQL 数据库管理工具中执行 SQL 语句后，表 `tb_user` 中的数据已成功插入。
画面4：展示项目根目录下的 `pom.xml` 文件，其中包含 Maven 的基本配置信息。
画面5：展示 `pom.xml` 文件中添加了 Spring Boot 的父项目依赖。
画面6：展示 `pom.xml` 文件中添加了 Spring Boot 的测试依赖和 MyBatis-Plus 的依赖。
画面7：展示 `pom.xml` 文件中添加了 MySQL 驱动依赖，并切换到“2.3.3 编写 application.properties”章节。
画面8：展示 `application.properties` 文件中的配置内容，包括应用名称、数据库连接信息和日志配置。
画面9：展示 `application.properties` 文件中数据库密码配置为 `mysql`。
画面10：展示 `application.properties` 文件中数据库密码配置为 `mysql`，光标在配置行上。
画面11：展示 `User.java` 文件的开头部分，包含类注解和字段声明。
画面12：展示 `User.java` 文件中字段声明部分，光标在 `private` 关键字上。
画面13：展示 `User.java` 文件中使用 `@TableField` 注解映射数据库字段。
画面14：展示 `User.java` 文件中使用 `@TableField` 注解映射数据库字段，光标在 `@TableField("user_name")` 注解上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
2.1 准备环境
• JDK 8+
• Maven 3.3.9
• IDEA 2018.2
• MySQL 5.7

画面2：
创建数据库并设置字符集为utf-8：
CREATE DATABASE `mp` CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';

创建表和测试数据：
-- 创建测试表
CREATE TABLE `tb_user` (
`id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
`user_name` varchar(20) NOT NULL COMMENT '用户名',
`password` varchar(20) NOT NULL COMMENT '密码',
`name` varchar(38) DEFAULT NULL COMMENT '姓名',
`age` int(11) DEFAULT NULL COMMENT '年龄',
`email` varchar(50) DEFAULT NULL COMMENT '邮箱',
`birthday` datetime DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- 插入测试数据
insert into `tb_user` (`id`,`user_name`,`password`,`name`,`age`,`email`,`birthday`) values
(1,'zhangsan','123456','张三',18,'test1@itcast.cn','2019-09-26 11:42:01'),
(2,'lisi','123456','李四',20,'test2@itcast.cn','2019-10-01 11:42:08'),
(3,'wangwu','123456','王五',25,'test3@itcast.cn','2019-10-02 11:42:14'),
(4,'zhaozhu','123456','赵六',21,'test4@itcast.cn','2019-10-05 11:42:18'),
(5,'sunqi','123456','孙七',24,'test5@itcast.cn','2019-10-14 11:42:23');

画面3：
-- 插入测试数据
INSERT INTO `tb_user` (`id`,`user_name`,`password`,`name`,`age`,`email`,`birthday`) VALUES
(1,'zhangsan','123456','张三',18,'test1@itcast.cn','2019-09-26 11:42:01'),
(2,'lisi','123456','李四',20,'test2@itcast.cn','2019-10-01 11:42:08'),
(3,'wangwu','123456','王五',25,'test3@itcast.cn','2019-10-02 11:42:14'),
(4,'zhaozhu','123456','赵六',21,'test4@itcast.cn','2019-10-05 11:42:18'),
(5,'sunqi','123456','孙七',24,'test5@itcast.cn','2019-10-14 11:42:23');

画面4：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>cn.itcast.mp</groupId>
    <artifactId>itcast-mp-Spring Boot</artifactId>
    <version>1.0-SNAPSHOT</version>

</project>

画面5：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>cn.itcast.mp</groupId>
    <artifactId>itcast-mp-Spring Boot</artifactId>
    <version>1.0-SNAPSHOT</version>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.8.RELEASE</version>
    </parent>

</project>

画面6：
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>

    <!-- 一、开发工具 -->
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>

    <!-- 二、MyBatis-Plus支持 -->
    <dependency>
        <groupId>com.baomidou</groupId>
        <artifactId>mybatis-plus-boot-starter</artifactId>
        <version>3.1.0</version>
    </dependency>

</dependencies>

画面7：
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.1.0</version>
</dependency>

<!-- 一、mysql驱动 -->
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.11</version>
</dependency>

画面8：
spring.application.name = itcast-mp-Spring Boot
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/mp?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai&useSSL=false
spring.datasource.username=root
spring.datasource.password=root
# logger Config
logging.level.root: debug

画面9：
spring.datasource.password=mysql

画面10：
spring.datasource.password=mysql

画面11：
package cn.itcast.mp.pojo;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import java.time.LocalDateTime;

@Data
public class User {

画面12：
package cn.it

