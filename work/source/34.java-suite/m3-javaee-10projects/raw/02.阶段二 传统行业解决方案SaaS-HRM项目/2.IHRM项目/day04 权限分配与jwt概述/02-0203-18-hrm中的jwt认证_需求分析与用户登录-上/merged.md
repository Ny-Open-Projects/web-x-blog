# 18-hrm中的jwt认证：需求分析与用户登录-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day04 权限分配与jwt概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day04 权限分配与jwt概述\18-hrm中的jwt认证：需求分析与用户登录-上_【海量资源尽在 ubkz.com】.mp4
- 时长 12分12秒（音频 732s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 我们已经把JWT工具列写好了那接下来呢就可以以JWT的形式完成我们这个人力资源管理系统当中的用户的登录以及他身份的一个识别那我们接下来要做的事情怎么办呢首先呢需要对我们这个需求做一个简单的说明那在这边呢我打开一张图片以一张图片的形式和各位来做一个我们的案例的一个需求分析那是这样的在我们的前端呢可以在一个用户界面上
[00:33] 输上我们的用户名填上我们的这个密码用户名好了再填写上他的密码那接着呢点击登录按钮登录那好了接着他发送请求发送到我们的服务端那在我们服务端这边呢要做的事情呢其实比较简单咱们要做的事情登录好了第一件事我们需要去查询根据用户名
[01:10] 查询用户那查询用户之后呢接着比较密码好了接着第三件事生成我们叫做token好了接着第四件事响应那其实这就是我们登录要做的事情那我们这个登录这边那响应数据究竟响应的是什么样子我们可以看一下我们的API在我们这边用户管理当中呢我已经把这个登录的API给各位补充好了那用户登录你会发现
[01:40] 用登录传递的是我们的这边是手机号mobile和password密码那传递过来之后我们给它返回数据返回数据里code flag message跟之前的套路是一样的其中有一个data那data现在代表的就是token那各位会发现那各位会发现你请求过来输入的叫做mobile和password那我给你返回的其中最重要的就是token那接着这是我们用户登录
[02:07] 做的事情那除了登录做的事情那接下来呢还有一个就是服务端登录客户端或者我们浏览器登录成功之后在前端立马他要发送第二个请求那第二个请求干嘛呢它是用来获取用户信息的那获取用户信息他发送的请求地址呢就叫做SYSS下的profile那接下来他有没有参数呢什么参数都没有那接下来我们用户
[02:43] 那我们在服务端这边那这个时候就需要做一些事情了那么这边获取用户信息那么获取用户信息应该如何去做呢这个就不得不提我们的JWT token要对token进行解析了因为你获取用户信息发送请求的时候你会在我们的请求头这边请求header带上我们的token数据
[03:13] 那这样一来那在我们获取用户信息的时候我们就首先要识别出你当前登录的用户是谁那我们就需要获取投信息中的我们的token那获取到了token之后接下来第二件事我们就需要从token中提取我们的UID好了那接下来查询用户好了接着第四步我们叫做构造数据这个就是我们整个
[03:45] 练习的我们叫做JWT它的一个登录以及我们这边对它全新的一个验证的这么一个操作OK那好了这个需求呢各位应该都了解了那接下来呢我们就关注于一个一个功能首先呢这个登录功能那登录功能在API里面呢刚才我们看的比较清晰了这个并且比较简单我们需要写一个方法并且呢
[04:10] 接收两个参数接着去验证一把是否有内容接着生成的token数据哎就可以了OK那接下来呢我们就把这个登录方法先给他写好那么要完成用户登录呢由于要用到了GWT所以在登录这边呢我们先把我们要做的事情呢先给他简单的分析一下
[04:32] 那么要做的事情由于要用到了JWT那我们已经把它封装到JWT封装成工具类了所以我们需要在我们的系统模块中引入我们的JWT工具类当然了创建对象交给Spring容器管理好了接下来呢我们可以在任一个Controller当中添加上用户登录的方法比如说呢就在user添加用户登录
[05:01] 好了那接下来呢第三件事呢我们就可以在方法当中验证用户信息那接着第四件事返回数据其实就够了那好了接着我们把这个功能给它实现出来那首先呢我们定位到我们这个注意用户登录等等等等它是我们的系统模块下所以我在系统模块下当中找到一个Controller我们把它放到user Controller下吧这就是我们的user Controller在user Controller
[05:31] value sys那需要各位注意的是这个登录的这个玩意儿其实不是在user下的我把它放到了sys这个模块下所以呢我就放到user Controller但是我们没有加user前缀OK 到了接下来呢我在底下完成我们登录相应的功能这个就是用户登录那对于用户登录来说at request他买品配置登录信息登录的我们的请求地址-login
[05:58] 注意上面有sys所以给我拼接出来没有问题那接下来method那我们的请求方式呢各位来看指定了就是post所以我写成post那也没有问题那接下来写一个方法返回值都是result这个没有疑问login那我们的请求呢它传递的参数呢一共有两个好了一个叫做mobile一个叫做password所以这边呢我先从我们的请求数据当中提取出我们的mobile
[06:28] 提取出我们的passwordOK那Controller层呢这边呢就需要依赖于Service那依赖于Service是不是根据我们的用这个手机号从数据库里面查查询了之后是不是跟密码进行比较其实就能验证它是否登录成功啊所以呢接下来我们在这个登录当中要完成的事情呢第一个通过Service查询我们的通过Service根据mobile
[06:58] 查询用户好了接着第二件事比较password比较密码那接着第三件事如果比较成功我们开始着手生成我们的JWT token好了那接下来呢我们一个一个来看首先通过Service查询那么Service就是user Service打点打点好了这个方法呢我们还没写那我们在user Service里面补充一个方法根据我们叫做mobile
[07:33] 查询用户publicservice抱歉这个打错了找到user Service添加一个方法publicuser我就叫做find by mobileOK传递一个死菌过来死菌类型的mobile进来好了接下来在user Service里面我们调用什么就开始调用do那这个do呢我就在do当中添加一个方法了public返回值
[08:12] user find by mobileOK 传递一个参数进来mobile好了这个是我们借助GPA的一个特性SpringData GPA的一个特性是方法命名的规则那我们这边写翻代开头那接着呢后面写mobile那mobile什么意思它其实指的是我们这个user对象当中的mobile属性那这样一来它就会去根据这个属性拼接circle
[08:39] 他拼接思考就是slashin from user where mobile等于某某这个mobile是跟我们的实体类来的OK好了这个我们做了一个简单的声明那在survey当中我们就可以直接返回returnuser deal打点find by mobile把mobile传递下去那好了这样一来survey层写好了那我们回到Controller那在Controller当中就可以放心大胆的打点find by
[09:11] 把mobile传递下去得到我们的用户好了得到一个user那得到了user之后呢我们可以做一个判断ifuser等于等于那或者user.getPassword.ecosPassword当然了不等于就是说呢你根据手机号没查出来或者你密码不匹配
[09:42] 那针对这种情况呢我们是不是就可以给它构造一个返回告诉它用户名或密码失败啊所以呢这边我们可以构造一个返回new一个result好了resultcode.那这里面呢有很多的内容有很多的内容当然了我们现在这个内容呢现在还没包括用户操作的那用户操作我这边添加一个就是usermobile password arrow哦哦pass
[10:22] word w o r dok那我们这边写的比较清楚了用户返回码呢如果是用户相关的我们全部是2开头的2 0 0 0 1好了那后边呢我就加上是一个用户名或密码错误ok每一句呢这边呢简单的定义一下好了那这边呢我就可以直接返回打点mobile or password arrow好了那接下来呢剩下的事情
[10:59] 那就比较稍微有点点麻烦了上面呢代表的是我们登录失败那底下就代表我们登录成功那如果登录成功呢我们刚才根据分析大家都知道了大家都知道了我需要构造一些返回的数据而我们的返回数据其实就需要生成一个token那token里面可以放很多的内容所以我们需要借助JWT来去帮我们生成那JWT现在在我们的系统当中呢还没有所以我在
[11:31] 思维这边呢把它引入到我的系统工程当中add它并创建对象交给死不容器管理好了我们叫做jwt utilsjwt utilsreturn new一个jwt那这样一来我对象创建好了在我死不容器当中我就可以out to where注入到我的user Controller所以我载随上方呢add它out to where private我们叫做jwt utils
[12:05] OK那我着手通过JWTUTILS开始去生成token信息

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解在 Spring Boot 项目中实现 JWT（JSON Web Token）用户登录与权限控制的流程，包括工具类创建、登录流程、用户信息获取及权限校验等。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDEA中“5.3 JWT工具类”页面，代码为在`hrm_common`工程中创建`JwtUtil`类，代码如下：
```java
@ConfigurationProperties("jwt.config")
public class JwtUtil {
    private String key;
    private long ttl;
    public String getKey() {
        return key;
    }
    public void setKey(String key) {
        this.key = key;
    }
    public long getTtl() {
        return ttl;
    }
    public void setTtl(long ttl) {
        this.ttl = ttl;
    }
}
```

画面2：展示登录流程图，左侧为“用户名”、“密码”、“登录”输入框，右侧为“登录”步骤：1.根据用户名查询用户；2.比较密码；3.生成token；4.响应数据。

画面3：在登录流程图基础上，增加“获取用户信息”模块，标注请求头为“token数据”，并指向右侧“获取用户信息”模块，该模块内容为：获取用户信息，请求头：token数据。

画面4：在登录流程图基础上，完善“获取用户信息”模块，内容为：1.获取头信息中的token；2.从token中提取userid；3.查询用户；4.构造数据。

画面5：展示IDEA中`UserController.java`文件，代码为：
```java
@RequestMapping(value = "/user/{id}", method = RequestMethod.PUT)
public Result update(@PathVariable("id") String id, @RequestBody User user) {
    user.setId(id);
    userService.update(user);
    return new Result(ResultCode.SUCCESS);
}

// 删除注释
@RequestMapping(value = "/user/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable("id") String id) {
    userService.deleteById(id);
    return new Result(ResultCode.SUCCESS);
}
```

画面6：在`UserController.java`中，对`update`方法进行注释，代码为：
```java
// 根据id删除
@RequestMapping(value = "/user/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable("id") String id) {
    userService.deleteById(id);
    return new Result(ResultCode.SUCCESS);
}
```

画面7：在`UserController.java`中，对`delete`方法进行注释，代码为：
```java
// 删除注释
@RequestMapping(value = "/user/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable("id") String id) {
    userService.deleteById(id);
    return new Result(ResultCode.SUCCESS);
}
```

画面8：展示IDEA中`UserDao.java`文件，代码为：
```java
package com.ihrm.system.dao;
import ...
public interface UserDao extends JpaRepository<User,String>,JpaSpecificationExecutor<User> {
    Page<User> findAll(Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User> findAll(Specification specification, Pageable pageable)
    Page<User

