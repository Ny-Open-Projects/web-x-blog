# 13-刷脸登录：搭建环境-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\13-刷脸登录：搭建环境-上_【海量资源尽在 ubkz.com】.mp4
- 时长 10分47秒（音频 647s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 简单的和各位介绍了一下我们这个二维码那接下来呢就可以把这些所有的内容全部融合到一起就是一个搭建环境的一个过程搭建好环境之后我们开始着手去编写我们刷脸登录的这个代码实现那其实对于搭建环境来说呢有很多的地方其实是比较浪费时间的并且这些地方呢我们都已经都掌握了所以呢对于搭建环境希望各位呢和我一样
[00:28] 从今天的资料当中把这些东西直接抠进来就可以我们只写关键的代码就可以了好了在我的资源当中呢有一个代码在这个代码当中把我们今天要用到的一些请求的实体类要用到的一些工具类要用到的一些坐标等等全部给各位准备好了那接下来我们就开始进行搭建环境的工作首先呢第一件事注意搭建环境第一件事
[00:54] 导入我们的坐标那这个坐标呢一共有三部分内容首先第一部分就是我们百度运营爱后两部分这两部分总和起来就是我们生成二维码图片的所以把这个Ctrl C Copy下来那注意我们Copy到哪个工程是这样的不管是用户登录还是我们的面部识别的这种登录我们全部是在系统微服务当中所以我直接把它引入到我系统微服务的工程里面就可以了好了我写到下边
[01:25] 好 这边让它自己加载我不管了那这样一来第一件事我们搞定了就是把坐标引入进来那坐标一如进来了之后接来就是说我进行一个请求的过程当中可能会涉及到一些实体类这两个实体类Ctrl C也把它拷过来注意拷到哪儿我们之前说过所有的实体类全部是在我们的model这个里面好了那接下来拷到model部分
[01:53] 靠到我们system当中注意我把它放到响应里面因为它跟数据库没什么关系OK靠到这两个实体内一个叫做QR code一个叫做face login result那这个QR code代表的是什么含义是这样的我们可以一起再回到我们刚才讲需求的时候的这个人链登录的样图那我们都知道刚才总结出来了整个人链登录我们副端后台需要提供四个接口第一个接口二维码的
[02:25] 第二个接口查询登录状态第三个接口调用摄影头判断是否是人的一个头像的好了第四个接口是不是就是进行我们叫做人脸进行人脸识别并且进行人脸查找的这么一个接口所以一共四个接口这四个接口里面其中第一个生成二维码那你请求到服务端后台要有一个唯一的标志返回给我那接着那你还要生成一个二维码那这个二维码也是我们服务端生成那怎么
[02:54] 把这个二维码信息交给我们的前端是这样的我准备通过Data UIL的形式也就是拼成一个字符串返回给前端那前端直接拿到字符串展示二维码图片是不是就可以了所以呢这个返回对应的是一个射体类对象在这边就是QR Code那这个QR Code两个参数第一个一个随机的一个Code字符码当然了它是一个唯一的那还有一个Fill这是我们的二维码文件当然了这是一个
[03:24] Data URL的一个形式OK第一个我们说清楚了接着第二个那对于第二个呢叫做Face Logging Result这个代表什么含义来还是一张图片那我们在登录页呢其实有一个轮循查询的这么一个过程就是不断的通过这个V1编码去查询后台那查询后台的时候那可以给它一个状态比如说-1你查询之后V扫描
[03:48] 那如果是1代表登录成功如果是-1代表登录失败如果是0保健这边应该是0代表登录失败那这些呢都需要有响应那如果说登录成功的时候那登录成功的时候我除了要知道是1这个状态之外我还要知道当前登录用户的ID还要知道当前用户登录的那个别忘了我们还有个token字符串这个token字符串不管是JWT的里面的token还是我们share当中的session ID
[04:18] 这应该各位还有印象但是你必须要有所以呢对于这个查询返回做响应也是一个实体类封装到FaceLoginResult那其中有二维码的使用状态我们刚才说过了-1未使用好了接着0登录失败1代表登录成功当登录成功的时候我需要返回用户ID和我们的tokenOK所以底下又有两个一个叫做token
[04:50] 就是我们的token信息用户信息还有一个叫做IDOK那这个咱们也已经说清楚了那除了实体类之外呢还给各位准备了很多的资源那比如说呢还有工具类两个工具类这两个工具类Ctrl C注意这两个工具呢直接把它移入到我们的system当这个工程当中了这两个工具类其实既是一个是用来生成二维码的另一个是用来对百度云AI进行调用的所以我在Java这边
[05:21] 创建一个包抱歉创建一个包右键new一个packageutils好了把这两个Ctrl C Ctrl V全部拷过来那拷过来之后简单的做一个说明其中第一个叫做QR code utils那这个QR code utils它主要目的接收一个我们叫做content一个字符信息好了接下来接收了之后注意这里面QR code writerbeta max rates
[05:53] 好了还有buffer的image什么write这边呢返回new一个死郡这不是跟我们刚才写的那个生成二维码以base的data url形式一模一样嘛所以我把它抽取到一个工具类当中只不过我上面用一个component那这样一来其他地方直接auto-vare注入进来方便我们的使用OK好了那这个我们说过了接下来还有一个工具类这个工具类呢叫做百度云烟Utils
[06:20] 那这个百度云烟油条我们要做的事情有什么一共其实就这么四件事第一件事简单的说一下人脸注册那人脸注册注意接收两个参数user id和image那这个image其实也是一个我们叫做base64的这么一个形式好了这边呢就是client.adduser人脸注册我们之前也写过没错吧好了接下来接下来这边呢根据返回值判断注册是否成功
[06:51] 如果返回值是0代表成功如果失败代表false好了就这么一个人脸注册的当然除了人脸注册还有人脸更新我们说过了人脸注册和人脸更新其实是一模一样的好了那除了注册以及更新之外还有一个叫做人脸检测那这个人脸检测呢其实也是clant.editcat这么一个方法好了那这个方法里面呢返回值看一下是否包含叫做error code
[07:22] 那并且这个值是否为0如果是0的话代表的是处理成功的那处理成功的底下又有我自己的处理注意我这个处理是干什么的注意从里面拿到一个反为值叫做face number这个face number指的是你当前检测的人脸数量可能有这种情况就是说你发上来一张照片这张照片可能是一张合影里面有多个人那多个人显然不符合我们的要求我们检测的时候是不是只检测一个人
[07:51] 所以如果有多个人的话其实也是错误的所以这边如果只有一个人脸的话我们返回处如果是多个直接返回false当然了底下有一个人脸查找这个人脸查找就是client.search同样的判断一下是否是返回值为0是否我们的查询成功了查询成功之后我们底下从里面拿到user list还记得我们之前说过
[08:17] 要拿到user list因为这个user list是里面涵盖了相似度最高的这么几个用户信息那这个用户信息里面注意我们虽然是一个数组但是我们只用第一个因为第一个才是含金量最高的也就是最相似的没错吧那所以从这边我从数组里面拿到一个那我拿为啥要拿一个呀有的朋友说他给你返回了你直接用不就可以了吗不行因为还记住刚才说过了
[08:47] 它有一个评分在里面只有大于80分的我们才认为是同一个人所以这边我做了一个判断if评分大于80我才真正的得到这个用户的所有信息OK那这个代码咱们都之前都写过直接拿过来用就可以了我唯一不同的是把咱们什么的APP IDAPI Key还有Security Key还有Image Type和Group ID这些都是我们用到的一些
[09:15] 配置的一些基本属性我把这些基本属性以配置文件的形式体现到这边了OK好了同样的在上面ata component我们也是双间对象放到Sprite我们用的时候直接auto-vare进来就可以了OK那这个我们写好了之后那这两个工具呢由于要用到一些配置所以在这边打开resource配置文件在配置文件里面需要对一些基本的内容咱们也先做一个交代那这边呢同样配置文件里面的一些内容我也给各位准备好了
[09:46] Ctrl C拿过来Ctrl A好了AI这些是我们百度云AI里面相应的一些配置里面APP ID还有Key还有TabGroup ID等等这些都是我们之前玩过的好了还有一个QRURL那这个QRURL什么含义是这样的是这样的我们刚才不是要去生成一个二维码图片吗那这二维码图片是不是也是个
[10:15] 一个请求的一个地址啊那这个请求地址我在这边也给他写好了当了这个请求地址我要在本机测试的话其实可以写成localhost8080注意这个localhost8080是我们前端工程里面的某一个页面OK那也就意味着我通过手机扫描之后是不是就进入到了我这个前端工程的某一个页面方便我们进行处理啊OK好了那这样一来我这个基本的工程呢其实第一部分咱们就已经打结好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成百度人脸 API 实现人脸登录功能，包括依赖配置、实体类、工具类开发和配置文件设置。

2) 按时间顺序列出每张画面的要点：
画面1：桌面环境，显示“黑马程序员”和“博学谷”标志，无具体操作。
画面2：Notepad++ 编辑器中显示 Maven 依赖配置，包含百度 SDK 和 ZXing 依赖。
画面3：IntelliJ IDEA 项目结构，展示 ihm_parent 项目下的 ihm_system 模块。
画面4：桌面环境，鼠标悬停在“ihm”文件上。
画面5：PPT 页面，展示用户登录流程图，包含二维码生成、Redis 状态存储、人脸检测、登录成功/失败状态码逻辑。
画面6：IntelliJ IDEA 中展示 FaceLoginResult 实体类代码，包含 state、token、userId 字段和构造方法。
画面7：IntelliJ IDEA 项目结构，选中 ihm_common_model 模块。
画面8：IntelliJ IDEA 项目结构，选中 ihm_system 模块。
画面9：IntelliJ IDEA 中展示 BaiduAIUtil 工具类代码，包含 @Component 注解、私有字段和 init 方法。
画面10：IntelliJ IDEA 中展示 BaiduAIUtil 类的 faceRegister 和 faceUpdate 方法。
画面11：IntelliJ IDEA 中展示 BaiduAIUtil 类的 faceCheck 和 faceSearch 方法。
画面12：IntelliJ IDEA 项目结构，选中 ihm_employee 模块。
画面13：Notepad++ 编辑器中显示百度人脸 API 的配置信息，包括 apiId、apiKey、secretKey、imageType、groupId 和 url。
画面14：IntelliJ IDEA 中展示 application.yml 配置文件，包含数据库、Redis、ai 配置项。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```xml
<dependency>
    <groupId>com.baidu.sip</groupId>
    <artifactId>java-sdk</artifactId>
    <version>4.8.0</version>
</dependency>
<dependency>
    <groupId>com.google.zxing</groupId>
    <artifactId>core</artifactId>
    <version>3.2.1c</version>
</dependency>
<dependency>
    <groupId>com.google.zxing</groupId>
    <artifactId>javasec</artifactId>
    <version>3.2.1c</version>
</dependency>
```

画面6：
```java
package com.ihm.domain.system.response;
import java.io.Serializable;
@Data
@NoArgsConstructor
@ToString
public class FaceLoginResult implements Serializable {
    private static final long serialVersionUID = -1618426841373762391L;
    // 二维使用状态
    private String state;
    // 登录信息
    private String token;
    // 用户ID
    private String userId;
    public FaceLoginResult(String state, String token, String userId) {
        this.state = state;
    }
}
```

画面9：
```java
package com.ihm.system.utils;
import org.springframework.stereotype.Component;
@Component
public class BaiduAIUtil {
    @Value("${ai.appId}")
    private String APP_ID;
    @Value("${ai.apiKey}")
    private String API_KEY;
    @Value("${ai.secretKey}")
    private String SECRET_KEY;
    @Value("${ai.imageType}")
    private String IMAGE_TYPE;
    @Value("${ai.groupId}")
    private String groupId;
    private AipFace client;
    private HashMap<String, String> options = new HashMap<>();
    public BaiduAIUtil() {
        options.put("quality_control", "NORMAL");
        options.put("liveness_control", "LOW");
    }
    @PostConstruct
    public void init() { client = new AipFace(APP_ID, API_KEY, SECRET_KEY); }
}
```

画面10：
```java
public Boolean faceRegister(String userId, String image) {
    // 人脸注册
    JSONObject res = client.addUser(image, IMAGE_TYPE, groupId, userId, options);
    Integer errorCode = res.getInt("error_code");
    return errorCode == 0 ? true : false;
}
public Boolean faceUpdate(String userId, String image) {
    // 人脸更新
    JSONObject res = client.updateUser(image, IMAGE_TYPE, groupId, userId, options);
    Integer errorCode = res.getInt("error_code");
    return errorCode == 0 ? true : false;
}
```

画面11：
```java
Integer errorCode = res.getInt("error_code");
return errorCode == 0 ? true : false;
public Boolean faceCheck(String image) {
    JSONObject res = client.detect(image, IMAGE_TYPE, options);
    if (res.has("error_code") && res.getInt("error_code") == 0) {
        JSONObject resultObject = res.getJSONObject("result");
        Integer faceNum = resultObject.getInt("face_num"); // 人脸数量
        return faceNum == 1 ? true : false;
    } else {
        return false;
    }
}
public String faceSearch(String image) {
    JSONObject res = client.search(image, IMAGE_TYPE, groupId, options);
    if (res.has("error_code") && res.getInt("error_code") == 0) {
        JSONObject result = res.getJSONObject("result");
        JSONArray userList = result.getJSONArray("user_list");
        if (userList.length() > 0) {
            return userList.getJSONObject(index: 0);
        }
    }
}
```

画面13：
```
apiId: 15191935
apiKey: cyWSHgac93Vtdmt42OwbM6pu
secretKey: yflGusMvCLBdOnyabFlubMyod91EDEZW
imageType: BASE64
groupId: itcast
url: https://192.168.50.110:8080/4/FaceLogin
```

画面14：
```yaml
driver-class-name: com.mysql.jdbc.Driver
url: jdbc:mysql://localhost:3306/ihm?useUnicode=true&characterEncoding=utf8
username: root
password: 111111
jpa:
  database: MySQL
  show-sql: true
  open-in-view: true
redis:
  host: 127.0.0.1
  port: 6379
jwt:
  config:
    key: adds-ihm
    ttl: 3600000
ai:
  appId: 15191935
  apiKey: cyWSHgac93Vtdmt42OwbM6pu
  secretKey: yflGusMvCLBdOnyabFlubMyod91EDEZW
  imageType: BASE64
  groupId: itcast
  url: https://localhost:8080/faceLogin
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面5：PPT 页面标题为“用户登录页面”和“落地页（魔扫篇）”。流程图结构：
- 用户登录页面 → 生成二维码 → 存入 Redis（用户未扫描状态：-1）
- 用户扫描二维码 → 调用手机摄像头拍照 → 检查是否有面部头像 → 1234：-1（未扫描）
- 根据唯一标识是否登录成功 → 查询 Redis 状态 → 进行后续操作
- Redis 状态：1234：-1（未扫描）→ 1234：1（登录成功）→ 1234：0（登录失败）

5) 无其他内容。

