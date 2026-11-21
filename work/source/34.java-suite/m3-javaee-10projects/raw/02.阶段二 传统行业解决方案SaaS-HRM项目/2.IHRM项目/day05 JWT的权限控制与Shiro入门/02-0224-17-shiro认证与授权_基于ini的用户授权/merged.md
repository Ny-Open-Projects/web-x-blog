# 17-shiro认证与授权：基于ini的用户授权

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\17-shiro认证与授权：基于ini的用户授权_【海量资源尽在 ubkz.com】.mp4
- 时长 6分43秒（音频 403s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 用户的认证呢我们看过了之后接下来呢就可以玩一下它用户授权的相关的内容当然我们现在全部都是基于ANI的这种方式来做的主要是看一下它基本的一个代码的结构那以及最后我们总结一下它认证和授权的这么一个总的一个步骤在里面好了那接下来呢我们完成这个用户授权的一个操作那用户授权跟我们用户认证它都是使用这种基于ANI的形式来做的那怎么去这么
[00:27] 去完成这个授权的一个操作呢首先我去准备一个配置文件Ctrl C Ctrl V 拷过来这是我们第二个案例要用的配置文件那第二个案例要用的配置文件呢这回呢我们是要讲究授权相应的内容那其实Sheryl它默认支持的就是这种基于RBAC的这种授权方式
[00:49] 所以在这里面它除了要体现出user用户之外还应该要体现出你当前有没有什么角色所以这回我们配置的数据除了用户user之外还应该有我们叫做肉丝好了user丝里面写的内容注意这回的数据格式就变了张三等于123456接着加逗号肉一逗号肉二这个代表的是什么含义这回的数据格式就是用户名等于密码
[01:21] 逗号后面加的是角色角色名逗号你有多少写多少其实就可以了那除了有张三之外呢可以再来一个李四叫李四那李四呢也是123456了给他来一肉依那底下就可以定义我们的角色那定义角色的时候呢可能比如说来肉依等于这个肉依他能够仿这是注意他这个格式是这样的也先简单的去写一下他这个格式是这样的角色名称
[01:58] 等于后面的权限列表它指的是角色名称等于权限列表那比如说我们进行用户操作的时候可能有user下滑线user杠sig当然这个值呢是我们自己随便定义的我们为了更加醒目一些我写的是user杠好了update那好了row2等于user爱冒号我们这边来一个增find好了那这样一来大家会抱歉这个改成了row2
[02:28] 那这样一来各位会发现我呢现在写了两个用户第一个用户呢有角色一角色二第二个用户呢有角色二第一个用户那间接着就有保存和修改的操作和以及查询那对于第二个用户是不是只有查询啊OK那这样一来我这个用户授权的配置文件也已经搞定了那搞定了之后接下来我们就开始去写一个简单的测试去看一下Shadow它
[02:52] 整个的授权的一个过程那授权的过程Ctrl C Ctrl V我从之前的案例就直接copy过来了那这个代码呢其实跟之前这个逻辑都差不多首先呢也是去得到当前的这个内容那我可以把这个代码呢做一个简单的改造以备我们之后去测试的更加方便一些好了那这个改造如何去做呢咱们就可以借助
[03:21] 这些注释就不要了咱们怎么做咱们可以把这个公共的内容以比方的形式给我们抽取出来好了以比方的形式抽取来publicviewidinit好了那由于我要用到这个security managersecurity manager所以我这边呢在比方当中去对它进行一个注释化实力化好了那这个代码呢也比较简单我们可以从我们之前写好的这个代码直接把它拷过来就可以了
[04:00] OK好了实例化那接下来呢subject从security当中直接获取其实就OK了好了那接下来那对于我们这个授权的过程如何去做这个代码应该怎么去编写其实也比较简单也不难首先呢你得想方设法的让它登录因为对于我们授权来说必须先登录才能进行授权好了那这边我已经把登录的这个代码给它准备好了
[04:31] 那如果登录成功上面就是登录登录成功之后完成授权那授权什么意思授权其实就是检验当前登录用户是否具有操作权限当然除了操作权限还可以判断是否具有某个角色所以接下来我们围绕着这两个方面去做文章
[05:06] 那对于这两个方面如何去进行判断的其实很简单其实很简单我们可以SOT打印一把注意所有的如果你登录成功之后所有内容都可以在subject里面进行获取那我们这边可以subject打点有一个叫做hasrose它是hasrose你当前是否具有某个角色比如说呢我们刚才写了一个角色叫肉依肉依好了我们可以打印一把比如说呢还可以去验证SOT
[05:37] 你当前是否具备某个权限subject打点ispermitted你当前是否具备某个权限比如说user-我们写了一个save好了各位来看在我们的配置文件当中我们模拟了也是数据库模拟的模拟了一个张三他有肉依角色并且他具备save方法这玩意一来登录成功是不是两个处所以我们验证一把走抱歉抱歉
[06:10] 现在两个false是有原因的我们这边加载的配置文件不对当前应该加载配置文件2了走 各位来看一下效果两个处都没问题接下来注意注意我还有个用户叫李四李四也去让他登录登录了之后我再去执行李四我们都知道了他是row2row2没有save方法所以这样一来我们就通过share完成了基本的这么一个认证

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中使用 Apache Shiro 进行用户登录认证和权限校验，并通过 JUnit 单元测试验证功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中，将 `shiro-test-1.ini` 文件复制到 `src/main/resources` 目录下，准备用于 Shiro 配置。
画面 2: 展示 `ShiroTest01.java` 文件，其中包含一个测试方法 `testLogin()`，用于验证用户登录功能。
画面 3: 展示 `ShiroTest02.java` 文件，该文件用于演示 Shiro 的用户登录和权限校验功能。
画面 4: 在 `ShiroTest02.java` 中，为测试类添加 `@Before` 注解，用于在测试前初始化 SecurityManager。
画面 5: 在 `ShiroTest02.java` 中，为测试类添加 `@Test` 注解，用于标记测试方法。
画面 6: 在 `ShiroTest02.java` 中，为测试类添加 `@Before` 注解，用于在测试前初始化 SecurityManager。
画面 7: 在 `ShiroTest02.java` 中，为测试类添加 `@Before` 注解，用于在测试前初始化 SecurityManager。
画面 8: 在 `ShiroTest02.java` 中，为测试类添加 `@Before` 注解，用于在测试前初始化 SecurityManager。
画面 9: 在 `ShiroTest02.java` 中，为测试类添加 `@Before` 注解，用于在测试前初始化 SecurityManager。
画面 10: 在 `ShiroTest02.java` 中，为测试类添加 `@Before` 注解，用于在测试前初始化 SecurityManager。
画面 11: 在 `ShiroTest02.java` 中，为测试类添加 `@Before` 注解，用于在测试前初始化 SecurityManager。
画面 12: 在 `ShiroTest02.java` 中，为测试类添加 `@Before` 注解，用于在测试前初始化 SecurityManager。
画面 13: 在 `ShiroTest02.java` 中，为测试类添加 `@Before` 注解，用于在测试前初始化 SecurityManager。
画面 14: 在 `ShiroTest02.java` 中，为测试类添加 `@Before` 注解，用于在测试前初始化 SecurityManager。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
Copy file E:\workspace\hrm\...\shiro_demo\src\main\resources\shiro-test-1.ini
New name: shiro-test-1.ini
To directory: E:\workspace\hrm\shiro-demo\src\main\resources
Use Alt+Shift for path completion
```

画面 2:
```java
@Test
public void testLogin() {
    //1.根据配置文件创建SecurityManagerFactory
    Factory<SecurityManager> factory = new IniSecurityManagerFactory( "classpath:shiro-test-1.ini");
    //2.通过工厂获取SecurityManager
    SecurityManager securityManager = factory.getInstance();
    //3.将SecurityManager绑定到当前运行环境
    SecurityUtils.setSecurityManager(securityManager);
    //4.从当前运行环境中构造subject
    Subject subject = SecurityUtils.getSubject();
    //5.主体登录
    String username = "zhangsan";
    String password = "1234561";
    UsernamePasswordToken token = new UsernamePasswordToken(username,password);
    subject.login(token);
    //6.验证登录是否成功
    System.out.println("用户登录是否成功："+subject.isAuthenticated());
    //7.获取登录用户的权限
    System.out.println(subject.getPrincipal());
}
```

画面 3:
```java
package cn.itcast.shiro;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.subject.Subject;
import org.apache.shiro.util.Factory;
import org.apache.shiro.config.IniSecurityManagerFactory;
import org.apache.shiro.mgt.SecurityManager;
import org.apache.shiro.util.SecurityUtils;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

public class ShiroTest02 {
    @Test
    public void testLogin() {
        //1.根据配置文件创建SecurityManagerFactory
        Factory<SecurityManager> factory = new IniSecurityManagerFactory( "classpath:shiro-test-1.ini");
        //2.通过工厂获取SecurityManager
        SecurityManager securityManager = factory.getInstance();
        //3.将SecurityManager绑定到当前运行环境
        SecurityUtils.setSecurityManager(securityManager);
        //4.从当前运行环境中构造subject
        Subject subject = SecurityUtils.getSubject();
        //5.主体登录
        String username = "zhangsan";
        String password = "1234561";
        UsernamePasswordToken token = new UsernamePasswordToken(username,password);
        subject.login(token);
        //6.验证登录是否成功
        System.out.println("用户登录是否成功："+subject.isAuthenticated());
        //7.获取登录用户的权限
        System.out.println(subject.getPrincipal());
    }
}
```

画面 4:
```java
package cn.itcast.shiro;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.subject.Subject;
import org.apache.shiro.util.Factory;
import org.apache.shiro.config.IniSecurityManagerFactory;
import org.apache.shiro.mgt.SecurityManager;
import org.apache.shiro.util.SecurityUtils;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

public class ShiroTest02 {
    @Before
    public void init() {
    }
}
```

画面 5:
```java
package cn.itcast.shiro;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.subject.Subject;
import org.apache.shiro.util.Factory;
import org.apache.shiro.config.IniSecurityManagerFactory;
import org.apache.shiro.mgt.SecurityManager;
import org.apache.shiro.util.SecurityUtils;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

public class ShiroTest02 {
    @Test
    public void testLogin() {
        //1.根据配置文件创建SecurityManagerFactory
        Factory<SecurityManager> factory = new IniSecurityManagerFactory( "classpath:shiro-test-1.ini");
        //2.通过工厂获取SecurityManager
        SecurityManager securityManager = factory.getInstance();
        //3.将SecurityManager绑定到当前运行环境
        SecurityUtils.setSecurityManager(securityManager);
        //4.从当前运行环境中构造subject
        Subject subject = SecurityUtils.getSubject();
        //5.主体登录
        String username = "zhangsan";
        String password = "1234561";
        UsernamePasswordToken token = new UsernamePasswordToken(username,password);
        subject.login(token);
        //6.验证登录是否成功
        System.out.println("用户登录是否成功："+subject.isAuthenticated());
        //7.获取登录用户的权限
        System.out.println(subject.getPrincipal());
    }
}
```

画面 6:
```java
package cn.itcast.shiro;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.subject.Subject;
import org.apache.shiro.util.Factory;
import org.apache.shiro.config.IniSecurityManagerFactory;
import org.apache.shiro.mgt.SecurityManager;
import org.apache.shiro.util.SecurityUtils;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

public class ShiroTest02 {
    @Before
    public void init() {
    }
}
```

画面 7:
```java
package cn.itcast.shiro;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.subject.Subject;
import org.apache.shiro.util.Factory;
import org.apache.shiro.config.IniSecurityManagerFactory;
import org.apache.shiro.mgt.SecurityManager;
import org.apache.shiro.util.SecurityUtils;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

public class ShiroTest02 {
    private SecurityManager securityManager;
    @Before
    public void init() {
    }
}
```

画面 8:
```java
package cn.itcast.shiro;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.subject.Subject;
import org.apache.shiro.util.Factory;
import org.apache.shiro.config.IniSecurityManagerFactory;
import org.apache.shiro.mgt.SecurityManager;
import org.apache.shiro.util.SecurityUtils;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

public class ShiroTest02 {
    private SecurityManager securityManager;
    @Before
    public void init() {
        //1.根据配置文件创建SecurityManagerFactory
        Factory<SecurityManager> factory = new IniSecurityManagerFactory( "classpath:shiro-test-1.ini");
        //2.通过工厂获取SecurityManager
        SecurityManager securityManager = factory.getInstance();
        //3.将SecurityManager绑定到当前运行环境
        SecurityUtils.setSecurityManager(securityManager);
    }
}
```

画面 9:
```java
package cn.itcast.shiro;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.subject.Subject;
import org.apache.shiro.util.Factory;
import org.apache.shiro.config.IniSecurityManagerFactory;
import org.apache.shiro.mgt.SecurityManager;
import org

