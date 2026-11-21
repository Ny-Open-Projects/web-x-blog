# 画面线理解：07-百度云API入门：人脸检测

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\07-百度云API入门：人脸检测_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:19, 00:59, 01:40, 01:47, 02:07, 02:24, 02:57, 03:37, 04:04, 04:39, 05:15, 05:37, 06:01, 06:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:57:52

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
