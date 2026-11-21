# 画面线理解：17-shiro认证与授权：基于ini的用户授权

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\17-shiro认证与授权：基于ini的用户授权_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:32, 02:47, 03:02, 03:24, 03:31, 03:38, 03:55, 04:26, 05:04, 05:23, 05:39, 05:47, 06:12, 06:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:18:11

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
