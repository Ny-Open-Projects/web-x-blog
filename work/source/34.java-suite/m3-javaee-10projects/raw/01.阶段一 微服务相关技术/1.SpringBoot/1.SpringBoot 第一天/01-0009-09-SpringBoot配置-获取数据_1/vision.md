# 画面线理解：09-SpringBoot配置-获取数据_1

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\09-SpringBoot配置-获取数据_1_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:28, 01:22, 01:58, 02:39, 03:09, 03:56, 04:25, 05:10, 05:56, 06:53, 07:25, 08:12, 08:39, 09:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 02:16:55

1) 这一组画面整体在讲什么（一句话）：
演示 Spring Boot 中使用 @Value、Environment 和 @ConfigurationProperties 三种方式读取配置文件内容。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: PPT 页面，标题为“SpringBoot 配置”，子标题“读取配置内容”，列出三种方式：1) @Value，2) Environment，3) @ConfigurationProperties。
画面 2: IDE 中展示 HelloController.java 代码，其中包含 @RestController 和 @RequestMapping 注解，以及一个返回 "hello Spring Boot 222!" 的 hello 方法。
画面 3: IDE 中展示 HelloController.java 代码，添加了 @Value("${name}") 注解和 private String name 字段。
画面 4: IDE 中展示 application.yml 文件，内容为 server: port: 8082 和 name: abc。
画面 5: IDE 中展示 application.yml 文件，内容更新为 name: zhangsan，person: {name: zhangsan, age: 20}，address: beijing，以及 address2: [beijing, shanghai]。
画面 6: IDE 中展示 application.yml 文件，内容为 person: {name: zhangsan, age: 20}，address: beijing，address2: [beijing, shanghai]，以及 msg1: 'hello \n world'，msg2: 'hello \n world'。
画面 7: IDE 中展示 HelloController.java 代码，添加了 @Value("${person.name}") 和 @Value("${person.age}") 注解，并在 hello 方法中打印 name 和 age。
画面 8: IDE 中展示 HelloController.java 代码，添加了 @Value("${address[0]}") 注解和 private String address 字段，并在 hello 方法中打印 address。
画面 9: IDE 中展示 HelloController.java 代码，添加了 @Value("${msg2}") 注解和 private String msg2 字段，并在 hello 方法中打印 msg2。
画面 10: IDE 中展示 application.yml 文件，内容为 person: {name: zhangsan, age: 20}，address: beijing，address2: [beijing, shanghai]，以及 msg1: 'hello \n world'，msg2: 'hello \n world'。
画面 11: IDE 中展示 HelloController.java 代码，添加了 @Autowired Environment env 字段。
画面 12: IDE 中展示 HelloController.java 代码，添加了 @Value("${msg2}") 注解和 private String msg2 字段，并在 hello 方法中打印 msg2。
画面 13: IDE 中展示 HelloController.java 代码，添加了 System.out.println(env.getProperty("address[0]")); 语句，并在 hello 方法中返回 "Hello Spring Boot 222!"。
画面 14: PPT 页面，标题为“SpringBoot 配置”，子标题“读取配置内容”，列出三种方式：1) @Value，2) Environment，3) @ConfigurationProperties。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
package com.ithema.springboot;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @RequestMapping("/hello")
    public String hello() { return "hello Spring Boot 222!"; }
}
```

画面 3:
```java
package com.ithema.springboot;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @Value("${name}")
    private String name;
    @RequestMapping("/hello")
    public String hello() { return "hello Spring Boot 222!"; }
}
```

画面 4:
```yaml
server:
  port: 8082
name: abc
```

画面 5:
```yaml
server:
  port: 8082
name: zhangsan
person: {name: zhangsan, age: 20}
address: beijing
address2: [beijing, shanghai]
```

画面 6:
```yaml
person: {name: zhangsan, age: 20}
address: beijing
address2: [beijing, shanghai]
msg1: 'hello \n world'
msg2: 'hello \n world'
```

画面 7:
```java
package com.ithema.springboot;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @Value("${person.name}")
    private String name;
    @Value("${person.age}")
    private int age;
    @RequestMapping("/hello")
    public String hello() {
        System.out.println(name);
        System.out.println(age);
        return "hello Spring Boot 222!";
    }
}
```

画面 8:
```java
package com.ithema.springboot;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @Value("${address[0]}")
    private String address;
    @RequestMapping("/hello")
    public String hello() {
        System.out.println(name);
        System.out.println(age);
        System.out.println(address);
        return "hello Spring Boot 222!";
    }
}
```

画面 9:
```java
package com.ithema.springboot;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @Value("${msg2}")
    private String msg2;
    @RequestMapping("/hello")
    public String hello() {
        System.out.println(name);
        System.out.println(age);
        System.out.println(address);
        System.out.println(msg2);
        return "hello Spring Boot 222!";
    }
}
```

画面 10:
```yaml
person: {name: zhangsan, age: 20}
address: beijing
address2: [beijing, shanghai]
msg1: 'hello \n world'
msg2: 'hello \n world'
```

画面 11:
```java
package com.ithema.springboot;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @Value("${msg2}")
    private String msg2;
    @Autowired
    private Environment env;
    @RequestMapping("/hello")
    public String hello() {
        System.out.println(name);
        System.out.println(age);
        System.out.println(address);
        System.out.println(msg2);
        return "hello Spring Boot 222!";
    }
}
```

画面 12:
```java
package com.ithema.springboot;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @Value("${msg2}")
    private String msg2;
    @Autowired
    private Environment env;
    @RequestMapping("/hello")
    public String hello() {
        System.out.println(name);
        System.out.println(age);
        System.out.println(address);
        System.out.println(msg2);
        return "hello Spring Boot 222!";
    }
}
```

画面 13:
```java
package com.ithema.springboot;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @Value("${msg2}")
    private String msg2;
    @Autowired
    private Environment env;
    @RequestMapping("/hello")
    public String hello() {
        System.out.println(name);
        System.out.println(age);
        System.out.println(address);
        System.out.println(msg2);
        System.out.println(env.getProperty("address[0]"));
        return "Hello Spring Boot 222!";
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 和 14: PPT 页面，标题为“SpringBoot 配置”，子标题“读取配置内容”，列出三种方式：1) @Value，2) Environment，3) @ConfigurationProperties。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求完成）
