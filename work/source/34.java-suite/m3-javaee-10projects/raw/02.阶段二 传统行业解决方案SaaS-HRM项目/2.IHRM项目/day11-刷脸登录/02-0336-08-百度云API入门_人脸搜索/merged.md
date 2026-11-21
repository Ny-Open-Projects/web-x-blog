# 08-百度云API入门：人脸搜索

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\08-百度云API入门：人脸搜索_【海量资源尽在 ubkz.com】.mp4
- 时长 9分9秒（音频 550s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 完成了人脸检测这个功能那么我们接下来呢就继续往后看我们接下来要完成这个功能呢叫做人脸检索或者人脸搜索那这个人脸搜索它主要要干什么呢是这样就是说呢你可以拿手机拍摄一张照片那拍摄一张照片传递给百度云AI那接下来呢它就会载百度云AI这个我们叫做
[00:31] 人脸库当中帮你进行检索因为我们都知道人脸库里面可能有比如说这个用户组里面可能有很多个用户001 002 一万个用户那你上传一张照片它就会根据这一万个用户里面一个一个的进行比对找到相似度最高的那个或者找到相似度最高的某几个告诉你那这样一来比如说你上传一个照片你这里面有100条记录那你会发现你上传的照片是
[01:01] 100号用户的那比较之后它会给你返回你当前用户的ID100并且呢它会给你返回出一个评分就是说跟100这个用户的这张图片它的相似度究竟是多少分就是这么一个含义那接下来呢我们来看一下如何去完成这个功能那人脸搜索呢其实咱们总结一下人脸搜索呢其实就是根据
[01:29] 用户上传的图片和指定人脸库中的所有人脸进行比较获取相似度最高的最高的一个或者某几个的就的评分情况当然了对于究竟是一个还是某几个这个是我们可以指定的他默认是拿一个他默认是从里面找到一个
[02:07] OK那好了接下来这个代码呢也比较简单好了ETATESTPUBLICUIDTESTFACE SEARCHSEARCH好了那这个代码呢写起来呢也不难首先呢就是说你得有张图片那这张图片呢我在今天资料当中也给各位准备了那第一张图片是我已经放到人脸库里了那我这边呢还有第二张图片还有第三张图片
[02:39] 那你明显你就知道了第一张图片和第二张图片是我第三张图片是其他老师没错吧好了那我一会儿比如说我用第二张上传的时候我就能拿到第一个有它的评分好了好了接着拿第三个注意第三个传上去它也会把第一张的资料告诉你因为它会找到相似度那其实是只要是人它就有某些相似的地方只不过我第二张图片的相似度评分会比较高那第三个是不是相似度会比较低
[03:08] OK那好了接着我们一起来看一下这个代码首先呢第一件事我们应该构造图片跟之前逻辑一样好了图片构造好了之后接下来呢我们就可以进行人脸搜索好了那接下来构造图片那构造图片呢这个代码呢就是一模一样的OK比如说呢我用第二张图片来进行构造这边呢有异常我处理一下
[03:38] 好了图片构造好了之后接着就开始进行人脸搜索人脸搜索同样是调用Client的方法Client打点这边有一方法就叫做Search好了这个Search里面的参数有很多有很多我们一起打开来看首先第一个参数Image这个不用多解释了就是图片的UIL地址或者图片的base64字符串Typebase64或者UIL字符串好了Group ID List我们刚才说过了Group ID只要写好了就是固定了
[04:08] 好了第三个是一些基本的设置OK那接着前几个参数都比较简单第一个image第二个base64字符串接着第三个我们叫做groupidgroupid我们刚才说过了itcast一旦写好就固定了好了接着最后一个是我们的一些基本配置那对于这些基本配置在今天的讲义当中人脸查找底下都有基本配置可以是control
[04:39] 对对可以是Ctrl等等还有MaxUserNumber那这些就是刚才说过了你可以返回一个可以返回多个都是这样进行匹配的那对于我而言那对于我而言我这边其实就写一None了全部用默认配置即可OK那好了接着这样一来我们就能得到返回结果得到返回结果之后打印一下返回结果看一下它的效果
[05:08] 那需要各位注意001和这个002这两张明显是同一个人明显是同一个人接着我们可以执行一下看一下效果好了各位会发现这边的AeroCode是0没问题说明我们的比对操作是成功的并且这边它给我一个返回值叫做user list这个user list里面得到的就是一个数组包含相似度
[05:39] 最高的几个用户的一些情况并且它是根据相似度进行一个倒序排序如果有多个的话是进行倒序排序那对于我们来说其实只拿一个就行了不用拿多个拿到相似度最高的这个那各位来看各位来看那其中它返回值里面有个user id那注意这个user id各位应该还有印象我注册的时候是把我们自己的user id给它传过去了
[06:08] 那这样一来你根据一个图片通过百度云AI的一个对比是不是把这个相似度最高的这个优优的ID给我返回了那这样一来我们就知道当前你拍摄照片的这个人他的用户ID是100i并且呢这边有个scorescore指的是相似度评分那这个相似度评分是95你会发现95其实代表的就比较相似啊OK那好了接着这边呢需要跟各位做一个简单的说明
[06:38] 简单的说明一定一定要遵守这个规则来做那这个说明是什么呢就是这个返回值它是一个数组但是我们只需要第一条第一条代表的是相似度最高的数据那这边呢有一个评分score那score指的是相似度评分那这个相似度评分它满分是100满分是100那这个相似度评分究竟
[07:15] 到达多少一个数值就可以理解为两张图片是一个人因为你发现我001跟002那其实是一个人但是这个评分呢究竟达到多少可以是一个人这个是百度云AI他的推荐80分以上可以认为是同一个同一个用户或者同一个人这个能理解吧所以对于我们而言所以对于我们而言有可能有可能你把003传进去
[07:51] 它也会有这个数据范围只不过只不过score它不是95而是一个比较低的一个分值我们一起来看一下走那各位来看我把003传过去了传过去之后这个用户也是1000也能拿到只不过这个评分是不是就是41那它为什么有这种情况是这样的毕竟它是一个机器在进行对比那机器对比的时候这几张图形里面有可能会有一些相似的地方
[08:25] 比如说呢都是大眼睛大眼睛那他就认为加10分那比如说呢这边都是大额头他也加10分那剩下的事情不一样那是不是就变成20分了所以对于人家进行比较的时候他是以这种相似度的情况让用户最终进行判断的这么一个情况来做的OK那接着就跟各位简单聊一下人脸搜索能做什么其实人脸搜索就已经可以接触到我们进行人脸登录的这么一个真相了我们可以在用户
[08:54] 用手机拍出一张照片跟资料库里面的用户照片进行对比那拿到最相似的一个看一下他返回的ID是多少以及他的评分如果评分大于80我们就认为是同一个人OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

