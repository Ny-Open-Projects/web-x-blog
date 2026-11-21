# 18-刷脸登录：人脸检测

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\18-刷脸登录：人脸检测_【海量资源尽在 ubkz.com】.mp4
- 时长 5分42秒（音频 343s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那各位现在呢已经看到了就目前而言我们完成了二维码生成完成了我们这个二维码它的一个状态的一个查询那接下来呢咱们继续往下去做那接下来我们就去完成一个叫做图像检测那这个图像检测呢其实很简单了咱们之前说过了就是你可以上传一张图片当然了这张图片是通过我们的摄像头拍摄出来的一张图片
[00:28] 那前端不管怎么去调用摄像头不管怎么去调用你的那些外部的一些设备那在我们的后端那得到的其实就是一个文件所以在我们的后端这边得到的是你拍摄好的一张图片当然了你调用摄像头拍摄过来那我们去判断一下这张图片当中是否包含人的面部信息那所以在这边我接受一个参数是一个文件好了这个也能理解那接下来呢就是说我这里面的代码应该如何去写
[00:58] 其实这个代码写起来也不难我们全部的这些业务逻辑全部的调用关系全部是在Service当中所以我需要在Face Logging Service打点咱们也去添加一个方法我们一起找到它好了这个方法就叫做抱歉这个不能调用Face Service了我们这回之前封装了一个工具类好了这个工具类Private我们叫做百度AI Utils
[01:30] 那这个百度AI Utils里面呢我们写过一个方法其实就是用来对一张图片进行判断的那这些基本的这些方法呢我们之前都玩过就叫做FaceCheck那FaceCheck点进去来看一下需要接收一个我们叫做Data URL的数据那接收Data URL数据调用API调用百度的给我们开放的一些API那接着是不是给我返回一些内容
[01:57] 那这个返回内容之前课程做过这个API的一个说明是这样的就是你的如果返回code等于0返回code等于0并且你上传的图片人的头像信息只有一个那就是错剩下就是false这个比较简单所以对于我们前端进行判断的时候前端进行判断的时候我们只需要把这个文件给它构造成我们Data URL数据的形式其实就可以了那这个如何去做也不难
[02:27] base我们之前玩过base64utils打点encode好了那接下来在我们这个multipadfile我们的文件对象当中恰巧有所有的我们叫做bat数组直接打点getbats得到bat数组那这样一来我们就能得到了我的一个图片信息好了把这个图片信息传递到工具类当中OK那这样一来得到我们的一个判断的一个方法
[02:57] OK那好了接下来呢我们底下直接就是根据这个返回值不令返回值我们做判断如果说它是处那就代表具有面部信息如果是false就没有呗所以呢我直接return当然了我这个return写一个if判断吧if如果为真else那如果为真的话我在上边直接returnnew一个我们叫做result好了里面resultcode.succes代表成功
[03:32] 好了如果为false我们直接这边呢还写过一个fail代表操作失败就可以了OK那这样一来我图像检测的这个代码也写好了那写好了之后呢同样的我们可以刷重新启动一下系统vf我们一起来验证一下这个check face接口OK
[03:55] 这边呢让他去重启我去打开post们我们再来一个新的标签页来进行判断好了前面这边部分呢我就直接call过来了Ctrl C这边拿过来Ctrl V那我们关注的是我刚才写好的这个接口请求名称这个face那上面有附录镜不再多说了那我们的请求方式postok拿过来post请求那接下来我要往里上传一个文件这个文件的名称叫做feelokCtrl C回来post们回来
[04:26] 好了这边呢可以添加一个我们的题内容那注意我们这边选的是formal dataok key代表的是我的上传的文件的名称好了这个文件的名称跟我们这个方法的名称里面的name要保持一致ok那接下来我们这回呢上传的是一个文件所以fail好了接着选择一个文件那我选择的文件就是在今天的第11天资料当中的这一个照片那我们之前都玩过可以打开它一起来简单的看一下
[04:54] 那其中呢我准备以001这张照片和logo这张照片举例那我们都知道logo照片里面并不含有人面的头部信息那所以我一检测必然是false代表的是失败那001是不是必然代表的是成功啊那我们一起来验证一下好了我先用logo来进行声明来进行测试logo点击send你发现操作失败
[05:20] 这个好像有一点像我们的跟我们想的差不多接下来再选择文件001那001里面里面001当中包含面部的一些信息所以必然是操作成功才对我一send给我来看操作成功这样一来我们面部检测的接口是不是也已经下落了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

