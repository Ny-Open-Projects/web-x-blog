# 画面线理解：18.后台服务系统之Dubbo负载均衡策略

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\18.后台服务系统之Dubbo负载均衡策略【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 02:07, 02:53, 03:30, 04:34, 04:58, 05:52, 06:22, 06:56, 07:35, 07:53, 08:54, 09:56, 10:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:37:21

1) 这一组画面整体在讲什么（一句话）：
演示 Dubbo 服务提供者（Provider）与消费者（Consumer）之间的服务调用及负载均衡机制，通过代码和测试验证服务版本与负载均衡策略。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示一个手绘的架构图，包含四个“消费者”节点分别指向两个“UserService”节点，分别标注“版本：1.0”和“版本：2.0”，用于说明服务版本管理或负载均衡场景。
画面 2：展示 Dubbo 官网文档页面，内容为“RoundRobin LoadBalance”和“LeastActive LoadBalance”等负载均衡策略的说明，其中“LeastActive LoadBalance”被高亮。
画面 3：展示 IntelliJ IDEA 中的 `UserServiceImpl.java` 代码，其中 `queryAll()` 方法生成并返回一个包含 10 个 User 对象的列表，每个对象的 ID、密码和用户名按序号生成。
画面 4：展示 IntelliJ IDEA 中的 `UserServiceImpl.java` 代码，其中在 `queryAll()` 方法中添加了 `System.out.println("----------Service 1--------------");` 语句，用于标识服务版本。
画面 5：展示 IntelliJ IDEA 中的 `DubboProvider.java` 代码，其中 `SpringApplicationBuilder` 设置了 `WebApplicationType.NONE`，表示这是一个非 Web 应用。
画面 6：展示 IntelliJ IDEA 中的 `DubboProvider.java` 代码，光标位于 `main` 方法的末尾，准备运行。
画面 7：展示 IntelliJ IDEA 中的 `UserServiceImplTest` 测试类，其中 `@Reference(version = "1.0.0")` 注解用于指定调用的服务版本。
画面 8：展示 IntelliJ IDEA 中的 `UserServiceImplTest` 测试类，其中 `testQueryAll()` 方法中使用 `this.userService.queryAll()` 调用服务，并打印输出。
画面 9：展示 IntelliJ IDEA 中的 `UserServiceImplTest` 测试类，光标位于 `testQueryAll()` 方法的末尾，准备运行。
画面 10：展示 IntelliJ IDEA 中的 `UserServiceImplTest` 测试类，其中 `testQueryAll()` 方法中添加了 `System.out.println("开始调用远程服务 >>>>> " + i);` 语句，用于调试输出。
画面 11：展示 IntelliJ IDEA 中的 `UserServiceImplTest` 测试类，其中 `testQueryAll()` 方法中添加了 `System.out.println("开始调用远程服务 >>>>> " + i);` 语句，用于调试输出。
画面 12：展示 IntelliJ IDEA 中的 `UserServiceImplTest` 测试类，其中 `@Reference(version = "1.0.0", loadbalance = "roundrobin")` 注解用于指定调用的服务版本和负载均衡策略。
画面 13：展示 IntelliJ IDEA 中的 `UserServiceImplTest` 测试类，其中 `@Reference(version = "1.0.0", loadbalance = "roundrobin")` 注解被高亮，表示正在配置负载均衡策略。
画面 14：展示 Typora 编辑器中的文档内容，其中包含 Dubbo 协议的架构图，图中包含“Proxy”、“Codec”、“Serialization”、“Implement”、“ThreadPool”、“Dispatcher”等组件，以及“Client”和“Server”之间的数据流向。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3：
```java
public List<User> queryAll() {
    List<User> list = new ArrayList<>();
    for (int i = 0; i < 10; i++) {
        User user = new User();
        user.setAge(10 + i);
        user.setPassword("123456");
        user.setUsername("username_" + i);
        list.add(user);
    }
    return list;
}
```

画面 4：
```java
user.setAge(10 + i);
user.setPassword("123456");
user.setUsername("username_" + i);
list.add(user);
System.out.println("----------Service 1--------------");
return list;
```

画面 5：
```java
package cn.itcast.dubbo;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.WebApplicationType;
@SpringBootApplication
public class DubboProvider {
    public static void main(String[] args) {
        new SpringApplicationBuilder(DubboProvider.class)
                .web(WebApplicationType.NONE) // 非 Web 应用
                .run(args);
    }
}
```

画面 7：
```java
@Reference(version = "1.0.0")
private UserService userService;
```

画面 8：
```java
@Test
public void testQueryAll() {
    for (int i = 0; i < 100; i++) {
        List<User> users = this.userService.queryAll();
        for (User user : users) {
            System.out.println(user);
        }
    }
}
```

画面 10：
```java
System.out.println("开始调用远程服务 >>>>> " + i);
List<User> users = this.userService.queryAll();
for (User user : users) {
    System.out.println(user);
}
```

画面 12：
```java
@Reference(version = "1.0.0", loadbalance = "roundrobin")
private UserService userService;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14：
架构图标题：“3.2.8. dubbo// 协议”
图中组件从左到右依次为：
- “Proxy” → “Codec” → “Serialization” → “Implement” → “ThreadPool” → “Dispatcher”
- “Client” → “Proxy” → “Codec” → “Serialization” → “Implement” → “ThreadPool” → “Dispatcher” → “Server”
- “Transporter” 在图下方，表示传输层。
图中还包含以下文字说明：
- “Transporter: mina, netty, grizzy”
- “Serialization: dubbo, hessian, java, json”
- “Dispatcher: all, direct, message, execution, connection”
- “ThreadPool: fixed, cached”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
