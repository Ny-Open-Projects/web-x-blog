# 画面线理解：14-模板制作：项目路径处理

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\14-模板制作：项目路径处理_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:09, 02:04, 03:02, 03:30, 04:01, 04:16, 05:27, 05:45, 06:32, 07:55, 08:16, 08:40, 09:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:04:59

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 SpringBoot 代码生成器快速创建项目模板，并展示生成的实体类、配置文件和项目结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT内容，讲解SpringBoot通用模板的分层结构（实体类、持久化层、业务逻辑层、表现层）和配置文件。
画面2：打开记事本，准备编写或查看代码。
画面3：在文件资源管理器中，弹出“代码生成器v1.0”窗口，设置项目信息（原项目名：ihm，包名：com.ihm.system，项目中文名称：人力系统，作者：Haaat，用户名：root，密码：111111），模板选择“springboot通用的模板”，点击“生成代码”。
画面4：展示项目目录结构，重点是 resources 目录下的 application.yml 文件。
画面5：在IntelliJ IDEA中打开项目 ihm_common_model，展示其目录结构，包含 com.ihm.domain 包下的 Company、Department、Employee、PoI、System 等类。
画面6：在记事本中显示 Company.java 文件内容，包含多个私有属性，如 companyName、managerId、version、renewalDate、expirationDate、companyArea、companyAddress、companyLogoId。
画面7：在记事本中显示 Company.java 文件的注释部分，说明如何使用 Lombok 注解（@Data、@Setter、@AllArgsConstructor）自动生成 getter、setter、构造方法，并列出需要添加的 Maven 依赖。
画面8：在文件资源管理器中，展示项目 ihm_company 的目录结构，包含 src、main、java、com、ihm、company 等子目录。
画面9：在文件资源管理器中，展示项目 ihm_company 的目录结构，包含 src、main、java、com、ihm、company 等子目录。
画面10：在记事本中显示 pom.xml 文件内容，包含父项目依赖（<artifactId>ihm_parent</artifactId>）、项目依赖（<artifactId>ihm_company</artifactId>）和多个子模块依赖（如 spring-boot-starter-data-jpa、mysql-connector-java、spring-cloud-starter-netflix-eureka-client）。
画面11：在IntelliJ IDEA中打开项目 codeutils，展示其目录结构，包含 src、main、java、com、codeutils 等子目录。
画面12：在IntelliJ IDEA中打开项目 codeutils，展示其目录结构，包含 src、main、java、com、codeutils 等子目录。
画面13：在IntelliJ IDEA中打开项目 codeutils，展示其目录结构，包含 src、main、java、com、codeutils 等子目录。
画面14：在记事本中显示 pom.xml 文件内容，包含父项目依赖（<artifactId>ihm_parent</artifactId>）、项目依赖（<artifactId>ihm_company</artifactId>）和多个子模块依赖（如 spring-boot-starter-data-jpa、mysql-connector-java、spring-cloud-starter-netflix-eureka-client）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
模板：springboot通用的模板
原项目名（英文）：ihm
包名：com.ihm.system
项目中文名称：人力系统
作者：Haaat
模块：ihm
用户名：root
密码：111111

画面4：
无代码或配置内容。

画面5：
无代码或配置内容。

画面6：
```java
/**
 * 公司名称
 */
private String name;
/**
 * 企业登录账号ID
 */
private String managerId;
/**
 * 当前版本
 */
private String version;
/**
 * 续期时间
 */
private Date renewalDate;
/**
 * 到期时间
 */
private Date expirationDate;
/**
 * 公司地区
 */
private String companyArea;
/**
 * 公司地址
 */
private String companyAddress;
/**
 * 营业执照-图片ID
 */
private String companyLogoId;
```

画面7：
```java
import javax.persistence.Column;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;
import java.io.Serializable;
import java.util.Date;

/**
 * 实体类
 * @author
 * @version 1.0
 */
//Lombok 注解：使用注解的形式替换getter、setter、构造方法
//1.添加依赖（在工程中引入相应的插件坐标即可）
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.16.16</version>
</dependency>
//2.使用注解配置
@Setter
@Getter
@Builder
@AllArgsConstructor
@Data
//使用JPA操作数据
```

画面8：
无代码或配置内容。

画面9：
无代码或配置内容。

画面10：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>ihm_parent</artifactId>
        <groupId>com.ihm</groupId>
        <version>1.0-SNAPSHOT</version>
        <modelVersion>4.0.0</modelVersion>
    </parent>
    <artifactId>ihm_company</artifactId>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <dependency>
            <groupId>com.ihm</groupId>
            <artifactId>ihm_common</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
    </dependencies>
</project>
```

画面11：
无代码或配置内容。

画面12：
无代码或配置内容。

画面13：
无代码或配置内容。

画面14：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>ihm_parent</artifactId>
        <groupId>com.ihm</groupId>
        <version>1.0-SNAPSHOT</version>
        <modelVersion>4.0.0</modelVersion>
    </parent>
    <artifactId>ihm_company</artifactId>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <dependency>
            <groupId>com.ihm</groupId>
            <artifactId>ihm_common</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
    </dependencies>
</project>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
PPT标题：3.3 SpringBoot通用模板
子标题：3.3.1 实体类
内容：
- 实体类
  - 类路径，类名，属性列表（getter, setter方法）
- 持久化层
  - 类路径，类名，引用实体类
- 业务逻辑层
  - 类路径，类名，引用实体类，引用持久化层代码
- 表现层
  - 类路径，类名，引用实体类，引用业务逻辑层代码，请求路径
- 配置文件
  - pom文件，springboot配置文件

画面5：
无PPT标题或架构图。

画面12：
无PPT标题或架构图。

画面13：
无PPT标题或架构图。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
