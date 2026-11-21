# 画面线理解：10-SpringBoot配置-获取数据_2

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\10-SpringBoot配置-获取数据_2_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:22, 01:52, 02:51, 03:12, 03:47, 04:46, 05:31, 05:57, 07:13, 07:41, 08:25, 08:59, 09:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 02:19:55

1) 这一组画面整体在讲如何在 Spring Boot 中使用 @ConfigurationProperties 注解将 YAML 配置文件中的属性绑定到 Java Bean，并演示了配置处理器的使用和相关报错解决。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 application.yml 文件内容，其中定义了 server.port、name、person、address、msg 等配置项，用于演示属性绑定。
画面 2: 切换到 Person.java 文件，准备编写实体类。
画面 3: 编写 Person.java 类，包含 name、age 字段和 getter/setter 方法。
画面 4: 编写 HelloController.java，使用 @Value 注解注入配置属性。
画面 5: 浏览器访问 http://localhost:8082/hello，显示 "hello Spring Boot 222!"。
画面 6: 在控制台输出了从配置文件中读取的属性值，包括 name、age、address、msg。
画面 7: 编写 Person.java 类，添加 address 字段和 setter 方法。
画面 8: 编写 HelloController.java，使用 @Value 注解注入配置属性。
画面 9: 在控制台输出了从配置文件中读取的属性值，包括 name、age、address、msg。
画面 10: 打开 Spring Boot 官方文档，查看 @ConfigurationProperties 注解的说明，了解配置处理器的使用。
画面 11: 在 Person.java 中添加 @ConfigurationProperties(prefix = "person") 注解。
画面 12: 在 application.yml 文件中，将 person 配置项的值修改为 "zhangsan"。
画面 13: 在 application.yml 文件中，将 person 配置项的值修改为 "zhangsan"。
画面 14: 在 Person.java 中添加 @ConfigurationProperties(prefix = "person") 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```yaml
server:
  port: 8082

name: abc
# 1. 基础属性
name: ${name} # zhangsan
age: 20

# 2. 对象属性
person: {name: zhangsan,age: 20}

# 3. 数组
address:
  - beijing
  - shanghai

# 4. 数组属性
address2: [beijing,shanghai]

# 5. 变量
msg1: 'hello \n world' # 不会识别转义字符，会原样输出
msg2: "hello \n world" # 会识别转义字符
```

画面 2:
```yaml
server:
  port: 8082

name: abc
# 1. 基础属性
name: ${name} # zhangsan
age: 20

# 2. 对象属性
person: {name: zhangsan,age: 20}

# 3. 数组
address:
  - beijing
  - shanghai

# 4. 数组属性
address2: [beijing,shanghai]

# 5. 变量
msg1: 'hello \n world' # 不会识别转义字符，会原样输出
msg2: "hello \n world" # 会识别转义字符
```

画面 3:
```java
import org.springframework.stereotype.Component;

@Component
public class Person {
    private String name;
    private int age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
```

画面 4:
```java
import org.springframework.stereotype.Component;

@Component
public class Person {
    private String name;
    private int age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}
```

画面 5:
```java
@Value("${person.name}")
private String name;
@Value("${person.age}")
private int age;
@Value("${person.address}")
private String address;
@Value("${person.msg1}")
private String msg1;
@Value("${person.msg2}")
private String msg2;

@Autowired
private Environment env;
@Autowired
private Person person;

@GetMapping("/hello")
public String hello() {
    System.out.println(name);
    System.out.println(age);
    System.out.println(address);
    System.out.println(msg1);
    System.out.println(msg2);
    System.out.println(person);
    String[] address = person.getAddress();
    for (String s : address) {
        System.out.println(s);
    }
    return "hello Spring Boot!";
}
```

画面 6:
```
hello Spring Boot 222!
```

画面 7:
```yaml
server:
  port: 8082

name: abc
# 1. 基础属性
name: ${name} # zhangsan
age: 20

# 2. 对象属性
person: {name: zhangsan,age: 20}

# 3. 数组
address:
  - beijing
  - shanghai

# 4. 数组属性
address2: [beijing,shanghai]

# 5. 变量
msg1: 'hello \n world' # 不会识别转义字符，会原样输出
msg2: "hello \n world" # 会识别转义字符
```

画面 8:
```java
public void setName(String name) {
    this.name = name;
}

public int getAge() {
    return age;
}

public void setAge(int age) {
    this.age = age;
}

public String getAddress() {
    return address;
}

public void setAddress(String[] address) {
    this.address = address;
}

@Override
public String toString() {
    return "Person{" +
            "name='" + name + '\'' +
            ", age=" + age +
            ", address=" + address +
            '}';
}
```

画面 9:
```java
@Value("${person.name}")
private String name;
@Value("${person.age}")
private int age;
@Value("${person.address}")
private String address;
@Value("${person.msg1}")
private String msg1;
@Value("${person.msg2}")
private String msg2;

@Autowired
private Environment env;
@Autowired
private Person person;

@GetMapping("/hello")
public String hello() {
    System.out.println(name);
    System.out.println(age);
    System.out.println(address);
    System.out.println(msg1);
    System.out.println(msg2);
    System.out.println(person);
    String[] address = person.getAddress();
    for (String s : address) {
        System.out.println(s);
    }
    return "hello Spring Boot!";
}
```

画面 10:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-configuration-processor</artifactId>
    <optional>true</optional>
</dependency>
```

画面 11:
```java
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Component
@ConfigurationProperties(prefix = "person")
public class Person {
    private String name;
    private int age;
    private String[] address;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String[] getAddress() {
        return address;
    }

    public void setAddress(String[] address) {
        this.address = address;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", address=" + address +
                '}';
    }
}
```

画面 12:
```yaml
person:
  name: zhangsan
  age: 20
  address:
    - beijing
    - shanghai
```

画面 13:
```yaml
person:
  name: zhangsan
  age: 20
  address:
    - beijing
    - shanghai
```

画面 14:
```java
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Component
@ConfigurationProperties(prefix = "person")
public class Person {
    private String name;
    private int age;
    private String[] address;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String[] getAddress() {
        return address;
    }

    public
