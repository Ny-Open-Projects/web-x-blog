# 画面线理解：5.服务调用链路追踪-入门案例

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-1 服务调用链路追踪的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-1 服务调用链路追踪的理解和使用\5.服务调用链路追踪-入门案例_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:13, 02:06, 03:09, 03:50, 04:43, 06:17, 07:26, 08:38, 09:54, 10:21, 11:36, 12:05, 13:39, 14:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:06:15

1) 这一组画面整体在讲如何通过 RestTemplate 实现两个微服务之间的调用，并集成 Spring Cloud Sleuth 进行链路追踪。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PPT 页面，内容为“2.2.2.2 功能实现”下的“2.2.2.1 微服务A”，并说明需新建名为 SleuthDemo1 的 Maven 工程并引入依赖。PPT 中展示了一个调用链图，前端请求先调用微服务A（节点1和3），再由微服务A调用微服务B（节点2）。
画面2：在 IntelliJ IDEA 中，展示 SleuthDemo1 项目结构，光标位于 TestController.java 文件，该文件中定义了 @RestController 和 @RequestMapping 注解的 TestController 类。
画面3：在 IntelliJ IDEA 中，展示 SleuthDemo2 项目结构，光标位于 application.properties 文件。
画面4：展示 PPT 页面，内容为 Maven 依赖配置，包括 spring-boot-starter-web 和 spring-cloud-starter-sleuth。
画面5：在 IntelliJ IDEA 中，展示 SleuthDemo2 的 application.properties 文件，其中配置了 spring.application.name、server.servlet.context-path、server.port 和 spring.sleuth.enabled。
画面6：在 IntelliJ IDEA 中，展示 SleuthDemo1 的 TestController.java 文件，光标位于类定义处，提示符为 @RestController。
画面7：在 IntelliJ IDEA 中，展示 SleuthDemo1 的 TestController.java 文件，光标位于类定义处，提示符为 @RestController。
画面8：展示 PPT 页面，内容为“2.2.1 案例简介”，说明需创建两个微服务并通过 RestTemplate 实现调用，形成调用链。
画面9：展示 PPT 页面，内容为“4. 启动类”和“5. Controller类”，分别展示 SleuthDemo1Application 启动类和 TestController 控制器类的代码。
画面10：展示 PPT 页面，内容为“3. spring boot配置”和“4. 启动类”，分别展示 application.properties 文件中的配置和 SleuthDemo2Application 启动类代码。
画面11：在 IntelliJ IDEA 中，展示 SleuthDemo2 的 TestController.java 文件，光标位于 node1 方法中，代码为使用 RestTemplate 调用服务1。
画面12：在 IntelliJ IDEA 中，展示 SleuthDemo2 的 TestController.java 文件，光标位于 node2 方法中，代码为使用 RestTemplate 调用服务2。
画面13：展示 PPT 页面，内容为 Maven 依赖配置，包括 spring-cloud-starter-sleuth 和 spring-cloud-dependencies。
画面14：在 IntelliJ IDEA 中，展示 SleuthDemo2 的 TestController.java 文件，光标位于 node2 方法中，代码为使用 RestTemplate 调用服务2。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.3.RELEASE</version>
    <relativePath/>
</parent>
<groupId>com.ithema.msa.sleuthdemo</groupId>

画面4：
<java.version>1.8</java.version>
<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
<spring-cloud.version>Greenwich.RELEASE</spring-cloud.version>
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-sleuth</artifactId>
    </dependency>
</dependencies>
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>${spring-cloud.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

画面5：
spring.application.name=SleuthDemo2
server.servlet.context-path=/sleuth2
server.port=58012
#是否开启sleuth
spring.sleuth.enabled=true

画面9：
@SpringBootApplication
public class SleuthDemo1Application {
    public static void main(String[] args) {
        SpringApplication.run(SleuthDemo1Application.class, args);
    }
    @Bean
    public RestTemplate getRestTemplate() {
        return new RestTemplate();
    }
}

画面10：
spring.application.name=SleuthDemo2
server.servlet.context-path=/sleuth2
server.port=58012
#是否开启sleuth
spring.sleuth.enabled=true

画面11：
@GetMapping("service1")
public String node1(){
    log.info("sleuth_service1");
    String sleuth_service1 = restTemplate.getForObject(url, String.class);
    return "sleuth_service1---"+sleuth_service1;
}

画面12：
@GetMapping("service2")
public String node2(){
    log.info("sleuth_service2");
    return "sleuth_service2";
}

画面13：
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-dependencies</artifactId>
    <version>${spring-cloud.version}</version>
</dependency>

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：标题为“2.2.2.2 功能实现”，子标题“2.2.2.1 微服务A”，图示为前端请求调用微服务A（节点1和3），再由微服务A调用微服务B（节点2）。
画面8：标题为“2.2.1 案例简介”，图示为前端请求调用微服务A（节点1和3），再由微服务A调用微服务B（节点2）。
画面9：标题为“4. 启动类”和“5. Controller类”，分别展示 SleuthDemo1Application 启动类和 TestController 控制器类的代码。
画面10：标题为“3. spring boot配置”和“4. 启动类”，分别展示 application.properties 文件中的配置和 SleuthDemo2Application 启动类代码。

5) 无。
