# 画面线理解：15-企业微服务：搭建环境

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\15-企业微服务：搭建环境_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:20, 00:59, 01:17, 01:44, 02:13, 02:24, 03:25, 05:05, 05:19, 05:57, 06:26, 06:52, 07:14, 07:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:58:06

1) 这一组画面整体在讲什么（一句话）：
构建企业微服务模块（hrm_company）的 Maven 依赖配置和 Spring Boot 启动类及配置文件的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录结构，当前选中“5.1 模块搭建”，页面内容为“5.1 模块搭建”小节，包含（1）搭建企业微服务模块hrm_company, pom.xml引入依赖和（2）添加配置文件application.yml。
画面2：与画面1内容相同，只是鼠标悬停在“5.1 模块搭建”上。
画面3：在 IntelliJ IDEA 中展示项目结构，选中“Company.java”，代码中包含 Lombok 注解（@Data, @AllArgsConstructor, @NoArgsConstructor）和一个 main 方法。
画面4：与画面1内容相同。
画面5：展示“5.1 模块搭建”页面，鼠标在“（2）添加配置文件application.yml”下方，页面底部显示“黑马程序员”Logo和标语。
画面6：在 IntelliJ IDEA 中，项目结构显示“ihrm_company”模块，右侧编辑区为空白。
画面7：在 IntelliJ IDEA 中，打开“application.yml”文件，内容为注释行“#服务配置”、“#1.应用配置”、“#2.数据库连接池”、“#3.JPA”。
画面8：在 IntelliJ IDEA 中，打开“CompanyApplication.java”文件，代码中包含 Spring Boot 的注解（@SpringBootApplication, @EntityScan）。
画面9：在 IntelliJ IDEA 中，编辑“CompanyApplication.java”，注释中说明“//1.设置springboot的包扫描”和“//2.设置jpa包扫描”，代码中使用了 @SpringBootApplication(scanBasePackages = "com.ihrm.company")。
画面10：在 IntelliJ IDEA 中，编辑“CompanyApplication.java”，注释中说明“//1.设置springboot的包扫描”和“//2.设置jpa包扫描”，代码中使用了 @SpringBootApplication(scanBasePackages = "com.ihrm.company") 和 @EntityScan(value="com.ihrm.company")。
画面11：在 IntelliJ IDEA 中，项目结构中选中“ihrm_common_model”模块，右侧编辑区显示“CompanyApplication.java”文件，代码中包含 @SpringBootApplication(scanBasePackages = "com.ihrm.company") 和 @EntityScan(value="com.ihrm.domain.company")。
画面12：在 IntelliJ IDEA 中，编辑“CompanyApplication.java”，代码中包含 @SpringBootApplication(scanBasePackages = "com.ihrm.company") 和 @EntityScan(value="com.ihrm.domain.company")，并添加了 main 方法。
画面13：在 IntelliJ IDEA 中，编辑“CompanyApplication.java”，代码中包含 @SpringBootApplication(scanBasePackages = "com.ihrm.company") 和 @EntityScan(value="com.ihrm.domain.company")，并添加了 main 方法。
画面14：在 IntelliJ IDEA 中，打开“application.yml”文件，内容为：
#服务配置
server:
  port: 9001
spring:
  #应用配置
  application:
    name: ihrm-company #指定服务名
  #数据库配置
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf8
    username: root
    password: 111111
  jpa:
    database: MySQL
    show-sql: true
    open-in-view: true

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1、4：
(1) 搭建企业微服务模块hrm_company, pom.xml引入依赖
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
<dependency>
    <groupId>com.ihrm</groupId>
    <artifactId>ihrm_common</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependency>
(2) 添加配置文件application.yml

画面7：
#服务配置
#1.应用配置
#2.数据库连接池
#3.JPA

画面8：
//1.配置springboot的包扫描
@Repository (org.springframework.data.jpa.repository)
@EnableAspectAutoProxy (org.springframework.context.annotation)
Around (org.aspectj.annotation)
JoinColumn (javax.persistence)
GeneratedValue (javax.persistence)
Entity (javax.persistence)
Entity (org.hibernate.annotations)
Deprecated (java.lang)
FunctionalInterface (java.lang)
SuppressWarnings (java.lang)
SupportedAnnotationTypes (java.annotation.processing)
SupportedSourceVersion (java.annotation.processing)
WebServiceProvider (java.xml.ws)
XmlAccessorType (javax.xml.bind.annotation)

画面9：
//1.设置springboot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm.company")
//2.设置jpa包扫描
@EntityScan

画面10：
//1.设置springboot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm.company")
//2.设置jpa包扫描
@EntityScan(value="com.ihrm.company")

画面11：
//1.设置springboot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm.company")
//2.设置jpa包扫描
@EntityScan(value="com.ihrm.domain.company")

画面12：
//1.设置springboot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm.company")
//2.设置jpa包扫描
@EntityScan(value="com.ihrm.domain.company")
public class CompanyApplication {

}

画面13：
//1.设置springboot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm.company")
//2.设置jpa包扫描
@EntityScan(value="com.ihrm.domain.company")
public class CompanyApplication {

}

画面14：
#服务配置
server:
  port: 9001
spring:
  #应用配置
  application:
    name: ihrm-company #指定服务名
  #数据库配置
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf8
    username: root
    password: 111111
  jpa:
    database: MySQL
    show-sql: true
    open-in-view: true

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、2、4：PPT 标题为“5.1 模块搭建”，子标题为“（1）搭建企业微服务模块hrm_company, pom.xml引入依赖”和“（2）添加配置文件application.yml”。
画面5：PPT 底部显示“黑马程序员”Logo和标语“改变中国IT教育，我们正在行动”。
画面6、7、8、9、10、11、12、13、14：无 PPT 内容，均为 IDE 编辑器界面。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
