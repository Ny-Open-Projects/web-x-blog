# 2.9 用户服务 - 工程运行分析

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day2 微服务框架与基础服务
- 源文件：06.阶段六 冷链监控平台项目\day2 微服务框架与基础服务\2.9 用户服务 - 工程运行分析_【海量资源尽在 666java.com】.mp4
- 时长 11分57秒（音频 718s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 前面我们非常快速的来整个的看了一下我们整个用户服务它的一个整个的一个代码结构那么我们现在呢来给大家演示一下整个代码的如何运行起来的那首先的话因为我们当前的服务连接了我们的服务注册中心那么首先呢我需要把我们的服务注册中心给启动起来那么这个服务注册中心启动的也比较快一些因为它的这个服务相对来讲也比较简单
[00:28] 紧接着我们再把我们的这个用户服务给它启动起来OK我们服务制作中心已经启动起来了那么启动起来之后呢我们可以先看一看我们当前的这个服务制作中心它的里边有什么样的一些服务local host然后端口是多少8001对吧我们的这个服务我们看一看我们有8001没错OK那
[01:03] 此时我们当前只有一个Unicore的服务因为我们把自己注册上去了那紧接着我们再把我们的user application给添加进去那么我们先启动user application在这个地方大家其实可以注意到我们当前他选择的profile其实就叫deevee对吧这是我们前面也给大家讲过我们的deeveeapplication-deeveok
[01:35] 此时已经启动起来了那么启动起来之后呢我们如何来测试它呢因为我们知道当前的这个用户服务它它提供相外提供的服务就是有登录服务和我们的这个退出服务那么登录服务的话我们可以用Postman来测试它那么Postman是一个什么东西Postman实际上就是一个测试工具那么我们可以测试一些接口当然了还有其他的一些工具我们来
[02:04] 其他的一些工具我们可以使用那么我们在Postman里边需要输入些什么信息第一我们需要选择我们当前的发送的一个方法这个方法是什么是get还是post这取决于我们当前的这个服务比如说loginlogin的话它是post的卖品所以我们在这儿我们要选择我一个post那么它的URL是什么URL的话http然后我们的loghost
[02:35] 然后下一步的话就是我们的端口对吧我们端口是多少是当前这个server的端口我们看一下我们在配置里边我们配置了什么8185对吧81858185然后紧接着是什么紧接着是我们的我们看一看啊紧接着是我们的这个code为什么是code呢因为我们在当前的application的yaml文件里边配置的是一个我们server的
[03:01] Serverlet的context path也就是我们当前这个工程的它的路径那么这个路径的话就是code而不是code-user我们可以看看我们的这个服务桌的中心里边服务桌的中心里边我们刷新一下服务桌的中心里边这个application应用的名字叫什么code-user这个code-user就是下边这个application name但是我们在如果Postman来调用请求的时候我们需要使用的是这个code
[03:31] OK 我们下一个其实就是个code接着是我们 API 它的一个地址这个地址实际上是由 sys user再加上一个loginOK 此时我们有了这个方法是post然后URL是有了那下一步的话是我们的提交的参数而这个提交参数是什么呢它是一个request body
[04:00] 那么request body其实就是一个body类型的那么这个body类型的我们需要用的是raw类型然后呢它的类型我们选择是一个json也就是说我们需要传递一个json字符串的类型那么这个json字符串我们可以添加一个json的字符串然后呢这个json字符串里边是有什么呢有username对吧因为这个对象实际上是syslogin form那么syslogin form是里边的
[04:29] 数据是什么第一个use nameuse nameuse name是什么呢是叫做admin就是我们的用户名那紧接着有一个是什么passwordpassword那么这个密码是什么呢密码就是我们当前用户对应的一个密码password123那下面的话可不可以写这个capture这是一个字段这个字段实际上是一个验证码那么我写也行我其实不写也行
[05:04] 因为我们在我们的程序里面其实没有用到它那我就不写它了那此时我们已经把我们的body给它组装好了也就是说我们参数组装好了那下一步我们点散的散的时候它此时它会调用我们后台反回了一个结果那反回结果是一个什么样子的呢我们定义好了一个result那么这个result我们可以看一看我们的Controller层里边我们Controller里边Controller层我们调用它
[05:33] 调用它之后呢我们首先它查询数据库里面有没有这个用户那么它发现有用户的时候它如果是发现用户名密码相匹配也就是说我把前台传过来的密码我经过一次加密之后和我数据库里面存储的这个密码是否是匹配的比如说我们打开这个这个密码实际上在数据库里面是一个加密的一个密码
[06:02] 那么我们通过这种方式也就是说我们前后两次的这个加密的方式是一样那么我们对于相同的字符串进行了一个加密那得的结果是一样的对吧所以说我们在这进行了一个比对如果是密码不密码不对或者用后账号不存在的情况下我们就会给它返回一个result arrow就是一个密账号或密码不正确那我们再看一看我们poster manposter man里边我们如果密码我们随便给它再加一个字符串
[06:31] 那就是这个密码是错误的对不对那它给我返回的是一个什么code是arrow500然后它的message就是账号或密码不正确就是我们在这里面设置的你的账号和密码实际上是不正确的那如果我们的账号密码是正确的情况下我们在这它的账号密码是正确的情况它给我们返回的是第一有一个code等于0第二有一个message等于success我们看一看如果它是正确了之后
[06:59] 我们在这儿我们返回了是什么我们要生成一个token生成一个token之后我们啊直接把这个作为一个result返回过来了那么这个result是一个什么呢我们看看这个result这个类这个result类呢它是在我们的这个common里边了我们看一下common的有tail这里边有resultresult它会给我们封装了一个code
[07:30] 就是code然后呢message就是message就这有两个字段对吧有这两个字段那其他这两个字段是从哪来的呢而且code的值是从哪来的呢那么我们看一看接着看我们刚才的这个Controller层Controller层里边它会生成一个token我们看一看这个sysuser token Service而这个Service里边它会生成一个token就是这个地方生成token然后它会调用我们common的里边的一个
[08:00] token generator那么它来生成一个新的一个token然后呢把当前的值设置上然后过期时间设置上过期时间就是当前的时间再加上一个过期的一个频率比如说这个是12小时12小时然后再乘1000然后我们判断是否生成过token那么根据我们的用户这是一堆算法了我们根据当前的用户的ID
[08:30] 用户的这个然后设置他的ID设置token设置过去时间然后这个时候我们把它保存token了而保存token的时候这个是一个token的一个servicesysuser token Service这个来讲的话它会把我们的这个token保存到我们的另外一张表里边就是我们的这个sysuser token这张表里边那保存完了之后它会返回一个result那么这个result是什么呢result.ok.put
[09:01] 就是put他put什么呢put第一个是token第二再put一个expert也就是过去的时间这个就是我们在前刚才在poster man里边调用的时候我们发现的有一个过去时间有一个token那么就是在代码里边在这实现的那么result ok是什么东西result ok我们可以看一下result ok这是result那么result ok在哪呢result ok
[09:32] 我们看一看那么resultOK在这默认的情况下它是一个我们的有一个就是说这个result新生成的时候它是一个code是0然后的message呢是一个success那么当它进行resultOK的时候那它其实就是新生成了这么一个result然后呢再把其他的给它迁移进来对吧所以说这个时候它的默认的就是一个0和success那么这和我们前端
[10:03] 拿到的就是我们Posman拿到的这个一个code等于0一个message等于success是一样的OK这是我们的整个的一个接口它在调用的过程中的一个流转的一个方向那么我们前面经过了经过了什么呢经过了我们的controllercontroller层里边大家需要在这个地方需要了解Controller层里边它提供给前端的这个接口的路径到底是什么
[10:29] 它包含了几部分包含了实际上包含了三部分第一部分是我们的application的一个application的一个一个地址就是这个token这个code然后另外一部分呢是包含了我们这个类的前面这部分sysc user那么最后一部分是包含了我们这个方法的一个地址那么整体构成了我们的一个
[10:56] API的一个地址那么把参数传进来然后返回结果返回的是一个统一的一个结构的那么有了这样统一结构那么前端其实是不是比较容易解析容易处理了因为前端的话首先会拿到这个阶层字幕率会得到什么呢会得到一个code等于多少然后会得到message等于什么那么如果他会发现code等于0的情况下那我就可以做额外的做什么样的处理了我等于
[11:21] 等于500的时候我做什么样的处理这是前端根据这我们返回给他们的值那么得到的一个结果这是我们给大家演示的我们的整个code user这个过程code user这个服务里边的一个登录的一个过程那么从这个里边大家要学会或者叫了解我们的如何来进行定义我们的返回值然后我们
[11:46] 每一个返回值是如何通过Controller来调用我们Service由Service来查询我们数据库这样的一个过程大家需要深刻的了解的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Cloud 的用户登录系统，包括配置文件设置、Eureka 服务注册、数据库连接、登录接口实现及通过 Postman 发起登录请求并验证返回结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- IDE 中打开并编辑 `application.yml` 文件，配置了 Tomcat、端口、字符编码、Spring 应用名、激活的 profile 为 `dev`、时区、日期格式等。
- 项目结构中可见 `application.yml`、`application-dev.yml`、`application-test.yml` 等配置文件。
- 代码内容：
  ```yaml
  server:
    Tomcat:
      uri-encoding: UTF-8
      max-threads: 1000
      min-spare-threads: 30
    port: 8185
    connection-timeout: 1000ms
    servlet:
      context-path: /cold
  spring:
    application:
      name: cold-user
      # 打开 dev/test/prod
      profile: dev
    # jackson时间格式化
    time-zone: GMT+8
    date-format: yyyy-MM-dd HH:mm:ss
    servlet:
      multipart:
  ```

画面 2：
- 展示了在浏览器中搜索 JDBC 驱动的场景，但未显示具体结果。
- 未提供任何代码或配置。

画面 3：
- IDE 中编辑 `application-dev.yml` 文件，配置了 Eureka 客户端地址和数据源信息。
- 代码内容：
  ```yaml
  Eureka:
    client:
      Service-url:
        defaultZone: http://Eureka.itheme.com:800/Eureka
  spring:
    datasource:
      type: com.alibaba.druid.pool.DruidDataSource
      druid:
        driver-class-name: com.mysql.jdbc.Driver
        url: jdbc:mysql://1/12.17.0.249:3306/cold-user?useUnicode=true&characterEncoding=UTF-8&allowMultiQueries=true&useSSL=false
        username: cold
        password: druid
  ```

画面 4：
- IDE 中显示了 `application-dev.yml` 文件，其中 `spring.datasource.druid` 配置块被选中。
- 未提供任何代码或配置。

画面 5：
- Postman 界面，新建了一个未命名的 GET 请求。
- 未提供任何代码或配置。

画面 6：
- IDE 中编辑 `application.yml` 文件，配置了 Spring 应用名和激活的 profile 为 `dev`。
- 代码内容：
  ```yaml
  spring:
    application:
      name: cold-user
      # 打开 dev/test/prod
      profile: dev
  ```

画面 7：
- Postman 界面，新建了一个 POST 请求，目标地址为 `http://localhost:8185/`。
- 未提供任何代码或配置。

画面 8：
- 展示了桌面多窗口切换的场景，包括 Postman、IDE、浏览器、Typora 等。
- 未提供任何代码或配置。

画面 9：
- Postman 界面，设置了一个 POST 请求，目标地址为 `http://localhost:8185/cold/user/login`，Body 为 JSON 格式。
- 代码内容：
  ```json
  {
    "username": "cold1",
    "password": "cold123"
  }
  ```

画面 10：
- IDE 中显示了 `SysLoginController.java` 文件中的 `login` 方法，用于处理登录请求。
- 代码内容：
  ```java
  @PostMapping("/login")
  public Map<String, Object> login(@RequestBody SysLoginForm form) throws Exception {
      //用户不存、密码错误
      if (user == null || !user.getPassword().equals(new Sha256HashForm().getPassword(), user.getSalt().toHex())) {
          throw new RuntimeException("账户或密码不正确");
      }
      //生成token，并保存到数据库
      Result result = sysUserTokenService.createToken(user.getUserId());
      return result;
  }
  ```

画面 11：
- IDE 中显示了 `Result.java` 文件，其中定义了 `error` 和 `ok` 方法。
- 代码内容：
  ```java
  public static Result error() { return error(HttpStatus.SC_INTERNAL_SERVER_ERROR, "未知异常，请联系系统管理员"); }
  public static Result error(String msg) { return error(HttpStatus.SC_INTERNAL_SERVER_ERROR, msg); }
  public static Result error(int code, String msg) {
      Result result = new Result();
      result.put("code", code);
      result.put("msg", msg);
      return result;
  }
  public static Result ok(String msg) {
      Result result = new Result();
      result.put("msg", msg);
      return result;
  }
  ```

画面 12：
- IDE 中显示了 `SysUserTokenServiceImpl.java` 文件中的 `createToken` 方法。
- 代码内容：
  ```java
  @Override
  public Result createToken(long userId) {
      //生成一个token
      String token = TokenGenerator.generateValue();
      //当前时间
      Date now = new Date();
      //过期时间
      Date expireTime = new Date(now.getTime() + EXPIRE * 1000);
      //判断是否已超出token
      SysUserTokenEntity tokenEntity = this.getByUserIdTo();
      if (tokenEntity != null) {
          //更新token
          tokenEntity.setToken(token);
          tokenEntity.setExpireTime(expireTime);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime(now);
          tokenEntity.setUpdateTime

