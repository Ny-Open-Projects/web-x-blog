# 画面线理解：day03-4-校验手机号功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-4-校验手机号功能实现2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:25, 00:59, 01:24, 01:50, 02:06, 02:34, 02:58, 03:24, 03:41, 04:17, 04:42, 05:03, 05:33, 05:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:30:08

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
package cn.itcast.wanxing2p.account.mapper;

import com.bacniodou.mybatisplus.core.mapper.BaseMapper;

public interface AccountMapper extends BaseMapper {
```

画面 9:
```java
package cn.itcast.wanxing2p.account.mapper;

import cn.itcast.wanxing2p.account.entity.Account;
import com.bacniodou.mybatisplus.core.mapper.BaseMapper;

public interface AccountMapper extends BaseMapper<Account> {
```

画面 10:
```java
// 无直接代码，为菜单操作
```

画面 11:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="...">
```

画面 12:
```java
// 无直接代码，为弹出对话框
```

画面 13:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="cn.itcast.wanxing2p.account.mapper">
</mapper>
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
