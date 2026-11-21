# 画面线理解：14-工程搭建：搭建子工程之搭建实体类模块和lombok插件

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\14-工程搭建：搭建子工程之搭建实体类模块和lombok插件_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:57, 01:36, 02:02, 02:58, 03:44, 03:56, 05:36, 06:10, 06:49, 07:20, 07:40, 08:42, 09:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:57:23

1) 这一组画面整体在讲什么（一句话）：
构建并配置一个用于企业级HRM系统的公共实体类模块，包括创建模块、引入坐标、编写实体类并使用Lombok注解自动生成getter/setter方法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，当前选中“5.5 搭建公共的实体类模块”，并用红色箭头标注“ihrm_common”为“domain类模块”，“ihrm_parent”为“工具类模块”。
画面2：展示父模块“ihrm_parent”的pom.xml文件内容，其中定义了<parent>和<properties>，并包含一个<dependency>。
画面3：展示子模块“ihrm_common_model”的pom.xml文件内容，其中定义了<parent>和<dependencies>。
画面4：在“ihrm_common_model”模块的src/main/java目录下，弹出“New Package”对话框，提示输入新包名。
画面5：在“com.ihrm.domain.company”包下创建并打开“Company.java”文件，光标位于“private”关键字前。
画面6：弹出“Select Fields to Generate Getters and Setters”对话框，选中“id”和“name”字段，准备生成getter/setter方法。
画面7：在“Company.java”中，已生成getter/setter方法，光标位于“public static void main(String[] args) {”行，下方有“Company”类的图标。
画面8：在项目结构中选中“ihrm_parent”的pom.xml文件。
画面9：在“Company.java”中，光标位于“@Data”注解上方，显示了Lombok注解的使用说明。
画面10：在“Company.java”中，光标位于“@Data”注解上方，显示了Lombok注解的使用说明。
画面11：在“Company.java”中，光标位于“@Data”注解上方，显示了Lombok注解的使用说明。
画面12：在“Company.java”中，光标位于“@Data”注解上方，显示了Lombok注解的使用说明。
画面13：在“Company.java”中，光标位于“@Data”注解上方，显示了Lombok注解的使用说明。
画面14：在“Company.java”中，光标位于“@Data”注解上方，显示了Lombok注解的使用说明。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
(1) 构建子模块ihrm_common_model
(2) 引入坐标
<dependencies>
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
</dependencies>

画面2：
<parent>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-parent</artifactId>
<version>2.0.5.RELEASE</version>
<relativePath/>
</parent>

<properties>
<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
<java.version>1.8</java.version>
<fastjson.version>1.2.47</fastjson.version>
</properties>

<dependencies>
<groupId>org.springframework.boot</groupId>

画面3：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>

<parent>
<groupId>com.ihrm</groupId>
<artifactId>ihrm_parent</artifactId>
<version>1.0-SNAPSHOT</version>
</parent>

<artifactId>ihrm_common_model</artifactId>

<dependencies>
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
<groupId>com.ihrm</groupId>
<artifactId>ihrm_common</artifactId>
<version>1.0-SNAPSHOT</version>
</dependency>
</dependencies>

画面4：
New Package
Enter new package name:

画面5：
package com.ihrm.domain.company;
public class Company {
private

画面6：
Select Fields to Generate Getters and Setters
Getter template: IntelliJ Default
Setter template: IntelliJ Default
com.ihrm.domain.company.Company
idString
nameString

画面7：
package com.ihrm.domain.company;
public class Company {
private String id;
private String name;
public String getId() {
return id;
}
public void setId(String id) {
this.id = id;
}
public String getName() {
return name;
}
public void setName(String name) {
this.name = name;
}
public static void main(String[] args) {
Company

画面8：
<parent>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-parent</artifactId>
<version>2.0.5.RELEASE</version>
<relativePath/>
</parent>

<properties>
<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
<java.version>1.8</java.version>
<fastjson.version>1.2.47</fastjson.version>
</properties>

<dependencies>
<groupId>org.springframework.boot</groupId>

画面9：
@lombok 插件：使用注解的形式省略getter setter，构造方法
如何使用插件：
1. 安装插件（在工程中引入相应的插件坐标即可）
<dependency>
<groupId>org.projectlombok</groupId>
<artifactId>lombok</artifactId>
<version>1.16.16</version>
</dependency>
2. 使用注解配置到实体类上

画面10：
@lombok 插件：使用注解的形式省略getter setter，构造方法
如何使用插件：
1. 安装插件（在工程中引入相应的插件坐标即可）
<dependency>
<groupId>org.projectlombok</groupId>
<artifactId>lombok</artifactId>
<version>1.16.16</version>
</dependency>
2. 使用注解配置到实体类上

画面11：
@lombok 插件：使用注解的形式省略getter setter，构造方法
如何使用插件：
1. 安装插件（在工程中引入相应的插件坐标即可）
<dependency>
<groupId>org.projectlombok</groupId>
<artifactId>lombok</artifactId>
<version>1.16.16</version>
</dependency>
2. 使用注解配置到实体类上

画面12：
@lombok 插件：使用注解的形式省略getter setter，构造方法
如何使用插件：
1. 安装插件（在工程中引入相应的插件坐标即可）
<dependency>
<groupId>org.projectlombok</groupId>
<artifactId>lombok</artifactId>
<version>1.16.16</version>
</dependency>
2. 使用注解配置到实体类上

画面13：
@lombok 插件：使用注解的形式省略getter setter，构造方法
如何使用插件：
1. 安装插件（在工程中引入相应的插件坐标即可）
<dependency>
<groupId>org.projectlombok</groupId>
<artifactId>lombok</artifactId>
<version>1.16.16</version>
</dependency>
2. 使用注解配置到实体类上

画面14：
@lombok 插件：使用注解的形式省略getter setter，构造方法
如何使用插件：
1. 安装插件（在工程中引入相应的插件坐标即可）
<dependency>
<groupId>org.projectlombok</groupId>
<artifactId>lombok</artifactId>
<version>1.16.16</version>
</dependency>
2. 使用注解配置到实体类上

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“4.5 搭建公共的实体类模块”，并用红色箭头标注“ihrm_common”为“domain类模块”，“ihrm_parent”为“工具类模块”。
画面9：在“Company.java”中，显示了Lombok注解的使用说明，包括“@Setter”、“@Getter”、“@AllArgsConstructor”、“@NoArgsConstructor”、“@Data”等注解。
画面10：在“Company.java”中，显示了Lombok注解的使用说明，包括“@Setter”、“@Getter”、“@AllArgsConstructor”、“@NoArgsConstructor”、“@Data”等注解。
画面11：在“Company.java”中，显示了Lombok注解的使用说明，包括“@Setter”、“@Getter”、“@AllArgsConstructor
