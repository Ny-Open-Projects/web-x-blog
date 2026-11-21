# day03-4-校验手机号功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-4-校验手机号功能实现2_【海量资源尽在 666java.com】.mp4
- 时长 5分54秒（音频 354s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才我们在Account这个微服务当中把MP的环境以及相关的配置都已经修改过了或者说添加过了接下来咱就要动手编码去实现校验手机号是否存在的这个功能在编码的时候我们首先要做的第一件事就是先搞定实体类就是先增加一个实体类这个实体类就是Account
[00:27] 那在咱们的表里边大家看啊P2P下滑线Account这个数据库里边呢有一个表叫Account就这个表账户表对不对这里边有几个字段主件啊用户名啊手机号啊密码啊加密研啊账号状态啊等等等等因为咱涉及到数据库操作嘛数据库操作的时候呢自然都需要用到这个实体类所以说咱需要把这个实体类呢先加进来
[00:59] 那这个实体类呢大家不用写我们给大家提供的有你直接拿过来用就行了在这儿资料文件夹里边啊Ctrl C然后呢我们应该是放到哪了Entity对吧这个包里边粘贴粘过来之后呢大家最好呢是要把这个代码从上往下啊过一遍这里边呢都是咱讲过的东西你看你还有印象没有这个注解谁的注解这注解谁的呀什么Lombok对不对
[01:31] 它的作用是什么对它的作用就是帮我们生成这一堆属性的什么呀getter setter方法对不对然后下边这些注解就是跟谁有关的呀是不是mp对吧mp有关的这个是用来设置什么呀表名的是不是它表名没写错吧account没错然后呢这个是设置什么呀主件的字段名咱这个主件就是id下边这些呢就是设置普通字段的这个你
[02:03] 下去自己检查吧应该是没有问题的啊这个字段名别写错了代号写无所谓这就不再说了啊这是这个实体类吧大家直接拿过来用但是里边代码要熟悉一下那这个实体类有了之后呢咱接下来首先写的是哪一层代码三层表现层业务层还有什么呀数据访问层咱应该先写数据访问层的代码数据访问层老简单了对不对对MP来说基本上就是写一个空接口
[02:37] 是吧再写一个基本上也是空的一个什么呀Mapper映射配置文件就OK了咱前面讲MP的时候是不是都说过了对不对那来开始干吧对不对注意我们都应该放到这个包里边Mapper这个包里边好咱先新建一个接口Mapper接口名字就叫ACCUNTMAPPR接口就这个样子吧
[03:09] 那肯定不对啊你这样写你这个接口绝对是空接口空接口你写的干嘛呀我们需要让它继承MP的一个接口叫base什么呀map对没错而且呢这儿是不是还要指定一个范形就是实体类ACC OUNT对吧倒一下包你这么一写的话一定要注意了这个接口看着是空的其实就
[03:40] 不是空的因为它继承了base map这里边增伤改差那一套方法是不是全部都有是不是好这是接口大家看一下就有了然后呢跟这个接口相配套的是不是还有一个map映射配置文件来咱写一下啊是不是也是应该放到这个包里边对不对刚才那个配置啊那个路径你得注意了好这个new一个配置文件怎么new啊ID里边有这个东西吗没有但是我这儿有你看
[04:09] MPMapperXML但是你的IDL里边还真没有啊真没有这个东西是我是我自己设置的啊怎么设置我跟大家说一下因为这个东西咱也会经常用在这儿看我这儿啊这儿editor下面有个file按的code templates就是模板了对不对在files里边你看我自己新建了一下就是点加号新建新建了一个模板就是它这个名字我自己起了那么你把它的这个一个基本的代码粘到这里边就行了
[04:42] 粘到这儿是不是粘进来然后把这两个勾给打上点击OK注意这儿一定要选择XMLXML就OK了这个搞好之后呢你看你点右键菜单new的时候它就有这项跑哪去了在这儿对不对点击一下咱起个名字就叫ACCUNTMAPP没错吧点击OK大家看一下这个配置文件就有了
[05:14] 然后这儿是不是要补一补啊这是补什么代码的是不是说它对应的这个Mapper接口对不对adcast-one-sin-p2p.account.Mapper.对,account-Mapper,没错对,就这个样子那到这儿的话咱是不是就添加了一个实体类然后把什么层的代码写完了呀这是什么层呢对,数据访问层的很简单啊用MP

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
创建一个名为 Account 的实体类，并为其生成对应的 MyBatis-Plus Mapper 接口和 XML 映射文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于修改 Apollo 配置和创建实体类的说明，其中包含修改配置的代码片段。
画面 2: PDF 文档中展示实体类 Account 的定义，包含 @Data 和 @TableName 注解。
画面 3: 在 IntelliJ IDEA 中，展示 Account 实体类的代码，包含 @TableId 和 @TableField 注解。
画面 4: 在 MySQL Workbench 中，展示账户表（t_user）的建表语句和字段信息。
画面 5: 在 IntelliJ IDEA 中，展示 Account 实体类中为手机号字段添加 @TableField 注解。
画面 6: PDF 文档中展示实体类 Account 的定义，包含 @TableId 和 @TableField 注解。
画面 7: 在 IntelliJ IDEA 中，展示 Account 实体类中为盐字段添加 @TableField 注解。
画面 8: 在 IntelliJ IDEA 中，展示 AccountMapper 接口的初始代码，继承 BaseMapper。
画面 9: 在 IntelliJ IDEA 中，展示 AccountMapper 接口的完整代码，导入实体类并指定泛型。
画面 10: 在 IntelliJ IDEA 中，右键点击 AccountMapper.java 文件，弹出菜单，选择“New” -> “XML File”。
画面 11: 在 IntelliJ IDEA 的设置中，展示“File and Code Templates”页面，选择“MP Mapper XML”模板。
画面 12: 在 IntelliJ IDEA 中，弹出“New MP Mapper XML”对话框，准备创建 XML 文件。
画面 13: 在 IntelliJ IDEA 中，展示创建好的 AccountMapper.xml 文件内容，包含 MyBatis 的 XML 声明和 namespace。
画面 14: PDF 文档中展示 Mapper 接口和 XML 文件的创建说明。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<dependency>
    <groupId>org.mybatis.typehandlers</groupId>
    <artifactId>mybatis-typehandlers-jsr310c</artifactId>
</dependency>

<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid-spring-boot-starter</artifactId>
</dependency>

<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
```

画面 2:
```java
@Data
@TableName("account")
public class Account implements Serializable {
    private static final long serialVersionUID = 1L;
```

画面 3:
```java
@Data
@TableName("account")
public class Account implements Serializable {
    private static final long serialVersionUID = 1L;

    @TableId("ID")
    private Long id;

    @TableField("USERNAME")
    private String username;
```

画面 4:
```sql
CREATE TABLE `t_user` (
  `id` BIGINT(20) NOT NULL COMMENT '主键ID',
  `user_name` VARCHAR(20) NOT NULL COMMENT '用户名',
  `password` VARCHAR(30) DEFAULT NULL COMMENT '密码',
  `age` INT(11) DEFAULT NULL COMMENT '年龄',
  `email` VARCHAR(50) DEFAULT NULL COMMENT '邮箱',
  `mobile` VARCHAR(11) DEFAULT NULL COMMENT '手机号',
  `salt` VARCHAR(50) DEFAULT NULL COMMENT '盐',
  `status` TINYINT(1) DEFAULT NULL COMMENT '账号状态',
  `domain` VARCHAR(50) NOT NULL COMMENT '域名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
```

画面 5:
```java
@TableField("MOBILE")
private String mobile;
```

画面 6:
```java
@Data
@TableName("account")
public class Account implements Serializable {
    private static final long serialVersionUID = 1L;

    @TableId("ID")
    private Long id;

    @TableField("USERNAME")
    private String username;
```

画面 7:
```java
@TableField("SALT")
private String salt;
```

画面 8:
```java
package cn.itcast.wanxing2p.account.Mapper;

import com.bacniodou.mybatisplus.core.Mapper.BaseMapper;

public interface AccountMapper extends BaseMapper {
```

画面 9:
```java
package cn.itcast.wanxing2p.account.Mapper;

import cn.itcast.wanxing2p.account.entity.Account;
import com.bacniodou.mybatisplus.core.Mapper.BaseMapper;

public interface AccountMapper extends BaseMapper<Account> {
```

画面 10:
```java
// 无直接代码，为菜单操作
```

画面 11:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="...">
```

画面 12:
```java
// 无直接代码，为弹出对话框
```

画面 13:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="cn.itcast.wanxing2p.account.Mapper">
</Mapper>
```

画面 14:
```java
public interface AccountMapper extends BaseMapper<Account> {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PDF 文档标题为“万能金服-第2章 讲义-开户”，内容包括“3) 修改Apollo关于MP的配置”和“4) 实体类”。
画面 2: PDF 文档标题为“万能金服-第2章 讲义-开户”，内容包括“4) 实体类”。
画面 3: PDF 文档标题为“万能金服-第2章 讲义-开户”，内容包括“3.6.1.1 概念定义”。
画面 4: MySQL Workbench 中展示表结构，字段包括 ID、USER_NAME、PASSWORD、AGE、EMAIL、MOBILE、SALT、STATUS、DOMAIN。
画面 5: PDF 文档标题为“万能金服-第2章 讲义-开户”，内容包括“3.6.1.1 概念定义”。
画面 6: PDF 文档标题为“万能金服-第2章 讲义-开户”，内容包括“4) 实体类”。
画面 7: PDF 文档标题为“万能金服-第2章 讲义-开户”，内容包括“3.6.1.1 概念定义”。
画面 8: PDF 文档标题为“万能金服-第2章 讲义-开户”，内容包括“5) Mapper接口”。
画面 9: PDF 文档标题为“万能金服-第2章 讲义-开户”，内容包括“5) Mapper接口”。
画面 10: PDF 文档标题为“万能金服-第2章 讲义-开户”，内容包括“5) Mapper接口”。
画面 11: PDF 文档标题为“万能金服-第2章 讲义-开户”，内容包括“5) Mapper接口”。
画面 12: PDF 文档标题为“万能金服-第2章 讲义-开户”，内容包括“5) Mapper接口”。
画面 13: PDF 文档标题为“万能金服-第2章 讲义-开户”，内容包括“5) Mapper接口”。
画面 14: PDF 文档标题为“万能金服-第2章 讲义-开户”，内容包括“5) Mapper接口”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

