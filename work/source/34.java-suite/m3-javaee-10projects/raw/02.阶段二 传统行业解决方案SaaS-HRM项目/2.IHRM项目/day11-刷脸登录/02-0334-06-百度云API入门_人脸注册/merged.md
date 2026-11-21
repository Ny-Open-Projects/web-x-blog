# 06-百度云API入门：人脸注册

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\06-百度云API入门：人脸注册_【海量资源尽在 666java.com】.mp4
- 时长 14分20秒（音频 860s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们的开发环境搭建好了之后接下来呢去完成第一个功能ETA testpublic view id我们叫做test face resetjim jimstr reset其实就是我们的人脸注册的一个功能人脸注册ok那对于这个人脸注册我们的代码应该如何去写呢其实一共有
[00:36] 这么几步需要各位要遵循首先第一件事呢我们要创建我们Java代码和百度云交互的Client对象这个对象呢是百度云他提供的这个jar 包为我们提供好的我们直接用就能和百度云交互那这个对象创建好了之后接下来第二件事那接下来就是说呢对于我们真正要进行人脸注册
[01:09] 那要想进行人脸注册有一些参数我们需要进行一个设置就是一些参数的一些设置好了这个参数设置好了之后接下来第三件事我们就需要构造一张图片那这张图片呢可以是我们本地的一张图片也可以是一个文件的流的等等的这么一种形式都可以那所以一张图片要给他准备好别忘了我们其实就是一个人的一个头像照片嘛
[01:37] OK那这些我们都准备好了之后接着才是我们的第四步第四步就是真真正正的调用我们的API方法来完成人脸注册一共有这么几个步骤首先第一件事创建Java代码和百度云交互的Client对象那这个对象叫什么它叫做AIP Face这个是百度云专门提供的这么一个对象
[02:07] 通过这个对象可以完成人脸注册人脸识别人脸查询等等所有的功能我们直接调用这个方法就可以了好了这个叫做client好了等于等于new一个AIP client那接下来就是说呢对于这个AIP client而言它的构造方法我们需要点进去来看一下是因为呢对于我们要想进行人脸注册或者人脸比较等等等等这些功能
[02:37] 你需要去指定究竟你的应用是哪一个你的key是什么你的密钥又是什么那各位来看有API ID有API Key有Squid Key那这些内容如果各位还有印象的话是不是就是我们刚才注册一个应用给我们提供的这些内容啊所以对于我们而言对于我们而言你要想去创建这个对象的话需要去填写上你的API ID
[03:06] App ID需要填写上你的API Key那接着还需要填写上这个密钥点击打开就能获取到OK那这样一来我们第一个对象就已经创建好了看了对象我们创建好了接下来呢就是说我要想进行人脸注册的话还有一些参数我们可以进行设置那这些参数呢是以Map集合的形式来进行提供了所以我这边呢创建一个Map集合
[03:38] 好了它的参数全部都是死菌死菌类型的一个map好了我起一个名字就叫做option吧onsoptions等于new一个hashimap好了那这些参数有什么注意这些参数呢在今天讲义当中最下方也跟各位有一个简单的说明那这些参数里面有比如说呢quality control比如说呢还有lemnese control这些是什么注意这两个其实代表的是第一个
[04:09] 图片的一个质量那因为你上传一个图片呢可以是一个质量要求比较高的那清晰度比较高那也可能还有一个就是有一个活体检测的这么一个功能就是活体检测要不要控制起来那你想控制要以多严格的形式进行控制就这么一个概念第一个呢我们也把它Ctrl C Copy过来Options.put好了那这个代表的是我们的图片质量那图片质量可选的范围呢一共有
[04:41] 这么几个第一个是None不控制第二个呢靠过来Low就是一个低级别的控制还有一个Normal普通级别的当然了我再回到讲义Hi一共有这么几个一共有这么几个当然了你可以任意选择我们就来一个Normal普通级别的其实就可以了好了除了这个之外还可以去选择活体检测活体
[05:14] 检测那这个活体检测呢简单的再来说一下其实这个是为了防止有一些人就是说我最终不是要拍摄你用照片进行一个登录吗其实就是判断一下你当前这个照片它究竟是一张图片还是一个真正的是一个人拍摄出来的这么一个概念那对于这个活体检测来说呢这边也有自己的选择Lemnitz Control好了它的选择范围呢也是NoneLowNormalHigh
[05:43] 好了这边也说了如果是一个low的话就是一个较低级别的活体要求好了如果是normal就是一般要求high就是较高的那对于我们而言对于我们而言随便填我就来一low了最低级别的其实就可以了因为我们是为了做测试好了这样一来我基本的参数设置其实就已经设置好了那参数设置好了之后接着来我们着重关注的是一个叫做构造图片
[06:11] 那构造这个图片我在今天的这个资料当中各位来看在今天资源当中呢这边有一个照片我自己拍摄了一张照片叫001我准备把这个照片传到百度云的人像人脸库当中那对于这个来说呢这个路径我们把它copy一下001.png好了回来street pass等于路径call过来001.png
[06:43] 这一张图那接下来我想跟各位来聊的就是说呢对于百度云AI来说你上传的这个图片它有两种格式那这两种格式呢第一个是一个URL地址就是一张真正的地址的这么一张图片那这个地址呢咱们之前用过一些其他的存储存储完了之后是不是可以通过一个URL地址进行访问那所以这个图片呢可以是URL地址的形式那除了URL地址形式之外还可以是base
[07:16] 64字符串形式那这个字符串形式之前也跟各位做过一个了解那别看是一个字符串它其实也能代表一张图片其实就是通过把图片流的二进制文件以base64进行加密的这么一种处理来做的所以它支持这么两种形式两种形式那我这个pass这玩意儿这地址你想都不要想它不是UL所以咱们只能是不是用base64的形式来给它体现
[07:47] 那所以对于我而言我接下来要处理的就是说把这个图片路径的这个图片以base64的形式给它进行触笔那这个如何去做其实也不难也比较简单好了一起来看一下首先呢我们要得到二进制的这个流二进制数据好了注意我们可以借助一个叫做fills的这么一个工具类来进行读取好了它可以有一方法叫做read all
[08:19] BytesRead all bytes好了里面接收的是一个路径的这么一个对象PassPassPass打点Get pass好了把我这个路径传进来OK好了这边呢有一个小小的问题啊这个passPass印象包OK那这样一来呢它其实就根据我们的一个路径直接获取到了它的by的数组
[08:54] OK这边有一个异常我也处理一下好了接下来就是说我们有了byte速度我最终的目的其实就是要对byte速度进行base64处理这个如何去做也不难base64有条注意百度它的工具当中已经帮我提供好了这么一个工具类打点Encode接着把byte传递过来这样一来我们就能得到
[09:21] 一个字符串当然这个字符串其实也是一张图片的一种形式好了那接下来要做的就是最后一件事了调进我们这个API Client这个Client完成我们人脸注册的这个功能好了通过Client打点里面有个方法打点有个方法叫做addUser那addUser呢这个方法里面呢有很多个参数第一个叫做image那这个image其实代表的是我们的图片好了第一个参数参数一
[09:58] 它其实代表的是图片的UIL或者图片的base64字符串OK那接着来有参数二那这个参数二代表的什么含义我写到上边吧这个注释可能比较长参数一参数二那对于参数二呢各位这个参数二代表的是一个叫做image type指的是我们的图像的图片的形式那这个图片形式呢对于我们而言可以传递两种
[10:34] 一种呢叫做URL我们选择就是URL另一种呢叫做base64注意base64大写的字母OK那这两个我们看过了之后接着还有第三个第三个叫group ID第四个叫做user ID这个需要跟各位说明一下参数三那参数三呢是组ID那对于这个组ID对我们来说一般没什么用我们可以给它固定一个字符串即可你就可以给它固定一个字符串
[11:12] 当然这个固定的字符串一旦固定我们不管是今天的人脸注册还是一会人脸对比我们这个组ID就是固定了好了接着还有参数4那这个参数4参数4代表的是用户的ID那这个用户ID注意是我们系统里的用户ID你可以给他指定你什么意思就是说你上传一张图片这个图片可能是我们系统当中的某一个用户你就把这个用户的ID给他附上值其实就可以了
[11:44] OK那我们一会进行人脸查找的时候人脸查找的时候你上传一张头像他去里面找找找最终给你告诉你好了他是属于某一个人这个人的user id在你的系统里叫1234就这个意思OK那user id我们看过了接着第五个参数就是我们的配置就是我们的hashi map中的基本参数配置
[12:14] OK那这些我们都做过简单的说明那接下来我们要做的事情就把这方法给它补充完整就可以了图片的URL或者图片的base64字符创Encode拿过来好了那接着图片的形式base64我们是经过base64处理的好了接着第三个组ID这个我们说过了固定字符创我叫做ITcast好了接着第四个参数用户ID我也随便填100比如说这个用户ID就叫100那第五个就是我们的options
[12:44] OK那这样一来我们可以发送请求接着得到我们的响应我叫做res那好了有了res我们可以做一个打印输出看一下究竟是否已经把一张图片注册到人脸库当中res打点toOK那这样一来我这个人脸注册的代码就已经写好了好了那接下来呢我们开始执行一把看一下效果来走
[13:17] 好了这边程序在执行好了各位来看就目前来说已经执行成功那执行成功了之后底下有很多它响应的一些参数那我需要关注的点就是说这个error message和这个error code那在这边如果error code等于0代表操作成功那我们已经真真正正的向我百度云的这个应用当中注册了一个人脸好了我们一起找到
[13:48] 百度云在这边找到我们之前的应用列表好了我们右边看到了有一个查看人脸库我刚才已经往这个SaaS-HRM当中注册了一张人脸点击来来各位来看用户组IDcast好了那各位这边用户ID刚才取了一个名字叫一千还有印象吗那接着我们打开看一下我这张照片OK那这样一来其实我就已经把一张照片注册到他的人脸库当中了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Java 代码调用百度人脸识别 API 完成人脸注册功能。

2) 按时间顺序列出每张画面的要点：
画面1：在 IntelliJ IDEA 中，展示 `FaceTest.java` 文件，光标位于 `@PostConstruct` 注解下方，项目结构中显示了 `face-demo` 项目及其依赖的 Maven 仓库，包括 `junit`、`log4j`、`hamcrest` 和 `baidu` 的 SDK。
画面2：在 `FaceTest.java` 中，编写 `@Test` 注解的方法 `testFaceRegister()`，准备调用百度人脸识别 API，但尚未导入相关包。
画面3：在 IDEA 中打开百度人脸识别 SDK 的反编译类文件 `ApFace.class`，查看 `detect` 方法的实现，同时弹出百度云控制台页面。
画面4：在 `FaceTest.java` 中，导入 `java.util` 包，准备使用 `HashMap`，并设置注释说明。
画面5：在 PPT 页面中，展示多个窗口，包括 IDEA、百度云控制台等，标题为“人脸注册 返回数据参数详情”。
画面6：在 `FaceTest.java` 中，初始化 `ApFace` 客户端，设置 `appId`、`apiKey` 和 `secretKey`。
画面7：在 PPT 页面中，展示百度人脸识别 API 的返回参数表，包括 `group_id`、`user_id`、`user_info`、`quality_control`、`liveness_control` 等字段。
画面8：在 `FaceTest.java` 中，导入 `Base64` 工具类，准备对图片进行 Base64 编码。
画面9：在 `FaceTest.java` 中，设置图片路径，使用 `Files.readAllBytes` 读取图片文件。
画面10：在 IDEA 中打开百度人脸识别 SDK 的反编译类文件 `ApFace.class`，查看 `addUser` 方法的实现。
画面11：在 `FaceTest.java` 中，使用 `Base64Util.encode` 对图片进行 Base64 编码。
画面12：在 `FaceTest.java` 中，调用 `client.addUser()` 方法完成人脸注册，并打印返回的 `JSONObject`。
画面13：在百度云控制台中，展示“应用列表”，包含两个应用：“sass-hrm”和“itcast”。
画面14：在百度云控制台中，展示“人脸注册”页面，显示已注册的人脸图片。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
package cn.itcast.test;
public class FaceTest {
    @PostConstruct
    @Test
    @Before
    @After
    @Getter
    @Setter
    @Target
    @Retention
    @FunctionalInterface
    @Override
    @SafeVarargs
    @SuppressWarnings
}
```
画面2：
```java
import com.baidu.aip.face.AipFace;
import org.junit.Test;
public class FaceTest {
    @Test
    public void testFaceRegister() {
        //人脸注册
        AipFace client = null;
    }
}
```
画面3：
```java
package com.baidu.aip.face;
public class AipFace extends BaseClient {
    public AipFace(String appId, String apikey, String secretKey) {
        super(appId, apikey, secretKey);
    }
    public JSONObject detect(String image, String imagetype, HashMap<String, String> options) {
        AipRequest request = new AipRequest();
        this.preparation(request);
        request.addBody("image", image);
        request.addBody("image_type", imageType);
        if (options != null) {
            request.addBody(options);
        }
        request.setUri("https://aip.baidubce.com/rest/2.0/face/v3/detect");
        request.setBodyFormat(BodyFormat.RAW_JSON);
        this.postOperation(request);
        return this.requestServer(request);
    }
}
```
画面4：
```java
import java.util.*;
public class FaceTest {
    //人脸注册
    @Test
    public void testFaceRegister() {
        //1.创建java代码和百度云交互的client对象
        AipFace client = null;
        //2.参数设置
        //3.构造图片
        //4.调用api方法完成人脸注册
    }
}
```
画面6：
```java
import com.baidu.aip.face.AipFace;
import org.junit.Test;
import java.util.HashMap;
public class FaceTest {
    //人脸注册
    @Test
    public void testFaceRegister() {
        //1.创建java代码和百度云交互的client对象
        AipFace client = new AipFace("15246423", "QFVuW01b5mHfA819Xt6lGjji", "mvgF3pPoOLsMadGiemuztBayE3jfIDv");
        //2.参数设置
        HashMap<String, String> options = new HashMap<>();
        //3.构造图片
        //4.调用api方法完成人脸注册
    }
}
```
画面7：
```markdown
| group_id | 是 | String | 用户组id（由数字、字母、下划线组成），长度限制128B |
| user_id | 是 | String | 用户id（由数字、字母、下划线组成），长度限制128B |
| user_info | 否 | String | 用户资料，长度限制256B |
| quality_control | 否 | String | NONE:不进行控制 LOW:较低的质量要求（高通过率 低攻击拒绝率）NORMAL:一般的质量要求（高攻击拒绝率 低通过率）HIGH:较高的质量要求（高攻击拒绝率 低通过率）默认NONE |
| liveness_control | 否 | String | NONE:不进行控制 LOW:较低的活体要求（高通过率 低攻击拒绝率）NORMAL:一般活体要求（高攻击拒绝率 低通过率）HIGH:较高的活体要求（高攻击拒绝率 低通过率）默认NONE |
```
画面8：
```java
import java.util.*;
import org.apache.commons.codec.binary.Base64;
public class FaceTest {
    //人脸注册
    @Test
    public void testFaceRegister() {
        //1.创建java代码和百度云交互的client对象
        AipFace client = new AipFace("15246423", "QFVuW01b5mHfA819Xt6lGjji", "mvgF3pPoOLsMadGiemuztBayE3jfIDv");
        //2.参数设置
        HashMap<String, String> options = new HashMap<>();
        //3.构造图片
        //4.调用api方法完成人脸注册
    }
}
```
画面9：
```java
import com.baidu.aip.face.AipFace;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
public class FaceTest {
    //人脸注册
    @Test
    public void testFaceRegister() {
        //1.创建java代码和百度云交互的client对象
        AipFace client = new AipFace("15246423", "QFVuW01b5mHfA819Xt6lGjji", "mvgF3pPoOLsMadGiemuztBayE3jfIDv");
        //2.参数设置
        HashMap<String, String> options = new HashMap<>();
        //3.构造图片
        String path = "C:\\Users\\ThinkPad\\Desktop\\day11\\资源\\图片\\1.jpg";
        //上传图片，两种模式：url地址、Base64字节流格式
        byte[] bytes = Files.readAllBytes(Path.get(path));
        //4.调用api方法完成人脸注册
    }
}
```
画面11：
```java
import com.baidu.aip.face.AipFace;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
public class FaceTest {
    //人脸注册
    @Test
    public void testFaceRegister() {
        //1.创建java代码和百度云交互的client对象
        AipFace client = new AipFace("15246423", "QFVuW01b5mHfA819Xt6lGjji", "mvgF3pPoOLsMadGiemuztBayE3jfIDv");
        //2.参数设置
        HashMap<String, String> options = new HashMap<>();
        //3.构造图片
        String path = "C:\\Users\\ThinkPad\\Desktop\\day11\\资源\\图片\\1.jpg";
        //上传图片，两种模式：url地址、Base64字节流格式
        byte[] bytes = Files.readAllBytes(Path.get(path));
        //4.调用api方法完成人脸注册
    }
}
```
画面12：
```java
import com.baidu.aip.face.AipFace;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
public class FaceTest {
    //人脸注册
    @Test
    public void testFaceRegister() {
        //1.创建

