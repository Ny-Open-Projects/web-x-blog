# 画面线理解：11-SpringBoot事件监听

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\11-SpringBoot事件监听_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 05:35, 06:55, 10:20, 11:21, 12:58, 15:20, 16:26, 17:46, 19:10, 20:36, 21:38, 22:33, 23:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:01:52

1) 这一组画面整体在讲什么（一句话）：
讲解 SpringBoot 应用程序的监听机制，包括 SpringApplicationRunListener、ApplicationRunner、ApplicationListener 等接口的使用和执行时机。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: PPT 标题页，显示“SpringBoot 监听机制”。
画面 2: IDE 中展示项目结构，选中了 SpringApplicationRunListeners.java。
画面 3: 展示 SpringApplicationRunListener.java 中的 contextPrepared、contextLoaded、started、running 方法及其注释。
画面 4: 在 IDE 中右键点击 MySpringApplicationRunListener.java，弹出菜单。
画面 5: 在 IDE 中搜索并选中 ApplicationRunner.class。
画面 6: 展示 Spring Boot 源码中 ApplicationRunner 接口的定义。
画面 7: 编写 MyApplicationRunner 类，实现 ApplicationRunner 接口，并在 run 方法中打印 args.getSourceArgs()。
画面 8: 编写 MyApplicationContextInitializer 类，实现 ApplicationContextInitializer 接口，并在 initialize 方法中打印信息。
画面 9: 运行 SpringBootListenerApplication，控制台输出了 MyApplicationContextInitializer 的初始化信息。
画面 10: 展示 SpringApplicationRunListener 的源码，其中包含 starting、environmentPrepared、contextPrepared、contextLoaded、started、running、failed 等方法。
画面 11: 控制台输出了 MySpringApplicationRunListener 的 starting 方法执行信息。
画面 12: 在 MySpringApplicationRunListener 中重写 starting 方法，打印“starting...项目启动中”。
画面 13: 展示 Spring Boot 源码中 org.springframework.boot.context.event 包下的类结构。
画面 14: 在 MySpringApplicationRunListener 中重写 environmentPrepared、contextPrepared、contextLoaded、started、running、failed 方法，分别打印对应阶段的信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
void contextPrepared(ConfigurableApplicationContext context);
// Called once the application context has been loaded but before it has been
// refreshed.
// @param context the application context

void contextLoaded(ConfigurableApplicationContext context);
// The context has been refreshed and the application has started but
// @link CommandLineRunners and @link ApplicationRunners have not been called.
// @param context the application context.
// @since 2.0.0

void started(ConfigurableApplicationContext context);
// Called immediately before the run method finishes, when the application context
// has been refreshed and all @link CommandLineRunners and @link ApplicationRunners
// have been called.
// @param context the application context.

void running(ConfigurableApplicationContext context);
// Called when a failure occurs when running the application.
// @param context the application context or @code null if a failure occurred before
// the context was created.
```

画面 4:
```java
starting() {
    out.println("Starting...项目启动中");
}

environmentPrepared(ConfigurableApplicationContext context) {
    out.println("environmentPrepared...上下文对象开始准备");
}

contextLoaded(ConfigurableApplicationContext context) {
    out.println("contextLoaded...上下文对象加载完成");
}

started(ConfigurableApplicationContext context) {
    out.println("started...上下文对象加载完成");
}

running(ConfigurableApplicationContext context) {
    out.println("running...项目启动完成，开始运行");
}

failed(ConfigurableApplicationContext context, Throwable exception) {
    out.println("failed...项目启动失败");
}
```

画面 6:
```java
/**
 * Interface used to indicate that a bean should {@code run()} when it is contained
 * within a {@link SpringApplication}. Multiple {@link ApplicationRunner} beans can be
 * defined within the same application context and can be ordered using the {@link Ordered}
 * interface or the {@link @Order} annotation.
 * @author Phillip Webb
 * @since 1.3.0
 */
@FunctionalInterface
public interface ApplicationRunner {
    void run(ApplicationArguments args) throws Exception;
}
```

画面 7:
```java
package com.theima.springbootslistener.listener;

import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class MyApplicationRunner implements ApplicationRunner {
    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println("ApplicationRunner...run");
        System.out.println(args.getSourceArgs());
    }
}
```

画面 8:
```java
package com.theima.springbootslistener.listener;

import org.springframework.context.ApplicationContextInitializer;
import org.springframework.context.ConfigurableApplicationContext;

@Component
public class MyApplicationContextInitializer implements ApplicationContextInitializer {
    @Override
    public void initialize(ConfigurableApplicationContext applicationContext) {
        System.out.println("ApplicationContextInitializer...initialize");
    }
}
```

画面 10:
```java
void starting();

// Called once the environment has been prepared, but before the
// @link ApplicationContext has been created.
// @param environment the environment

void environmentPrepared(ConfigurableEnvironment environment);

// Called once the @link ApplicationContext has been created and prepared, but
// before sources have been loaded.
// @param context the application context

void contextPrepared(ConfigurableApplicationContext context);

// Called once the application context has been loaded but before it has been
// refreshed.
// @param context the application context

void contextLoaded(ConfigurableApplicationContext context);

// Called once the application context has been refreshed and the application has started but
// @link CommandLineRunners and @link ApplicationRunners have not been called.
// @param context the application context.

void started(ConfigurableApplicationContext context);

// Called immediately before the run method finishes, when the application context
// has been refreshed and all @link CommandLineRunners and @link ApplicationRunners
// have been called.
// @param context the application context.

void running(ConfigurableApplicationContext context);

// Called when a failure occurs when running the application.
// @param context the application context or @code null if a failure occurred before
// the context was created.
```

画面 12:
```java
public class MySpringApplicationRunListener implements SpringApplicationRunListener {
    @Override
    public void starting() {
        System.out.println("starting...项目启动中");
    }
}
```

画面 13:
```java
package org.springframework.boot.context.event;

import org.springframework.context.ApplicationEvent;
import org.springframework.context.ApplicationListener;
import org.springframework.context.event.ApplicationContextEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.context.event.ContextStoppedEvent;
import org.springframework.context.event.ContextClosedEvent;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework
