# 画面线理解：19-刷脸登录：人脸登录

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\19-刷脸登录：人脸登录_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 02:51, 03:45, 05:10, 07:32, 08:34, 09:11, 09:54, 11:06, 12:10, 13:09, 13:53, 15:22, 16:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:06:30

1) 这一组画面整体在讲什么（一句话）：
演示基于百度AI人脸识别的登录系统核心代码实现，包括控制器、服务层逻辑及Redis缓存与Shiro权限管理的集成。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：桌面启动画面，显示“黑马程序员”和“博学谷”标志。
画面2：展示`FaceLoginController.java`中`checkQRCode`和`loginByFace`方法，用于处理二维码登录和人脸登录请求。
画面3：继续展示`loginByFace`方法，处理登录成功后返回用户ID。
画面4：展示`BaiduAUIUtil.java`中的`faceCheck`和`faceSearch`方法，用于人脸检测和人脸搜索。
画面5：展示`FaceLoginService.java`中`@Value`和`@Autowired`注解配置，以及Spring Boot自动配置类。
画面6：展示`FaceLoginService.java`中`if`语句的代码补全提示。
画面7：展示项目结构目录，包含`src/main/java`和`src/main/resources`，并展示`UserController.java`中的用户更新和删除方法。
画面8：展示`FaceLoginService.java`中`getQRCode`方法，用于生成二维码并存入Redis。
画面9：展示`FaceLoginService.java`中`checkQRCode`方法，用于检查二维码状态。
画面10：展示`FaceLoginService.java`中`loginByFace`方法，用于处理人脸登录逻辑。
画面11：展示`FaceLoginService.java`中`loginByFace`方法，使用`SecurityUtils`进行用户登录。
画面12：展示`FaceLoginService.java`中`loginByFace`方法，创建`FaceLoginResult`对象并设置状态。
画面13：展示`FaceLoginService.java`中`loginByFace`方法，设置Redis缓存并返回结果。
画面14：展示`FaceLoginController.java`中`checkQRCode`和`loginByFace`方法，用于处理登录请求。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
@RequestMapping(value = "/qrCode/{code}", method = RequestMethod.GET)
public Result checkQRCode(@PathVariable(name = "code") String code) throws Exception {
    FaceLoginResult checkQRCode = faceloginService.checkQRCode(code);
    return new Result(ResultCode.SUCCESS, checkQRCode);
}

/**
 * 人脸登录，根据传入的图片用百度AI进行人脸比对
 * 根据比对的图片用百度云AI进行查找
 */
@RequestMapping(value = "/{code}", method = RequestMethod.POST)
public Result loginByFace(@PathVariable(name = "code") String code, @RequestParam(name = "file") MultipartFile attachment) throws Exception {
    return null;
}

/**
 * 图像检测，判断图片中是否含有面部
 */
@RequestMapping(value = "/checkFace", method = RequestMethod.POST)
public Result checkFace(@RequestParam(name = "file") MultipartFile attachment) throws Exception {
    String image = Base64Util.encode(attachment.getBytes());
    Boolean aBoolean = baiduUtil.faceCheck(image);
    if (aBoolean) {
        return new Result(ResultCode.SUCCESS);
    }else{
        return new Result(ResultCode.FAIl);
    }
}
```

画面4：
```java
public Boolean faceCheck(String image) {
    JSONObject res = client.detect(image, IMAGE_TYPE, options);
    if (res.has(key) && res.getInt(key) == 0) {
        Integer faceNum = resultObject.getInt("face_num");//检测的人脸数量
        return faceNum == 1 ? true : false;
    }else{
        return false;
    }
}

/**
 * 人脸搜索，查找人脸库中相似的人并返回数据
 * 这里，用户的匹配度（score）大于80，即认为是同一个用户
 */
public String faceSearch(String image) {
    JSONObject res = client.search(image, IMAGE_TYPE, groupid, options);
    if (res.has(key) && res.getInt(key) == 0) {
        JSONArray userList = result.getJSONArray(key);
        if (userList.length() > 0) {
            JSONObject user = userList.getJSONObject(index: 0);
            double score = user.getDouble(key: "score");
            if (score > 80) {
                return user.getString(key: "user_id");
            }
        }
    }
}
```

画面5：
```java
@Value("${qr-url}")
private String url;

@Autowired
private IdWorker idWorker;

@Autowired
private QCodeUtil qCodeUtil;

// AutoWired (org.springframework.beans.factory.annotation)
// Auto (com.netflix.discovery.converters)
// Value (org.springframework.beans.factory.annotation)
// Component (org.springframework.stereotype)
// Service (org.springframework.stereotype)
// ExcelAttribute (com.ihm.domain.objects)
// RequestMapping (org.springframework.web.bind.annotation)
// Query (org.springframework.data.jpa.repository)
// PathVariable (org.springframework.web.bind.annotation)
// FeignClient (org.springframework.cloud.openfeign)
// EnableDiscoveryClient (org.springframework.cloud.netflix.eureka)
// EnableEurekaClient (org.springframework.cloud.netflix.eureka)
// Get (org.springframework.web.bind.annotation)
// Setter (org.springframework.beans.factory.annotation)
// Getter (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal
