# 13.圈子功能实现之编写接口服务（下）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\13.圈子功能实现之编写接口服务（下）_【海量资源尽在 666java.com】.mp4
- 时长 10分4秒（音频 605s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来测试一下首先呢我们需要呢先把我们这个double呢先跑起来那么就是我们这个这个server然后double Service然后呢找到我们这个mint这个方法然后呢我们去做一个启动好那我们来等待它的启动好那么现在呢我们这个double这个服务呢就已经跑起来了那么接下来呢我们就将我们的sso呢再跑起来那我们来执行一下哎找到它
[00:29] 然后有个myapplication然后我们去run一下把它跑起来就可以做登录了好那么SSO也跑起来了那么跑起来之后我们就把我们刚刚所写这个server这个工程也跑起来我们就可以去做测试了好我们来启动一下它把它也跑起来好我们来稍微等待一下它的一个启动
[00:53] 那么OK我们这个server这个服务呢也跑起来了那么接下来呢我们就实际的来测试一下当然我们这个server呢我们应该是去通过这个debug启动啊那我们就重新来启动一下吧那么我们把它呢去跑起来当然了接下来呢我们就可以来准备我们的测试的工作了那么首先呢我们其实呢是需要去做登录的对不对那么我们先来做登录
[01:19] 那么我们来看一下这个位置呢我们会有一个这个Loki啊这个登录那么我们来看一下我们的这个用户一啊用户一呢是就是他对吧那手机号是他我们改一下他然后呢我们去做一下这个登录当然了那我目前的连接到的是80端口也就是走的我们的Ngex啊好那么我们就去点击这个Send发送来看一下
[01:45] 那么验证码是不是就发送成功了那么验证码发送成功之后呢接下来呢我们就去做一个校验那么在这做校验那么验证码呢就是123456然后呢去做一个Send发送好那么等待一下OK那么这个就是我们所得到的一个Token就是有效的一个Token那么接下来呢我们就来去做一个测试就是我们的一个这个发表我们一个动态啊
[02:15] 那么首先我们需要给他添加一个这个投信息就是这样的一个投信息那么接下来我们给他去发起post请求那么要注意这个路径是在哪里我们一起来看一下是在这个里面那么上面会有一个叫做movins就他那么我们就直接就到这儿把它就去掉发起一个post请求那么接下来我们会有几个参数我们来看一下那么
[02:42] 首先第一个啊这个参数就是我们的这个文本对吧文本然后呢我们比如说随便写一点内容啊比如说就是叫什么呢就是今天啊今天很开心啊很开心好嘞那么然后呢我们再去添加几个那么下面还有我们的一个地址地址呢比如说我们现在就在北京啊或者上海都可以那么我这个就随便写了因为我们做测试嘛
[03:08] 然后呢我们去这个是它的一个经路和纬度那我们就随便写了那么就写个1.111随便写一些这不是真实的然后呢我们这个再去写比如说2.222然后呢我们再去写什么呢这个它的一个图片图片呢我们不能往这丢对吧图片呢我们要丢到这个里面来然后呢去做一个选择图片比如说我们就选择它然后呢我们可以再来一个
[03:38] 我们就选择它吧好嘞那么这样的话是不是就可以做一个提交了呢然后呢当然了我们需要呢在我们这个位置是不是打一个断点那我们看一下它是否能够去接受到我们这个请求呢走好那我们稍微等待一下哎看断点来了吗哎来了那么我们现在呢其实可以看到呢我们这个呃这个文本啊文本是已经被做过一个这个编码了
[04:06] 然后呢location也做过这个编码了但是呢我们其实已经看到呢它是有一些我们的这个参数了对吧图片图片我们直接收到了一个长度呢可以看到是1原因是我们刚刚这个名字呢并没有改啊应该把它改成它啊这个呢我们肯定接受不到了好那我们就直接先进入吧先来看一下它的一个执行效果吧先去通过token做查询那么token呢是拿到这个优势对象了然后往下面走走走走走走
[04:36] 然后呢去上传图片看能不能够上传成功呢我们去稍微等待一下OK那么上传成功了那么我们继续就一张图片对吧然后呢我们来看一下这个图片的链接对不对那么就是这个链接了那我们拷贝它的一个value那我们去尝试的去访问一下OK这个图片是不是已经成功上传到这个阿里云上面去了然后呢我们就通过执行来看一下最终的一个结果
[05:06] 响应是200那就说明已经成功了那我把这个呢去调一下这个改成呃改成相同的这个名字他就会接收到有两个这个图片了那么我们来看一下这个是不是做了这个那编译之后的编码之后的对吧我们把这个改一下吧比如说这个呃今天呃心情很好啊然后呢下面这个地址location那么就改成上海吧上海
[05:35] 然后我们再次发起请求来看一下这个效果那么来看一下这个结果呢是不是就符合我们的预期了对吧这两个值OK的然后呢这个文件呢也会有两个这个文件了就是我们图片的文件然后走走走也就是说我们会发表了两个这个动态了然后走走做上传拿到再做上传两个这个图片
[06:00] 没有问题OK好走通过最后的响应的是200那就说明成功了那么接下来我们通过我们的mongodb来查看一下这个数据对不对好那我们来先来看一下public那么总共会有三条那么这个是我们刚刚所提交的一条还有刚刚我们所提交的第二条对吧好那么然后这个是我的用户ID唯一的用户去发表动态他会向
[06:26] 他的好友去写入他的动态那么我们来看一下比如说就以他为例他的 id 尾号是024我们来看一下 id 为2的用户有没有这个动态是不是也有024对吧然后 id 为3的是不是同样的是不是也有也有024ok 好那么基本上可以看到我们刚刚所编写的一个用户的发布我们这个动态
[06:53] 这个功能啊那我们是不是就已经搞定了对吧OK好那么接下来呢我们其实呢就可以来整合啊整合我们的一个这个测试那我们来看也可以来测试一下啊那么接下来呢我们就打开我们的这个就是我们那个模拟器啊那模拟器呢我这边的需要重启一下那我们稍微等待一下好那么现在呢这个模拟器呢就启动好了那么接下来呢我们来找到我们的这个碳花这个应用
[07:21] 然后呢我们去做一下这个测试然后呢我们首先呢其实需要去修改一下我们的这个请求的地址就是我本机的这个地址那么我这个地址呢我来看一下其实是在这个位置我来拷贝一下这个是我本机的地址那么大家呢要修改成你自己的这个地址然后呢我们就到这吧然后这个得输入一个这个内容才能够去做一个粘贴要不然那个粘贴的这个选项是出不来的
[07:48] 那么点击一个这个保存然后呢我们呃还是按照一个登录注册这样的一个先来登录再来测试这样的一个逻辑吧那么我们的测试的手机号呢是17602026868啊这样的一个手机号然后呢获取这个验证码验证码其实已经获取到了那么我们就直接输吧123456哎输错了对吧应该是叫什么呢1
[08:19] 1232456好验证通过然后呢我们进入这个圈子然后我们去点击这个发布当然了我测试呢我就先把这个断点呢我就先给它去掉然后呢我们直接来看一个这个结果看OK不OK就行了好那么比如说我写些内容这个因为在这个位置写中文不是很好写那我就随便去写吧对吧比如说我写个test1
[08:49] 然后我去选择这个图片这个图片大家需要去在模拟器中先准备这么几张图片比如说我去选择这个当然了这个我们看它能不能够去多选我希望多选几张图片你比如说选择这个和下面这个我需要长按住它然后再选择一下这样的话就OK了点击这个打开这样的话就变成两张图片了我们点击这个发帖走
[09:18] 那么可以看到这个动态是不是就已经发布成功了那我们来看一下在我们的mongodb中这个动态有没有去发布成功呢可以看到是不是已经就成功了对吧已经就成功了那么这个location name是不是也有对吧然后它的一些这个就是我们这个图片图片是不是也有那我们可以来访问一下比如拷贝它的一个value那我们来访问一下看它这个效果怎么样
[09:48] OK是不是会有这样的一个这个图片OK好嘞好那么这样的话呢我们是不是就已经整合到我们的一个前端呢去做了这样的一个测试了对吧OK好那么关于我们这个接口服务的一个测试呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个基于 Spring Boot 的移动社交应用中，用户发布带图片动态功能的后端实现，包括 Controller、Service 层代码、数据库表结构、API 测试及移动端效果演示。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 `MovementsService.java` 中的 `saveMovements` 方法，用于构建并保存一个动态对象，包含设置用户 ID、文本内容、位置名称、经纬度和图片 URL。代码中包含图片上传逻辑，调用 `picUploadService.upload` 方法并收集返回的图片 URL。
画面 2: 展示 `ServerApplication.java` 的 `main` 方法，启动 Spring Boot 应用。控制台日志显示 MyBatis Plus、HikariCP、Tomcat 等组件已成功加载。
画面 3: 展示 Navicat Premium 中的 `tb_user` 数据库表，包含用户 ID、密码、创建时间等字段，用于验证用户信息。
画面 4: 展示 `MovementsController.java` 中的 `@PostMapping` 方法，接收前端传来的文本内容、位置、经纬度、图片和 token 参数。
画面 5: 展示 `MovementsController.java` 中的 `saveMovements` 方法，包含 try-catch 块，用于处理异常并返回 HTTP 状态码。
画面 6: 展示 `MovementsController.java` 中的 `saveMovements` 方法，调试器已断点，变量窗口显示 `textContent`、`location`、`longitude` 等参数值。
画面 7: 展示 `MovementsService.java` 中的 `saveMovements` 方法，通过 `userService.queryUserByToken` 查询用户，然后创建并设置 `Publish` 对象的属性。
画面 8: 展示 Advanced REST Client 中的 POST 请求，用于测试发布动态的 API，包含 Authorization 头和两个图片文件的上传。
画面 9: 展示 `MovementsService.java` 中的 `saveMovements` 方法，调试器断点，变量窗口显示 `user` 对象和 `textContent` 等参数值。
画面 10: 展示 Robo 3T 中的 `quanzi_publish` 集合，显示已保存的动态数据，包括用户 ID、文本内容、经纬度、图片 URL 等字段。
画面 11: 展示 Genymotion 模拟器启动，显示 Android 系统桌面，用于测试移动端应用。
画面 12: 展示 Genymotion 模拟器中打开的“推荐”页面，用于测试移动端应用的界面。
画面 13: 展示 Genymotion 模拟器中打开的“发动态”页面，显示用户已上传的图片，用于测试移动端应用的发布功能。
画面 14: 展示 Typora 中的 `day03 四子.md` 文件，包含测试的图片和文字内容，用于记录和展示测试结果。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```java
Publish publish = new Publish();
publish.setUserId(user.getId());
publish.setText(textContent);
publish.setLocationName(location);
publish.setLatitude(latitude);
publish.setLongitude(longitude);

//图片上传
List<String> imageUrls = new ArrayList<>();
for (MultipartFile file : multipartFile) {
    PicUploadResult uploadResult = this.picUploadService.upload(file);
    imageUrls.add(uploadResult.getName());
}

publish.setMedias(imageUrls);
return this.quanziApi.savePublish(publish);
```

画面 4:
```java
@PostMapping
public ResponseEntity<Void> saveMovements(
    @RequestParam("textContent") String textContent,
    @RequestParam("location") String location,
    @RequestParam("longitude") String longitude,
    @RequestParam("latitude") String latitude,
    @RequestParam("imageContent") MultipartFile[] multipartFile,
    @RequestHeader("Authorization") String token) {
```

画面 5:
```java
try {
    Boolean bool = this.movementsService.saveMovements(textContent, location, longitude, latitude, multipartFile, token);
    if (bool) {
        return ResponseEntity.ok(null);
    }
} catch (Exception e) {
    e.printStackTrace();
}
return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
```

画面 7:
```java
String latitude, latitude: "2.2222"
User user = this.userService.queryUserByToken(token) {
    if (null == user) {
        return false;
    }
    Publish publish = new Publish();
    publish.setUserId(user.getId());
    publish.setText(textContent);
    publish.setLocationName(location);
    publish.setLatitude(latitude);
    publish.setLongitude(longitude);
```

画面 9:
```java
User user = this.userService.queryUserByToken(token);
if (null == user) {
    return false;
}
Publish publish = new Publish();
publish.setUserId(user.getId());
publish.setText(textContent);
publish.setLocationName(location);
publish.setLatitude(latitude);
publish.setLongitude(longitude);
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 无。

