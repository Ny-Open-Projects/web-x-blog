# 09-百度云API入门：人脸更新

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\09-百度云API入门：人脸更新_【海量资源尽在 ubkz.com】.mp4
- 时长 2分38秒（音频 159s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那刚才简单的看了一下人脸注册人脸检测还有一个人脸搜索的这几个功能那除了这几个功能之外呢还有一个需要跟各位简单的提一下叫什么呢就是人脸更新我写到这边了人脸更新那为什么要有人脸更新的这么一个功能呢其实是这样的就是我们都知道啊咱们每一个人呢随着不同的阶段随着年龄的不断增长咱们的面部呢可能会有一点点稍微一点点细节的一个变化
[00:32] 那比如说呢开始你是50斤那到最后你变成了200斤你面部变化那就更大了所以呢面部的差异越来越大那对于这个人脸库的这个图片也就是人脸库里面这张照片是不是也应该进行一个更新的一个操作啊那为了防止它的一个识别不准确吧所以对于这个人脸库来说还有一个更新的一个操作来做就是更新人脸人脸库
[01:05] 中的我们叫做照片好了这个如何去做呢很简单很简单和注册基本上是一模一样的改变方法叫做updateupdate那注意不一样的点在哪不一样的点在调用client方法的时候我们刚才我们刚才用的全部是一个叫做add user我们刚才用的是一个add user现在我们要把add user变成update user即可
[01:37] 所以更新和注册是一模一样只不过不一样的就是调用的方法不同一个叫做add user一个叫做update user调用一下方法剩下的参数一模一样好了那接着我们一起来看一下还是对这个100这个用户来进行操作刚才的图片这边有那接下来我把这个图片改成002好了改成002之后走好了这边有返回结果返回结果呢其中
[02:11] error code 0代表成功那我们一起刷新一下百度的人脸库好了刷新一下你会发现图片也发生了变化没错吧那这样一来当一个用户他的面部的一些特征发生比较大的一个变化的时候我们就可以进行人脸库图片的一个更新操作了当然更新和注册基本上是一样的就是一个叫做add user一个叫做update user

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
"C:\Program Files\Java\JDK 8.0_92\bin\java" ...
```
画面13：
无代码。
画面14：
无代码。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无PPT标题、架构图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

