# 09-Activiti7与SpringBoot整合-SpringSecurity配置信息

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\09-Activiti7与SpringBoot整合-SpringSecurity配置信息_【海量资源尽在 ubkz.com】.mp4
- 时长 14分1秒（音频 841s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那下一个步骤我们就开始啊来做我们的SplitBoot所依赖的这个SplitSecurity这个框架的一些相关的配置啊我们先也可以一起来刷新一下我们整个的这个工程啊好我们可以这样啊来刷一下它的这个myWin依赖啊那刚才我们所添加的这些坐标所对应的这个价包应该都会被导入到我们的这个library啊导入到我们的这个扩展library里头来
[00:31] 我们一起来看一下整个的这个过程中的确是引入了很多相关的这个坐标对吧那这个坐标中我们来找一找是否已经把我们的这个Spring Securite对应的这个坐标也都添加进来了这个各位可以看到我们在引入的时候把Spring Securite所对应的这个坐标都已经添加进来了那加入了Spring Securite这个框架之后
[01:00] 我们在早期课程中应该各位同学已经学习过SplintSecret我们就需要去做我们SplintSecret本身所需要用到的一些配置项这样的一些配置项我们有同学就会思考我们是否要自己到这里头来写一写这一次我在这边主要就是比如说我再去搞一个新的package
[01:28] 将来就去放我们相关的一些配置比如说叫做itk叫点acti viti比如说来一个叫做demo好或者是直接叫做activity这样就可以了点ok然后我们所对应的sprint-circuit整合所需要用到的相关的配置信息我们肯定是需要加入进来的对吧
[01:57] 这样的配置信息怎么去弄如果你要去写的话肯定是需要消耗很多时间的我们这一次别忘了我们早期给各位提供的资料中还有我们所对应的开发势力对吧在开发势力中你将我们的主峰值或者是开发者的峰值直接解压出来比如说我解压出来了就在这里面这个时候我们早期所
[02:25] 给各位所介绍所需要用到的像我们的这个Spring像我们用到的这个Spring Secureit我们来找一下整合所需要用到的这个配置文件中我们就可以去添加一个Secureit的油条工具类这个类我们其实是不需要自己去写它可以直接找到除了添加这个Secureit油条这个工具类我们还可以去
[02:51] 添加我们的configuration的配置类这个部分我们可以这样做来我们走一下到我们的类子里面我们直接去搜索一下到这里面去搜索一下搜索一下我们的sqlite我们的有一个叫做securit1sqlite的U条对吧
[03:15] 各位你就可以发现在我们这里边有好几个包底下都有这样的一个类对不对我们直接就可以拿过去直接就可以拿过去这样我们就可以直接去使用了好比如说我这个时候点进去对吧这个类其实就已经本身是写好的我现在要点的是直接进到目录下里头去对不对我们可以看一下在搜索的结果中我现在可以去
[03:44] 找到它对吧找到它好我这个时候看一下它所对应的这个文件的位置在哪各位我们现在可以找到它发现它是在我们的exampleweb example对吧web example底下就有我现在就可以直接去找到我们的这个文件所在的位置叫做web example就这个部分打开它
[04:16] 找我们的Java内对不对好我们可以去看一下它刚才的具体的位置是在哪个地方去了我们再看一下刚才我搜索的文件的位置是叫做secretor我们再看一下不是在这个下面应该是另外一个应该是另外一个
[04:53] 我把这个路径再好好看一下activity API sprint整合的事例刚才看错了我们这个时候就可以整合的这个事例对吧这个部分来找到我们的src找到我们的java logoactivity example好这时候各位就可以看到我们有一个叫secret油条这样的一个工具类对不对这个工具类我呢
[05:21] 这边因为我也要用Split Secure来进行一些测试所以我就需要把它加入进来同时我们这边还需要用到一个叫做Demo Application Config这个也是我们的Example事例中本身就提供有的它里面放置了有我们的用户权限的一些配置信息我们也可以直接拿过来用其实就在这个目录下Demo Application Config A型
[05:50] 这时候我们就可以copy把它直接拿到我们的项目中来看巧威,对吧好,然后OK好,这样呢各位就可以看到我们所需要用到的两个部分都已经添加进来其中第一个是Circulate油条它作为一个component的组件我们将来就可以直接用Eta AutoVal
[06:15] 因为在整个Splint容器中进行管理的我们可以用Ata AutoVal来实现对Secure的油条的用用这是一个部分各位可以看到我们整个这个地方就有一个叫做Logging As来实现模拟或者说我们登录的时候我们需要去用到的一个这样的用到一个这样的类Logging As通过这种方式我们就可以来实现我们
[06:44] 相关用户的这个用户用户身份信息的一些获取那我们还有一个是叫做demoobligation configuration是这个类这个类呢它在这上面呢加了有一个叫做eta configuration说明它是我们的一个配置类那这个配置类里面各位同学可以看到我们这边呢提供的这个用户的信息都放在这里面当然这个
[07:13] 当然我们的这个用户组的信息不全啊应该我们才这里边还能够找到一个更全面的这个类这一点呢我们也可以来尝试找一下可以吗copy一下啊好那就再次回到我们的这个master 峰之下啊我这时候呢再去要找的是他对不对你发现呢有好几个地方其实都有他啊这是整合的啊我们看看这个部分
[07:39] 这是activity API WebExample这是API WebExample我们可以看一下这个里头所对应的用户角色信息就更多一些我在这里面打算就用这个类可以吧这样的话我就可以直接进入到API WebExample中去找到它对不对比如说API WebExample是这个
[08:10] API web example这个我对应的进入到src进入到我们的这个java到这里边我们去找到它就是这一下那copy那这样的话我就相当于打算去更新一下我们的这个demo application configuration的这个类我把原来的这个类从我们的从我们的这个目录底下
[08:37] 比如说给它,真正啊,给它delete删掉啊,OK那它就删除了啊然后呢,我在这里边加入我们新的这个叫demo-application-configuration,可以吧control v啊没有加入进来是吧复制一下啊复制,对吧然后呢,control v啊,来到这来,OK好,这样它就加入进来了啊它跟之前的那个类啊,其实写法上是一
[09:06] 其实写法上是基本上一样的然后我们可以看到的是它在这里面它的用户角色信息更多一些了对不对我们就把它直接也加入也把它引入进来这两个类直接引入进来后我们应该说Spring和我们的Activity和我们的Spring Boot整合进来的Spring Secreter所需要用到的配置信息
[09:35] 基本上我们就从我们的这个demo示例中直接拿出来了拿出来下一步我们再去做工作的话就是呢它真正将来是不是circulate要去连接我们的这个mycircle数据库对不对那我们连接mycircle数据库的时候这个地方就需要引入我们的这个相关的这个yaml配置文件那这个yaml配置文件呢
[10:03] 我们这一次就不打了不打这个YAML配置文件了那我从我们的这个里边copy一下把它也把它也作为我们今天给各位的一个资料可以吗然后放到我们的基本资料中那我们整合的时候这个application的yml这个文件呢我们也是需要直接加入进来的那对于我而言我应该是在这个部分找到我们的这个resource对吧
[10:32] 在这里面直接把我们的application的yml这个文件直接加入进来当然有同学说我要自己打你要自己打的话我认为这个地方也不是说不行只是说这个地方比较简单对不对我们可以这样做直接还是复制过来你要自己去打的话直接去新建一个spleen的yaml配置文件就可以了
[11:01] 我们直接还是control v这样扔进来扔进来这个时候我们就可以直接在这里头看到我们数据库连接相关的一些配置信息如果你要打的话你就把这个地方删了自己试试也是可以的因为本身没有什么难度好我们可以看到这一次我们连接的真正的数据库是叫做activity对吧这样的话就要求我们保证
[11:28] 我们的系统中必须有一个在那库对不对否则的话你就不能够连接成功用户名密码在那些帐户信息也需要设置一下对不对好我们可以Service.msc我们来看一下我们的myseq服务我再走一下这是我们的myseq服务给它起起来然后我们这时候再到这个部分来找一下我们的
[11:58] activity的库目前我们的activity库是有的所以说它基本上就已经具备了我们myseq数据库也是已经有的连接也配好了驱动也有然后我们sprint-secret这样的准备工作也做好了对不对下面还要做工作的话就是我们的真正我们的BPMN文件需要我们自己去画
[12:27] 然后就可以去做一些测试了对不对好这是我们在这个部分给各位啊做的一些环境上的准备啊主要是我们的这个Spring Secrets所需要用到的两个类我们要加载进来它一个是配置类啊一个是我们这个读取用户信息的一个工具类啊就是这两个部分然后呢我们为了将来能够使得我们Activity背后所操作的库
[12:56] 有相应的连接信息这个部分我是直接复制过来的没有去打如果它没有打的话你就直接这样去写在这个地方就可以写上我们的叫做Spring Boot这个打错了应该是Spring Data Source其实这里面都有提示我们整个写起来应该是很快速就可以写完就这样的然后它的具体的
[13:25] driver就是它对不对然后你再去写的话就是下一项的对吧就是我们的比如说还有像user name吧user name也都这么去写Spring Data Source的user name还有像password等等这样的一些信息那这个部分我们借助于提示可以快速的给它整完对吧非常简单好当我们一切条件都准备充足之后我们整个
[13:55] 整个的环境准备基本上就给各位讲完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成 Activiti7，包括添加依赖、配置 SpringSecurity 安全框架、使用新 API 实现工作流开发等步骤。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面，标题为“Spring Boot 整合 Activiti7 的”，列出整合步骤：1. 添加 Spring Boot 整合 Activiti7 的坐标；2. 添加 SpringSecurity 安全框架的整合配置信息；3. 使用 Activiti7 新支持的类来实现工作流开发；4. 使用新的 API 实现工作流开发，主要包括流程定义查询、启动流程实例、任务的查询、任务的完成。
画面 2: 展示 IntelliJ IDEA 中的 Maven 项目结构和 pom.xml 文件内容，其中包含 Activiti7 的 Spring Boot Starter 依赖。
画面 3: 展示课程 PPT 页面，标题为“3.1 Spring Boot 整合 Activiti7 的”，内容与画面 1 相同。
画面 4: 展示 Windows 资源管理器，路径为“activiti-examples-master”，列出多个 Activiti 示例项目文件夹。
画面 5: 展示 Windows 资源管理器，路径为“activiti-api-spring-integration-example”，列出 DemoApplication.java、DemoApplicationConfiguration.java 和 SecurityUtil.java 等文件。
画面 6: 展示 IntelliJ IDEA 中 SecurityUtil.java 文件内容，其中包含 @Component 注解、@Autowired 注解和 loginAs 方法。
画面 7: 展示 Windows 资源管理器，路径为“activiti-examples-master”，列出 DemoApplicationConfiguration.java 和 SecurityUtil.java 文件。
画面 8: 展示 IntelliJ IDEA 中 DemoApplicationConfiguration.java 文件内容，其中包含 @Configuration 注解和 configure 方法，用于配置 UserDetailsService。
画面 9: 展示 IntelliJ IDEA 中 DemoApplicationConfiguration.java 文件内容，其中包含 configure 方法的详细代码，用于创建 InMemoryUserDetailsManager 并注册用户。
画面 10: 展示 Windows 资源管理器，路径为“activiti-api-spring-integration-example”，列出 DemoApplicationConfiguration.java 文件。
画面 11: 展示 IntelliJ IDEA 中 pom.xml 文件内容，其中包含 Activiti7 的 Spring Boot Starter 依赖。
画面 12: 展示 Windows“服务”管理器界面，显示 MySQL 服务状态为“已启动”。
画面 13: 展示 IntelliJ IDEA 中 SecurityUtil.java 文件内容，其中包含 loginAs 方法。
画面 14: 展示 IntelliJ IDEA 中 application.yml 文件内容，其中包含数据库连接配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<project>
    <dependencies>
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-spring-boot-starter</artifactId>
            <version>7.0.0.Beta2</version>
        </dependency>
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis</artifactId>
            <version>3.4.5</version>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>5.1.7</version>
        </dependency>
    </dependencies>
    <build>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </build>
</project>
```

画面 6:
```java
@Component
public class SecurityUtil {
    @Autowired
    private UserDetailsService userDetailsService;

    public void loginAs(String username) {
        UserDetails user = userDetailsService.loadUserByUsername(username);
        if (user == null) {
            throw new IllegalStateException("User " + username + " doesn't exist, please provide a valid user name.");
        }
        SecurityContextHolder.setContext(new SecurityContextImpl(new Authentication() {
            @Override
            public Collection<? extends GrantedAuthority> getAuthorities() { return user.getAuthorities(); }
            @Override
            public Object getCredentials() { return user.getPassword(); }
            @Override
            public Object getDetails() { return user; }
            @Override
            public Object getPrincipal() { return user; }
            @Override
            public boolean isAuthenticated() { return true; }
            @Override
            public void setAuthenticated(boolean b) throws IllegalArgumentException {}
        }));
    }
}
```

画面 8:
```java
@Configuration
public class DemoApplicationConfiguration {
    @Bean
    public UserDetailsService myUserDetailsService() {
        InMemoryUserDetailsManager inMemoryUserDetailsManager = new InMemoryUserDetailsManager();
        String[][] usersGroupsAndRoles = {
            {"salboby", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
            {"erdmdeiros", "password", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
            {"other", "password", "ROLE_ACTIVITI_USER", "GROUP_otherTeam"},
            {"admin", "password", "ROLE_ACTIVITI_ADMIN", "GROUP_adminTeam"}
        };
        for (String user : usersGroupsAndRoles) {
            List<String> authoritiesStrings = Arrays.asList(Arrays.copyOfRange(user, 2, user.length));
            logger.info("> Registering new user: " + user[0] + " with the following Authorities: " + authoritiesStrings + "]");
            inMemoryUserDetailsManager.createUser(new User(user[0], passwordEncoder().encode(user[1]), authoritiesStrings.stream().map(s -> new SimpleGrantedAuthority(s)).collect(Collectors.toList())));
        }
        return inMemoryUserDetailsManager;
    }
}
```

画面 9:
```java
public void configure(AuthenticationManagerBuilder auth) throws Exception {
    auth.userDetailsService(myUserDetailsService());
}
```

画面 14:
```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/activiti?useUnicode=true&characterEncoding=utf8&autoReconnect=true&failOverReadOnly=false&maxReconnects=10
    username: root
    password: root
    driver-class-name: com.mysql.jdbc.Driver
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“Spring Boot 整合 Activiti7 的”，内容为整合步骤列表。
画面 3: PPT 标题为“3.1 Spring Boot 整合 Activiti7 的”，内容与画面 1 相同。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

