# 画面线理解：18-刷脸登录：人脸检测

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\18-刷脸登录：人脸检测_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:10, 01:22, 01:32, 01:57, 02:55, 03:14, 03:29, 03:49, 04:14, 04:27, 04:55, 05:12, 05:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:05:34

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中通过控制器调用人脸识别服务完成登录功能，包括获取二维码、校验二维码、上传人脸图片并进行比对。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 `FaceLoginController` 类中 `@RequestMapping(value = "/qrcode", method = RequestMethod.GET)` 方法，用于获取二维码。
画面 2: 展示 `FaceLoginController` 类中 `@RequestMapping(value = "/qrcode/{code}", method = RequestMethod.GET)` 方法，用于校验二维码。
画面 3: 展示 `FaceLoginController` 类中 `@RequestMapping(value = "/qrcode/{code}", method = RequestMethod.GET)` 方法，用于校验二维码。
画面 4: 展示 `FaceLoginController` 类中 `@RequestMapping(value = "/{code}", method = RequestMethod.POST)` 方法，用于登录。
画面 5: 展示 `FaceLoginService` 类中 `faceCheck` 和 `faceSearch` 方法，用于人脸检测和人脸搜索。
画面 6: 展示 `FaceLoginController` 类中 `@RequestMapping(value = "/checkFace", method = RequestMethod.POST)` 方法，用于上传人脸图片并进行比对。
画面 7: 展示在 `FaceLoginController` 中，`@RequestParam(name = "file") MultipartFile attachment` 的类型提示。
画面 8: 展示 `FaceLoginController` 中 `@RequestMapping(value = "/checkFace", method = RequestMethod.POST)` 方法，用于上传人脸图片并进行比对。
画面 9: 展示 `FaceLoginController` 中 `@RequestMapping(value = "/checkFace", method = RequestMethod.POST)` 方法，用于上传人脸图片并进行比对。
画面 10: 展示多个窗口，包括 IDEA、Postman、文件资源管理器和终端，说明项目结构和测试环境。
画面 11: 展示 Postman 中用于测试 `/checkFace` 接口的请求配置，选择 `form-data` 格式。
画面 12: 展示文件资源管理器中 `day11` 目录下的 `001.png` 文件，该文件为测试用的人脸图片。
画面 13: 展示文件资源管理器中 `day11` 目录下的 `001.png` 文件，该文件为测试用的人脸图片。
画面 14: 展示 Postman 中用于测试 `/checkFace` 接口的请求配置，选择 `form-data` 格式，并上传 `001.png` 文件，返回结果为 `{"success": false, "code": 10004, "message": "操作失败", "data": null}`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public class FaceLoginController {
    @Autowired
    private FaceLoginService faceLoginService;

    /**
     * 获取扫码登录二维码
     * 返回值：QRCode对象（code, image）
     */
    @RequestMapping(value = "/qrcode", method = RequestMethod.GET)
    public Result qrcode() throws Exception {
        QRCode qrcode = faceLoginService.getQrcode();
        return new Result(ResultCode.SUCCESS, qrcode);
    }

    /**
     * 校验二维码，登录页面轮询调用此方法，根据唯一标识code判断用户登录情况
     * 返回值：FaceLoginResult
     * state: -1, 0, 1 (userId/token)
     */
    @RequestMapping(value = "/qrcode/{code}", method = RequestMethod.GET)
    public Result qrcodeCheck(@PathVariable String code) throws Exception {
        FaceLoginResult checkQrcode = faceLoginService.checkQrcode(code);
        return new Result(ResultCode.SUCCESS, checkQrcode);
    }
```

画面 4:
```java
    /**
     * 人脸登录：根据提交的图片调用百度AI进行人脸检测
     * 根据检测结果判断是否是有效人脸
     */
    @RequestMapping(value = "/{code}", method = RequestMethod.POST)
    public Result loginByFace(@PathVariable String code, @RequestParam(name = "file") MultipartFile attachment) {
        return null;
    }
```

画面 5:
```java
    /**
     * 人脸检测：判断上传图片中是否有人脸分镜
     */
    public Boolean faceCheck(String image) {
        JSONObject res = client.detect(image, IMAGE_TYPE, options);
        if (res.has(key: "error_code") && res.getInt(key: "error_code") == 0) {
            Integer faceNum = res.getJSONObject(key: "result").getInt(key: "face_num"); // 检测到的人脸数量
            return faceNum > 0 ? true : false;
        } else {
            return false;
        }
    }

    /**
     * 人脸登录：直接在人脸库中寻找相似的人脸并返回
     * 即可判断是否是同一个用户
     */
    public String faceSearch(String image) {
        JSONObject res = client.search(image, IMAGE_TYPE, groupId, options);
        if (res.has(key: "error_code") && res.getInt(key: "error_code") == 0) {
            JSONObject result = res.getJSONObject(key: "result");
            return result.getString(key: "face_token");
        } else {
            return null;
        }
    }
```

画面 6:
```java
    /**
     * 人脸登录：根据提交的图片调用百度AI进行人脸检测
     * 根据检测结果判断是否是有效人脸
     */
    @RequestMapping(value = "/{code}", method = RequestMethod.POST)
    public Result loginByFace(@PathVariable String code, @RequestParam(name = "file") MultipartFile attachment) {
        return null;
    }
```

画面 8:
```java
    /**
     * 人脸登录：根据提交的图片调用百度AI进行人脸检测
     * 根据检测结果判断是否是有效人脸
     */
    @RequestMapping(value = "/{code}", method = RequestMethod.POST)
    public Result loginByFace(@PathVariable String code, @RequestParam(name = "file") MultipartFile attachment) {
        return null;
    }
```

画面 9:
```java
    /**
     * 人脸登录：根据提交的图片调用百度AI进行人脸检测
     * 根据检测结果判断是否是有效人脸
     */
    @RequestMapping(value = "/{code}", method = RequestMethod.POST)
    public Result loginByFace(@PathVariable String code, @RequestParam(name = "file") MultipartFile attachment) {
        return null;
    }
```

画面 14:
```json
{
    "success": false,
    "code": 10004,
    "message": "操作失败",
    "data": null
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
