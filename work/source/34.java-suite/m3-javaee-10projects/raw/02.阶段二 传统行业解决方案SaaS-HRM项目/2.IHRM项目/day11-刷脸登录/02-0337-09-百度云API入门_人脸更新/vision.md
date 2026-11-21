# 画面线理解：09-百度云API入门：人脸更新

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\09-百度云API入门：人脸更新_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:04, 00:14, 00:22, 00:54, 01:13, 01:30, 01:33, 01:40, 01:45, 01:59, 02:06, 02:15, 02:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:59:01

1) 这一组画面整体在讲什么（一句话）：
演示如何使用百度AI开放平台的人脸识别Java SDK，通过单元测试代码实现人脸注册、更新、检测和搜索功能，并最终在百度云控制台验证注册成功。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `testFaceSearch` 方法，用于人脸搜索，调用 `client.search` 方法，参数包括图片Base64编码、图像类型、分组ID和选项。
画面2：展示 `testFaceCheck` 方法，用于人脸检测，调用 `client.detect` 方法，参数包括图片Base64编码、图像类型和选项。
画面3：展示 `testFaceCheck` 方法，设置活体检测参数 `liveness_control` 为 "LOW"。
画面4：展示 `testFaceRegister` 方法，用于人脸注册，调用 `client.addUser` 方法，参数包括图片Base64编码、图像类型、分组ID、用户ID和选项。
画面5：展示 `testFaceRegister` 方法，设置质量控制参数 `quality_control` 为 "NORMAL"，活体检测参数 `liveness_control` 为 "LOW"。
画面6：展示 `testFaceRegister` 方法，设置质量控制参数 `quality_control` 为 "NORMAL"，活体检测参数 `liveness_control` 为 "LOW"。
画面7：展示 `testFaceUpdate` 方法，用于更新人脸，调用 `client.updateUser` 方法，参数包括图片Base64编码、图像类型、分组ID、用户ID和选项。
画面8：展示 `testFaceUpdate` 方法，设置质量控制参数 `quality_control` 为 "NORMAL"，活体检测参数 `liveness_control` 为 "LOW"。
画面9：展示 `testFaceUpdate` 方法，设置质量控制参数 `quality_control` 为 "NORMAL"，活体检测参数 `liveness_control` 为 "LOW"。
画面10：展示 `testFaceUpdate` 方法，设置质量控制参数 `quality_control` 为 "NORMAL"，活体检测参数 `liveness_control` 为 "LOW"。
画面11：展示 `testFaceUpdate` 方法，设置质量控制参数 `quality_control` 为 "NORMAL"，活体检测参数 `liveness_control` 为 "LOW"。
画面12：在IDEA终端中运行 `testFaceUpdate` 方法，显示编译成功。
画面13：在百度云控制台的人脸识别页面，显示正在等待响应。
画面14：在百度云控制台的人脸识别页面，显示已成功注册的人脸信息，包括用户ID 1000 和注册时间。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
JSONObject res = client.detect(image, imageType: "BASE64", options: null);
System.out.println(res.toString(indentFactor: 2));
```
画面2：
```java
JSONObject res = client.updateUser(encode, imageType: "BASE64", groupid: "itcast", userid: "1000", options);
System.out.println(res.toString());
```
画面3：
```java
options.put("liveness_control", "LOW"); //活体检测
```
画面4：
```java
JSONObject res = client.addUser(encode, imageType: "BASE64", groupid: "itcast", userid: "1000", options);
System.out.println(res.toString());
```
画面5：
```java
options.put("quality_control", "NORMAL"); //图片质量控制
options.put("liveness_control", "LOW"); //活体检测
```
画面6：
```java
options.put("quality_control", "NORMAL"); //图片质量控制
options.put("liveness_control", "LOW"); //活体检测
```
画面7：
```java
JSONObject res = client.updateUser(encode, imageType: "BASE64", groupid: "itcast", userid: "1000", options);
System.out.println(res.toString());
```
画面8：
```java
options.put("quality_control", "NORMAL"); //图片质量控制
options.put("liveness_control", "LOW"); //活体检测
```
画面9：
```java
options.put("quality_control", "NORMAL"); //图片质量控制
options.put("liveness_control", "LOW"); //活体检测
```
画面10：
```java
options.put("quality_control", "NORMAL"); //图片质量控制
options.put("liveness_control", "LOW"); //活体检测
```
画面11：
```java
options.put("quality_control", "NORMAL"); //图片质量控制
options.put("liveness_control", "LOW"); //活体检测
```
画面12：
```bash
"C:\Program Files\Java\jdk1.8.0_92\bin\java" ...
```
画面13：
无代码。
画面14：
无代码。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无PPT标题、架构图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
