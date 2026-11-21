# 12-SpringBoot流程分析-初始化

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\12-SpringBoot流程分析-初始化_【海量资源尽在 ubkz.com】.mp4
- 时长 8分15秒（音频 496s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 简单的看了一下Spring Boot里边定义的事件的监听机制接下来我们就可以来说一下Spring Boot启动的一个流程的分析了看一下通过圆满的方式我们看一下Spring Boot在启动的时候到底它做了什么样的事情OK我们一个个来看这个地方我们准备了一张图片这个图太大了所以我们在这个地方用个链接我们一点就可以看到这个图片这个图片在今天的资料里边提供的是有的
[00:28] Spring Boot启动的时候做了这么多事情可以看一下这个图很大那么我们一点一点来看把它缩小一点缩小一点之后我们来看第一部分它干了一些事情橙色的这个地方干了一个初始化的动作待会我们根据原码来看然后第二部分我们看了一下搞了很多这个地方是不是有个监听监听的模块你看Spring Application Run Listener就是刚才我们写的那个玩意儿是吧那么它其实实现了一种观察者的模式观察者跟我们的实现监听的机制其实基本上类似
[00:58] 我们事件监听不是有三个角色吗事件事件员监听器对吧那么观察者有两个一个是被观察者一个是观察者那么那个被观察者其实就是我们的事件和事件员组合在一起他被观察然后观察者呢就可以就是我们的监听器了那么他看到那个被观察者发生变化了他就执行某些操作其实都是一样的逻辑那么在这个地方呢还有很多的一个模块的一个初始化的功能
[01:27] 那么这个我们待会再来看这个图现在你可能看不懂然后最后呢我们看这个地方这个就是Spring Boot的自动配置你看这些我们是不是都讲完了然后通过这个Spring的Factories这个文件对吧获取这个指定的文件这个文件呢在jar 包里面存在在Spring的那个Boot ConfigurationAuto Configuration里面也存在很多的这个文件那么把这些所有的文件里边的类呢都加载到获取的全路径
[01:54] 然后呢通过反射的方式来创建这个对象的实力对吧就是自动配置的原理嘛这一块我们是不是已经讲完了好那么这个图呢我们先放一放待会我们再回过头来看这个图那么现在呢我们在代码里边来通过debug的断点的方式来去看一看这个启动的流程我们在这打个断点然后右键呢我们给它来一个来一个叫做debug的方式debug的方式呢好我们进去启动一下
[02:26] 启动之后那个断点就进来了进来了之后呢我们先说一下这有两个按钮一个呢是step over就是跳过这一行继续执行下一行代码这个step input呢就是进入到这个代码的内部相当于要进入到run方法内部对吧那么我们来int一下int一下之后呢我们就进到了这个run方法好我们把这个呢往这拉一下进到这个run方法之后呢这是个静态的方法那个静态方法里边你看它又调用了另外一个
[02:54] 当前这个类的另外一个静态的软方法因为只有静态方法是不是才能调静态方法那么来进去进去之后呢你注意看又是一个软方法你看其实这两个软方法就是挨着的这个软方法这是一个软方法然后我们直接调用的是这个吧调用的是这个对吧这个呢之后呢它要进到了这个软方法而这个软方法我们就要看一看了这个软方法它创建了一个Spring Application这个对象这个对象刚才我们有一点点印象
[03:24] 哪有印象呢我们在定义我们自己的这个监听的时候是不是需要构造里面传一个Spring Application对吧OK那么这个对象呢我们可以来看一下Spring Application这个对象呢其实就是我们的事件源的对象将来呢所有的事件都是在这个对象上面产生的而这个对象呢有两部分我们要说第一部分呢就是来构造这个对象初始化的过程第二部分呢就是执行它的run方法的过程
[03:53] 那么我们先来说第一件事就是构造初始化这个对象的过程很麻烦的我们点到这个构造方法里边去看一下好在这个地方呢有这么一个这么一个Spring Application的构造函数构造函数里边接收了这么两个参数我们可以把断点呢放过来放过来之后呢你注意看好这开始执行代码了Resource Loader来复制这就不说了然后呢判断它是否为Con为Non这个叫做PrimarySources
[04:23] 主要的Sources就是我们传递过来的我们需要运行的入口的函数入口类启动类引导类其实可以传多个的我们在这就传了一个判断肯定不为难然后搞了一个空的Linux的HashSite这么一个集合然后往下一步这一步就要说一下叫做Web Application Type就是来判断是否是Web的环境
[04:51] 现在我们可以点进去看一下这个里面是否是外部环境呢其实它就是判断有没有对应的像Servlet对应的一些个class对吧OK那么我们再回到之前再看那么现在我们不是外部的环境是吧不是外部环境因为我没有导那个外部的坐标我们点一下看
[05:11] 你看它说不是web的环境这个返回的一个字幕串是None对吧如果你点了导了web的环境这个字幕串将来会返回比如说你用Tomcat的话它返回的是Solid然后接下来这两个就要说一下了一个是设置你初始化的InitializersInitializers这个东西刚才我们看到了是不是我们自己实现了一个就是我自己的一个Initializers对吧还有我们还要实现设置所有的一些监听器
[05:40] 那么这两个东西呢从哪来呢东西它要从我们的SpringFactories文件里边去加载了你看这个地方是不是都是SpringFactoriesOK然后呢我们下一步你可以看一下Initial Letters现在这个地方呢有了之后我们来看一下这个this里边的Initial Letters好找一下啊来看一下是不是有这么七个不仅有我们自己定义的你看我们自己定义的有吧
[06:06] OK 我们自己定义的有对不对而且人家也系统提供了很多个initial letters系统提供的那么同样的监听器我们也可以往下走一步来看一下listenerslisteners你可以看一下有10个这是listeners这个listeners跟我们刚才定义的那个不太一样待会我们来说他们的一个区别它就是application listener它现在有10个我们自己定义的mine不在这里边执行
[06:32] 我们定义的那个叫做SpringRoundListener跟它还不太一样其实我们定义的这个SpringRoundListener是对这个原生的ApplicationListener的一个封装好那么初始化的过程呢基本上就是来去干啥呢基本上就是来判断你有没有主类对吧主类的意思呢就是你有一个问方法的那个类如果没有的话呢可能就报错了
[06:55] 然后第二个呢他去判断是否是web的环境现在呢我们不是web的环境啊因为是web的环境呢他家里的资源可能要更多一些然后第三个呢搞了两个集合啊相当于这两个集合呢一个是把我们的需要调用的初始化的initial layers这么一些东西呢其实它都是一些监听啊放到了一个集合里边去对吧然后呢又搞了另外一个集合listeners这个集合也搞了进去了这些东西从哪来的呢从配置文件里边来的但是这些东西
[07:25] 还没有执行仅仅是把他们名字获取出来了而已仅此而已就是搞了一个名字而已把他们放到一个集合里边去了就这个意思好嘞那么这个初始化的过程就完事了我们可以来看这个图看这个图我们把它缩小一点来看第一个部分Spring Boot的开始开始之后呢你看构造一个新的Spring Boot Application的应用对吧然后呢初始化这个模块初始化干啥呢配置一些source呀判断是否是web环境呀然后初始化去构造啊
[07:55] 然后创建一个应用的监听器这个地方其实仅仅是把他们搞过来了并没有开始执行他们的因为执行他们是待会我们要去触发对应的事件才会执行他们的对吧配置应用的方法所在的主类等等好初始化的动作我们就先讲到这个地方

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
分析 Spring Boot 应用的启动流程，从主函数调用到初始化监听器、配置环境、创建工厂等核心步骤。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: PPT 标题页，显示“Spring Boot 启动流程分析”，并提示将展示“Spring Boot启动流程.png”。
画面 2: 展示 Spring Boot 启动流程图，包含“new SpringApplication”、“initialize 初始化模块”、“SpringApplicationRunListener”、“ConfigurableEnvironment”等模块及其相互关系。
画面 3: 展示 Spring Boot 启动流程图的下半部分，重点是“获取传入的工厂类名、类路径”、“Spring Boot 自动化配置”、“生成工厂类实例”等步骤。
画面 4: IDE 中显示项目结构和主类 `SpringBootListenerApplication.java`，其中包含 `@SpringBootApplication` 注解和 `SpringApplication.run(...)` 方法。
画面 5: IDE 中显示 `SpringApplication.java` 的源码，展示 `run` 方法的实现，包括 `new ConfigurableApplicationContext` 和 `run` 方法的调用。
画面 6: IDE 中显示 `MySpringApplicationRunListener.java` 的源码，展示 `starting` 和 `environmentPrepared` 方法的实现。
画面 7: IDE 中显示 `SpringApplication.java` 的源码，调试器停留在 `deduceMainApplicationClass` 方法中。
画面 8: IDE 中显示 `SpringApplication.java` 的源码，调试器停留在 `deduceMainApplicationClass` 方法中，变量 `this.mainApplicationClass` 被赋值。
画面 9: IDE 中显示 `SpringApplication.java` 的源码，调试器停留在 `deduceMainApplicationClass` 方法中，变量 `initializers` 数组内容被展示。
画面 10: IDE 中显示 `SpringApplication.java` 的源码，调试器停留在 `deduceMainApplicationClass` 方法中，变量 `listeners` 数组内容被展示。
画面 11: IDE 中显示 `SpringApplication.java` 的源码，调试器停留在 `deduceMainApplicationClass` 方法中，变量 `listeners` 数组内容被展示。
画面 12: IDE 中显示 `SpringApplication.java` 的源码，调试器停留在 `deduceMainApplicationClass` 方法中，变量 `listeners` 数组内容被展示。
画面 13: IDE 中显示 `SpringApplication.java` 的源码，调试器停留在 `deduceMainApplicationClass` 方法中，变量 `listeners` 数组内容被展示。
画面 14: 展示 Spring Boot 启动流程图，与画面 2 类似，但部分节点文字略有不同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```java
package com.itheima.springbootlistener;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SpringBootListenerApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringBootListenerApplication.class, args);
    }
}
```

画面 5:
```java
public static ConfigurableApplicationContext run(Class<?>[] primarySources,
                                                 String... args) {
    return run(new SpringApplication(primarySources), args);
}

public static ConfigurableApplicationContext run(Class<?>[] primarySources,
                                                 String[] args) {
    return new SpringApplication(primarySources).run(args);
}
```

画面 6:
```java
package com.itheima.springbootlistener.listener;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.context.config.ConfigurableApplicationContext;
import org.springframework.context.ApplicationListener;
import org.springframework.core.Ordered;
import org.springframework.core.annotation.Order;

public class MySpringApplicationRunListener implements SpringApplicationRunListener {

    @Override
    public void starting() {
        System.out.println("项目启动中...");
    }

    @Override
    public void environmentPrepared(ConfigurableApplicationContext environment) {
        System.out.println("环境对象已准备");
    }
}
```

画面 7:
```java
public SpringApplication(ResourceLoader resourceLoader, Class<?>... primarySources) {
    this.resourceLoader = resourceLoader;
    this.primarySources = new LinkedHashSet<>(Arrays.asList(primarySources));
    this.webApplicationType = WebApplicationType.deduceFromApplicationContext();
    this.initializers = new ArrayList<>();
    this.listeners = new ArrayList<>();
    this.mainApplicationClass = deduceMainApplicationClass();
}
```

画面 8:
```java
private Class<?> deduceMainApplicationClass() {
    try {
        StackTraceElement[] stackTrace = new RuntimeException().getStackTrace();
        for (StackTraceElement stackTraceElement : stackTrace) {
            if ("main".equals(stackTraceElement.getMethodName())) {
                return Class.forName(stackTraceElement.getClassName());
            }
        }
    } catch (ClassNotFoundException ex) {
        // Ignore
    }
    return null;
}
```

画面 9:
```java
private Class<?> deduceMainApplicationClass() {
    try {
        StackTraceElement[] stackTrace = new RuntimeException().getStackTrace();
        for (StackTraceElement stackTraceElement : stackTrace) {
            if ("main".equals(stackTraceElement.getMethodName())) {
                return Class.forName(stackTraceElement.getClassName());
            }
        }
    } catch (ClassNotFoundException ex) {
        // Ignore
    }
    return null;
}
```

画面 10:
```java
private Class<?> deduceMainApplicationClass() {
    try {
        StackTraceElement[] stackTrace = new RuntimeException().getStackTrace();
        for (StackTraceElement stackTraceElement : stackTrace) {
            if ("main".equals(stackTraceElement.getMethodName())) {
                return Class.forName(stackTraceElement.getClassName());
            }
        }
    } catch (ClassNotFoundException ex) {
        // Ignore
    }
    return null;
}
```

画面 11:
```java
private Class<?> deduceMainApplicationClass() {
    try {
        StackTraceElement[] stackTrace = new RuntimeException().getStackTrace();
        for (StackTraceElement stackTraceElement : stackTrace) {
            if ("main".equals(stackTraceElement.getMethodName())) {
                return Class.forName(stackTraceElement.getClassName());
            }
        }
    } catch (ClassNotFoundException ex) {
        // Ignore
    }
    return null;
}
```

画面 12:
```java
private Class<?> deduceMainApplicationClass() {
    try {
        StackTraceElement[] stackTrace = new RuntimeException().getStackTrace();
        for (StackTraceElement stackTraceElement : stackTrace) {
            if ("main".equals(stackTraceElement.getMethodName())) {
                return Class.forName(stackTraceElement.getClassName());
            }
        }
    } catch (ClassNotFoundException ex) {
        // Ignore
    }
    return null;
}
```

画面 13:
```java
private Class<?> deduceMainApplicationClass() {
    try {
        StackTraceElement[] stackTrace = new RuntimeException().getStackTrace();
        for (StackTraceElement stackTraceElement : stackTrace) {
            if ("main".equals(stackTraceElement.getMethodName())) {
                return Class.forName(stackTraceElement.getClassName());
            }
        }
    } catch (ClassNotFoundException ex) {
        // Ignore
    }
    return null;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: 流程图结构：
- “new SpringApplication” 指向 “initialize 初始化模块”。
- “initialize 初始化模块” 指向 “SpringApplicationRunListener”。
- “SpringApplicationRunListener” 指向 “创建配置环境 (web/notweb)”。
- “创建配置环境 (web/notweb)” 指向 “配置监听”。
- “配置监听” 指向 “Spring Boot 自动化配置”。
- “Spring Boot 自动化配置” 指向 “生成工厂类实例”。
- “生成工厂类实例” 指向 “获取传入的工厂类名、类路径”。
- “获取传入的工厂类名、类路径” 指向 “Spring Boot 自动化配置”。
- “Spring Boot 自动化配置” 指向 “生成工厂类实例”。
- “生成工厂类实例” 指向 “获取传入的工厂类名、类路径”。
- “获取传入的工厂类名、类路径” 指向 “Spring Boot 自动化配置”。
- “Spring Boot 自动化配置” 指向 “生成工厂类实例”。
- “生成工厂类实例” 指向 “获取传入的工厂类名、类路径”。
- “获取传入的工厂类名、类路径” 指向 “Spring Boot 自动化配置”。
- “Spring Boot 自动化配置” 指向 “生成工厂类实例”。
- “生成工厂类实例” 指向 “获取传入的工厂类名、类路径”。
- “获取传入的工厂类名、类路径” 指向 “Spring Boot 自动化配置”。
- “Spring Boot 自动化配置” 指向 “生成工厂类实例”。
- “生成工厂类实例” 指向 “获取传入的工厂类名、类路径”。
- “获取传入的工厂类名、类路径” 指向 “Spring Boot 自动化配置”。
- “Spring Boot 自动化配置”

