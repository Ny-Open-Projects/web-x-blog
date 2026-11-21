# 画面线理解：06-百度云API入门：人脸注册

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\06-百度云API入门：人脸注册_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 02:04, 02:55, 03:38, 04:28, 04:45, 05:39, 08:02, 08:30, 09:45, 11:37, 13:02, 13:51, 14:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:57:01

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
