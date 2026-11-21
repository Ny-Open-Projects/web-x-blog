# 16-刷脸登录：生成二维码

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\16-刷脸登录：生成二维码_【海量资源尽在 ubkz.com】.mp4
- 时长 10分17秒（音频 617s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们已经把这个人脸注册和人脸更新这一块呢搞定了那接下来呢我们就去完成第二块内容就是二维码生成那对于二维码生成呢也比较简单也不难那我们开始打开idea在这边找到我们刚才的face login Controller那对于这个face login Controller我们要进行一个修改就是去完成第一块功能就是一个二维码
[00:27] 那对于这个二维码来说呢我们要返回一个QRQR code这一个对象那这个对象我们从哪获取其实很简单可以通过我们的Service所以这边out to where依赖注入过来我们的叫做face login serviceface login Service好了那接下来呢我们可以通过face login Service打点调用你们的方法好了我们写过一个方法叫做来看一下get QR code
[00:59] get qr code那这样一来呢我们就可以得到一个qr code这么一个对象那这个对象我们得到了之后直接就可以返回了好了当我们返回成功new一个resultresultcode打点success逗号第二个参数qr code即可那我们的Controller代码各位会发现比较简单比较简单我们之前还是跟我们之前的逻辑一模一样
[01:27] 把所有内容封装到result对象当中我们现在封装的是QR code那QR code如何获取其实就是根据Service来做的那接下来我们要补充的其实就是Service层这个代码了那对于Service层代码就是要去创建一个二维码那这个二维码如何创建它有没有一些规定在里面那我们一起来看一下首先我们创建二维码第一件事
[01:52] 干嘛呢就是对于我们而言是不是要获取一个叫做唯一的这么一个标志所以我需要创建唯一的标志那创建唯一的标识如何去做这个也不难我们之前呢是不是保存用户的时候保存其他内容的时候保存一切的时候都可以得到一个唯一的ID啊那我们是不是可以通过我们叫做ID worker我们的ID生成器也能得到一个唯一标志吗所以在这边我out to where进来一个我们叫做ID
[02:24] 我可ID我可那好了ID我可已经准备好了那我就可以创建唯一标志那唯一标志创建好了之后接来我们要做的第二件事干嘛呢其实就可以生成二维码二维码那生成二维码之后接来注意别忘了是这样的就是说还是我们之前这张图你生成二维码的时候你需要往ready当中
[02:54] 放条数据代表的是当前这个唯一标志对应的二维码它还未扫描所以我需要把一个数据存到readits里面好了那接下来存入当前二维码的状态OK那当然存到二维码状态呢我们其实是存入ready当中了OK那接下来我们把这个代码呢都给它搞定首先第一件事创建唯一标志那唯一标志ID worker打点
[03:27] 打点我们可以next id好了这样一来呢来一死郡我就叫code了当然死郡也行呢后面加一引号了代表是一个死郡OK那好了接下来第二件事我们要生成二维码那我们都知道生成的二维码其实就是一个url地址没错吧所以呢在生成二维码的时候先把这个url地址呢给他先写出来给他拼装好就是content
[03:54] 那这个URL地址从哪来呢首先就是上面我们是不是把它配置到配置文件里了OK那好了注意那在URL地址里面要生成的一个在二维码当中要生成的这么一个URL地址那这个地址是我们通过手机进行扫描那通过手机进行扫描是不是也应该得到这个唯一标志啊那通过这个唯一标志最终是不是要修改数据库里面用户的一个登录状态
[04:21] 没错吧所以这个code也要携带到URL当中所以怎么做呢很简单URL加上问号code等于加上code那这样一来我拼接好了这么一个URL地址那这个code其实也携带到你扫描的那边了好了那这个地址我们搞定了之后接着可以调用我们的工具类去生成二维码了
[04:48] 那我们的工具也需要out to where依赖注入进来这个工具叫做QRcodeUtilsOKQRcode那别忘了这QRcode我们是common所以可以注入进来那好了我们借助方法借助方法QRcodeUtils打点进入里面的createQRcode把content传递进去那这样一来就能得到了我们的二维码代表的
[05:20] 这个data ui数据好了那接下来呢就是说别忘了别忘了当我把所有都搞定的时候需要存入二维码这个状态那存入二维码状态我们要存入到ready当中那存入readies我们可以借助一个工具这个工具呢叫做也是需要注入进来啊叫做previtareadiestimeletmp啊这个readytimelet还没有啊没有的话那我这边呢需要打开
[05:54] 碰点S秒引入一下SpringData里面的Ready相关的功能这个坐标好了这个坐标也比较简单直接GPA改成Ready是即可OK好了这边已经引入进来了那我可以通过AutoWear注入一个叫做ReadyTimeLeak的这么一个对象好了就叫做ReadyTimeLeak了好了当然了这个ReadyTimeLeak里面你可以指定它的key的类型死菌类型的后面来一个object
[06:28] 对象类型的一个value即可OK那好了接下来呢我们就可以通过redis-tml往redis数据库里进行数据的一个存入那需要各位注意啊那redis-tml呢其实还是要有一个基本的配置这个配置呢在我们之前的代码之前写过它其实就是sprint redis host report这个其实我们之前代码写过所以咱们就在这边不需要进行额外的配置了
[06:57] 好了接下来存入二维码信息如何去存其实也不难可以借助ready time lake来进行存储好了这边如何进行存储借助他们里面的一个方法叫做bound value OPS好了这边需要一个key这个key如何生成很简单我底下写了一个专门得到key的这么一个小的一个方法所以对于我来说你需要传递一个code进来我们的key都叫做qr code
[07:28] 加上你这个 q 的唯一标志就可以了所以我这边把 code 传递过去根据唯一标志来进行生成的那你存读的这个 key 就是 qr code 下滑线你这个唯一标志吧好了接下来调用里面的方法打点打点我开始往里 set好那 set 的时候我们可以用哪个方法来做其实都可以其实都可以
[07:54] 那比如说比如说我就以第三个举例因为第三个方法呢它里面可以指定它的一个过期时间嘛好了那接下来我们往里存存的数据第一个第一个参数就是我们的这个状态二维码状态状态对象好了第二个第二个是什么第二个就是我们的过期失效时间好了接着第三个第三个是我们的单位就是这个失效时间呢你可以写30但是30究竟是30秒30分钟
[08:25] 还是三十个小时所以有一个单位给他进行一个描述那接着我们想说的是你这个状态对象那你可以写注意我们这个刚才说过了我们这个状态10-110这么一个状态但是呢为了方便我们查找我们把这个状态封装到我们查询的这个对象里面别忘了我们还有一个叫做facelogin result这么一个result对象
[08:55] 那这个resolve对象里面其实里面包含了二人码状态包含了你这个token和user id只不过当前是一个初始化的情况这个状态是不是可以给它指定为我们叫做-1即可呀那同时我底下有一构造方法所以对于我来说直接等于你有一个对象拿过来我们这边是初始化的一个状态给它来一个-1不就可以了吗OK那这样一来
[09:27] 抱歉我们这边接收的是一个死菌类型的一个值所以我这边用死菌包裹上好了那接下来呢我们就可以把result放进去OK那第二个失效时间失效时间呢比如说可以写10写一10然后呢我们的单位单位呢记住time unit我可以写比如说hour或者写分钟都可以我就来10分钟即可那这样一来我这里面的业务咱们已经搞定了那接下来就是返回值
[09:58] 那返回值直接new一个QR code那里面我也写好了构造方法我们可以通过把code传递进去通过把我们的fill传递进去那这样一来我们业务搞定了并且也有了返回值

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解基于人脸识别的登录系统后端实现，重点是二维码生成、状态管理及与Redis的交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT，列出完成人脸识别登录需解决的5个问题：人脸注册、二维码生成、二维码检测、人脸检测、人脸登录。
画面2：展示IDEA中`FaceLoginController`类，定义了`@RequestMapping("/qrcode")`和`@RequestMapping("/qrcode/{code}")`两个GET接口。
画面3：在`FaceLoginController`中，`@RequestMapping("/qrcode")`接口的注释说明“获取二维码”，并提示“可用工具生成二维码对象”。
画面4：展示`FaceLoginService`类，定义了`@Value("${qr.url}")`注入配置，以及`@Autowired`注入`IdWorker`。
画面5：在`FaceLoginService`中，`getQRCode()`方法的注释“//1.创建唯一标识”和“//2.生成二维码（url地址）”。
画面6：在`FaceLoginService`中，`getQRCode()`方法中调用`qrCodeUtil.createQRCode(content)`生成二维码文件。
画面7：在`FaceLoginService`中，`getQRCode()`方法中调用`redisTemplate.boundValueOps(getCacheKey(code)).set(result, 10, TimeUnit.MINUTES);`设置二维码状态。
画面8：在`FaceLoginService`中，`getCacheKey()`方法的注释“//构造缓存key”。
画面9：在`FaceLoginService`中，`getCacheKey()`方法的实现`return "qrcode_" + code;`。
画面10：在`FaceLoginService`中，`getCacheKey()`方法的实现`return "qrcode_" + code;`。
画面11：在`FaceLoginService`中，`getCacheKey()`方法的实现`return "qrcode_" + code;`。
画面12：在`FaceLoginService`中，`getCacheKey()`方法的实现`return "qrcode_" + code;`。
画面13：在`FaceLoginService`中，`getCacheKey()`方法的实现`return "qrcode_" + code;`。
画面14：在`FaceLoginService`中，`getCacheKey()`方法的实现`return "qrcode_" + code;`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面2：
```java
package com.ihrm.system.Controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/sys/facelogin")
public class FaceLoginController {
    @Autowired
    private FaceLoginService faceLoginService;
    @RequestMapping(value = "/qrcode", method = RequestMethod.GET)
    public Result getQRCode() throws Exception {
        return null;
    }
    @RequestMapping(value = "/qrcode/{code}", method = RequestMethod.GET)
    public Result loginByFace(@PathVariable String code, MultipartFile attachment) throws Exception {
        return null;
    }
}
```

画面3：
```java
package com.ihrm.system.Controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/sys/facelogin")
public class FaceLoginController {
    @Autowired
    private FaceLoginService faceLoginService;
    @RequestMapping(value = "/qrcode", method = RequestMethod.GET)
    public Result getQRCode() throws Exception {
        return null;
    }
    @RequestMapping(value = "/qrcode/{code}", method = RequestMethod.GET)
    public Result loginByFace(@PathVariable String code, MultipartFile attachment) throws Exception {
        return null;
    }
}
```

画面4：
```java
@Service
public class FaceLoginService {
    @Value("${qr.url}")
    private String url;
    @Autowired
    private IdWorker idWorker;
    @Autowired
    private QrCodeUtil qrCodeUtil;
    @Autowired
    private RedisTemplate redisTemplate;
}
```

画面5：
```java
@Service
public class FaceLoginService {
    @Value("${qr.url}")
    private String url;
    @Autowired
    private IdWorker idWorker;
    @Autowired
    private QrCodeUtil qrCodeUtil;
    @Autowired
    private RedisTemplate redisTemplate;
    public QrCode getQRCode() throws Exception {
        String code = idWorker.nextId() + "";
        String content = url + "?code=" + code;
        String file = qrCodeUtil.createQRCode(content);
        return null;
    }
}
```

画面6：
```java
@Service
public class FaceLoginService {
    @Value("${qr.url}")
    private String url;
    @Autowired
    private IdWorker idWorker;
    @Autowired
    private QrCodeUtil qrCodeUtil;
    @Autowired
    private RedisTemplate redisTemplate;
    public QrCode getQRCode() throws Exception {
        String code = idWorker.nextId() + "";
        String content = url + "?code=" + code;
        String file = qrCodeUtil.createQRCode(content);
        return null;
    }
}
```

画面7：
```java
@Service
public class FaceLoginService {
    @Value("${qr.url}")
    private String url;
    @Autowired
    private IdWorker idWorker;
    @Autowired
    private QrCodeUtil qrCodeUtil;
    @Autowired
    private RedisTemplate redisTemplate;
    public QrCode getQRCode() throws Exception {
        String code = idWorker.nextId() + "";
        String content = url + "?code=" + code;
        String file = qrCodeUtil.createQRCode(content);
        redisTemplate.boundValueOps(getCacheKey(code)).set(result, 10, TimeUnit.MINUTES);
        return null;
    }
}
```

画面8：
```java
@Service
public class FaceLoginService {
    @Value("${qr.url}")
    private String url;
    @Autowired
    private IdWorker idWorker;
    @Autowired
    private QrCodeUtil qrCodeUtil;
    @Autowired
    private RedisTemplate redisTemplate;
    public QrCode getQRCode() throws Exception {
        String code = idWorker.nextId() + "";
        String content = url + "?code=" + code;
        String file = qrCodeUtil.createQRCode(content);
        return null;
    }
}
```

画面9：
```java
@Service
public class FaceLoginService {
    @Value("${qr.url}")
    private String url;
    @Autowired
    private IdWorker idWorker;
    @Autowired
    private QrCodeUtil qrCodeUtil;
    @Autowired
    private RedisTemplate redisTemplate;
    public QrCode getQRCode() throws Exception {
        String code = idWorker.nextId() + "";
        String content = url + "?code=" + code;
        String file = qrCodeUtil.createQRCode(content);
        return null;
    }
}
```

画面10：
```java
@Service
public class FaceLoginService {
    @Value("${qr.url}")
    private String url;
    @Autowired
    private IdWorker idWorker;
    @Autowired
    private QrCodeUtil qrCodeUtil;
    @Autowired
    private RedisTemplate redisTemplate;
    public QrCode getQRCode() throws Exception {
        String code = idWorker.nextId() + "";
        String content = url + "?code=" + code;
        String file = qrCodeUtil.createQRCode(content);
        return null;
    }
}
```

画面11：
```java
@Service
public class FaceLoginService {
    @Value("${qr.url}")
    private String url;
    @Autowired
    private IdWorker idWorker;
    @Autowired
    private QrCodeUtil qrCodeUtil;
    @Autowired
    private RedisTemplate redisTemplate;
    public QrCode getQRCode() throws Exception {
        String code = idWorker.nextId() + "";
        String content = url + "?code=" + code;
        String file = qrCodeUtil.createQRCode(content);
        return null;
    }
}
```

画面12：
```java
@Service
public class FaceLoginService {
    @Value("${qr.url}")
    private String url;
    @Autowired
    private IdWorker idWorker;
    @Autowired
    private QrCodeUtil qrCodeUtil;
    @Autowired
    private RedisTemplate redisTemplate;
    public QrCode getQRCode() throws Exception {
        String code = idWorker.nextId() + "";
        String content = url + "?code=" + code;
        String file = qrCodeUtil.createQRCode(content);
        return null;
    }
}
```

画面13：
```java
@Service
public class FaceLoginService {
    @Value("${qr.url}")
    private String url;
    @Autowired
    private IdWorker idWorker;
    @Autowired
    private QrCodeUtil qrCodeUtil;
    @Autowired
    private RedisTemplate redisTemplate;
    public QrCode getQRCode() throws Exception {
        String code = idWorker.nextId() + "";
        String content = url + "?code=" + code;
        String file = qrCodeUtil.createQRCode(content);
        return null;
    }
}
```

画面14：
```java
@Service
public class FaceLoginService {
    @Value("${qr.url}")
    private String url;
    @Autowired

