# 19-刷脸登录：人脸登录

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day11-刷脸登录
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day11-刷脸登录\19-刷脸登录：人脸登录_【海量资源尽在 ubkz.com】.mp4
- 时长 16分19秒（音频 979s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那人脸检测这个功能我们也已经实现了那接下来呢就是我们刷脸登录最重要的一个接口也就是最后一个接口哎我们可以借助人脸进行登录那这个人脸登录它的一个调用逻辑是什么样子呢就是说在我的落地页也就是说用户扫描之后打开了一个页面这个页面先去对你拍摄的一张照片进行面部的一个识别如果面部识别成功也就是刚才我们说了如果返回成功
[00:31] 那返回成功的话他立马把这张图片传递过来帮助我们进行一个叫做人脸的一个搜索找到他评分最高的这么一个人如果评分是80分以上咱们就认为是同一个人并且获取到我们存储到百度那边的用户ID用户信息接着让他进行一个自动登录的这么一个功能其实就可以了所以接下来我们关注的是login by face这个接口
[01:00] 那对于这个接口而言我们写的代码逻辑呢其实也是比较简单你会发现control的代码并不难我们把所有都放到survey当中了那么这个代码应该如何去写呢是这样的那我呢已经在survey这边呢预留好了一个接口那这个接口各位就叫做login by face那login by face的时候你需要把你得到的code唯一标志传给我那还需要把一个文件传给我因为这个人脸登录其实还是要用到这个文件嘛那
[01:30] 接下来我们要做的事情就是说当登录成功之后返回一个死菌类型的返回值那这个返回值它代表的什么代表的就是登录成功之后返回的叫做用户ID也就是user ID那如果说你登录失败那这个user ID就是None所以对于我们来说如何判断在Controller判断是登录成功了还是登录失败了我们可以直接调用方法
[02:02] 得到返回值判断一下是否为空即可所以在我的Controller能从代码的一个编写就比较简单了首先我这边需要一个方法这个方法两个参数两个参数一个是我们的唯一标志我们回到这张图形我们都知道在落地页用户扫描之后的这个页面你要想进行一个人脸的登录那我们同样也能拿到这个code这个编码
[02:28] 那拿到code之后我们可以通过这个code去操作我们的redis如果登录成功代表的是这个二维码它登录成功了如果登录失败代表是登录失败了吧为啥要这么设计是因为我前面还有轮巡是不是也要操作这个redis呀所以对于我们而言code必不可少那还有第二个参数代表的是我们拍摄的那张照片所以在这边两个参数和各位交代清楚了那接下来我们关注的就是这个方法打点调用login by face
[02:57] 那第一个参数code好了那第二个参数就是我们这个文件OK那这样一来我们得到的其实代表的是user id好了人脸登录获取用户id那这个用户id呢如果不为空不为难代表登录成功所以在我这边需要做一个简单的判断if好了user id
[03:37] 不等于None当它不等于None的时候代表着就是我们登录成功了好了那接下来这边就是代表登录失败了好了登录成功如何表示也简单直接success即可好了登录失败好了直接fail即可OK那这样一来我Controller层写好了那我简单的说一下我为什么返回的时候以一个成功或者一个简单的失败就可以了呢其实这张图形已经说的很明白了对于我们
[04:07] 落地也就是手机扫描之后的这个页面你登录成功了告诉你扫码成功OK那如果失败了告诉你登录失败重新扫描是不是就可以了如果成功我们随之发生变化的是不是就是用户登录的这个用户登录这个用户的这个登录页面啊所以在这边扫描这边我们做的相对简单来些简单一些其实就可以了OK那我Controller代码写好了关注的就变成了Service那接下来我想说的是这个Service代码
[04:35] 我们应该如何进行编写好了我这个survey代码当中呢要做的事情呢相对来说有这么一点点麻烦我们要做的事情呢有如下这么几件事首先呢第一件事我们应该调用百度云AI查询当前对比的用户的用户就是扫描的这个用户了那这个如何去做呢很简单
[05:06] 我们之前也写过一些基本的一些代码其实总之就是调用我们搞好的百度云AI Utils找到里面的FaceShirt其实就是一个根据一张图像从人甲的人脸库里面查询的这么一个逻辑查询的时候找到面部最相似或者最相近的一个数据给我们返回回来返回回来的时候这边有它的评分我们之前说过大于80分代表就是当前用户了
[05:35] 那我们可以简单的来看一下这个是我们自己想要的工具类这个工具类里面如果大于80才返回当前这个用户的ID如果没有返回或者如果出错了是不是就是None啊所以对于我们这边Service而言调用的内容也不难可以通过百度云AI进行调用那我们调用好了之后接下来第二件事要做什么那第二件事我们要做的事情就是说让它进行一个自动
[06:03] 登录因为对于我们而言目前目前有很多的内容因为对于我们这个系统来说呢它有一个叫做token的一个设置对于这么一个token的一个设置那我们现在不管是我们基于JWT的认证还是基于share的认证都必须要有token没错吧那所以我们也需要把这个token获取到那这个token应该如何去做呢其实就是模拟一个自动登录即可
[06:32] 因为咱们登录之后是不是可以生成token的这么一个字符串OK生成了token字符串之后接着第三件事我们要做的别忘了回到这张图形当我们用户成功登录之后我们需要把状态设置给readies如果登录成功的时候除了有状态之外是不是还应该有用户ID是不是还有我们刚才生成的token是不是都要放到ready当中所以接下来第三件事就是修改二维码
[07:03] 为马的我们叫做状态所以对于我们来说一共三件事我们一个一个来完成首先第一件事调用百度云AI查询用户那这个比较简单百度我们写好一个工具类打点其中有一个抱歉手有小血其中呢有一个我们的方法有啊百度云AI现在没有注入进来是吧atautowareprivate百度云AI
[07:40] 好了接下来我们底下就可以百度云AI Utils打点调用里面的方法我们有一个方法叫做Face Search进行查找我进行查询的时候各位来看只需要给我一个IMG一个image图片就可以了所以对于这个图片来说我们全部都是使用base64的形式所以在这边我需要把你上传的文件进行一个格式的转化这个格式转化比较简单咱们也写过很多次了
[08:10] 直接写到中间了base64 utils打点encode好了接着文件打点get bytes那这样一来我们就能得到用户IDuseruserID那接下来我们要完成的事情呢就是让它去进行一个自动登录的这么一个过程好了if当然我们要做一判断userID不等于那必须不为空才行OK
[08:41] 好了那接下来如果不为空的话让它自行自动登录那这个不为空我里面应该如何去写如何让它自动登录其实很简单我们可以自己模拟一个注意自己模拟一个我们的登录过程即可那我们现在使用的登录这套逻辑呢需要各位来简单的看一下user Controller那我们现在这个登录的这个逻辑我稍微快一点找一下我们这个登录的逻辑
[09:13] login那我们现在这个登录逻辑是不是通过用户名密码接着借助share的那一套来做所以对于我们而言模拟share的这一套让他自己去执行或者让他跑一下就可以了我们之所以要模拟这一套逻辑是因为我们要把一些登录信息是不是绑定到我们的readies当中没错只有走过这一套逻辑只有经过了real只有经过了share是不是他才自动的把这个数据放到我们的readies当中
[09:42] 所以对于我们来说就是让他自己登录即可那我们自己登录如何去做也不难首先咱们自己登录的时候需要用户名密码那这边我就需要进行一个user的一个查询工作那user查询如何去做查询用户对象OK那查询好了这个咱们先把步骤写好了那查询好了用户对象之后那接下来呢我们需要获取叫做subject那获取了subject之后调用login
[10:17] 方法登录即可那接着登录成功了之后我们可以获取token因为这个token呢现在是基于share的一个认证那我们这边这个token呢其实就是我们的session id当然了如果你是用jwt那种方式你直接生成一个jwt串其实是不是就可以了ok当然了我们现在是基于share所以我就用share这种方式来做那接着查询那查询用户对象需要private注入进来我们的user当然了
[10:47] 不管是user.do或者user.Service其实都可以我就user.do了好那接下来呢我们这边开始经查询useruser等于user.do打点find by iduser id传进去打点get这样一来我们得到用户对象那得到用户对象底下呢也需要做一个简单的判断if user不等于 not
[11:17] 因为有可能你根据这个ID没查询出这个user那只有当它不等于none的时候我们再去执行里面的这个自动登录的这个过程好了获取subject这个也比较简单subjectsubject等于这个代码希望各位还有印象就是securitys e r s e c u没错security打点get subject那得到subject的这个对象好了这边呢这个范围这个
[11:51] 包啊刚才引错了subjectoksubject再重新引下包没问题了好了那获取subject之后调用subject里面的方法点login方法进行登录那我们在login的时候呢中间需要传递的是不是一个叫做token啊所以我们这边new一个user name and password token
[12:21] 那不管是用户名还是密码其实全部都已经存到了我们这个user对象里所以这边user打点get mobile构造用户名user打点get password构造密码那这样一来就是进行登录当我登录成功之后能够获取
[12:38] 我们的session那这个session id如何去做也不难可以借助subject这些代码我们之前都写过subject打点get session打点get idok那这样一来我们这个id或者我们的token也已经准备好了好了到目前为止呢我们自动登录的这个逻辑呢其实也写好剩下的之后我们就是要修改二维码状态那修改二维码状态呢其实也不难
[13:05] 咱们就是借助Reddit Timelake里面的方法打点ops for value打点我们这边进行一个set即可那我们这个key中间要接收一个key我们就可以get catch key把code传递进去得到一个keyget catch keycode没问题那接着我们开始进行抱歉不是ops for value我们这边应该是点bound
[13:33] bound value ops没错应该是他好了那接下来呢我们开始往里设置值那设置值的时候由于我这个值呢这里面的代码判断太多了只有当登录的时候里面可能给他构造一些基本的数据所以呢我把先给他设置一个最先给他设置一个初始值吧face logging result等于new一个face logging result那我现在在里面先给他设置一个0那这个0咱们之前说过了0是不是代表的是叫做登录
[14:04] 失败啊登录失败所以当我们先给它一个初始值登录失败往里面进行设置往里面进行设置当我登录成功的时候我接着对它进行一个扩展其实就可以了所以在这边如果登录成功result等于new一个result重新给它付一个值哎即可拿过来那我们现在付的这个值呢代表一登录成功那接下来呢我们还需要token
[14:37] 那这个token呢就是我们得到的这个token值OK那除了token之外还有第三个就是user idOK上面这个要转型死均的话做一个处理OK那这样以来各位来看我这边直接借助里面的构造方法把state把token把user id全部都复好了那接下来我们这边关注的就是说当我登录成功的时候我改成登录成功的状态复制上了token复制上了user id那当我
[15:14] 登录失败是不是就给他来一个0是不是就可以了当然这些我们都处理好了之后我们可以将好了当然都处理好了之后我们可以将这些这个状态呢其实给他放到redis里面即可当然有的朋友说放到redis里面呢你没有设置实像那这个实像我们也给他进行一个设置其实就可以了OK好了这个逻辑和我们刚才初始化一个二维码的时候配置的是一模一样
[15:42] 那接下来呢还有最后一项就是一个返回值我们直接把user id返回a就可以了那这样一来我登录的这个逻辑其实也已经写好那接着我们简单的来说一下就是人脸登录那对于人脸登录来说呢你需要把一个code传递给我并且需要把这个拍摄一张图片传递给我如果全部都满足的话我会返回给你一个成功或者失败那成功或者失败
[16:10] 如果一旦成功我是不是已经将Redis里面的结果进行了一个更新啊OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示基于百度AI人脸识别的登录系统核心代码实现，包括控制器、服务层逻辑及Redis缓存与Shiro权限管理的集成。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：桌面启动画面，显示“黑马程序员”和“博学谷”标志。
画面2：展示`FaceLoginController.java`中`checkQRCode`和`loginByFace`方法，用于处理二维码登录和人脸登录请求。
画面3：继续展示`loginByFace`方法，处理登录成功后返回用户ID。
画面4：展示`BaiduAUIUtil.java`中的`faceCheck`和`faceSearch`方法，用于人脸检测和人脸搜索。
画面5：展示`FaceLoginService.java`中`@Value`和`@Autowired`注解配置，以及Spring Boot自动配置类。
画面6：展示`FaceLoginService.java`中`if`语句的代码补全提示。
画面7：展示项目结构目录，包含`src/main/java`和`src/main/resources`，并展示`UserController.java`中的用户更新和删除方法。
画面8：展示`FaceLoginService.java`中`getQRCode`方法，用于生成二维码并存入Redis。
画面9：展示`FaceLoginService.java`中`checkQRCode`方法，用于检查二维码状态。
画面10：展示`FaceLoginService.java`中`loginByFace`方法，用于处理人脸登录逻辑。
画面11：展示`FaceLoginService.java`中`loginByFace`方法，使用`SecurityUtils`进行用户登录。
画面12：展示`FaceLoginService.java`中`loginByFace`方法，创建`FaceLoginResult`对象并设置状态。
画面13：展示`FaceLoginService.java`中`loginByFace`方法，设置Redis缓存并返回结果。
画面14：展示`FaceLoginController.java`中`checkQRCode`和`loginByFace`方法，用于处理登录请求。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
@RequestMapping(value = "/qrCode/{code}", method = RequestMethod.GET)
public Result checkQRCode(@PathVariable(name = "code") String code) throws Exception {
    FaceLoginResult checkQRCode = faceloginService.checkQRCode(code);
    return new Result(ResultCode.SUCCESS, checkQRCode);
}

/**
 * 人脸登录，根据传入的图片用百度AI进行人脸比对
 * 根据比对的图片用百度云AI进行查找
 */
@RequestMapping(value = "/{code}", method = RequestMethod.POST)
public Result loginByFace(@PathVariable(name = "code") String code, @RequestParam(name = "file") MultipartFile attachment) throws Exception {
    return null;
}

/**
 * 图像检测，判断图片中是否含有面部
 */
@RequestMapping(value = "/checkFace", method = RequestMethod.POST)
public Result checkFace(@RequestParam(name = "file") MultipartFile attachment) throws Exception {
    String image = Base64Util.encode(attachment.getBytes());
    Boolean aBoolean = baiduUtil.faceCheck(image);
    if (aBoolean) {
        return new Result(ResultCode.SUCCESS);
    }else{
        return new Result(ResultCode.FAIl);
    }
}
```

画面4：
```java
public Boolean faceCheck(String image) {
    JSONObject res = client.detect(image, IMAGE_TYPE, options);
    if (res.has(key) && res.getInt(key) == 0) {
        Integer faceNum = resultObject.getInt("face_num");//检测的人脸数量
        return faceNum == 1 ? true : false;
    }else{
        return false;
    }
}

/**
 * 人脸搜索，查找人脸库中相似的人并返回数据
 * 这里，用户的匹配度（score）大于80，即认为是同一个用户
 */
public String faceSearch(String image) {
    JSONObject res = client.search(image, IMAGE_TYPE, groupid, options);
    if (res.has(key) && res.getInt(key) == 0) {
        JSONArray userList = result.getJSONArray(key);
        if (userList.length() > 0) {
            JSONObject user = userList.getJSONObject(index: 0);
            double score = user.getDouble(key: "score");
            if (score > 80) {
                return user.getString(key: "user_id");
            }
        }
    }
}
```

画面5：
```java
@Value("${qr-url}")
private String url;

@Autowired
private IdWorker idWorker;

@Autowired
private QCodeUtil qCodeUtil;

// AutoWired (org.springframework.beans.factory.annotation)
// Auto (com.netflix.discovery.converters)
// Value (org.springframework.beans.factory.annotation)
// Component (org.springframework.stereotype)
// Service (org.springframework.stereotype)
// ExcelAttribute (com.ihm.domain.objects)
// RequestMapping (org.springframework.web.bind.annotation)
// Query (org.springframework.data.jpa.repository)
// PathVariable (org.springframework.web.bind.annotation)
// FeignClient (org.springframework.cloud.openfeign)
// EnableDiscoveryClient (org.springframework.cloud.netflix.Eureka)
// EnableEurekaClient (org.springframework.cloud.netflix.Eureka)
// Get (org.springframework.web.bind.annotation)
// Setter (org.springframework.beans.factory.annotation)
// Getter (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal (org.springframework.beans.factory.annotation)
// Internal

