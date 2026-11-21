# 15_通用说明_事务管理配置

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\15_通用说明_事务管理配置【海量资源尽在 666java.com】.mp4
- 时长 6分12秒（音频 372s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们再来去设置另外一个类啊就是关于事务管理的一个配置类那这个配置类呢咱们呢可以直接考过来啊咱们简单读一读因为呢在一个项目中呢咱们只要去设置一次事务就可以了这个在板呢不要求会写只要求能够看明白就可以好吧那放到这之后啊咱们简单来读一读啊好首先呢把这个导向包啊long book这也是long book啊
[00:32] 那有报错啊报错咱们去找一找啊把这个也找一下吧好那没有报错了啊这标红的话咱们一会再说好吧你看这个类啊这个类里边呢是关于事物的一个配置类那配置里边呢主要是有三个方法第一个是初始化一个事物管理器然后第二个呢是设置一个事物的拦截器然后第三个呢咱们就可以去设置一个切面主要是包含了当前的一个什么一个
[01:06] 通知和一个什么切点表达式好咱们一路再说首先咱们从第一个开始讲啊那首先呢你要初始化一个事物管理器呢你要先知道你要初始化一个什么样的事物管理器咱们都知道啊不同的持久层技术呢是要去使用不同的这种事物管理器目前呢咱们采用的本项目采用的是买白地址所以说咱们用的是
[01:31] DataSourceTransactionManager如果说你是HybridNet或者JPA的话你要去设置对应的这种数换了器才行好那这个啊这是一个AdBit大家都知道啊这个的话就是把当前的返回值放到Sprinter容器中对吧那这个你要创建它之后呢首先你要去设置一个参数这个参数就是当前的数据源那数据源的话呢其实在咱们之前的上一个节课呢咱们已经把它给
[02:00] 创建出来了就是当前这个MySQLDataSource是吧那这时候呢你可以把它给录进来直接考到这就可以了啊好那标红其实没有问题啊这个它只是没有识别但是子编容器中到底有没有呢哎肯定是有的因为我在这是不是已经定义了是吧这个没有关系啊那行啊那这个呢是就是初熟化了一个15关键器然后下面再看啊
[02:27] 下面呢下面是一个叫设置事物的拦截器主要拦截的是某一些方法某一些方法你看啊我的鼠标上面选中的这些东西呢主要呢就是一些增伤改查是吧下面呢是一些查询那查询跟增伤改查有什么区别吗有区别什么区别呢主要就是它的事物的方式是不一样的你看啊你看上面这个事物呢它是一个propagation required那这个呢就是什么意思呢
[02:57] 它这是默认的一个事物的传播行为对吧就是说当前有事物我就用当前的事物如果没有事物呢我就新创建一个事物对吧保证一直有事物去执行然后下面这个呢查询事物呢它也是啊也是履块的但是有一点不同就是在这去设置了什么设置了一个什么
[03:19] read only就是只读对吧OK这块你千万不要说错了啊就是说在查询的时候咱们才会去设置只读的事物好吧那行啊最终呢咱们这块也算是创建完了然后最后呢最后咱们是有一个东西啊就是咱们需要去创建一个这种七面那七面里面包含两部分啊第一部分呢就是创建一个什么defund point cut advisor是吧这里边第一部分就是point cut
[03:46] 其实就是当前的切入点表达式第二个就是MySQL当前他们创建这个拦截器就是当前的这个拦截器当然这会儿咱们需要去给个名称名称其实跟它保持一致就可以好这样的话咱们就算是完了这里边刚才说了这个切入点表达式其实怎么来的就是在咱们配置文件中已经定义了这种方式跟刚才那个
[04:18] 跟刚才这个myserver中是一样的啊也是从配置文件中去读读完之后这个有设的一个前缀最终是tsscanpackage就在咱们这其实已经设了这么个东西他就会默认去拦截Service下面所有的类和所有的方法进行事物的增强好吧那行啊那这里边还有一个事需要大家注意啊
[04:43] 哪个事呢就是当前呢就加了两个新的诸解一个是 s pack 定义的商前是一个切面啊这个必须要加然后第二个呢是要去开启这种什么s 派系的自动代理那这自动代理的话他默认的采用的呢是当前的 cg live那还有一个啊这里边还有一个诸解就是要去应用或者开启当前的 trisection management有开启他你当前的事务管理好吧那行
[05:12] 那这个呢就是事务管理配置类好那咱们这个就介绍到这里那这个介绍完之后啊咱们再顺便来说一说另外一个东西啊就是当前的所有的环境配置里边有一个实体类和miper文件存放的位置啊那这在哪呢那这个主要的是在当前的一个model里边啊model里边所有的实体类呢都是在某一个业务包下边
[05:40] 咱们去讲具体业务的时候还会再去说但是里边有一个东西就是咱们的所有的MIPRO接口呢都是存放到了当前的这个MIPRO4下边所有对应的映射文件呢都在resource这个目录resourceMIPRO4下边我说这也是对应的当前业务模块下边都去定义好了那好啊那这个目录结构呢大家呢应该是去熟悉一下那好到目前为止呢咱们这个所有的环境准备工作呢
[06:10] 都已经做完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring 框架中通过配置类 TransactionConfig 实现数据源和事务管理器的初始化，并结合注解方式配置事务拦截器，最终实现对指定方法的事务控制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 TransactionConfig.java 文件内容，包含 @Configuration、@EnableTransactionManagement、@PropertySource 注解，以及初始化数据源和事务管理器的代码。
画面2：展示项目结构，重点在 mysql-core 包下的 TransactionConfig.java 文件，以及其依赖的 mysql-core-jdbc.properties 配置文件。
画面3：展示 TransactionConfig.java 中配置事务拦截器的代码，使用 @Bean 注解创建 Advice，并通过 AspectJ 表达式匹配指定包下的方法。
画面4：展示 TransactionConfig.java 中配置事务拦截器的代码，使用 @Bean 注解创建 Advice，并通过 AspectJ 表达式匹配指定包下的方法。
画面5：展示 MysqlCoreConfig.java 文件内容，定义了数据源的配置，包括数据库连接信息和最大连接数。
画面6：展示 TransactionConfig.java 中初始化数据源和事务管理器的代码。
画面7：展示 TransactionConfig.java 中配置事务拦截器的代码，使用 @Bean 注解创建 Advice，并通过 AspectJ 表达式匹配指定包下的方法。
画面8：展示 TransactionConfig.java 中配置事务拦截器的代码，使用 @Bean 注解创建 Advice，并通过 AspectJ 表达式匹配指定包下的方法。
画面9：展示 TransactionConfig.java 中配置事务拦截器的代码，使用 @Bean 注解创建 Advice，并通过 AspectJ 表达式匹配指定包下的方法。
画面10：展示 TransactionConfig.java 中配置事务拦截器的代码，使用 @Bean 注解创建 Advice，并通过 AspectJ 表达式匹配指定包下的方法。
画面11：展示 TransactionConfig.java 中初始化数据源和事务管理器的代码。
画面12：展示 TransactionConfig.java 文件内容，包含 @Configuration、@EnableTransactionManagement、@PropertySource 注解，以及初始化数据源和事务管理器的代码。
画面13：展示 PPT 页面“6.4.3 实体类及 Mapper”，说明实体类按模块划分，Mapper 接口单独在一个包下。
画面14：展示 PPT 页面“7.1 文章列表后端开发”，展示项目结构图，说明实体类、Mapper 接口包、Mapper 文件路径等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import org.springframework.context.annotation.Configuration;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.transaction.annotation.EnableTransactionManagement;

