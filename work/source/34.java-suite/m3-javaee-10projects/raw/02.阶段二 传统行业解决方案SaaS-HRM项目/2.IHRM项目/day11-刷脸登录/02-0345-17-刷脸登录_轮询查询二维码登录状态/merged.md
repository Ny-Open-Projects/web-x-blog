# 17-刷脸登录：轮询查询二维码登录状态

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\17-刷脸登录：轮询查询二维码登录状态_【海量资源尽在 ubkz.com】.mp4
- 时长 8分16秒（音频 497s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们已经写好了这个创建二维码的这个代码那接下来呢我们其实就可以着手进行一个简单的测试工作但是在测试前有必要和各位简单的来说一下就是我们整个系统来说呢不管是系统为服务还是其他为服务都有一个用户认证以及健全的一个控制咱们是使用SERO来做的那在SERO的时候呢咱们进行了一个配置就是说有一些URL必须要经过登录才能访问还有意见吗
[00:29] 那我们现在今天完成的这个刷链登录的这些不管是二维码生成还是检查二维码或者是这边链登录或者是图像检测不管是哪一个方法是不是都是不用登录也能进访问啊所以我们需要配置一把这几个请求接口的一个认证的一个过滤那我们怎么去配置呢其实很简单把这个接口下的所有请求链接咱们都把它
[00:59] 设置为匿名访问其实就可以了那也比较简单好了这个呢是我们当前刷脸登录所涉及到的所有接口的一个副地址那我在这边share a page将所有的这些地址给它设置为nanon的这种匿名访问就可以了filter map打点put好了里面可以添加上相当路径注意这回来一个杠星星这个代表的是当前这个路径下的所有此路径
[01:29] 当然也包含自己代表所有好了那接下来这边全部配置成ANON的这么种匿名访问的情况OK那这样一来我已经把所有的这些都配置好了准备好了之后为了我们一会儿方便观察其实我可以把这个Fill对象给它打印出来我们来看一下是否可以生成
[01:49] OK那接着我们开始进行启动那需要各位注意的是我这个系统呢现在已经配置了Erica所以在这边我也需要把Erica服务先给它启动起来OKErica启动那接着找到我的系统微服务好了找到我们的启动类System ApplicationOK走好了那这样一来呢这两个工程呢就开始启动了当然了启动呢也是比较快的也是比较快的好了让它慢慢启动吧我在这边
[02:23] 打开POSMAN开始准备做一个简单的测试工作OK这个稍微有点慢啊好了这个POSMAN呢现在已经打开了各位耐心等待一下OK已经打开了那打开了之后我们可以进行访问那我们现在访问的其实就是localhost的冒号我们的系统微服务9002的端口那现在我请求的接口路径我也copy过来Ctrl C拿到这边Ctrl V好了第一个QR Code生成二维码
[02:57] 靠过来那注意我们的请求方式get方式也没问题get方式OK走各位发现现在呢已经操作成功了这边呢有我们的code返回的唯一标志还有我们的fail指的是我们一个dateurl的所有数据当然了我从这边靠呢可能会有点问题啊我就不从这边靠了我们刚才专门打印出了相应的这段内容system application哎这一段是我所有二维码的
[03:28] Data URL数据Ctrl C Copy过来打开论运器我们看一下是否生成二维码走过来看二维码已经生成成功了那二维码生成成功之后呢接着呢咱们就继续的往下去做了那我们接下来完成的是第二个接口第二个接口就是查询那这个接口呢刚才也跟各位仔细的说过什么意思就是在我的页面端你调出来二维码
[03:57] 接下来这个二维码立马在我们的登录页就开始不断的进行轮旋查询根据我们这个唯一标志就是我们刚才生成的code给你传过来去看一下我当前这个二维码它的一个登录情况用户是当前正在登录还是已登录还是登录失败了或者是还没有开始扫描所以它不断的在查询不断的在查询的过程当中我们开始给它一些响应
[04:21] 给它一个返回结果那么的返回结果封装到result当中当然我们这边是不是用一个face logging result里面有我们的返回状态里面有我们的用户ID里面有我们的token当然了token和UID是当你征服成功之后才会拿到的没错吧那好了接下来我们开始把这个代码也给它编写完整
[04:42] 那这个代码呢相对来说就比较简单了就比较简单了我们可以同样的借助face logging Service打点调用里面的方法好了我们这里面的方法呢之前也写过一个调用它的check qr code即可check qr code那接着我们把传递过来的code参数传递过去得到我们的响应对象好了那接下来呢这边直接包装成result对象并返回其实就可以了result
[05:15] 好了跟上边是一模一样OK这个QR code那接下来呢就是说我关注的是Service当中的这个代码的写法Service当中的代码的写法好了找到Service那接着我想说的是Service代码我们应该如何编写其实这个并不难那如何去做呢因为我们已经把设计到的所有的状态打开这张图形把四设计到的当前二维码
[05:46] 它登录的所有状态全部放到ready的数据库里面了那ready数据库里面其实我们刚才放的时候是不是就是这么一个对象啊所以我直接根据key从ready里面获取是不是就可以了那如果还没扫描是不是我就初始放进去的这个如果底下已经登录成功登录成功我里面是不是就是一个新的状态是不是就会随之进行一个更改啊没错吧所以对于我这边来说很简单直接通过code
[06:14] 构造出缓存的key构造出key之后从ready当中直接查询并返回其实就可以了所以呢这个比较简单来一起完成它string key等于好了get catch key把code放进去那简单说一下code其实还是一个唯一的标志所以这个key你构造出来也是一个唯一的这个各位都能理解那接下来呢我们就可以调用ready time leak调用里面的方法打点ops for
[06:45] valueops for value这么一个方法其中再打点get那我们的key已经有了通过key进行获取那其实获取到的就是我们的这个resolve对象直接返回即可当然了返回的过程当中需要做一个强制转型那这样一来呢我们第二个接口也写好了其实操作的就是一个redis的一个查询OK好了这个接口写好了之后同样的重新启动一下我们这个微服务
[07:16] 同样的重新启动这个vivo那启动成功了之后我在这边就对刚才这个code进行反复的查询OK那好了接下来这边呢再去启动一个窗口Ctrl C Ctrl V那我们现在访问的路径呢是QR code后面加上刚才请求的这个标志Ctrl C拿到这边Ctrl VOK那好了接着
[07:46] 我进行发送看一下请求的方式get没问题走send好了各位来看就目前来说我刚才这个二维码现在的一个状态是什么-1-1刚才我们说过了是不是代表的就是当前这个用户还没进行扫描那一会儿我如果把这改成0是不是代表失败了我又改成1是不是代表成功了那成功必然有user id必然要有我们的token那到时候我们一会儿测试的时候再说OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot、Shiro 和 Redis 的人脸识别登录系统的核心代码实现与接口测试流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- IDE 中展示 `ShiroConfiguration.java` 文件，其中定义了 Shiro 的过滤器工厂。
- 代码片段：
  ```java
  public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) {
      //1.创建过滤器工厂
      ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
      //2.设置安全管理器
      filterFactory.setSecurityManager(securityManager);
      //3.设置登录url
      filterFactory.setLoginUrl("/autherror/code-1");//跳转url地址
      filterFactory.setUnauthorizedUrl("/autherror/code-0");//未能授权的url
      Map<String,String> filterMap = new LinkedHashMap<>();
      filterMap.put("/autherror","anon");
      filterMap.put("/sys/login","anon");
      filterMap.put("/auth","authc"); //认证之后访问（登录）
      filterMap.put("/sys","authc"); //认证之后访问（登录）
      filterFactory.setFilterChainDefinitionMap(filterMap);
  }
  ```

画面2：
- IDE 中展示 `FaceLoginService.java` 文件，其中包含生成二维码和校验二维码的逻辑。
- 代码片段：
  ```java
  public QRCode getQRCode() throws Exception {
      //1.创建唯一标识
      String code = IdWorker.nextId() + "";
      //2.生成二维码
      String content = url + "?code=" + code;
      String file = qRCodeUtil.createQRCode(content);
      //3.存入当前二维码
      FaceLoginResult result = new FaceLoginResult(state: "1");
      redisTemplate.boundValueOps(getCacheKey(code)).set(result, 10, TimeUnit.MINUTES);//状态对象，失效时间，单位
      return new QRCode(code,file);
  }
  ```

画面3：
- IDE 中展示 `FaceLoginService.java` 文件，继续展示 `checkQRCode` 方法。
- 代码片段：
  ```java
  public FaceLoginResult checkQRCode(String code) {
      return null;
  }
  ```

画面4：
- IDE 中展示 `SystemApplication.java` 文件，其中包含 Spring Boot 的启动类和相关配置。
- 代码片段：
  ```java
  @SpringBootApplication(scanBasePackages = "com.ihrm")
  @EntityScan(value="com.ihrm.domain.system")
  @EnableEurekaClient
  @EnableDiscoveryClient
  @EnableFeignClients
  public class SystemApplication {
      public static void main(String[] args) { SpringApplication.run(SystemApplication.class, args); }
      @Bean
      public IdWorker idWorker() { return new IdWorker(); }
      @Bean
      public JwtUtils jwtUtils() { return new JwtUtils(); }
      @Bean
      public OpenEntityManagerInViewFilter openEntityManagerInViewFilter() { return new OpenEntityManagerInViewFilter(); }
  }
  ```

画面5：
- IDE 中展示 `SystemApplication.java` 文件，鼠标光标位于 `openEntityManagerInViewFilter` 方法上。
- 代码片段：
  ```java
  public OpenEntityManagerInViewFilter openEntityManagerInViewFilter() { return new OpenEntityManagerInViewFilter(); }
  ```

画面6：
- Postman 界面，准备发送一个 GET 请求到 `localhost:8002`。
- 请求 URL：`GET localhost:8002`

画面7：
- IDE 中展示 `FaceLoginController.java` 文件，其中包含 `@RestController` 注解的类和 `@RequestMapping` 注解的方法。
- 代码片段：
  ```java
  @RestController
  public class FaceLoginController {
      @Autowired
      private FaceLoginService faceLoginService;
      @RequestMapping(value = "/qrcode", method = RequestMethod.GET)
      public Result qrcode() throws Exception {
          QRCode qrCode = faceLoginService.getQRCode();
          return new Result(ResultCode.SUCCESS,qrCode);
      }
  }
  ```

画面8：
- 浏览器界面，显示一个二维码图片。
- 二维码内容：`data:image/png;base64,VRORw0K...`

画面9：
- IDE 中展示 `FaceLoginController.java` 文件，其中包含 `@RequestMapping` 注解的方法。
- 代码片段：
  ```java
  @RequestMapping(value = "/qrcode/{code}", method = RequestMethod.GET)
  public Result qrcodeCheck(@PathVariable("code") String code) throws Exception {
      return null;
  }
  ```

画面10：
- IDE 中展示 `FaceLoginController.java` 文件，鼠标光标位于 `qrcodeCheck` 方法上。
- 代码片段：
  ```java
  public Result qrcodeCheck(@PathVariable("code") String code) throws Exception {
      return null;
  }
  ```

画面11：
- IDE 中展示 `FaceLoginService.java` 文件，其中包含 `checkQRCode` 方法。
- 代码片段：
  ```java
  public FaceLoginResult checkQRCode(String code) {
      return null;
  }
  ```

画面12：
- IDE 中展示 `FaceLoginService.java` 文件，其中包含 `loginByFace` 方法。
- 代码片段：
  ```java
  public String loginByFace(String code, MultipartFile attachment) throws Exception {
      return null;
  }
  ```

画面13：
- IDE 中展示 `FaceLoginController.java` 文件，其中包含 `@RequestMapping` 注解的方法。
- 代码片段：
  ```java
  @RequestMapping(value = "/qrcode", method = RequestMethod.GET)
  public Result qrcode() throws Exception {
      QRCode qrCode = faceLoginService.getQRCode();
      return new Result(ResultCode.SUCCESS,qrCode);
  }
  ```

画面14：
- Postman 界面，准备发送一个 GET 请求到 `localhost:8002/sysFaceLogin/qrcode/1077083504325447880`。
- 请求 URL：`GET localhost:8002/sysFaceLogin/qrcode/1077083504325447880`

