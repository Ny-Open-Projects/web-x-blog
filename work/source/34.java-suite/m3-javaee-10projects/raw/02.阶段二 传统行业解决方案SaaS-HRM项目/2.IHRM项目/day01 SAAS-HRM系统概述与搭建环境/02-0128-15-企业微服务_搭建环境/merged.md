# 15-企业微服务：搭建环境

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\15-企业微服务：搭建环境_【海量资源尽在 ubkz.com】.mp4
- 时长 7分53秒（音频 473s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 基本的工程结构我们搭建好了之后接下来在这套结构之上我们要完成一个叫做企业微服务的这么一个开发那开发这个企业微服务其实很简单首先呢我们先把这个模块给它搭建出来那搭建模块的过程当中呢我们要做的事情注意这是一个企业微服务我们要做第一个引入相应的坐标搭建创建一个工程
[00:29] 那接下来去对这个工程做一些其他的一些配置比如说你这个工程真真正正的要跑起来它的请求端口是什么样的你这个服务叫什么名称以及你连接数据库的地址等等等等很多内容所以第二件事就是配置文件那配置文件我们搞定了之后接下来Spring Boot我们需要配置一个启动类直接在启动类当中MEN方法的形式运行启动即可所以我们先来完成
[00:59] 企业CIUD里面的第一项就是模块的一个搭建那搭建模块呢很简单这个模块呢叫做IHM Company好了我在这边打开IDEA勾选上我们的复工程右键创建一个modelOK这个模型的这个模块的名称呢叫做IHRMIHRM下滑线CompanyC-O-M-P-A-N-YOK点击Next
[01:33] 点击Finish那模块搭建好了之后引入相应的坐标这些坐标不需要各位重点关注直接从我们的讲义当中右键call过来即可OK坐标也已经搞定了那对于一个Spring Boot工程我们要想运行的话还需要搞一个配置文件再需要搞出来一个它的启动类就可以了那好了配置文件我们一般把它放到Resource
[02:05] 这个目录下那这个配置文件呢你可以随意起名当然了Spring Boot它的配置文件的形式也有很多种我们这边配置文件使用的是VML这种形式所以接下来呢我去创建一个配置文件这些都是比较统一的我直接call过来了OK那在这个配置文件里面我们要添加的内容哎究竟有什么呢好了一共有这么几项首先呢第一项我们叫做
[02:36] 服务的配置第二项呢就是Spring的配置了配置那Spring配置里面呢又分成这么几个小项第一个呢我们把它称之为应用配置第二个是因为我们这个里面要真真正正和数据库打交道和数据库打交道要配置数据库连接池好了当然了还有第三个配置我们这边全部采用的是Spring Data JPA的形式来做所以我们要配置JPA
[03:11] OK一共呢就这么几项那这几项相对来说也比较简单我直接从我们的讲义当中直接call过来哎即可OKcall过来注意对齐contrary好了那第一项呢就是我们的当前服务的配置好了第二个其实里面全部都围绕的是Sprint在做文章就是Sprint的配置那Sprint配置呢第一小项就是应用第二小项呢就是数据库连接第三小项呢就是我们的GPA
[03:58] OK好了那这样一来我基本的配置文件也已经搞定了那配置文件写好了之后那接下来呢我在这边可以去创建一个我当前工程的启动类出来右键创建一个class把它放到com.ihrm.company这个包下com.p-a-n-y那这个给它起一个名字呢我就叫做company application了
[04:37] OK好了接下来呢在这个类当中我们就可以去完成基本配置类的一个配置首先第一个呢我们要配置SpringPageSpringBoot的包扫描好了接着配置我们叫做GPA注解的叫做扫描那Spring Boot包扫描如何去做呢不难很简单AddSpringBootSpringBootApplication其中呢
[05:13] 使用一个属性scan base base packageok那其中配置jpa注解的扫描at entity scan那第一个包呢我们把它全部都放到了我们叫做cn.ihrm这个包下其实如果说你要对这个包里面再划分的更加详细一些我们把它所有的代码全部都放到了叫做company这个包下所以我写company其实也可以c-o-m-p-a-n-y
[05:51] OK那接下来GPA注解那GPA注解和我们的实体类是息息挂相关的那我们这边所有的企业微服务用到的实体类是不是都放到了com.itcom.ihim.domain.com你这个包下所以我这边扫描包value就等于com.ihim.domain.com.pany这个包下
[06:24] 就可以了那当然了我们还可以配置一个叫做启动方法启动方法那配置启动方法这个比较简单来一个psvm闷方法那在闷方法里面写的代码呢相对而言呢它不难它不难我们借助sprintapplicationsprintapplication点打点它里面有一个方法叫做run好了那我们配置就是当前
[07:01] 启动类点class后面把我们的启动参数配置上即可OK那这样一来我整个这个微服务里面的启动方法就已经配置好那刚才我们配置的是其实就是企业微服务里面的基本结构那我们做的事情第一件事创建了这么一个工程引入了相当的坐标接着第二件事配置了这个
[07:29] 微服务的配置文件指定了它的服务的一些端口指定了这个Sprint的配置里面有应用它这边给它起了一个应用的名称还有数据库的一些配置和GPA那这些搞定了之后配置了一个启动类OK那这样一来我基本的企业微服务咱们就已经搭建成功了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面9：在 IntelliJ IDEA 中，编辑“CompanyApplication.java”，注释中说明“//1.设置Spring Boot的包扫描”和“//2.设置jpa包扫描”，代码中使用了 @SpringBootApplication(scanBasePackages = "com.ihrm.company")。
画面10：在 IntelliJ IDEA 中，编辑“CompanyApplication.java”，注释中说明“//1.设置Spring Boot的包扫描”和“//2.设置jpa包扫描”，代码中使用了 @SpringBootApplication(scanBasePackages = "com.ihrm.company") 和 @EntityScan(value="com.ihrm.company")。
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
//1.配置Spring Boot的包扫描
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
//1.设置Spring Boot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm.company")
//2.设置jpa包扫描
@EntityScan

画面10：
//1.设置Spring Boot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm.company")
//2.设置jpa包扫描
@EntityScan(value="com.ihrm.company")

画面11：
//1.设置Spring Boot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm.company")
//2.设置jpa包扫描
@EntityScan(value="com.ihrm.domain.company")

画面12：
//1.设置Spring Boot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm.company")
//2.设置jpa包扫描
@EntityScan(value="com.ihrm.domain.company")
public class CompanyApplication {

}

画面13：
//1.设置Spring Boot的包扫描
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

