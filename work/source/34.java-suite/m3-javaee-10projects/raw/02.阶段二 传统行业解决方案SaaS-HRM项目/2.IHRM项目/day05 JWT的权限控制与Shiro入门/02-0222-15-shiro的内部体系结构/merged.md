# 15-shiro的内部体系结构

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\15-shiro的内部体系结构_【海量资源尽在 ubkz.com】.mp4
- 时长 8分32秒（音频 512s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了我们看过了sharewell的一个简单的介绍那接下来呢我们关注的就是sharewell它内部的一个结构以及我们作为一个程序来说使用sharewell重点关注的究竟是哪几个点那么一个一个来看首先就是sharewell的一个内部结构那这边呢以一张图形的形式和各位来分享一下对于sharewell它支持的或者它内部的比较重要的这么几个组件那这张图形呢我放大一点咱们简单的来看一下首先呢
[00:30] 不管是哪一种语言其实都可以去访问我们的share安全框架比如说这边呢有c或者c++写的一些语言或者是pnp或者是其他的一些语言那都可以访问我们的share那访问share的时候需要各位注意的是需要各位注意的是在不同的里面呢都是通过一个叫做subject来进行访问的那所以对于我们要写代码操作其实关注的就是subject
[00:57] 那通过subject各位会发现它会去访问到我们这边总的一个叫做security manager那security manager其实是我们整个sharework框架它最核心的一个内容叫做安全管理器那其实通过这张图不难看说安全管理器要去管理所有所有的组件虽然这些组件还不知道什么意思但是我们就知道它能管理所有组件那管理所有组件的其中有认证器
[01:25] 有授权器那底下还有一些什么什么plugin宝好了rooms那还有这边session managersession do什么catch manager等等全部都是通过security manager经管理所以它是我们整个shareware框架的核心它用来调度整个shareware各个组件的一个运行那它这个我们看过了之后呢接下来就是说那security manager里面呢又包含了一个叫做认证器
[01:54] 又包含了一个叫做我们的授权器底下还有一个什么什么rooms那除了这个还有我们的session managersession deal catch manager那我们先对它有一个大概的了解那subject翻译成中文呢叫做主体我们可以看到如果说我们要想跟shadow进行交互那我们关注的其实就是通过主体去跟我们的shadow框架进行交互那subject其实也可以理解成我们的一些用户的一些数据OK就是谁在用这个框架
[02:23] 那除了Subject之外还有一个叫做Security Manager那Security Manager呢刚才说过了它其实是我们整个框架最核心的一部分这边呢有一个比喻其实就是Sherlock的一个心脏或者是他的一个大脑他控制整个Sherlock框架的所有组件的一个协调运行OK那接下来呢还有认证器那认证器它主要负责的是主体认证主体刚才说过了就是我们要完成一些功能就是你当前这个用户
[02:49] 那负责认证其实这个是我们也可以扩展的一个点可以扩展的一个点它当然也有自己的一些认证的一些机制那认证就是说了你如果用户想要进行登录的话我们subject代表的是用户访问到我们的安全管理器安全管理器立马是不是就是将你的登录的内容委托给认证器帮我们进行认证OK那这个各位要搞清楚那委托给认证那认证器它真的干活吗
[03:20] 抱歉认证器它不会做任何的一些处理因为对于它输入的用户名密码要登录那认证器不知道你的用户名密码是什么不知道你的规则是什么甚至不知道你的数据库究竟在哪所以各位继续往下走走到了RUMS所以对于这张图呢咱们就应该有一个简单的认识Subject调用Supply ManagerManager委托给认证器那认证器里面又找找到RUMSRUMS里面它究竟代表什么含义咱们继续往下看
[03:49] 它可以有一个或者多个RAM可以认为是安全实体的数据源这个其实说的还是比较抽象那这个RAM干嘛呢就是在RAM里面我们可以通过调用不同的数据库去查询你当前的用户数据接着去完成你整个用户认证登录的这么一个过程当然了还有除了认证之外还有一个叫做授权器咱们一起来看一下授权器或者访问控制器是用来判断
[04:17] 你这个人要想完成这个操作有没有相应的功能那这个逻辑又是什么样的各位来看还是刚才这张图如果说你已经登录成功了登录成功了你想要去访问某一个链接那访问某一个链接同样借助Subjects进入到了我们的整个的Security Manager我们的安全管理器那这个时候委托给我们的授权器进行判断那授权器其实它就开始干活了那干活的时候它能知道你当前这个用户是什么它当前有没有这个权限吗
[04:46] 那不能你的权限拦截规则在哪你的权限究竟在哪对它进行复制那怎么找继续委托给RIMS那RIMS有可能也要跟数据库进行交互所以这个时候我们就比较清晰了认证用来登录的那授权是用来判断权限的但是这些数据从哪来全部都是RIMS我们的安全数据数据员当然安全数据其实指的就是我们的用户的一些用户数据那好了这个我们看过了之后还有Session Manager
[05:14] 那session manager大家都知道什么概念了其实就是我们的一个绘画那这个绘画呢其实都是通过session manager进行统一管理那session do那do其实各位也知道就是持久层那对于这个session do是什么意思呢是因为那个share当中它可以自己去定义你的session也就是说完全脱离了我们之前web层的那个session
[05:37] 那我们自己可以定义那自己定义的这个session就有可能要完成对session数据的存储或者存储删除更新等等内容那这些操作怎么办呢session都是你自己定义的那session里面有什么set attribute等等的一些方法那方法究竟该怎么办呢我们自己需要去写我们就接住session do自己去重写好了接着还有一个catch manager
[05:59] 那Catch Manager呢其实就是缓存的一个控制因为我们都知道了这个用户的安全数据包括他具备什么角色包括什么他具有什么权限那这些呢都是不是经常变的不是经常变动的内容我们可以把它缓存起来嘛方便我们的一个使用好了这些呢我们简单的看过了之后我们可以从这张图当中啊第一明白它的内部结构第二可以提取出我们自己要使用Share我们关注的究竟是什么那首先第一件事
[06:28] 不管是认证或者是授权来说第一件事都是通过subject在我们的应用程序当中通过subject是不是去访问subject manager那所以这个subject如何去获取这是我们关注的第一个点那第一个点关注到了之后接着第二个点就是subject开始帮你访问那访问不管是访问认证还是访问我的授权那这两个认证器或者授权器是人家内部的一个机制我们一般很少干预
[06:53] 但是不管是认证还是授权我们是不是都应该获取用户数据那用户数据从哪来是不是就开始访问到不同的Rio或者访问到我们的Rio里面当中那这个Rio是不是跟我们的数据库进行交互那只要设计库你自己私有的内容那你的数据库在哪那你的数据库用户名密码它是怎么设计的它的体系结构是什么那针对这些内容是不是就引申出了Rio我们应该要自己去编写
[07:18] 所以对于我们来说要想玩shareware很简单我们总结出来了对于我们在应用程序当中使用shareware关注的就是应用程序如何获取subject就是我们当前的主体当然了这个就是我们操作用户以及我们通过subject调用security managersecurity manager通过我们的认证器受传器是不是调用到我们的room那这个room里面就是安全数据员我们要跟数据库打交道
[07:47] 那里面的代码是不是我们也要自己洗写啊所以我们总结出来了对于shadow我们自己要使用关注的点就两个第一个如何获取subject第二个如何通过subject得到rium或者咱们注入我们的rium因为rium是通过security manager经管理的那这个rium是我们自己写的以及第三件事如何通过rium获取我们的安全数据所以呢咱们通过内部结构
[08:16] 要让各位知道我们要想在应用程序当中使用shadow关注的点第一个获取subject第二个如何把我们自定的room交给security manager进行管理第三个room里面怎么去完成认证怎么去完成授权这些操作

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Apache Shiro 的内部架构组成及其各核心组件（SecurityManager、Authenticator、Authorizer、SessionManager、Realm、CacheManager）的作用和交互关系。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Shiro 内部结构图，Security Manager 为核心，包含 Authenticator、Authorizer、Session Manager、Cache Manager 等组件，下方连接多个可插拔的 Realm（如 JDBC、LDAP、ActiveDirectory 等），并标注 Subject 是与应用交互的“用户”。
画面 2: 画面 1 的截图，鼠标选中 Security Manager 区域，显示选中区域尺寸为 679 x 218。
画面 3: 画面 1 的截图，鼠标选中 Authenticator 区域，显示选中区域尺寸为 115 x 56，RGB 值为 (177,199,249)。
画面 4: 画面 1 的截图，未进行任何操作，完整展示 Shiro 内部结构图。
画面 5: 画面 1 的截图，底部出现“黑马程序员”和“改变中国IT教育，我们正在行动”的宣传语。
画面 6: 画面 1 的截图，底部出现“黑马程序员”和“改变中国IT教育，我们正在行动”的宣传语，同时鼠标在底部滚动条上。
画面 7: 画面 1 的截图，鼠标选中 Security Manager 区域，显示选中区域尺寸为 61 x 69。
画面 8: 展示 Shiro 内部结构图，Security Manager 为核心，包含 Authenticator、Authorizer、Session Manager、Cache Manager 等组件，下方连接多个可插拔的 Realm（如 JDBC、LDAP、ActiveDirectory 等），并标注 Subject 是与应用交互的“用户”。
画面 9: 展示 Shiro 内部结构图，Security Manager 为核心，包含 Authenticator、Authorizer、Session Manager、Cache Manager 等组件，下方连接多个可插拔的 Realm（如 JDBC、LDAP、ActiveDirectory 等），并标注 Subject 是与应用交互的“用户”。
画面 10: 展示 Shiro 内部结构图，Security Manager 为核心，包含 Authenticator、Authorizer、Session Manager、Cache Manager 等组件，下方连接多个可插拔的 Realm（如 JDBC、LDAP、ActiveDirectory 等），并标注 Subject 是与应用交互的“用户”。
画面 11: 展示 Shiro 应用程序使用示意图，包含 Application Code → Subject → Shiro SecurityManager → Realm 的流程，右侧标注“主体：当前‘用户’（the current user）”、“安全管理者：管理所有 Subject（manages all Subjects）”、“域：安全数据源，通过 Realm 访问安全数据（access your security data）”。
画面 12: 展示 Shiro 应用程序使用示意图，包含 Application Code → Subject → Shiro SecurityManager → Realm 的流程，右侧标注“主体：当前‘用户’（the current user）”、“安全管理者：管理所有 Subject（manages all Subjects）”、“域：安全数据源，通过 Realm 访问安全数据（access your security data）”。
画面 13: 展示 Shiro 应用程序使用示意图，包含 Application Code → Subject → Shiro SecurityManager → Realm 的流程，右侧标注“主体：当前‘用户’（the current user）”、“安全管理者：管理所有 Subject（manages all Subjects）”、“域：安全数据源，通过 Realm 访问安全数据（access your security data）”。
画面 14: 展示 Shiro 应用程序使用示意图，包含 Application Code → Subject → Shiro SecurityManager → Realm 的流程，右侧标注“主体：当前‘用户’（the current user）”、“安全管理者：管理所有 Subject（manages all Subjects）”、“域：安全数据源，通过 Realm 访问安全数据（access your security data）”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
PPT 标题：
- 画面 1: “4.2 Shiro的内部结构”
- 画面 11: “4.3 应用程序使用Shiro”

架构图/流程图结构：
- 画面 1: 上层“CC++/C#/.NET”、“PHP/Ruby/Python”、“Flex/Silverlight/Swing”、“Web MVC”、“Standalone Application”等技术栈通过箭头指向“Security Manager”。
- “Security Manager”向下连接“Authenticator”、“Authorizer”、“Session Manager”、“Cache Manager”。
- “Authenticator”下方连接“Pluggable Realms (1 or more)”，并向下连接“JDBC Realm”、“LDAP Realm”、“ActiveDirectory Realm”、“Custom Realm”等。
- “Session Manager”下方连接“Session DAO”和“Cache”。
- “Cache Manager”下方连接“Cache”。
- “Pluggable Realms (1 or more)”、“Session Manager”、“Cache Manager”等组件下方连接“JDBC”、“LDAP”、“Active Directory”、“Proprietary”、“Memory Realm, etc.”等数据源。
- 画面 11: “Application Code” → “Subject” → “Shiro SecurityManager” → “Realm”。
- 画面 11 右侧标注：
  - “主体：当前‘用户’（the current user）”
  - “安全管理者：管理所有 Subject（manages all Subjects）”
  - “域：安全数据源，通过 Realm 访问安全数据（access your security data）”

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

