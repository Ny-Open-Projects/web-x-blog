# 04-微服务发现组件Eureka：微服务注册

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\04-微服务发现组件Eureka：微服务注册_【海量资源尽在 ubkz.com】.mp4
- 时长 5分19秒（音频 320s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们现在已经启动了Erica服务的一个配置那接下来呢就是把我们写过的系统微服务企业微服务还有其他的微服务注册到我们的Erica组件上其实就可以了那接下来呢微服务如何去注册也比较简单那首先呢我们需要打开需要注册的这个微服务的配置文件做一点点简单的配置
[00:27] 那比如说呢我要把company这个微服务注册到Erica服务上那怎么办首先第一件事添加相应的Erica客户端的依赖通过客户端去调用我们的服务端好了这是第一件事第二件事添加我们Erica服务端的配置也就是打开我们这边Spring的application.yml配置文件进行配置那第三件事那启动我们微服务的时候找到启动类在启动类上添加Erica
[00:57] 客户端的注解就可以了接着我们一起来看一下如何去做首先第一件事添加依赖这个依赖在今天的资料当中给各位准备好了注意客户端依赖就是它ERICA CLANTCtrl Ccall到我们的工程部分Ctrl Acall过来call过来之后接下来就是对ERICA服务端的一个配置这个服务端的配置也给各位准备好了如何将微服务注册到ERICA
[01:27] 咱们的服务端这边就是Eureka Client那这边就是配置我这边是以一个微服务客户端的形式去注册到我们的Eureka服务上我们的Eureka服务不是Localhost 6868吗然后我们请求的地址各位来看上面是我们服务端的配置最后有一个你其他客户端注册的地址那我们配置上注册的地址即可那好了我把这一段Ctrl C也call到
[01:56] 我这个企业微服务上面当然了call到什么位置都所谓了我call到最上边了好了注册到ERICA的服务地址好了前两件事我们搞定了之后接着我们去完成第三件事的一个配置第三件事就是在我们启动类上面配置注册到ERICAU R E K注册到ERICA这个怎么做很简单一个注解即可
[02:36] at enable Eureka Client好了那这样一来呢我们就已经把企业微服务给它搞定了搞定了之后我可以重新启动一下我这个企业微服务找到企业微服务去重启好了让它去启动我不管了OK那除了我们这个企业微服务之外呢我们还有很多的其他的微服务比如说呢我们这边还有系统微服务那同样的要做的事情都是一模一样的找到启动类
[03:08] 那找到Po文件找到微服务的配置文件好了还有我们今天新添加的这做员工的微服务一模一样我稍微快一点OK Po文件Ctrl C添加过来还有一个Po文件DependenceOK这两个Po文件我们修改好了那修改好了之后还有一个就是我们注册的配置Ctrl C
[03:53] 都一样了都写到最上边了都是一模一样的我们要把所有的微服务全部都注册到Eureka组件当中OK那接着在每一个的我们的启动类上边at enable Eureka clientat enable Eureka clientOK搞定OK搞定那好了接下来呢把剩下的这两个微服务也重启一下好了系统微服务重新启动OK还有一个我们的雇员微服务重新启动
[04:38] 好了这些让他去重启那接下来呢我们就可以打开我们这个Erica服务端的这个界面我们刷新一下耐心等待看一下有没有把其他的我们的服务注册上来各位来看那两个还在重启啊我们先启动的是Comedy各位来看现在我们的叫做企业微服务也已经注册过来了好了我再刷新一把哎各位来看这回呢我所有的微服务都已经注册到我们的Erica组件当中了有企业的
[05:08] 有固源的以及有我们系统那这个ERICA呢我们都配置好了之后我们已经为之后多个微幅之间的调用就已经打好了基础

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在微服务架构中，通过配置文件将各个服务注册到 Eureka 服务发现中心，实现服务间的互相调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面，标题为“1.4.2 微服务注册”，内容说明将所有微服务注册到 Eureka 中，以便互相调用。同时展示了一个 Maven 依赖配置片段：
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-Eureka-client</artifactId>
</dependency>

画面 2: 在 IntelliJ IDEA 中，展示项目结构，当前选中的是 `ihrm_company` 模块的 `application.yml` 文件，文件中包含服务配置（如 server.port: 9001）和数据源配置。

画面 3: 在 IntelliJ IDEA 中，展示 `application.yml` 文件，光标位于文件顶部，准备进行编辑。

画面 4: 在 IntelliJ IDEA 中，编辑 `application.yml` 文件，添加了 Eureka 客户端配置：
Eureka:
  client:
    Service-url:
      defaultZone: http://localhost:8888/Eureka/
  server:
    port: 9001

画面 5: 在 IntelliJ IDEA 中，展示 `CompanyApplication.java` 文件，其中包含 Spring Boot 启动类的注解配置：
@EnableEurekaClient
@SpringBootApplication(scanBasePackages = "com.ihrm")
public class CompanyApplication {
    public static void main(String[] args) {
        SpringApplication.run(CompanyApplication.class, args);
    }
}

画面 6: 在 IntelliJ IDEA 中，展示项目结构，选中了 `ihrm_company` 模块，准备进行后续操作。

画面 7: 在 IntelliJ IDEA 中，展示 `ihrm_system` 模块的 `application.yml` 文件，光标位于 `jwt` 配置块附近。

画面 8: 在 Notepad++ 中，展示 `Eureka服务的配置文件`，其中包含 Eureka 服务的配置：
#Eureka服务的配置文件
server:
  port: 8888 #服务端口
Eureka:
  client:
    registerWithEureka: false #是否将自己注册到Eureka服务中，本身就是所有无需注册
    fetchRegistry: false #是否从Eureka中获取注册信息
    serviceUrl:
      defaultZone: http://127.0.0.1:8888/Eureka/
#微服务注册到Eureka配置
Eureka:
  client:
    Service-url:
      defaultZone: http://localhost:8888/Eureka/

画面 9: 在 IntelliJ IDEA 中，展示 `ihrm_employee` 模块的 `pom.xml` 文件，其中包含 Spring Boot Maven 插件配置：
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <configuration>
        <classifier>exec</classifier>
    </configuration>
</plugin>
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <configuration>
        <mainClass>com.ihrm.employee.EmployeeApplication</mainClass>
        <layout>ZIP</layout>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>repackage</goal>
            </goals>
        </execution>
    </executions>
</plugin>

画面 10: 在 IntelliJ IDEA 中，编辑 `ihrm_employee` 模块的 `application.yml` 文件，添加了 Eureka 客户端配置：
Eureka:
  client:
    Service-url:
      defaultZone: http://localhost:8888/Eureka/
  server:
    port: 9003

画面 11: 在 IntelliJ IDEA 中，展示 `SystemApplication.java` 文件，其中包含 Spring Boot 启动类的注解配置：
@EnableEurekaClient
@SpringBootApplication(scanBasePackages = "com.ihrm")
public class SystemApplication {
    public static void main(String[] args) {
        SpringApplication.run(SystemApplication.class, args);
    }
}

画面 12: 在 IntelliJ IDEA 中，展示 `EmployeeApplication.java` 文件，其中包含 Spring Boot 启动类的注解配置：
@EnableEurekaClient
@SpringBootApplication(scanBasePackages = "com.ihrm")
public class EmployeeApplication {
    public static void main(String[] args) {
        SpringApplication.run(EmployeeApplication.class, args);
    }
}

画面 13: 在 IntelliJ IDEA 中，展示 `EmployeeApplication.java` 文件，其中包含 Spring Boot 启动类的注解配置：
@EnableEurekaClient
@SpringBootApplication(scanBasePackages = "com.ihrm")
public class EmployeeApplication {
    public static void main(String[] args) {
        SpringApplication.run(EmployeeApplication.class, args);
    }
}

画面 14: 在浏览器中，访问 Eureka 服务发现页面，显示已注册的服务实例：
Instances currently registered with Eureka
Application | AMIs | Availability Zones | Status
IHMR-COMPANY | n/a (1) | (1) | UP (1) - localhost:ihrm-company:9001
IHMR-EMPLOYEE | n/a (1) | (1) | UP (1) - localhost:ihrm-employee:9003
IHMR-SYSTEM | n/a (1) | (1) | UP (1) - localhost:ihrm-system:9002

General Info
Name | Value
total-available-memory | 629mb
environment | test
num-of-cpus | 4
current-memory-usage | 147mb (23%)
server-uptime | 03:11
registered-replicas | http://127.0.0.1:8888/Eureka/
unavailable-replicas | http://127.0.0.1:8888/Eureka/

