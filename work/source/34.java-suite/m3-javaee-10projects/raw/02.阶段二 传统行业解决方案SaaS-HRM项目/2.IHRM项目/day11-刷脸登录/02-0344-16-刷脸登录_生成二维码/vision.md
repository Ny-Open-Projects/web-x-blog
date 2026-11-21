# 画面线理解：16-刷脸登录：生成二维码

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\16-刷脸登录：生成二维码_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:39, 01:16, 02:22, 03:31, 04:34, 05:12, 05:50, 06:17, 07:04, 07:37, 08:49, 09:41, 10:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:04:05

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
package com.ihrm.system.controller;
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
package com.ihrm.system.controller;
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
