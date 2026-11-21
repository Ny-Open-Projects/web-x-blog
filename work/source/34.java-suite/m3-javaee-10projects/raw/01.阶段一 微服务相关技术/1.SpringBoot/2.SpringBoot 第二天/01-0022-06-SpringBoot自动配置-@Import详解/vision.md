# 画面线理解：06-SpringBoot自动配置-@Import详解

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\06-SpringBoot自动配置-@Import详解_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:16, 02:18, 03:04, 03:49, 04:48, 05:34, 06:26, 08:06, 09:12, 10:44, 11:32, 12:09, 13:11, 13:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 08:56:21

1) 这一组画面整体在讲 SpringBoot 中 @Import 注解的四种使用方式，包括导入 Bean、配置类、ImportSelector 实现类和 ImportBeanDefinitionRegistrar 实现类。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示 IntelliJ IDEA 项目结构，项目名为 springboot-enable，包含 src/main/java 和 src/main/resources 目录，以及 pom.xml 文件。
画面 2: 显示 SpringBootEnableApplication.java 文件内容，其中使用了 @Import(User.class) 注解导入 User 类。
画面 3: 显示运行结果，控制台输出了获取到的 User 对象信息。
画面 4: 显示 SpringBootEnableApplication.java 文件内容，其中使用了 context.getBean(User.class) 获取 User 对象。
画面 5: 显示 UserConfig.java 文件内容，其中定义了 @Configuration 注解的类，并使用 @Bean 注解定义了 User 和 Role 两个 Bean。
画面 6: 显示 SpringBootEnableApplication.java 文件内容，其中使用了 context.getBean(Role.class) 获取 Role 对象。
画面 7: 显示在 IDEA 中搜索 @Import 注解相关的类，结果中包含 ImportBeanDefinitionRegistrar、AutoConfigurationImportSelector 等类。
画面 8: 显示项目结构，其中包含 MyImportSelector.java 文件。
画面 9: 显示 ImportBeanDefinitionRegistrar.java 文件内容，其中定义了 registerBeanDefinitions 方法。
画面 10: 显示 MyImportBeanDefinitionRegistrar.java 文件内容，其中实现了 registerBeanDefinitions 方法，用于注册 User Bean。
画面 11: 显示 SpringBootEnableApplication.java 文件内容，其中使用了 @Import(MyImportBeanDefinitionRegistrar.class) 注解导入自定义的 Bean 定义注册器。
画面 12: 显示 SpringBootEnableApplication.java 文件内容，其中使用了 context.getBean(name: "user") 获取 Bean，但控制台提示找不到类型为 com.ithema.domain.Role 的 Bean。
画面 13: 显示 ImportSelector.java 文件内容，其中定义了 selectImports 方法。
画面 14: 显示 PowerPoint 幻灯片，标题为“SpringBoot 配置”，内容为“@Import 应层依赖于 @Import 注解导入一些类，使用 @Import 导入的类会被 Spring 加载到 IOC 容器中。而 @Import 提供 4 中用法：① 导入 Bean ② 导入配置类 ③ 导入 ImportSelector 实现类。一般用于加载配置文件中的类 ④ 导入 ImportBeanDefinitionRegistrar 实现类。”

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 2:
```java
@Import(User.class)
public class SpringbootEnableApplication {
    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(SpringbootEnableApplication.class, args);
        Object user = context.getBean("user");
        System.out.println(user);
    }
}
```

画面 4:
```java
Map<String, User> map = context.getBeansOfType(User.class);
System.out.println(map);
```

画面 5:
```java
package com.ithema.config;

import com.ithema.domain.Role;
import com.ithema.domain.User;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class UserConfig {
    @Bean
    public User user() {
        return new User();
    }
    @Bean
    public Role role() {
        return new Role();
    }
}
```

画面 6:
```java
Role role = context.getBean(Role.class);
System.out.println(role);
```

画面 7:
```java
@Import(User.class)
@ComponentScan("com.ithema.config")
@EnableAutoConfiguration
public class SpringbootEnableApplication {
    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(SpringbootEnableApplication.class, args);
        Object user = context.getBean("user");
        System.out.println(user);
    }
}
```

画面 10:
```java
package com.ithema.config;

import org.springframework.beans.factory.support.BeanDefinitionBuilder;
import org.springframework.context.annotation.ImportBeanDefinitionRegistrar;
import org.springframework.core.type.AnnotationMetadata;

public class MyImportBeanDefinitionRegistrar implements ImportBeanDefinitionRegistrar {
    @Override
    public void registerBeanDefinitions(AnnotationMetadata importingClassMetadata, BeanDefinitionRegistry registry) {
        registry.registerBeanDefinition("user", BeanDefinitionBuilder.rootBeanDefinition().getBeanDefinition());
    }
}
```

画面 11:
```java
@Import(User.class)
@Import(UserConfig.class)
@Import(MyImportBeanDefinitionRegistrar.class)
public class SpringbootEnableApplication {
    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(SpringbootEnableApplication.class, args);
        Object user = context.getBean("user");
        System.out.println(user);
    }
}
```

画面 12:
```java
Object user = context.getBean(name: "user");
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14: PPT 标题为“SpringBoot 配置”，内容为“@Import 应层依赖于 @Import 注解导入一些类，使用 @Import 导入的类会被 Spring 加载到 IOC 容器中。而 @Import 提供 4 中用法：① 导入 Bean ② 导入配置类 ③ 导入 ImportSelector 实现类。一般用于加载配置文件中的类 ④ 导入 ImportBeanDefinitionRegistrar 实现类。”

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。
