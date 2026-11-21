# 画面线理解：27.Hystrix&Feign入门案例

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-5 Hystrix的理解和使用
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-5 Hystrix的理解和使用\27.Hystrix&Feign入门案例_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:52, 01:38, 02:38, 03:24, 04:00, 05:07, 06:11, 07:09, 08:01, 10:02, 11:35, 13:08, 14:15, 14:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:20:46

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Cloud 项目中集成 Feign 和 Hystrix，实现服务间的远程调用及熔断降级功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 的“3.1 父工程”章节，说明创建父工程 pom.xml。
画面 2: 在 IntelliJ IDEA 中展示父工程的 pom.xml 文件，高亮显示了 `spring-cloud-dependencies` 依赖。
画面 3: 在 IntelliJ IDEA 中展示 `service-a` 模块的项目结构，准备创建服务代理接口。
画面 4: 在 IntelliJ IDEA 中展示 `service-a` 模块的 `ServiceAgent.java` 文件，定义了 Feign 客户端接口。
画面 5: 在 IntelliJ IDEA 中展示 `service-b` 模块的 `application.properties` 文件，配置了服务端口和上下文路径。
画面 6: 展示课程 PPT 的“2. 引入依赖”章节，列出父工程的依赖配置。
画面 7: 展示课程 PPT 的“3. application.properties”章节，列出 `service-b` 的配置项。
画面 8: 在 IntelliJ IDEA 中展示 `service-a` 的 `ServiceAgent.java` 文件，高亮显示了 `@FeignClient` 注解。
画面 9: 展示课程 PPT 的“5. Hystrix”章节，展示 `ServiceAgentHystrix` 类的代码，实现 `FallbackFactory`。
画面 10: 展示课程 PPT 的“6. Controller”章节，说明 `ServiceAgentHystrix` 类的作用。
画面 11: 展示课程 PPT 的“6. Controller”章节，再次展示 `ServiceAgentHystrix` 类的代码。
画面 12: 在 IntelliJ IDEA 中展示 `service-a` 的 `ServiceAgent.java` 文件，高亮显示了 `@FeignClient` 注解。
画面 13: 在 IntelliJ IDEA 中展示 `service-b` 的 `ServiceAgent.java` 文件，高亮显示了 `@FeignClient` 注解。
画面 14: 在 IntelliJ IDEA 中展示 `service-a` 的 `ServiceAgent.java` 文件，高亮显示了 `@FeignClient` 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.1.3.RELEASE</version>
</parent>

<modelVersion>4.0.0</modelVersion>

<groupId>com.itheima.msa.hystrix</groupId>
<artifactId>feign-hystrix</artifactId>
<version>1.0-SNAPSHOT</version>
<packaging>pom</packaging>
```

画面 2:
```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>Greenwich.RELEASE</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

画面 4:
```java
@FeignClient(name = "feign-hystrix-service-b")
public interface ServiceAgent {
    @GetMapping("/service-b/service")
    String service();
}
```

画面 5:
```properties
server.port=9002
server.servlet.context-path=/service-b
```

画面 6:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
</dependency>
```

画面 9:
```java
@Component
class ServiceAgentHystrix implements FallbackFactory<ServiceAgent> {
    @Override
    public ServiceAgent create(Throwable throwable) {
        return new ServiceAgent() {
            @Override
            public String service() {
                return "service-b熔断...";
            }
        };
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题为“3.1 父工程”，内容为“创建一个名为FeignHystrix的maven工程作为父工程，pom.xml如下所示：”。
画面 6: 标题为“2. 引入依赖”，内容为列出父工程的依赖配置。
画面 7: 标题为“3. application.properties”，内容为列出 `service-b` 的配置项。
画面 9: 标题为“5. Hystrix”，内容为展示 `ServiceAgentHystrix` 类的代码。
画面 10: 标题为“6. Controller”，内容为说明 `ServiceAgentHystrix` 类的作用。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
