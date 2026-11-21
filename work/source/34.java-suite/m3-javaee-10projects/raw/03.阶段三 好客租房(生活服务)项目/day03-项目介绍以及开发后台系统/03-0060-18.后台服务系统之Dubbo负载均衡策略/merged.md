# 18.后台服务系统之Dubbo负载均衡策略

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\18.后台服务系统之Dubbo负载均衡策略【海量资源尽在 ubkz.com】.mp4
- 时长 10分14秒（音频 615s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面呢我们来说一下这个服务的负载坠痕啊这个是什么意思呢其实我们可以简单来画一个图啊大家就应该能够明白了那么就是说我们呢在我们的这个服务的这个提供方这一端呢比如说呢我们同样一个服务注意是同一个服务啊同一个服务呢假设我们又启动了有多个啊多个这个服务那么来画一下比如说我们有多个这个服务它是同一个服务啊
[00:28] 那么比如说还是我们前面所说这个User Service我们写的这个User Service把这个字体的颜色呢调一下颜色调成颜色黑色好那么这个就是我们的User Service这个服务那么假设呢我们这个User Service我们启动了多个我启动了多个我有好多这个User Service那么我是不是就会在我的注册中心里面是不是注册有这么多的一些这个
[00:59] 我的服务那么现在问题来了那么我这个是我的一个服务的一个消费者对吧服务的一个消费者消费者那么我这个服务的消费者那么是不是需要通过去拿到我的这个服务的一个提供者是不是才能够去做一个执行那么问题就是说在我的注册中心里面有四个那么问题我到底是我应该访问他呢还是说我应该访问他呢还是我应该访问下面他
[01:29] 那么究竟访问哪一个呢所以这个里面就会有个策略叫什么呢就叫负载均衡那么默认情况下呢这个double呢所使用的是一种叫做random就是随机随机调用就是说你我在选择选择调用的时候我也可能选择它我下一次选择有可能调用这个再下一次有可能选择调用它再下一次有可能直接调用还是原来这个
[01:53] 哎这是一种随机的一种策略啊那么double呢其实被我们提供了有多种的这种策略我们可以来看一下那么附带均衡它有多种啊呃这种随机还有轮旋还有叫什么呢最少活跃调用次数的还有一次性一次性哈希的这种调用的方式啊
[02:11] 那么其实大家都大同小异啊所以呢我们给大家去演示一个这个轮巡吧演示个轮巡因为他默认是不是就随机啊那么为了我们先验证这个随机我们再做一个轮巡的一个测试啊那么我们先把我们这刚刚的测试用力呢我们简单的去做一个这个改造啊那么我们这样我们把这个我们这个服务的这个提供者啊我们多给他启动几个注意看一下我们的测试啊
[02:39] 多启动几个那么什么叫多启动几个呢这么来玩那么为了看一个效果呢我是这样来做一个测试那么我们在这个里面啊把它全部都关掉然后呢我进入了我这个实现类那么我在这个里面呢就打印一句话吧打印一句话打印什么呢随便打一点内容啊这个这个无所谓比方说我们这个叫叫Service什么呢1service1这个服务好嘞那么行了
[03:09] 那我就启动它吧启动走那么我是不是就启动了我第一个这个Service第一个Service把它删除掉等待它的一个启动那么一旦我的我要调用这个方法是不是就会打印这个service1好等待它的一个重新启动好现在是不是就启动完成了那么接下来呢我再改一下啊我改成service2然后呢我注意啊你改只改这个位置不行啊
[03:45] 那么我们还需要呢改这个配置文件那么这个端口你不能重复对吧这个端口就不能重复的就是说你的这几个服务啊对吧它的端口是不能重复的如果重复的话那么在同一台机器那肯定是不能做一个监听的对不对如果说你每一个服务它都在一个不同的机器的话那么端口是可以一样的这个相信大家都能够理解那么改成20881然后呢我再来启动我这个服务走但是你发现好像启动不了因为我们这个IDL默认呢
[04:15] 给我们这个启动这个就是启动的这个Raw所启动的它是一个叫什么的单力的这种单实力的方式启动那么我们把它调一下改成一个多实力的怎么调呢点击这个editor然后选择它把这些勾给它去掉把这些勾去掉那我就可以启动多个了走是不是我又启动了一个对吧那么我接下来呢又可以去改一下我改成这个service3我给它启动三个吧
[04:45] 然后这个改成20882然后呢我再来启动我这个服务的提供者那么是不是相当于我现在有三个服务的这个提供者一个是服务服务一一个是服务二一个是服务三好把它清空掉那么我们进入到我们的刚刚的可视化这个界面中我们来查看一下那么能我们来看一下究竟他有几个几个这个服务搜一下demodemo
[05:22] 找不到了吗来搜一下没有提示Demo来了点击它搜索然后点击这个Detail发现你看在这个位置是不是有三个这个提供者三个提供者好那么接下来呢我们就去我们的消费者这一端然后呢我们去做一个调用那我们来看一下做Test这个测试用力这个位置
[05:52] 点到他然后呢在这个里面呢这样我们呃我们这个这个代码还先不改啊先不做修改我们在这个位置呢先去做一个比如说我们调用100次吧调100次呃然后呢把这个代码考到这来就是说我们做一个循环我们去调用100次然后呢每一次调用完之后啊我都做一个sleep比如说1000我去呃停这个一秒钟啊一秒钟啊加一个这个tracket
[06:22] 好嘞然后呢我启动我的一个服务的一个服务的一个消费者启动这样我还打一句话吧就是说在打印完应该是在每一次循环的时候我打一句话开始调用我的这个远程远程的服务对吧然后呢我加一个什么呢加一个i把它加进去好然后呢我再来启动看一下效果
[06:57] 那么我们要看什么效果呢是不是看前面的他的这个输出那么究竟是有没有规律的一种输出对不对因为他默认的一种策略是不是就是随机啊我们来看一下他有没有一种规律啊好等待他的一个调用的执行把它呢清掉好等待他的一个来我们就选中他啊查看他的一个输出啊现在还没有还没有启动啊我们稍等一下
[07:25] 稍等一下看它会怎么样看它能不能够实现这种随机这种效果那这样已经来了已经开始调用了调用了然后我们来看一下它调用的service3那么service2调用了这么多service1也这么多你看3相对少一点对吧对吧看到了吗是不是就是基本上是比较随机的去调用对吧基本随机的去调用
[07:51] 看到这个效果了吧哎OK好那么这样那么我把这个消费者我消费者的我给他停掉给他停掉停掉之后啊我把这个里面的内容给他清空我改一下他这个策略啊改一下策略我给他改成什么呢改成这种轮旋的这种方式那么这个策略怎么改呢其实我们在注解这个位置添加一个什么呢添加一个这个load bonus这样的一个属性那么就可以了
[08:19] 把它靠过来就是我们采用的这种负载均衡的策略我们采用轮循轮循是什么意思呢是不是就是你有三个服务是不是一次一次调用我第一次我第一次调用这个我第二次调用这个我第三次调用这个那我第四次呢是不是开始调用这个这个这个再回到这样的一种节奏
[08:40] 哎呀OK这个大家能够理解吧就是轮旋的一个效果好那么现在我们把这个消费者呢也启动起来那我们再来看一下我们的这个服务的提供者那么他是如何去打印这个效果的OK那么等待他的一个启动等待他的一个启动那么把这个呢停空掉放到这来看一下他应该马上就会有这个输出等待一下啊等待一下
[09:19] 目前还没有输出来了开始输出了好嘞那么我们来看一下这是消费者1消费者2消费者3然后呢是不是回消费者1下面消费者2是不是消费者3回到消费者1消费者2你看马上消费者3是不是轮序效果你看再看一下又来一次对吧又来一次
[09:46] 又来一次你看这样的话是不是就是一种轮行的效果那么OK这个意思其实就是指的就是我们是不是已经设置了它的一个负载均衡改变了它的一个负载均衡的一个策略OK那么我们其实讲一个大家就学会举一反三了那么如何调用下面的是不是就都一样了OK好你可以看一下这样去做一个调用OK好那么关于这个负载均衡我们就讲到这里OK好嘞

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

