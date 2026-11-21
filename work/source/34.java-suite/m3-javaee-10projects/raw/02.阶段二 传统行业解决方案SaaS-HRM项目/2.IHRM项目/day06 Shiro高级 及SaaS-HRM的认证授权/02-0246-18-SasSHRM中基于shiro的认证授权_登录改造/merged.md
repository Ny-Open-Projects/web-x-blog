# 18-SasSHRM中基于shiro的认证授权：登录改造

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day06 Shiro高级 及SaaS-HRM的认证授权
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day06 Shiro高级 及SaaS-HRM的认证授权\18-SasSHRM中基于shiro的认证授权：登录改造_【海量资源尽在 ubkz.com】.mp4
- 时长 8分38秒（音频 519s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 我们完成了环境搭建自定义room当然我们写的是这个自定义里面的代码还没写以及自定义会员管理器这些代码那接下来呢我们就是对于登录需要进行一个改造那么登录是在系统微服务里面我们写了一个login方法我们找到它进行简单的改造的一个过程找到我们的代码部分找到我们的系统微服务找到user Controller那在user Controller里面这是我们之前JWT的登录方式在上边在上边
[00:33] 那我们现在替换成我们叫做shared登录方式那替换成shared登录方式很简单一共呢就是这么几个步骤希望各位能够理解首先第一件事呢我们需要构造我们叫做登录的令牌那这个登录令牌呢叫做user nameuser name and pass word token好了接着第二件事我们要获取subject好了接着第三件事
[01:10] 调用subject logging方法进入我们叫做rium完成用户认证那别忘了在我整个的认证的过程当中可能会抛出异常那抛出异常我们要解决它出现异常意味着用户名或密码失败那当然了我们这个登录方法呢其实要返回一个数据那返回什么数据就是我们要得到一个字符串那我们之前呢JWT的方式其实得到的是token信息那么现在
[01:39] 是不是替换成叫做session id并返回其实就可以了没错吧所以接下来我们还要做第四件事就是获取我们叫做session id好了接着第五件事构造返回结果其实就可以了那接下来我们把这个代码呢一个一个的给他补充完整首先第一个构造用户登录令牌usernameand passwordusername password我们叫做token
[02:09] 那好了接下来呢我就叫做up tokenup token等于new一个new一个我们叫做user name and password token那希望各位要注意的是我们这个密码呢其实是应该经过加密的那所以在这边呢我们可以对密码加密那加密密码我们用的是一个Sherlock提供的一个工具类md5 hashmd5 hash那我们要new一个我们叫做md5 hash
[02:41] 里面呢借助它的构造方法构造方法里面三个参数那这三个参数还希望各位要知道第一个参数就是我们要加密的密码第二个就我们叫做延好了第三个呢其实我们就是迭代加密的次数那就是说呢这个延我们用什么来做的延其实就是一个混淆的字幕创那延不能随便写你今天写成一明天写成二那可能你这个延就不一致
[03:09] 那不一致的话也就意味着你每次登录的密码加密之后这个密码和数据库就不一样了没错吧所以对于我们而言严用什么比较合适我觉得严用它的手机号就更加合适了这样一来我们其实加密的是用户名和密码它的整个的一个结合体OK那接下来怎么加密很简单第一个参数密码传递过来那接着第二个参数我们叫做严也就是mobile我们的手机号那第三个加密次数加密次数我们写三次其实就可以了好了这边
[03:39] password等于重新加密里面调用它的tools认识方法得到支付创好了那接下来我们就可以构造token构造token也比较简单了首先第一个参数你的用户名我们是password我们用户名我们叫手机号好了第二个就是我们加密好的密码那token搞定了接着获取subject获取subject也比较简单securityutils打点get subject就能得到我们的操作主体subject
[04:10] 那得到操作主体接着调用操作主体的login方法把up token传递过去进行登录即可那千万别忘了我们整个的这个登录过程有可能会抛出异常所以我这边来一个叫做try catchtry catchok好了我把这两个注释也写到这个try catch当中吧好那接下来呢就是去登录登录一旦登录成功我们可以获取session id
[04:48] 好了这边呢我叫做死郡session id那session id怎么获取刚才我们也看过可以通过subject打点get session打点get id的形式get id的形式得到我们的session id好了这边呢做一个转型好了构造返回结果返回结果其实就是new一个result告他登录成功了接着把你这个session id叫做token传递下去就可以那中间catch抛出异常抛出异常代表的用户名密码
[05:19] 错误用户名码错误我们之前也写过Ctrl C Ctrl V拿过来即可那这样一来我登录这个方法就已经改造成功了其实各位可以想一下就目前我们这个登录呢改造好了之后其实还是有一些问题的问题其中的点是这样的我们可以打开数据库来看我们目前数据库里面保存一个用户之后它的密码是不是还是明文进行存储
[05:46] 所以对于我们接下来要做的事情就是说当你去保存一个用户的时候我们要把这个密码给它进行加密好了那我们保存用户的时候呢我们这个逻辑在哪呢各位可以跟我一起来找一下在我们之前写好的这个save方法里面调用Service.save那我们要做的事情这回是123456初始化的密码那我们要做的事情其实就是对这个密码进行一个加密即可那进行加密的逻辑呢和我们这个验证
[06:14] 密码的逻辑其实是一模一样的Ctrl C拿过来这边Ctrl V好了那我们的密码呢就是123456初始化的密码好了接着我们的手机号user打点getmobileOK 死菌password这个其实就是我们加密之后的这个密码了当然了对于我们保存用户来说呢我们之前知道了用户是有一个用户级别的里面分为了我们的超级管理员也就是SaaS平台的管理权还有企业的管理员
[06:47] 那不管是哪个管理员都不是通过我们保存用户能够实现的所以我们想说的在系统里面保存的用户保存的全部都是一个普通的一个用户所以我们可以给他设置一个用户的等级set level那普通用户等级呢我们就叫做user其实就可以了OK那这样一来我们保存用户的这个小的bug呢也已经解决了那我们一会儿可以做一个测试现在呢我们先把这个基本的一些逻辑先给他搞定啊
[07:15] 好了那这样一来呢我们再去新添加用户的时候密码其实就已经改了但是对于我们已经存在的这几个密码那我们怎么办呢那这边呢我就手动的去处理一下好了这个处理起来比较简单PSVM处理起来比较简单好了那怎么做呢SGIN PASSWORD等于这边我就自己写代码呢对它进行一个手动的修改其实就可以了好了那这个PASSWORD我们都叫做123456那手机号注意
[07:48] 每一个用户的手机号是不一样的比如说第一个呢就是叫01SOT我们把它打印出来然后呢手动的进行一个修改好了这边Ctrl C拿过来好了接着改02走好了接着改03刷新一下OK那这样一来我们这个真正的登录的改造呢除了有我们的代码部分还有我们的数据那这些我们都已经搞定了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中使用 Shiro 框架实现用户登录认证，包括 JWT 和 Shiro 两种方式的对比、登录逻辑代码实现、以及相关配置和工具的使用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了 PPT 页面，对比 JWT 和 Shiro 的认证授权方式。
- JWT 方式：前端调用服务 → 系统微服务 → 生成 token → 返回 token 信息 → 企业微服务 → 解析 token → 校验操作权限。
- Shiro 方式：前端调用服务 → 系统微服务 → 获取企业信息（含 sessionid）→ 企业微服务 → 获取安全数据 → Shiro 会话管理 → Redis 服务。
- PPT 右下角列出四个步骤：1. 搭建环境；2. 登录改造；3. 自定义 realm；4. 自定义会话管理器。

画面 2:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 3:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 4:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 5:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 6:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 7:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 8:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 9:
- 展示了项目结构，选中了 ihrm_system 模块。
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 10:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 11:
- 展示了 UserService.java 文件中 save 方法的代码片段。
- 代码逻辑：设置用户属性（id、password、enableState、deptId）→ 调用 dao 保存用户。

画面 12:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 13:
- 展示了 UserControll.java 文件中登录方法的代码片段。
- 代码逻辑：校验用户密码 → 构建权限字符串 → 创建 token → 返回结果。

画面 14:
- 展示了 Windows 桌面，多个窗口并列显示，包括 IntelliJ IDEA、Redis Desktop Manager、SQLyog Ultimate、PDF 文档等。
- 窗口标题显示为“ihm_parent [E:\workspace...]”、“shiro-test [E:\workspace...]”、“JWT与Shiro认证授权对比”等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
//登录失败
if(user == null || user.getPassword().equals(password)) {
    return new Result(ResultCode.MOBILEORPASSWORDERROR);
}
else {
    //登录成功
    //api权限字符串
    StringBuilder sb = new StringBuilder();
    for (Role role : user.getRoles()) {
        for (Permission perm : role.getPermissions()) {
            if(perm.getTypes() == PermissionConstants.PERMISSION_API) {
                sb.append(perm.getCode()).append(",");
            }
        }
    }
    //构建token
    Map<String, Object> map = new HashMap<>();
    map.put("apis", sb.toString()); //api权限字符串
    map.put("companyId", user.getCompanyId());
    map.put("username", user.getUsername());
    String token = JwtUtil.createJwt(user.getUsername(), map);
    return new Result(ResultCode.SUCCESS, token);
}
```

画面 3:
```java
@RequestMapping(value="/login",method = RequestMethod.POST)
public Result login(@RequestBody Map<String,String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    //1.将登录令牌
    //2.获取subject，进入realm完成认证
    //3.获取sessionid
    //4.获取sessionid
    //5.构造返回结果
    User user = userService.findByMobile(mobile);
    if(user == null || user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    }else {
        //登录成功
        //api权限字符串
        StringBuilder sb = new StringBuilder();
        for (Role role : user.getRoles()) {
            for (Permission perm : role.getPermissions()) {
                if(perm.getTypes() == PermissionConstants.PERMISSION_API) {
                    sb.append(perm.getCode()).append(",");
                }
            }
        }
    }
}
```

画面 4:
```java
@RequestMapping(value="/login",method = RequestMethod.POST)
public Result login(@RequestBody Map<String,String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    //1.将登录令牌
    //2.获取subject，进入realm完成认证
    //3.获取sessionid
    //4.获取sessionid
    //5.构造返回结果
    User user = userService.findByMobile(mobile);
    if(user == null || user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    }else {
        //登录成功
        //api权限字符串
        StringBuilder sb = new StringBuilder();
        for (Role role : user.getRoles()) {
            for (Permission perm : role.getPermissions()) {
                if(perm.getTypes() == PermissionConstants.PERMISSION_API) {
                    sb.append(perm.getCode()).append(",");
                }
            }
        }
    }
}
```

画面 5:
```java
@RequestMapping(value="/login",method = RequestMethod.POST)
public Result login(@RequestBody Map<String,String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    //1.将登录令牌
    //2.获取subject，进入realm完成认证
    //3.获取sessionid
    //4.获取sessionid
    //5.构造返回结果
    User user = userService.findByMobile(mobile);
    if(user == null || user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    }else {
        //登录成功
        //api权限字符串
        StringBuilder sb = new StringBuilder();
        for (Role role : user.getRoles()) {
            for (Permission perm : role.getPermissions()) {
                if(perm.getTypes() == PermissionConstants.PERMISSION_API) {
                    sb.append(perm.getCode()).append(",");
                }
            }
        }
    }
}
```

画面 6:
```java
@RequestMapping(value="/login",method = RequestMethod.POST)
public Result login(@RequestBody Map<String,String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    //1.将登录令牌
    //2.获取subject，进入realm完成认证
    //3.获取sessionid
    //4.获取sessionid
    //5.构造返回结果
    User user = userService.findByMobile(mobile);
    if(user == null || user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    }else {
        //登录成功
        //api权限字符串
        StringBuilder sb = new StringBuilder();
        for (Role role : user.getRoles()) {
            for (Permission perm : role.getPermissions()) {
                if(perm.getTypes() == PermissionConstants.PERMISSION_API) {
                    sb.append(perm.getCode()).append(",");
                }
            }
        }
    }
}
```

画面 7:
```java
@RequestMapping(value="/login",method = RequestMethod.POST)
public Result login(@RequestBody Map<String,String> loginMap) {
    String mobile = loginMap.get("mobile");
    String password = loginMap.get("password");
    //1.将登录令牌
    //2.获取subject，进入realm完成认证
    //3.获取sessionid
    //4.获取sessionid
    //5.构造返回结果
    User user = userService.findByMobile(mobile);
    if(user == null || user.getPassword().equals(password)) {
        return new Result(ResultCode.MOBILEORPASSWORDERROR);
    }else {
        //登录成功
        //

