# 26.完善个人信息之编写实现以及整合前端测试

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\26.完善个人信息之编写实现以及整合前端测试_【海量资源尽在 666java.com】.mp4
- 时长 14分30秒（音频 871s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面呢我们来看一下完善个人信息那么在前面呢我们其实讲到过就是用户呢在第一次登录的时候呢就需要去要求用户来完善个人的信息那么我们首先来看一下它的Mock接口那么会涉及到两个接口那么一个接口呢是完善个人的信息那么这个里面呢会提交一些像性别呢昵称呢等一些这样的一些数据
[00:28] 第二个接口就是上传头像也就是上传图片这样的一个接口那么也就是说我们需要去开发两个接口好接下来我们来看一下那么我们需要在我们的SSO工程中我们来再添加一个Mapper那么就叫谁呢我们这个U2info这个Mapper好那么我来一丢这个U2info这样的一个Mapper
[00:54] 那么有了它之后呢就可以和我们数据库进行交互了那么接下来呢我们来看一下Ureinfo的Service啊那么这个里面呢会涉及到两个的方法那么一个呢就是去保存我们的用户的这样的一个信息的数据啊那么这个呢是用于一些数据的分装然后呢去保存数据库啊这个逻辑比较简单然后呢下面这个呢就是去保存我们的这个用户的一个头像的信息
[01:23] 首先是需要去做一些人像的一个校验这个前面我们已经写好这样的一个API了直接调用就可以了然后在这个位置是调用阿里云的OSS服务然后进行做一个图片的上传就可以了那么也是比较简单的好那么我们把这个也拷贝过来然后我们放到这个Service中
[01:50] 这个里面会报一些错误这个错误是工具检测的问题然后呢他还会报出什么呢在这个Url Service中缺少一个这个QueryUrl的这个方法那么这个方法呢我们在下面会有这个方法我看一下那么这个方法没有吗在下面这个里面有这个方法那我们把这个方法拿过来吧这个就是根据我们这个Token去做一个查询那么我们就放到
[02:20] 放到下面吧那么这个方法呢就是可以来简单的看一下啊就是根据我们这个token然后呢走着我们readies然后呢去做一个查询查询完之后如果如果不存在的话那么就return down那么如果要是存在的话那么我们就给他去刷新一下这个时间然后呢我们再去做一个反序列化啊就是这样的一个逻辑了
[02:48] 好那么接下来呢我们再回到UFO这个Service中就OK了啊那么当然了呃在这个里面需要大家注意一点就是无论是我们是保存用户的信息这个方法还是图片上传的这个方法啊那么我们都需要去检验用户的这个token啊是否是有效的那么也就是说那么除了我们去呃发送验证码
[03:15] 和登录啊不需要去进行校验token的话那么其他的逻辑呢都是需要去校验这个token的啊这一点大家一定要注意好那么接下来呢我们来看一下这个Controller那么Controller呢我们就需要去写一个叫做usinfo的Controller然后去调用啊这两个API那我们来看一下在这那我们把这个呢也拿过来啊放到我们的Controller中那么其实可以看到在这个里面呢我们已经写了啊有两个啊
[03:44] 一个是这个完善个人信息那么一个呢就是上传这个头像了OK好那么在我们的Controller中的实现呢这属于基本啊比较标准这样的一个实现但是在这个里面需要有一点注意啊就在这个位置那么前面其实我们说到我我们使用这个JWT的这个标准和规范的话
[04:06] 那么他是把这个token是放哪里呢放到我们这个投信息中的啊所以我们需要通过这个request handler去获取我们的这个投信息中的这个token那么才可以啊那么把这个token的在传递到我们刚刚所说的Service中然后呢在Service中呢去做一个校验哎ok好那么这个和下面他都是一样的好嘞好那么到这里呢我们的这个
[04:31] 完善个人信息呢这个就基本就搞定了啊那么下面呢我们就来打两个断点我们可以来测试一下好那么我们需要把我们这个服务呢重新去启动起来好那我们稍微等待一下好那么现在我们这个服务呢就跑起来了接下来呢我们来做一下测试那我们还是呢使用这个restclient去做一个测试啊这个是之前所测试的这样的一个这样的一个脚本那么我们来测试一下点击它走
[04:59] 那么会发现呢我们往下面走啊走走走到这儿就通过了错误了是吧发生错误了那么什么错误呢显然是我们这个token它已经失效了啊这样的一个错误那么我们可以经过这个里面吧打一个钝点啊来再来测一下走那么往下面去测试走会发现我们Ribbon始终是没有的啊返回fos那么到这儿就失败了好那么接下来呢我们就需要来去先
[05:29] 做一个短信验证码的一个发送然后呢我们再去登录一下那我们找到这个login吧那么就用它来去做测试走好那么我们来看一下短信验证码呢就发送成功了那么下面我们找一个我们的这个登录啊这个找一个登录我看一下验证码已经收到了那我们来找一个这个登录就是在
[05:59] 在这个位置校验这个位置那么我们的这个验证码是叫626056056然后我们点击这个发送那么登录成功了那么我们就需要把这个token拿到手然后把它作为我们的一个这个提交中的一个投信息网站一丢然后我们再去提交走然后通过下一步走
[06:28] 发现是不是就已经有了然后走其实我们可以通过这个U的中是不是已经就可以看到我们的一些信息了对吧ID和我们手机号然后往下面走然后我们做一个音色的操作走好那么现在我们就已经执行完成了那我们来看一下U的info中有没有数据呢发现是不是已经有一条这个数据对吧但是我们会发现的头像并没有数据因为我还没有提交这个头像
[06:58] 那么下面我们再来看一下这个头像的一个提交它其实是在下面的这个逻辑中啊叫做就是U的infocontroller中下面有一个就是上传头像这个逻辑啊那我们再来测试一下那么比如说我们还是找到之前的一个例子吧那么我们找一个这个上传头像这个例子啊在这OK然后呢
[07:25] 前面这个数据就不需要了因为后面多了一个hand然后呢我们这个这个要换成什么我们刚刚所拷贝的这个token需要它然后呢我们这个文件呢我们需要上传的时候呢要和我们这个位置的它一样然后呢我们去上传一个这个图片然后呢点击这个发送请求来了然后呢我们就直接往下面走吧通过吧
[07:56] 那么我们来等待一下看它是执行成功还是失败呢那么我们稍微等待一下可能它第一次这个执行呢会有一点慢那么OK到这里呢我们可以看到它的这个返回值呢不二的为true那就说明它已经上传成功了然后呢我们再去通过一下那么我回到数据库来看一下那么数据库中会发现这个我们这个logo这个位置呢它就已经有了数据了是不是就是我们这个图片这个数据啊
[08:25] 那我们可以尝试的来访问一下啊走哎会发现这个是不是就是我们所上传的这张图片呢对吧好那么到这里呢这个逻辑是不是就跑通了那么在我们的API这个位置跑通了那么接下来呢我们来整合到啊我们的这个这个就是我们的客户端来做一个测试了那我们把这个呃先给他呃关掉吧关掉我们重新再打开一下那我们打开这个应用啊打开这个碳花这个应用
[08:55] 然后呢我们从获取验证码开始然后我们去做一个这个测试啊那么我输入我的这样我们先把这个我们先把这个数据的全部都给他删除掉这个删除掉还有我把这两个的也全部都删除掉就相当于我现在呢是一个新用户来做一个注册比如说我就去输入我的这个手机号然后呢去
[09:22] 发送这个验证码我来等待他的一个发送哎已经收到了217800好那么我们开始去设置我们的这个信息这个呢就是性别啊男女比如说我设置为女然后呢这个就随便去呃写了啊然后呢叫什么呢黑码哎呃这个这个是不是会有点问题呢
[09:51] 输入会有点问题我就写黑马吧然后呢生日然后呢我就写这个8月1号然后呢这个居住城市呢就去写它然后呢我们点击这个设置头像啊那么要注意点击这个设置头像的时候它就会提交数据到我们的这个后台了我把这个断点都给它去掉好嘞它说是否允许我们的这个相机使用这个使用这个位置啊那么我来点击一下这个是允许
[10:20] 然后呢他呢会呃我看一下这个是一开始的一个设置吧然后呢点击下一步他是无法连接到相机是不是我们没有给他去设置相机呢呃来设置一下啊那么首先我们来看一下吧我们数据有没有保存进来啊呃用户数据是有了然后呢我们的UZinfo有没有呢呃是不是已经有了一条这个数据了那么接下来呢我们来看一下给他来设置一下呃这个照相机啊那我们先把这个拿出来
[10:47] 在相机这个位置那么我们给它打开一下然后呢这个都给它选择一下一个相机然后呢我们再点击这个设置
[11:01] 相机停止运行那可能是我需要把这个模拟器重新启动一下那我们稍微等待一下那么我这个模拟器就重新启动起来了那么重新启动起来之后呢我们还是需要给它去配置一下这个那么还是跟刚才的配置方法是一样的那么我接下来呢就还是把这VGT拿掉然后呢我先去打开这个相机这个应用来看一下那么会发现它已经能够去拍到照片了
[11:31] 这个呢就是已经漏点了啊然后呢我先返回一下然后呢我还是去打开我们这个碳花的这个应用然后重新我们来走一下这个流程那么我可能需要换个手机号了刚刚是不是已经注册了一个了对吧158这个啊然后呢我们点击获取然后呢我来等待这个验证码那么稍微等待一下它还没有发过来了
[12:01] 就是57575534好那么我重新做一个设置啊比如说这个就写个1吧然后呢生日那么我就随便去写了好那么然后呢居住城市那就随便写随便去写一个然后点击设置图像他呢就会去调用这个摄像机其实可以看到正在拍这个照片了那么现在呢我就来
[12:29] 拍一张随便我来找一个东西去拍一下吧比如说我的手机我拿着我的手机再拍一个照片就像拍一个手好拍一个照片然后呢然后在这个位置呢我再来去做一个提交看它会怎么样我们来看一下它会有一个这样的一个扫描的这样的一个动画的一个效果然后呢后台呢会做一个图片的一个上传以及这个校验
[13:02] 那我们看他的结果会怎么样啊那么我们稍微等待一下他说你看图片是不是非人像然后呢请重新上传那我们点击啊重新上传那我就呃自拍一张吧那么哎我点击这个设置头像然后呢我来自拍一张那么走好那么自拍一张之后呢我们就呃那么我们就点击这个确定然后呢去上传这个照片
[13:34] 好那么其实可以看到他正在做扫描了正在做扫描了那我们来稍微等待一下那么看他审核的结果是一个什么样的结果OK发现他是不是已经审核成功了那么审核成功了就代表着我们这个图片是一个人像的图片然后点击这个开始交友好嘞好那么这样的话呢我们就已经完成了一个登录的这样的一个流程对不对好那么其实可以看到在这个我们刚刚写的这个波仔1
[14:04] 那么这个就是刚刚我们所上传这个图片啊那我们来打开看一下啊好那么这个是不是刚才我所上传的这张图片啊哎好嘞好那么到这里呢我们是不是就已经完成了我们这个呃功能的这个开发呀就是我们实现个人信息啊完善个人信息这样的一个功能的开发ok好那么关于啊这个呢就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现完善用户个人信息功能，包括前端接口定义、后端服务层代码编写、数据库操作及接口测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中“4.3. 实现完善个人信息”章节，包含 mock 接口地址 https://mock.boxuegu.com/project/164/interface/api/28553，用于定义完善个人信息的请求参数（Headers: Content-Type: application/json，Body: gender, nickname, birthday, city）。
画面2：展示 UserInfoService.java 代码，定义了 saveUserInfo 方法，注入了 UserInfoMapper、UserService、FaceEngineService、PicUploadService。
画面3：在 UserInfoService.java 中，展示 saveUserInfo 方法的逻辑，通过 token 查询用户，若用户为空则返回 false，否则创建 UserInfo 对象并设置属性。
画面4：展示 UserInfoController.java 代码，定义了 saveUserInfo 接口，接收 param 和 token 参数，调用 userInfoService.saveUserInfo。
画面5：展示 UserInfoController.java 的完整代码，包含注解 @RestController、@RequestMapping、@Autowired、@PostMapping 等。
画面6：在 Advanced REST Client 中，设置 POST 请求地址为 http://172.16.55.153:18080/user/loginRegInfo，设置 Authorization 头，Body 为 JSON 格式数据：{"gender": "man", "nickname": "张三", "birthday": "2000-01-01", "city": "北京"}。
画面7：展示 UserInfoService.java 中 saveUserInfo 方法的完整代码，包括设置用户信息、插入数据库、返回 true。
画面8：在 Advanced REST Client 中，展示历史请求记录，包含多个 POST 请求，如 /user/loginRegInfo、/user/login、/picupload 等。
画面9：展示 UserInfoController.java 中 saveLogo 方法的代码，用于处理头像上传，调用 userInfoService.saveLogo，异常时返回错误信息。
画面10：展示 Genymotion 模拟器中手机登录注册页面，用户输入手机号并点击“获取验证码”。
画面11：在 Navicat Premium 中，展示 tb_user 表的数据，包含 password、created、updated 字段。
画面12：展示 Genymotion 模拟器中手机登录注册页面，用户输入手机号并点击“获取验证码”。
画面13：展示 Genymotion 模拟器中手机登录注册页面，用户点击“获取验证码”按钮。
画面14：展示 Typora 文档中“4.3.1. UserInfoMapper”和“4.3.2. UserInfoService”章节，UserInfoMapper 接口定义了插入用户信息的方法，UserInfoService 包含 import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
import org.springframework.web.multipart.MultipartFile;
import java.util.Map;
@Service
public class UserInfoService {
    private static final Logger LOGGER = LoggerFactory.getLogger(UserInfoService.class);
    @Autowired
    private UserInfoMapper userInfoMapper;
    @Autowired
    private UserService userService;
    @Autowired
    private FaceEngineService faceEngineService;
    @Autowired
    private PicUploadService picUploadService;
    // 完善个人信息
    @Return
    public Boolean saveUserInfo(Map<String, String> param, String token) {
        User user = this.userService.queryUserByToken(token);
        if (user == null) {
            return false;
        }
        UserInfo userInfo = new UserInfo();
        userInfo.setUserId(user.getId());
        userInfo.setSex(StringUtils.equals(param.get("gender"), "man") ? SexEnum.MAN : SexEnum.WOMAN);
        userInfo.setNickname(param.get("nickname"));
        userInfo.setBirthday(param.get("birthday"));
        userInfo.setCity(param.get("city"));
        // 保存UserInfo数据到数据库
        this.userInfoMapper.insert(userInfo);
        return true;
    }
```

画面4：
```java
package com.tanhua.sso.Controller;
import ...
@RestController
@RequestMapping("user")
public class UserInfoController {
    @Autowired
    private UserInfoService userInfoService;
    /*
     * 完善个人信息
     * @param param
     * @param token
     * @return
     */
    @PostMapping("/loginRegInfo")
    public ResponseEntity<Object> saveUserInfo(@RequestBody Map<String, String> param, @RequestHeader("Authorization") String token) {
        Boolean saveUserInfo = this.userInfoService.saveUserInfo(param, token);
        return ResponseEntity.ok(saveUserInfo);
    }
```

画面7：
```java
UserInfo userInfo = new UserInfo();
userInfo.setUserId(user.getId());
userInfo.setSex(StringUtils.equals(param.get("gender"), "man") ? SexEnum.MAN : SexEnum.WOMAN);
userInfo.setNickname(param.get("nickname"));
userInfo.setBirthday(param.get("birthday"));
userInfo.setCity(param.get("city"));
// 保存UserInfo数据到数据库
this.userInfoMapper.insert(userInfo);
return true;
```

画面9：
```java
try {
    Boolean bool = this.userInfoService.saveLogo(file, token);
    if (bool) {
        return ResponseEntity.ok(null);
    }
} catch (Exception e) {
    e.printStackTrace();
    ErrorResult errorResult = ErrorResult.builder().errorCode("000000").errMessage("图片非人像，请重新上传").build();
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(errorResult);
}
```

画面14：
```java
package com.tanhua.sso.Mapper;
import com.baomidou.mybatisplus.core.Mapper.BaseMapper;
import com.tanhua.sso.pojo.UserInfo;
public interface UserInfoMapper extends BaseMapper<UserInfo> {
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

