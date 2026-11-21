# day05-19-Hmily实现注册-用户中心

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-13 Hmily框架
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-13 Hmily框架\day05-19-Hmily实现注册-用户中心_【海量资源尽在 666java.com】.mp4
- 时长 12分49秒（音频 769s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们已经在注册功能当中把这个Harmony框架的相关的环境给搭建好了搭建好之后呢咱接下来就开始动手实现功能我们要实现的功能就是在注册功能当中去解决分布式设问题其实这个代码的编写包括整个步骤啊套路啊跟前面那个转账那个例子基本上是一模一样
[00:31] 只不过前面那个例子是业务是什么转账咱这是什么注册其实其他基本上都是差不多的那咱首先第一步要搞定的事就是先分清楚咱们注册这个业务当中谁是事务发起方谁是事务参与方这个大家应该清楚咱们前面是不是提到过这个图吗咱看讲义里边吧讲义里边这个图这里边我们是不是说
[01:02] 这个涉及到两个微服务们一个用户中心一个统一账号服务那这里边谁调用谁啊对用户中心去调用统一账号服务也就是说我们发请求是先请求谁啊用户中心那因此谁应该是事务的发起方对用户中心就是consumer这边统一账号呢account这边应该是事务的对参与方所谓接下来的话我们先搞定哪一块的代码事务发起方就是consumer这边然后呢我们再搞定
[01:32] 事务的参与方就是account这表带嘛分开啊这样清晰一些那咱先看事务发起方consume这边我们先干的第一件事就是搞定配置Hemily相关的配置那这块配置呢咱考虑到啊考虑到将来有可能咱们P2P项目别的这个地方啊或者别的业务也有可能会用什么呀Hemily对吧他也有可能要搞这些配置所以说呢我们准备吧
[02:03] Harmony这一块相关的配置呢还是放到Apollo当中把它存储到这个什么呀通用模板这个项目当中建立成什么公共的Name Space这个咱以前的套路是不是就这么玩的对不对所以你看我这已经打开了Apollo咱找到这个通用配置模板这个项目点进去点进之后呢你看咱这个资产而下过一遍这里边是不是还没有加什么呀Harmony相关的对配置
[02:32] 所以说我们这需要新添加一个什么呀name space这个name space呢我们要新创建一个而且这要选择什么呀公共的那这个名字的话咱要跟讲义保持一致吧把这个名字给它粘过来Ctrl C前边的这一块就不要了这个前缀前面有了咱就是从对从这开始就行了公共的公共的
[03:04] 这儿备注想写可以不写可以我们这儿加上HMILY相关Page就行了好我们点击提交公共的是不是就可以被其他项目去关联是不是然后呢我们需要往里边加一些配置在最下面这边目前不就是还是空的吗对不对我们点击文本点击什么呀修改然后去讲义里边
[03:34] 把这一块配置给它粘贴过来这块配置咱前面在讲转账的例子的时候是不是都说过了你还有印象吗这是设置虚拟化工具的对不对这是重视的最大的次数这是存储化的不是持久化存储的方式我们数据库这个非常重要咱说的话这个是什么对初表示是事物的发起房FORCE表示事物的参与方对然后这个数据库你注意看了这一点非常重要
[04:05] 这个还记得咱前面搭建环境的时候提过我们是不是单独创建了一个数据库就这个是不是这个数据库目前是空的吗将来Harmony会自动往这里边建表来存储什么信息对日志信息所以说你这儿呢要指定指定这个数据库的名字找着密码你看着自己设置就行了加进来之后呢我们提交然后还要进行什么呀发布对发布这是Harmony相关的这个配置吧
[04:39] 我们先放到Apollo里边然后还没完啊咱们说了咱现在是不是在呃整事务发起房这边的代码对不对那他这边是不是要关联这个什么呀这个哈密的这个配置就是从呃扩办这个通用模板项目当中要把这个哈密的配置给关联过来那我们还得去Apollo里边找到谁呢找到consumer好这里边肯定没有哈密相关的配置吗我们在这要点一添加这是不是要进行什么呀
[05:10] 对关联关联哪个呢咱刚才新建的那个嘛找一找还没了啊往下滚动一下就这个是吧好点击提交成功了成功之后呢我们再回来啊回来我们去下面看一看这个配置是不是就有了吗对不对有了之后呢你先不要着急你也得想一想我们针对consumer这边这个相关的这些配置需不需要进行修改覆盖啊
[05:41] 看看有没有需要进行修改覆盖想想我们这个Consumer这边是不是正好就是事物的发起方这个值就应该为什么呀True那其他的你看还需要进行修改覆盖了没有没有是吧没有那你直接就关联过来就OK了这边相当于就有这个配置了所以说这是配置这一块咱基本上搞定搞定完之后呢大家还有印象吧咱当时转账的时候是不是还有相关联的一个什么配置类吗Hemily那个配置类你有印象吗这一块
[06:11] 它最终是不是就是要要产生一个这个Harmony这个事物的一个引导对象是不是那这个代码呢咱直接粘过来就行了从资料里边就这个我能Ctrl C给它粘到什么地方呢咱打开Consumer这个微服务这里边应该咱之前是不是应该有个Configure包吧咱正好放到这个Configure包里边对不对Ctrl VOK好粘过来粘过来看看这个里边只要没报错你就不用管它了
[06:44] 这个代码跟当时转账那个是一模一样这你就不用管它了这个配置类不就是读取刚才那些配置这是这件事然后接下来就是我们要改造咱们之前这个注册的这个代码注册功能咱其实都已经实现过了就是需要加上什么呀Harmony这个事务控制那都需要动哪些地方的代码呢大家看一下首先就是启动类上咱别忘了要把Harmony这个API的这个路径
[07:17] 扫描的这个路径给他加上去这以前肯定是没加嘛呃咱找找consumer的这个启动类加到哪加到哪哎你看好啊稍微有点不太一样你看这是不是有expressbootapplication对不对你看这个地方是不是这以前是排除了一下这个mongo吗这些路径其实当时都没有加那咱这一块把整个这块给他拷进去就行了我们粘过来
[08:03] 粘过来之后你最好要检查一下啊这个标点符号对吧之类的这些东西看这里边有没有报错包括这个路径啊你一定要检查检查因为我讲一里边这个路径跟你的项目当中这些路径不一定是完全什么呀一模一样了你最好是亲自再检查一下啊这是这一块我们要修就是修改以前的一个代码对吧还有还有就是这个非硬代理刚才咱说过了咱是不是要在consumer里边去远程调用这个谁啊可抗它吗
[08:32] 所以咱以前在实现注册功能的时候这儿是不是有一个呃一个非营代理就是一个接口对吧现在呢我们要在这个接口的方案上面加上这个什么呀Hemily的这个注解然后全部都要进行这个事务管理事务控制所以要找到以前的代码这个代理是不是咱放到这个而进他这个包里边了啊咱找一下就是这个那么在这个方法上面啊这不是在进行远程调的那个方法吗对不对在这我们要加上对Hemily这个注解就行了
[09:02] 这需要大家注意的这个倒一下包它自动倒过了稍微反应有点慢这块代码你需要修改一下你看这些东西其实是不是咱前面在搞定转账的时候是不是都是这么做的对不对然后再往下就是核心的这个业务代码就是实现注册的这个业务代码那这里边的话我们要把之前的这些代码稍微改造一下最终的话是要搞定三块就是tryconfirm还有什么cancel就是这三块代码
[09:34] 要稍微改造改造那么我们原来这个实现注册的这个方法上面要要加什么呀这还没这个注解相当于这块就是trytry然后呢在这呢要指定什么呀confirm这个代码是哪一块还有这个什么呀cancel执行的这个代码是哪一块我们需要把这块代码给他加上去那咱一个一个来吧咱先找到这应该是业务层嘛对不对consumer的业务层consumer的业务层咱找一找
[10:04] 我们要找到这个注册就是这个这是注册啊那我们现在呢就需要在这个注册上干什么呀对在注册上加这个注解而且要设置这两个方法我们加上at h m i还没啊然后呢指定两个方法一个叫 c o n对呃这个方案的名字呢咱一会再加然后接下来还有一个叫 c a n c l 对吧要指定两个方法看这是不是
[10:39] 然后呢这两个方法呢非常简单我就直接粘过来不再重新敲了非常非常简单你就放在这个谁啊放在注册的下边吧就放到这吧紧挨着他们粘过来之后稍微调一下就行了对这个log是咋回事还需要我自己倒包吗咱这里边是不是没加日志吧这边没有加日志啊没有加日志的话我看看嗯当时
[11:24] 当时我们是呃咱这就给他加上那个那个叫什么slf4g是吧加上就行了这样之后呢咱看一下这块代码这呢是不是那个执行confirm那个操作的对不对那咱注册的时候呢这里边其实没有啥具体业务需要执行我们就是打印个日日就行了那么cancel这一块就需要做什么事了需要回滚啊
[11:57] 因为在之前注册的时候他是不是执行了一个保存你看这对吧那现在出问题了我就需要把刚才保存的那条数据给干什么对remove掉也是根据手机号这个代码大家应该都能看到remove就是跟这个save是一个什么相反的操作回滚一定是跟try里边代码是什么对做的事是相反然后最后别忘了把这两个名字给他加到这个地方在这
[12:27] 好这里给他加到这这就OK了啊这个代码基本上就改造好了这是咱们哪一块的代码这是咱们事务发起方啊就是consumer这边代码我们就已经全部给他改造好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Apollo 配置中心为 consumer-Service 项目配置 Hmily 分布式事务相关参数，并修改服务端代码以实现注册、确认和取消功能。

2) 按时间顺序列出每张画面的要点：
画面1: 显示文件资源管理器，当前路径为“wanningp2p > day05 > 资料”，包含多个项目文档和图片。
画面2: Apollo配置中心页面，显示“common-template”应用下的多个公共命名空间，包括 micro_service.spring-boot-mysql、micro_service.spring-boot-http 等。
画面3: Apollo配置中心页面，显示“application”应用下的多个公共命名空间，包括 micro_service.spring-boot-mysql、micro_service.spring-boot-http 等。
画面4: SQLyog Professional 64 界面，显示数据库连接和表结构，当前打开的是 p2p_undo_log 表。
画面5: Apollo配置中心页面，显示“consumer-Service”应用的配置页面，尚未加载任何配置。
画面6: Apollo配置中心页面，显示“consumer-Service”应用的配置列表，包含多个 Hmily 相关配置项，如 org.dromara.hmily.serializer、org.dromara.hmily.retryMax 等。
画面7: IDEA 编辑器界面，显示 Hmily 事务配置代码，包括设置事务启动、配置数据库连接、用户名和密码等。
画面8: IDEA 编辑器界面，显示 Hmily 事务配置代码，包括设置事务启动、配置数据库连接、用户名和密码等。
画面9: IDEA 编辑器界面，显示多个窗口，包括 Apollo 配置中心、adminService、ApolloPortal、configservice 等，以及 ConsumerServiceImpl 代码。
画面10: IDEA 编辑器界面，显示 ConsumerServiceImpl 类的代码，包含 checkMobile、getMobile、register 方法。
画面11: IDEA 编辑器界面，显示 ConsumerServiceImpl 类的代码，包含 register 方法的详细实现，包括设置用户名、密码、保存等操作。
画面12: IDEA 编辑器界面，显示 ConsumerServiceImpl 类的代码，包含 checkMobile、getMobile 方法。
画面13: IDEA 编辑器界面，显示 ConsumerServiceImpl 类的代码，包含 cancelRegister 方法，其中包含日志记录和调用 restResponse 的代码。
画面14: IDEA 编辑器界面，显示“4.3.1 事务发起：consumer-Service”章节，包含在 Apollo 中新增的 Hmily 配置项和在 consumer-Service 项目中添加的 @Configuration 注解类。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面7代码：
```java
hmilyTransactionBootstrap.setRepositorySupport(env.getProperty("org.dromara.hmily.repositorySupport"));
hmilyTransactionBootstrap.setStarted(Boolean.parseBoolean(env.getProperty("org.dromara.hmily.started")));
HmilyDbConfig hmilyDbConfig = new HmilyDbConfig();
hmilyDbConfig.setDriverClassName(env.getProperty("org.dromara.hmily.hmilyDbConfig.driverClassName"));
hmilyDbConfig.setUrl(env.getProperty("org.dromara.hmily.hmilyDbConfig.url"));
hmilyDbConfig.setUsername(env.getProperty("org.dromara.hmily.hmilyDbConfig.username"));
hmilyDbConfig.setPassword(env.getProperty("org.dromara.hmily.hmilyDbConfig.password"));
hmilyTransactionBootstrap.setHmilyDbConfig(hmilyDbConfig);
return hmilyTransactionBootstrap;
```

画面14配置：
```properties
org.dromara.hmily.serializer = kryo
org.dromara.hmily.retryMax = 30
org.dromara.hmily.repositorySupport = db
org.dromara.hmily.started = true
org.dromara.hmily.hmilyDbConfig.driverClassName = com.mysql.cj.jdbc.Driver
org.dromara.hmily.hmilyDbConfig.url = jdbc:mysql://localhost:3306/p2p_undo_log?
org.dromara.hmily.hmilyDbConfig.username = root
org.dromara.hmily.hmilyDbConfig.password = 123
```

```java
@Configuration
@EnableAspectJAutoProxy(proxyTargetClass = true)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14 PPT标题：“4.3 功能实现”、“4.3.1 事务发起：consumer-Service”。
表格数据：
| Key | Value | 备注 | 最后修改人 | 最后修改时间 |
| --- | --- | --- | --- | --- |
| org.dromara.hmily.serializer | kryo |  | apollo | 2019-08-07 09:58:54 |
| org.dromara.hmily.retryMax | 30 |  | apollo | 2019-08-07 09:58:54 |
| org.dromara.hmily.repositorySupport | db |  | apollo | 2019-08-07 09:58:54 |
| org.dromara.hmily.started | true |  | apollo | 2019-08-07 09:58:54 |
| org.dromara.hmily.hmilyDbConfig.driverClassName | com.mysql.cj.jdbc.Driver |  | apollo | 2019-08-07 09:58:54 |
| org.dromara.hmily.hmilyDbConfig.url | jdbc:mysql://localhost:3306/p2p_undo_log? |  | apollo | 2019-08-07 09:58:54 |
| org.dromara.hmily.hmilyDbConfig.username | root |  | apollo | 2019-08-07 09:58:54 |
| org.dromara.hmily.hmilyDbConfig.password | 123 |  | apollo | 2019-08-07 09:58:54 |
| useUnicode | true |  | apollo | 2019-08-07 09:58:54 |

5) 不要评价画面美观，不要输出与课程无关的内容。

