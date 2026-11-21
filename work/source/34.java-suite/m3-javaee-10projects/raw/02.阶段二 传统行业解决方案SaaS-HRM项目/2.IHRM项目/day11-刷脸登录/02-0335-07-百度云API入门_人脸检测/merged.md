# 07-百度云API入门：人脸检测

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\07-百度云API入门：人脸检测_【海量资源尽在 ubkz.com】.mp4
- 时长 6分37秒（音频 397s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那人脸注册已经搞定了其实对于人脸注册来说就是像百度的人脸库库中添加用户的一个人面人脸的照片这么一个功能那好了接下来呢我们关注的就是第二个点那第二个点是什么含义是这样的就是说有可能你在注册照片的时候有可能这个照片里面没有投相信息
[00:33] 那比如说呢在今天的资料当中给各位准备了这么一张照片呢叫logo那这个logo一打开你会发现这个哪有人的一个面部的一个图像啊没有吧那我们在进行注册的时候就需要对这个照片进行一个检测看一下有没有人的面部的一些内容如果有是不是再注册如果没有是不是让他重新的去搞一张图片出来啊所以对于我们来说接下来要做的第二个判断第二件事就是去判断
[01:02] 当前的这个图片当中是否包含人的面部信息我们叫做人脸识别或者错了叫做人脸检测抱歉人脸检测人脸检测代表的功能就是判断图片中是否具有叫做面部信息OK那这个代码如何去写呢其实也很简单也是通过AIP这个face这个client对象来做的所以呢为了我这个简化代码的开发我们可以把这边
[01:31] 以初始化的形式把这个AIP face给它抽取出来这用于单元测试可以借助ETA BEFORE进行一些基本代码的一个配置VOIDINITOK那这样一来呢我里面就可以通过CLANTCtrl C靠过来Ctrl V放到上边其实就可以了
[01:58] OK那这样一来我底下代码这些那就不用再去使劲去写了就相对来说简单一些因为这个可能对象我们出转化一次就可以了好了那接下来呢这个出转化对象我们写好了接下来我们关注的是人脸检测的一个方法VUIDTestFaceCheckOK上面补充一个ataTestOK那我这个代码应该如何去写呢首先第一件事创建交互对象我们已经搞定了那接下来关注的
[02:30] 其实就是我们的第二件事那第二件事我要干什么呢也是如此我们要把一张图片传输给百度云让他帮我进行检测那这个图片的一些格式那这个图片究竟是URL形式还是base64形式那这个图片的URL地址是什么他的字符串究竟也是什么我们也需要进行提供所以我这边一上来就需要构造一张图片
[02:57] 那构造的图片这个代码呢咱们基本上都是一模一样的Ctrl C我就拿过来Ctrl V好了这边呢有异常我也解决一下那注意我现在要检测的图片呢就是我们刚才看到的logo.gopg我把这个Ctrl C拷过来图片名称拷过来OKCtrl V好了那接下来构造图片我们搞定了接下来呢我们就可以调用API方法进行
[03:30] 图片检测人人脸检测那这个API方法呢同样的通过clant点注意这有一个方法叫做detect那这个detect方法呢里面接收的参数有如下这么几个首先第一个image这个image代表的是图片的URL或者图片的Base64组创image tab
[03:56] 这个代表的是图片的类型可以是UIL可以是base64还有后面就是我们的参数设置那注意这个参数设置我们不需要做任何操作直接写None写之写None写之就可以了好了参数一好了参数二好了参数三OK那我们可以设置None设置None代表的是使用默认配置就可以
[04:30] 当然了这些配置呢全部在哪呢注意在我们讲义的每一个下方呢都有我们现在人脸检测下方都有比如说呢这边有一个配置max face number比如说face type这些都是基本配置直接往里填其实就可以了OK那我这边就不写了只弄就可以了好了那接下来呢我们关注的就是这几个参数首先呢第一个这个改成image吧因为是字符刷的形式表示一张图片吧image好了第二个
[04:57] 我们图片的类型注意图片类型只能填base64或者UIL好了接着第三个我们写innaOK那这样一来得到了结果想结果那我们可以进行一个打印一起来看一下效果就可以了res.tosgene好了我们刚才看到那个tosgene呢其实还是不太理想我们可以让它帮我们进行一个格式化填一数字自动帮我进行格式化了OK来走
[05:28] 那我这个是一个logo啊各位我这边打开了它里面有人一个头像吗没有啊所以各位来看它返回的这个参数arrow code 2222这个它是自己的一个错误编码啊那这边有错误的信息它告诉我picture not his face什么意思图片当中没有人的一个面部头像没错吧那如果说如果说我可以给它来一个我们刚才的这个001
[05:56] 那001这不是一个人的一个头像吗所以我们可以让他帮我检测一下001当中有没有面部001点注意这个图片是PNGOK我们再来看一下这一回这个返回值和说明究竟是什么给我来看返回值error code0说明代表success那这样一来是不是咱们可以通过error code这个返回值来判断
[06:26] 如果是0代表里面具有面部头像如果不是0是不是就是没有面部头像OK那这个就是跟各位来聊的人脸检测的功能

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Java 代码调用阿里云人脸识别服务，完成人脸注册和人脸检测功能。

2) 按时间顺序列出每张画面的要点：
画面1：展示 `FaceTest.java` 中的 `testFaceRegister` 方法，用于人脸注册，代码中包含 API Key、Secret Key、图片路径、Base64 编码及调用 `addUser` 方法的逻辑。
画面2：展示文件资源管理器，路径为 `ihm\day11\图片`，其中包含 `001.png`、`002.png`、`003.png`、`logo.jpg` 等图片文件。
画面3：展示 `FaceTest.java` 中 `@Test` 注解的测试方法，以及 `@Before` 注解的初始化方法，其中包含 `AlpFace` 客户端的初始化代码。
画面4：展示 `FaceTest.java` 中 `@Before` 注解的初始化方法，代码中包含 `AlpFace` 客户端的初始化和 `options` 配置。
画面5：展示 `FaceTest.java` 中 `@Test` 注解的测试方法，代码中包含 `AlpFace` 客户端的初始化和 `addUser` 方法的调用。
画面6：展示 `FaceTest.java` 中 `testFaceCheck` 方法的代码，用于人脸检测，代码中包含图片路径、Base64 编码及调用 `detect` 方法的逻辑。
画面7：展示 `FaceTest.java` 中 `testFaceCheck` 方法的代码，用于人脸检测，代码中包含图片路径、Base64 编码及调用 `detect` 方法的逻辑。
画面8：展示 `AlpFace` 类的源码，其中包含 `ClientInfoStatus`、`Client`、`Clipboard`、`ClientService` 等类的定义。
画面9：展示 `FaceTest.java` 中 `testFaceCheck` 方法的代码，用于人脸检测，代码中包含图片路径、Base64 编码及调用 `detect` 方法的逻辑。
画面10：展示阿里云人脸识别服务的官方文档页面，标题为“人脸检测 请求参数详情”，表格列出了 `image`、`image_type`、`face_field`、`max_face_num`、`face_type` 等参数的名称、类型、默认值和说明。
画面11：展示 `FaceTest.java` 中 `testFaceCheck` 方法的代码，用于人脸检测，代码中包含图片路径、Base64 编码及调用 `detect` 方法的逻辑。
画面12：展示 `FaceTest.java` 中 `testFaceCheck` 方法的代码，用于人脸检测，代码中包含图片路径、Base64 编码及调用 `detect` 方法的逻辑，同时显示了控制台输出结果。
画面13：展示文件资源管理器，路径为 `ihm\day11\图片`，其中包含 `001.png`、`002.png`、`003.png`、`logo.jpg` 等图片文件。
画面14：展示 `FaceTest.java` 中 `testFaceCheck` 方法的代码，用于人脸检测，代码中包含图片路径、Base64 编码及调用 `detect` 方法的逻辑，同时显示了控制台输出结果。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1：
```java
public void testFaceRegister() throws Exception {
    //1.创建java代码和巨量云交互的client对象
    AlpFace client = new AlpFace(appid: "15246423", apikey: "OFYUyDlB5mHTA8IXTG1gjM", secretKey: "mvqF3pPoOLsMadF61omuztBayE3jFIOv");
    HashMap<String,String> options = new HashMap<>();
    options.put("quality_control", "NORMAL"); //图片质量 NONE LOW NORMAL HIGH
    options.put("liveness_control", "LOW"); //活体检测
    String path = "C:\Users\ThinkPad\Desktop\ihm\day11\资源\图片\001.png";
    byte[] bytes = Files.readAllBytes(Paths.get(path));
    String encode = Base64Util.encode(bytes);
    //4.调用api方法完成人脸注册
    JSONObject res = client.addUser(encode, imageType: "BASE64", groupid: "itcast", userid: "1000", options);
    System.out.println(res.toString());
}
```

画面3：
```java
import java.util.HashMap;
public class FaceTest {
    private AlpFace client;
    @Test
    public void testFaceRegister() throws Exception {
        //1.创建java代码和巨量云交互的client对象
        client = new AlpFace(appid: "15246423", apikey: "OFYUyDlB5mHTA8IXTG1gjM", secretKey: "mvqF3pPoOLsMadF61omuztBayE3jFIOv");
        HashMap<String,String> options = new HashMap<>();
        options.put("quality_control", "NORMAL"); //图片质量 NONE LOW NORMAL HIGH
        options.put("liveness_control", "LOW"); //活体检测
        String path = "C:\Users\ThinkPad\Desktop\ihm\day11\资源\图片\001.png";
        byte[] bytes = Files.readAllBytes(Paths.get(path));
        String encode = Base64Util.encode(bytes);
        //4.调用api方法完成人脸注册
        JSONObject res = client.addUser(encode, imageType: "BASE64", groupid: "itcast", userid: "1000", options);
        System.out.println(res.toString());
    }
}
```

画面5：
```java
public void testFaceRegister() throws Exception {
    //1.创建java代码和巨量云交互的client对象
    client = new AlpFace(appid: "15246423", apikey: "OFYUyDlB5mHTA8IXTG1gjM", secretKey: "mvqF3pPoOLsMadF61omuztBayE3jFIOv");
    HashMap<String,String> options = new HashMap<>();
    options.put("quality_control", "NORMAL"); //图片质量 NONE LOW NORMAL HIGH
    options.put("liveness_control", "LOW"); //活体检测
    String path = "C:\Users\ThinkPad\Desktop\ihm\day11\资源\图片\001.png";
    byte[] bytes = Files.readAllBytes(Paths.get(path));
    String encode = Base64Util.encode(bytes);
    //4.调用api方法完成人脸注册
    JSONObject res = client.addUser(encode, imageType: "BASE64", groupid: "itcast", userid: "1000", options);
    System.out.println(res.toString());
}
```

画面6：
```java
//人脸检测，判断图片中是否具有面部信息
@Test
public void testFaceCheck() {
    //构造图片
    String path = "C:\Users\ThinkPad\Desktop\ihm\day11\资源\图片\001.png";
    //上传的图片  两种格式： url地址，Base64字符串形式
    byte[] bytes = Files.readAllBytes(Paths.get(path));
    String encode = Base64Util.encode(bytes);
    //调用api方法进行人脸转换
    client.detect();
}
```

画面9：
```java
//人脸检测，判断图片中是否具有面部信息
@Test
public void testFaceCheck() throws Exception {
    //构造图片
    String path = "C:\Users\ThinkPad\Desktop\ihm\day11\资源\图片\logo.jpg";
    //上传的图片  两种格式： url地址，Base64字符串形式
    byte[] bytes = Files.readAllBytes(Paths.get(path));
    String encode = Base64Util.encode(bytes);
    //调用api方法进行人脸转换
    client.detect();
}
```

画面12：
```java
//人脸检测，判断图片中是否具有面部信息
@Test
public void testFaceCheck() throws Exception {
    //构造图片
    String path = "C:\Users\ThinkPad\Desktop\ihm\day11\资源\图片\001.png";
    //上传的图片  两种格式： url地址，Base64字符串形式
    byte[] bytes = Files.readAllBytes(Paths.get(path));
    String encode = Base64Util.encode(bytes);
    //调用api方法进行人脸转换
    client.detect();
}
```

画面14：
```java
//人脸检测，判断图片中是否具有面部信息
@Test
public void testFaceCheck() throws Exception {
    //构造图片
    String path = "C:\Users\ThinkPad\Desktop\ihm\day11\资源\图片\001.png";
    //上传的图片  两种格式： url地址，Base64字符串形式
    byte[] bytes = Files.readAllBytes(Paths.get(path));
    String encode = Base64Util.encode(bytes);
    //调用api方法进行人脸转换
    client.detect();
}
```

4

