# 画面线理解：15-刷脸登录：功能介绍和人脸注册

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\15-刷脸登录：功能介绍和人脸注册_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:04, 01:56, 03:10, 04:29, 05:04, 06:15, 07:57, 08:48, 09:13, 09:30, 10:01, 10:41, 11:03, 11:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:03:11

1) 这一组画面整体在讲什么（一句话）：
讲解 iHRM 系统中实现人脸登录功能的前后端代码逻辑，包括用户注册、二维码生成、人脸检测与登录等环节。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面“4.5 功能实现”，内容包括人脸注册、二维码生成、二维码检测、人脸检测、人脸登录五个步骤。
画面 2: 展示 iHRM 后台登录页面，包含用户名、密码输入框和登录按钮。
画面 3: 在 IntelliJ IDEA 中展示 UserServic.java 文件，代码片段为上传图片到七牛云的逻辑。
画面 4: 在 IntelliJ IDEA 中展示 UserServic.java 文件，代码片段为上传图片到七牛云的逻辑，注释部分显示“上传到七牛云存储”、“注册到百度云AI人脸库”、“判断当前用户是否已经注册”、“已注册，更新”、“未注册，注册”。
画面 5: 在 IntelliJ IDEA 中展示 BaiduAIIUtil.java 文件，代码片段为人脸注册方法，使用百度AI接口。
画面 6: 在 IntelliJ IDEA 中展示 BaiduAIIUtil.java 文件，代码片段为初始化百度AI客户端和人脸注册方法。
画面 7: 在 IntelliJ IDEA 中展示 UserServic.java 文件，代码片段为上传图片并调用百度AI接口进行人脸注册。
画面 8: 在 IntelliJ IDEA 中展示 UserServic.java 文件，代码片段为上传图片并调用百度AI接口进行人脸注册，注释部分显示“判断是否已经注册”、“更新”、“注册”、“返回”。
画面 9: 展示浏览器地址栏输入“Swagger UI”，页面显示 Google 搜索结果。
画面 10: 展示百度AI人脸识别控制台，页面显示“产品概览”、“应用”、“用量”等信息。
画面 11: 展示 iHRM 系统员工详情页面，包含员工照片和基础信息表单。
画面 12: 展示百度AI人脸识别控制台，页面显示“/itcast”路径和“+ 新增用户”按钮。
画面 13: 展示 iHRM 系统登录用户设置页面，包含用户名、密码输入框和“更新”、“取消”按钮。
画面 14: 在 IntelliJ IDEA 中展示 UserServic.java 文件，代码片段为上传图片并调用百度AI接口进行人脸注册，注释部分显示“判断是否已经注册”、“更新”、“注册”、“返回”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3 代码：
```java
public String uploadImage(String id, MultipartFile file) throws IOException {
    User user = userDao.findById(id).get();
    String imgUrl = new QiniuUploadUtil().upload(user.getId(), file.getBytes());
    user.setStaffPhoto(imgUrl);
    userDao.save(user);
    return imgUrl;
}
```

画面 4 代码：
```java
public String uploadImage(String id, MultipartFile file) throws IOException {
    User user = userDao.findById(id).get();
    String imgUrl = new QiniuUploadUtil().upload(user.getId(), file.getBytes());
    user.setStaffPhoto(imgUrl);
    userDao.save(user);
    return imgUrl;
}
```

画面 5 代码：
```java
public Boolean faceRegister(String userId, String image) {
    // 人脸注册
    JSONObject res = client.addUser(image, IMAGE_TYPE, groupId, userId, options);
    Integer errorCode = res.getInt(key: "error_code");
    return errorCode == 0 ? true : false;
}
```

画面 6 代码：
```java
private AiFace client;
private HashMap<String, String> options = new HashMap<>();
public BaiDuAIIUtil() {
    options.put("quality_control", "NORMAL");
    options.put("liveness_control", "LOW");
}
@PostConstruct
public void init() { client = new AiFace(APP_ID, API_KEY, SECRET_KEY); }
// 判断用户是否已经注册了人脸信息
public Boolean faceExist(String userId) {
    // 返回错误码
    JSONObject res = client.getUser(userId, groupId, options);
    return res.getInt(key: "error_code") == 0 ? true : false;
}
```

画面 7 代码：
```java
public String up
    // 1. 上传图片
    // 2. 判断是否已经注册
    // 3. 已注册，更新
    // 4. 未注册，注册
    // 5. 返回
    // 上传图片，图片的byte数组
    // 判断是否已经注册
    // 更新
    // 注册
    // 返回
```

画面 8 代码：
```java
public String uploadImage(String id, MultipartFile file) throws IOException {
    User user = userDao.findById(id).get();
    String imgUrl = new QiniuUploadUtil().upload(user.getId(), file.getBytes());
    user.setStaffPhoto(imgUrl);
    userDao.save(user);
    return imgUrl;
}
// 判断是否已经注册
Boolean aBoolean = baiduAiiUtil.faceExist(id);
if (aBoolean) {
    // 更新
    baiduAiiUtil.faceUpdate(id, imgBase64);
} else {
    // 注册
    baiduAiiUtil.faceRegister(id, imgBase64);
}
// 返回
return imgUrl;
```

画面 14 代码：
```java
public String uploadImage(String id, MultipartFile file) throws IOException {
    User user = userDao.findById(id).get();
    String imgUrl = new QiniuUploadUtil().upload(user.getId(), file.getBytes());
    user.setStaffPhoto(imgUrl);
    userDao.save(user);
    return imgUrl;
}
// 判断是否已经注册
Boolean aBoolean = baiduAiiUtil.faceExist(id);
if (aBoolean) {
    // 更新
    baiduAiiUtil.faceUpdate(id, imgBase64);
} else {
    // 注册
    baiduAiiUtil.faceRegister(id, imgBase64);
}
// 返回
return imgUrl;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 PPT 标题：“4.5 功能实现”，内容包括：
- 人脸注册/人脸更新
- 二维码生成
- 二维码检测
- 人脸检测
- 人脸登录

画面 10 百度AI人脸识别控制台页面标题：“产品概览 / 人脸识别 - 概览”，包含“应用”、“用量”等信息。

画面 12 百度AI人脸识别控制台页面标题：“/itcast”，包含“+ 新增用户”按钮。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
