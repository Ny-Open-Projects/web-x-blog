# 02-Shiro与Springboot整合：配置依赖改造登录方法

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\02-Shiro与Springboot整合：配置依赖改造登录方法_【海量资源尽在 ubkz.com】.mp4
- 时长 11分23秒（音频 683s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 已经把Signal这个案例工程呢我们已经导入进来了那接下来呢这个工程全部都是一个基本的Spring Boot成工程那我们想用Shera进行控制的话就需要对Shera进行一个整合的这么一个操作那对Shera整合呢咱们主要围绕的是我们这么几个步骤首先呢就是我们需要在工程当中引入Shera和Spring进行整合的相应依赖的一些坐标那也是一些扎标jar 包
[00:32] 那接下来呢我们就可以基于shared形式完成我们的权限控制但是我们昨天通过一些基础咱们得知在shared世界当中完成权限控制全部都是通过我们的realm域来完成的所以我们需要自己定义realm域那当然了咱们这边呢遗留了一个小的登录的这么一个方法那我们传统的登录方式呢全部都是基于用户名的密码的形式咱们自己进行判断
[01:03] 那大家都知道对于shareware登录我们是不是借助subject点login来做呀所以对于我们整合整个的一个shareware来说咱们要完成的点有很多首先呢就是相应的依赖引入进来接着我们修改它的登录方法借助shareware帮助我们进行登录那不管是登录还是认证我们都是通过自定义用语的方式来做的那这些我们都搞定了之后接下来对于shareware整个这个工程
[01:30] 如果想在web应用当中去使用特别是在sprint boot的过程当中去使用它有一个配置的这么一个过程所以我们整合好了之后做一个简单的配置我们就能让它跑起来看一下效果了当然了我们上面讲的是一些基本的一些内容当然除了这些基本的我们还要做去它配置它的一个过滤器
[01:51] 那以及完成整个受传的一个内容好了这个就是我们整合sharework以及整合sharework之后我们要完成的两个点一个是认证一个受传咱们先来看第一个点就是整合sharework那对于整合sharework的时候呢我们需要引入整合sharework相应的一些怎么叫做依赖那这些依赖呢在今天的资料当中呢也给各位准备好了在这边基本配置里面有一个POM依赖可以把它打开
[02:22] Ctrl C 靠到我们这边的工程碰文件在碰文件底下copy过来好了当然了copy过来我全从靠一下吧这个虽然已经带了我再靠一下防止出错好那接下来呢这些坐标呢首先Sheryl整合Sprint的一个坐包一个依赖那底下呢是Sheryl的核心包还有一个我们要用到Sheryl跟Redis一个整合所以我这边呢想都不想直接全搞过来了咱们最后用到的时候还会跟各位简单的提一下
[02:52] 好了呢这个坐标我们引进来了之后接下来呢就是说我们关注的就是先去完成它的认证这个功能那认证这个功能我们说过很多次了认证其实代表的就是登录那我在user Controller这中呢已经写了一个简单的登录的这么一个接口那我们都知道都知道对于一个登录来说这边呢就不得不提两种登录方式呢一个叫做传统的登录一个叫做shared的登录
[03:24] 好了这边就是传统登录好了第二个就是我们叫做shared登录登录那对于传统登录来说呢我们通过发送登录请求前端发送登录请求那发送了登录请求那接下来呢我们就可以在接口部分获取接口部分获取我们的用户名密码那获取到用户密码之后呢那整个这个
[04:09] 登录的用户控制全部是我们程序员手动控制的程序员在我们的Controller或者在我们的接口部分手动进行控制那对于shareware而言则不一样shareware是什么样呢还是前端发送那在接口部分呢我们可以获取到用户名码那接下来呢我们通过room通过我们叫subjectsubject进行登录
[04:44] 那进行登录那登录之后在哪呢是不是就进入到我们的RAM的认证方法认证方法那接下来如果认证通过我们这边就就相当于认证成功了如果抛出异常是不是就可以理解为我认证失败了好了所以对于这是两种的我们的登录的方式那我们这边呢要完成第一个就是改造成shadow的那改造成shadow我们应该如何进行改造呢这个其实就不难了
[05:15] 我们改造的逻辑首先第一个就是想方设法的叫做获取subject好了获取了subject之后接着第二件事调用subject进行登录当然了在你进行登录之前在你登录之前我们需要构造我们的叫做构造登录令牌就是我们昨天讲过一个什么usernameand password token
[05:46] OK那好了这些呢我们都已经知道了之后我们接下来把这个代码呢可以给它补充完整构造登录论卡很简单了username我们之前都玩过password tokenup token好了等于new一个username password token那我们知道这个构造方法里面可以传递两个参数第一个参数就是你登录提供的用户名人好了第二个参数就是你登录提供的我们叫做密码
[06:12] 好了那up token我们获取到了之后我们如何构造subject很简单我们之前构造subject通过一个工具类subject错了叫做security utilssecurity utils打点get subject好了那绑定到了subject有了subject之后我们就可以调用subject的方法完成登录好了subject抱歉这边返回值没写啊得到subject对象那有了subject对象
[06:47] 通过Subtech打点Login去进行登录那登录需要参数就是我们的UP token好了呢我们都知道对于这个整个的过程呢可能会抛出异常那抛出异常的时候我们就是登录失败了没错吧那如何去控制呢其实也不难我们可以以Track Catch的形式来进行处理OK那把中间这一段进行登录的逻辑全部都写到这儿那接着如果说登录失败了我在这边
[07:20] return我们叫做用户名或密码错误OK那这样一来我们就已经把登录的这个过程给它改造成功了当了这个代码呢咱们还是写的比较简单因为我们这边login登录之后呢没有做任何的代码处理我直接就返回了一句话那返回一句话你点登录成功是不是就给你打印出四个字如果失败是会给打印出这几次啊
[07:47] 那我们现在把这个登录呢其实已经改造好了但是各位忽略了一个问题其实是这样那我们用户传递的用户名密码其实拿过来之后呢都是明文的这么一个处理那我们不可能直接用明文进行比较那我们一般是不是把密码进行加密之后才可以啊所以这边涉及到一点点的问题就是我们对密码的一个加密那对于密码加密来说呢我们都知道有很多种方式啦比如说我们之前学过的
[08:13] Security里面提供的一些密码加密或者我们可以把它以MD5的形式进行加密等等等等有很多种方式那在Sheryl当中它默认提供了其实MD5加密的方式那我们接着来看一下如何对密码进行加密我们使用的是Sheryl提供的MD5加密那Sheryl提供的MD5加密的其实是一个工具类我们叫做MD5Hash那我们可以new一个MD5Hash
[08:46] 放起来那这个MD5Hash的时候呢它需要有这么几个构造参数那这个MD5的构造参数首先呢参数一参数一就是你要加密的内容那对于我们来说加密的内容是不是就应该是这个密码password那还有一个参数二参数二叫做言那这个言是什么言是比较好理解的
[09:18] 那我们比如说呢对于这个MD5加密来说很多的互联网上它都能够对MD5声明声称说它能解密它真的能解密吗不能其实是这样的那对于普通的这个MD5来说比如说就是6个1它代表的MD5加密子幅串比如说ABCD那如果说各大量的人都用6个1的话其实我们就可以演算出来就是ABCD那它是一个匹配关系那如果是你真的是6个1的用户名密码的话用户名密码的话那这个时候
[09:46] 那ABCD太显而易见人工能够猜出来那如果说你加密的时候要6个1后面给它加一点我们的字符串的话那这样一来那这个玩意就容易进行一个混淆那所以对于我们这边这个言是什么它其实就是加密的混淆字符串那这样一来如果说传统的方式我们是6个1进行MD5加密的话那加上言就变了它可能就变成了6个1再加上其他的我们的混
[10:18] 小字符创来进行统一加密OK那接下来这个言呢在我们的应用当中一般来说用的是什么其实就可以用它的用户登录的用户名来做其实就可以了那所以在这边第二个我们的言就用usernameOKCtrl C Ctrl V接过来好了接下来它还有第三个参数参数三那这个参数三呢指的是我们的加密次数
[10:47] 是这样的对于MD5进行加密的时候其实它是对于我们整个的字符串它是做了很多个处理的它比如说把前几个挪一个位置把后几个挪一个位置再进行加密主要是为了让我们MD5的加密字符串更加复杂一些所以对于加密次数来说我们可以简单的设置一下比如说设置3其实就可以了OK那这样一来我们就对我们的密码进行了一个新的加密的密码方式OK好了当然了我们要想得到的是一个死菌字符串
[11:17] .toStream即可那这样一来我们就已经对密码进行了A加密

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成 Apache Shiro 进行用户认证，重点讲解登录接口中如何使用 Shiro 的 Subject.login 方法进行认证，并展示密码加密（MD5）的实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 ShiroApplication 启动类，包含 @SpringBootApplication 和 @EntityScan 注解，以及一个自定义的 OpenEntityManagerInViewFilter。
画面2：展示 UserController 中的增删改查接口和登录接口，登录接口目前仅打印日志。
画面3：展示项目目录结构，重点指向 shiro_springboot 目录下的 pom.xml 文件。
画面4：展示 pom.xml 中的 <repositories> 配置，包含 Spring Snapshots 和 Spring Milestones 仓库。
画面5：展示 pom.xml 中的 <dependencies> 部分，包含 mysql-connector-java、shiro-spring、shiro-redis 等依赖。
画面6：展示 UserController 的登录方法，准备添加 Shiro 认证逻辑。
画面7：在登录方法中，开始使用 Shiro 的 UsernamePasswordToken 和 SecurityUtils.getSubject()。
画面8：继续编写登录方法，准备获取 Subject。
画面9：展示 IDE 中的自动补全建议，包括 Shiro 的相关工具类。
画面10：在登录方法中添加 try-catch 块，用于捕获异常。
画面11：在 try 块中，使用 SecurityUtils.getSubject() 获取当前用户 Subject。
画面12：在 try 块中，调用 subject.login(upToken) 进行认证。
画面13：在 try 块中，使用 new Md5Hash() 对密码进行加密，准备生成 UsernamePasswordToken。
画面14：在 try 块中，使用 Md5Hash 对密码、用户名和迭代次数进行加密，生成 UsernamePasswordToken。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package cn.itcast.shiro;

import ...

@SpringBootApplication(scanBasePackages = "cn.itcast.shiro")
@EntityScan("cn.itcast.shiro.domain")
public class ShiroApplication {
    public static void main(String[] args) {
        SpringApplication.run(ShiroApplication.class, args);
    }

    @Bean
    public OpenEntityManagerInViewFilter openEntityManagerInViewFilter() { return new OpenEntityManagerInViewFilter(); }
}
```

画面2：
```java
//添加
@RequestMapping(value = "/user",method = RequestMethod.POST)
public String add() { return "添加用户成功"; }

//查询
@RequestMapping(value = "/user",method = RequestMethod.GET)
public String find() { return "查询用户成功"; }

//更新
@RequestMapping(value = "/user/{id}",method = RequestMethod.GET)
public String update(String id) { return "更新用户成功"; }

//删除
@RequestMapping(value = "/user/{id}",method = RequestMethod.DELETE)
public String delete() { return "删除用户成功"; }

//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    System.out.println("用户登录");
    return "登录成功";
}
```

画面3：
```
day1
day2
day3
day4
day5
day6
day7
day8
day9
day10
day11
day12
day13
day14
shiro案例代码
shiro_springboot
idea
src
main
java
cn
itcast
shiro
Controller
dao
domain
Service
test
target
```

画面4：
```xml
<repositories>
    <repository>
        <id>spring-snapshots</id>
        <name>Spring Snapshots</name>
        <url>https://repo.spring.io/snapshot</url>
        <snapshots>
            <enabled>true</enabled>
        </snapshots>
    </repository>
    <repository>
        <id>spring-milestones</id>
        <name>Spring Milestones</name>
        <url>https://repo.spring.io/milestone</url>
        <snapshots>
            <enabled>false</enabled>
        </snapshots>
    </repository>
</repositories>

<pluginRepositories>
    <pluginRepository>
        <id>spring-snapshots</id>
        <name>Spring Snapshots</name>
        <url>https://repo.spring.io/snapshot</url>
        <snapshots>
            <enabled>true</enabled>
        </snapshots>
    </pluginRepository>
</pluginRepositories>
```

画面5：
```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.16</version>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-spring</artifactId>
    <version>1.3.2c</version>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-core</artifactId>
    <version>1.3.2c</version>
</dependency>
<dependency>
    <groupId>org.apache.shiro</groupId>
    <artifactId>shiro-redis</artifactId>
    <version>3.0.0</version>
</dependency>
```

画面6：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    System.out.println("用户登录");
    return "登录成功";
}
```

画面7：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    //构造登录令牌
    UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
    //获取subject
    Subject subject = SecurityUtils.getSubject();
    //2.调用subject进行登录
    subject.login(upToken);
    return "登录成功";
}
```

画面8：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    //构造登录令牌
    UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
    //获取subject
    Subject subject = SecurityUtils.getSubject();
    //2.调用subject进行登录
    subject.login(upToken);
    return "登录成功";
}
```

画面9：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    //构造登录令牌
    UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
    //获取subject
    Subject subject = SecurityUtils.getSubject();
    //2.调用subject进行登录
    subject.login(upToken);
    return "登录成功";
}
```

画面10：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    try {
    } catch (Exception e) {
    }
}
```

画面11：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    try {
        //获取subject
        Subject subject = SecurityUtils.getSubject();
        //2.调用subject进行登录
        subject.login(upToken);
        return "登录成功";
    } catch (Exception e) {
        return "用户登录失败";
    }
}
```

画面12：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    try {
        //获取subject
        Subject subject = SecurityUtils.getSubject();
        //2.调用subject进行登录
        subject.login(upToken);
        return "登录成功";
    } catch (Exception e) {
        return "用户登录失败";
    }
}
```

画面13：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    try {
        //构造登录令牌
        UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
        //获取subject
        Subject subject = SecurityUtils.getSubject();
        //2.调用subject进行登录
        subject.login(upToken);
        return "登录成功";
    } catch (Exception e) {
        return "用户登录失败";
    }
}
```

画面14：
```java
//用户登录
@RequestMapping(value = "/login")
public String login(String username,String password) {
    try {
        //构造登录令牌
        UsernamePasswordToken upToken = new UsernamePasswordToken(username,password);
        //获取subject
        Subject subject = SecurityUtils.getSubject();
        //2.调用subject进行登录
        subject.login(upToken);
        return "登录成功";
    } catch (Exception e) {
        return "用户登录失败";
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

