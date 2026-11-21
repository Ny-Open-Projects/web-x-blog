# 画面线理解：08-七牛云存储：更新图片和访问图片

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\08-七牛云存储：更新图片和访问图片_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:26, 01:09, 01:35, 02:17, 02:27, 02:36, 03:38, 04:55, 05:21, 05:44, 05:58, 06:15, 07:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:26:17

1) 这一组画面整体在讲如何使用 Java SDK 将本地图片上传至七牛云对象存储服务，并通过 URL 访问上传后的图片。

2) 按时间顺序列出每张画面的要点：
画面1: 显示七牛云对象存储管理后台，展示名为“ihrm-bucket”的存储空间，其中包含一个名为“test”的文件（128.63 KB），文件路径为“image/png”，上传时间为“2018-12-26 09:02:16”。同时，任务栏显示 IntelliJ IDEA 中的项目结构和代码编辑器。
画面2: 显示 IntelliJ IDEA 中的 Java 代码，定义了上传图片的测试方法 testUpload01()，其中包含配置、上传管理器、访问密钥、密钥、存储空间名、本地文件路径和文件名等变量，并执行上传操作。
画面3: 与画面2相同，代码中注释“//图片路径”和“//存入到存储空间的文件名”被高亮显示。
画面4: 与画面2相同，代码中注释“//图片路径”和“//存入到存储空间的文件名”被高亮显示，同时代码中“String key = "test";”被高亮显示。
画面5: 与画面1相同，显示七牛云对象存储管理后台，展示名为“ihrm-bucket”的存储空间，其中包含一个名为“test”的文件（128.63 KB），文件路径为“image/png”，上传时间为“2018-12-26 09:02:16”。
画面6: 显示七牛云开发者中心的 Java SDK 文档页面，其中包含上传文件的示例代码，包括定义上传参数、获取上传凭证、上传文件等。
画面7: 显示七牛云开发者中心的 Java SDK 文档页面，其中包含上传文件的示例代码，包括定义上传参数、获取上传凭证、上传文件等。
画面8: 显示 IntelliJ IDEA 中的 Java 代码，测试方法 testUpload01() 已成功执行，终端显示“1 test passed”和“Process finished with exit code 0”。
画面9: 显示七牛云对象存储服务的 URL 页面，显示一张名为“test”的图片，图片内容为一位男士的肖像。
画面10: 显示 IntelliJ IDEA 中的 Java 代码，测试方法 testUpload01() 已成功执行，终端显示“1 test passed”和“Process finished with exit code 0”。
画面11: 显示 Windows 文件资源管理器，路径为“ihrm\day9\资源”，其中包含“001.png”、“002.png”、“dataurl.txt”和“test.xlsx”等文件。
画面12: 显示 IntelliJ IDEA 中的 Java 代码，测试方法 testUpload01() 已成功执行，终端显示“1 test passed”和“Process finished with exit code 0”。
画面13: 显示七牛云对象存储服务的 URL 页面，显示一张名为“test”的图片，图片内容为一位男士的肖像，同时右键菜单弹出，包含“属性”、“重命名”、“复制”等选项。
画面14: 显示 IntelliJ IDEA 中的 Java 代码，测试方法 testUpload01() 已成功执行，终端显示“1 test passed”和“Process finished with exit code 0”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面2代码：
```java
//指定上传文件服务器地址。
Configuration cfg = new Configuration(Zone.zone0());
//...其他资源访问类注释
UploadManager uploadManager = new UploadManager(cfg);
//...生成上传凭证，然后准备上传
String accessKey = "COuDRVa7JLsuursIvQ51_pEDceDv3yGfFEmvvw";
String secretKey = "3RkptJ853g3Qs1fF4mxBHXJ5JR2mAHQyYsSlr";
String bucket = "ihrm-bucket";
//图片路径
String localFilePath = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\资源\\资源\\1001.png";
//存入到存储空间的文件名
String key = "test";
//身份认证
Auth auth = Auth.create(accessKey, secretKey);
String upToken = auth.uploadToken(bucket,key);
//上传
Response response = uploadManager.put(localFilePath, key, upToken);
//解析上传结果
DefaultPutRet putRet = new Gson().fromJson(response.bodyString(), DefaultPutRet.class);
System.out.println(putRet.key);
System.out.println(putRet.hash);
```

画面6代码：
```java
String accessKey = "access_key";
String secretKey = "secret_key";
String bucket = "bucket_name";
Auth auth = Auth.create(accessKey, secretKey);
String upToken = auth.uploadToken(bucket);
```

画面7代码：
```java
String accessKey = "access_key";
String secretKey = "secret_key";
String bucket = "bucket_name";
Auth auth = Auth.create(accessKey, secretKey);
String upToken = auth.uploadToken(bucket, "test.jpg");
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 无。
