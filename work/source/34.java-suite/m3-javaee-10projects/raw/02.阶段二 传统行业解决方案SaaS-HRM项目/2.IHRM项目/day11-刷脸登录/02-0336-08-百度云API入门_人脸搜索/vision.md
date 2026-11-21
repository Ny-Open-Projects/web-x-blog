# 画面线理解：08-百度云API入门：人脸搜索

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\08-百度云API入门：人脸搜索_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:37, 02:13, 02:38, 02:53, 03:37, 03:51, 04:33, 04:52, 05:12, 05:30, 06:38, 08:30, 08:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:58:29

1) 这一组画面整体在讲什么（一句话）：
演示如何使用百度AI开放平台的人脸识别API，在Java项目中实现人脸检测与人脸搜索功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IntelliJ IDEA中FaceTest.java文件，其中包含人脸检测方法testFaceCheck()，代码中指定了图片路径为"C:\Users\ThinkPad\Desktop\ihrm\day11\资源\图片\001.png"，并使用Base64编码，调用client.detect方法进行检测。
画面2：百度AI开放平台的人脸识别管理界面，显示“正在处理数据，请稍候...”的提示，表明正在执行人脸检测或搜索操作。
画面3：IntelliJ IDEA中FaceTest.java文件，展示人脸检测方法testFaceCheck()的完整代码，包括Base64编码和调用client.detect方法。
画面4：Windows资源管理器中显示“003.jpg”图片，为刘德华的照片，是用于人脸检测或搜索的测试图片。
画面5：Windows资源管理器中显示“002.jpg”图片，为刘德华的照片，是用于人脸检测或搜索的测试图片。
画面6：IntelliJ IDEA中FaceTest.java文件，展示人脸搜索方法testFaceSearch()的代码，指定图片路径为"C:\Users\ThinkPad\Desktop\ihrm\day11\资源\图片\002.png"，并调用client.search方法。
画面7：IntelliJ IDEA中ApFace.class文件，展示搜索方法的内部实现，包括设置请求URL、添加请求体参数（image, imageType, groupId, options）并发送POST请求。
画面8：PPT页面，标题为“第11章 人脸识别”，当前显示“5.4 人脸搜索”部分。
画面9：PPT页面，展示“人脸搜索 返回数据参数详情”表格，包含字段、必选、类型、说明等信息，如face_token、user_list、group_id等。
画面10：Windows资源管理器中显示“001.jpg”图片，为刘德华的照片，是用于人脸搜索的测试图片。
画面11：IntelliJ IDEA中FaceTest.java文件，展示人脸搜索方法testFaceSearch()的执行结果，控制台输出JSON格式的返回数据，包含face_token、user_list、score等信息。
画面12：IntelliJ IDEA中FaceTest.java文件，展示人脸搜索方法testFaceSearch()的执行结果，控制台输出JSON格式的返回数据，包含face_token、user_list、score等信息。
画面13：Windows资源管理器中显示“002.jpg”图片，为刘德华的照片，是用于人脸搜索的测试图片。
画面14：IntelliJ IDEA中FaceTest.java文件，展示人脸搜索方法testFaceSearch()的执行结果，控制台输出JSON格式的返回数据，包含face_token、user_list、score等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1代码：
```java
@Test
public void testFaceCheck() throws Exception {
    String path = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day11\\资源\\图片\\001.png";
    byte[] bytes = Files.readAllBytes(Paths.get(path));
    String image = Base64Util.encode(bytes);
    //调用api方法进行人脸检测
    //参数一：（图片的url或者图片的Base64字符串）
    //参数二：图片格式（URL_BASE64）
    //参数三：hashMap中的基本参数配置（null，使用默认配置）
    JSONObject res = client.detect(image, imageType: "BASE64", options: null);
    System.out.println(res.toString( indentActor: 2));
}
```

画面3代码：
```java
//调用api方法进行人脸检测
//参数一：（图片的url或者图片的Base64字符串）
//参数二：图片格式（URL_BASE64）
//参数三：hashMap中的基本参数配置（null，使用默认配置）
JSONObject res = client.detect(image, imageType: "BASE64", options: null);
```

画面6代码：
```java
@Test
public void testFaceSearch() throws Exception {
    //图片路径
    String path = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day11\\资源\\图片\\002.png";
    byte[] bytes = Files.readAllBytes(Paths.get(path));
    String image = Base64Util.encode(bytes);
    //人脸搜索
    JSONObject res = client.search(image, imageType: "BASE64", groupIdList: "itcast", options: null);
}
```

画面7代码：
```java
public JSONObject search(String image, String imageType, String groupIdList, HashMap<String, String> options) {
    ApRequest request = new ApRequest();
    this.preparation(request);
    request.setUri("https://aip.baidubce.com/rest/2.0/face/v5/search");
    request.setBodyFormat(BodyFormat.RAW_JSON);
    this.postOperation(request);
    return this.requestServer(request);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8：PPT标题为“第11章 人脸识别”，左侧导航栏显示“5.4 人脸搜索”。
画面9：表格数据：
字段 | 必选 | 类型 | 说明
---|---|---|---
face_token | 是 | string | 人脸标志
user_list | 是 | array | 匹配的用户信息列表
+group_id | 是 | string | 用户所属的group_id
+user_id | 是 | string | 用户的user_id
+user_info | 是 | string | 注册用户时携带的user_info

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
