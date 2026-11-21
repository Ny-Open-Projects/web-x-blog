# 04-DataURL：实现员工头像保存

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\04-DataURL：实现员工头像保存_【海量资源尽在 ubkz.com】.mp4
- 时长 16分42秒（音频 1002s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了那我们现在已经把这个Data UIL呢咱们都已经搞定了那接下来呢我们要完成的其实就是可以借助Data UIL这种形式来实现我们用户头像的一个上传工作那我们要做这个基于Data UIL实现用户头像上传那我们应该怎么做呢OK我们来分析一下我们要的一个实现步骤是这样的对于我们而言首先呢在这个页面
[00:32] 能够把一张图片是不是传入到我们的服务端没错吧那传入到服务端之后那我们通过服务端把这张图片它的字节信息是不是要经过base64的一个编码处理那经过编码处理之后得到一个字幕串那这个字幕串是不是就代表的是你上传的这个图片那既然是一个字幕串的话那我们可不可以把这张图片信息直接存到数据库里呢
[00:59] 那存到数据库之后那又意味着数据库里面直接就有图片了那我们什么时候想用是不是什么时候直接从数据库里面把这个字段的数据查询出来然后在页面显示是不是就可以了那这样一来我们就不需要额外的把图片存到我们的服务的磁盘当中了没错吧好了那这个我们做过了一个分析那接着就是说我们如何实现它首先前端的这边我们要实现一个用户上传的这么一个功能
[01:30] 那这个功能呢我们之前就说过了前端不是我们的重点这个页面也给各位提供好了那我们一会再说首先第一件事我们的前端要进行改造那前端改造好了之后接下来我们要做的第二件事就是说呢你需要上传图片要放到后端那我们需要在后端去写这么一个Controller方法那Controller方法呢我个人习惯处理图片呢我不太在不太习惯在Controller里面直接写
[01:57] 我直接把它设置在survey当中那在survey当中我们要做的事情其实就是把图片进行base64的一个编码处理接着是把这张图片信息保存到用户对象或者用户的某一个字段当中即可OK那我们这个流程做了一个分析那接下来我们可以把这个功能给它实现首先我们说过了对于这个图片的头像信息我们要把它保存到数据库里面那所以呢我们来
[02:28] 对我们的用户实体类先做一个改造好了我们的用户实体类找到System找到User在User这边我要去添加一个属性好了这个属性没有的话添加一个Private死菌类型的staffoto
[02:59] OK这个其实代表的就是用户的头像了好了注意这个用户头像我给它放到了我们的用户对象当中当然了随之的我们也需要对数据库表进行一个更改好了这边呢我打开我的伺候样的打开数据库OK找到我们的HRM找到base user用户表在用户表这边我也添加了一个字段代表的是用户的这么一个头像
[03:28] OK都能对应上OK那我们现在把实体类改造成功了之后接下来我们需要简单的改造一下我们的页面好了这边我的页面其实也已经启动起来了我们可以登录进去简单的来看一下员工好了随便找一个比如说我就以ZBZ或者AG123举例个人详情这边我们需要实现用户上传的这么一个功能要想实现它怎么做
[03:59] 在今天给各位提供的这个资料当中资源有一个前端工具代码直接把这个代码Ctrl Ccopy到我们这边对应的位置即可好了我们要放到eplore工程下components这个里面好了右键资源管理器打开好了call到里面即可OK替换好了这样一来呢我前端的这些基本工作呢我都已经准备好了
[04:32] OK刷新项页面其实已经能够进来了没问题好了这边我们的前端工程做成什么样子咱们可以看一下这边员工照片我可以点击来上传一张各位打开F12我们看一下能不能发送一个请求好了随便来一张给我来看确确实实能够发送这么一个请求只不过它发送的请求SysUserUpload后面传递的其实是当前用户它的一个ID
[05:02] OK那这样一来呢我们前端的代码其实也已经搞定了那前端的我们搞定了接下来我们重点关注的其实就是后端代码的一个实现那在后端代码呢我们可以打开注意这个代码我要写到什么地方我就写到因为是对用户操作嘛所以我再写到系统微服当中找到用户controlleruser Controller找到用户Controller
[05:30] 在里面添加相应的代码即可好了我要写到什么地方呢我就写到最上边吧最上边OK好了写意方法Public那当然了我们是Result类型反为止ResultOK就叫Upload那对于一个文件上传来说呢其实我们主要要做的或者我们重点关注的就是说你前端进行一个图片的一个上传再来一下
[06:04] 那你会给我发送很多的内容主要看发送请求的接口sys user upload那后面接了一个参数这个参数是我们的用户ID那接下来呢是不是以流信息的形式把你传的这个图片给我传递到后端没错吧那接下来我们重点关注的是这个方法当中必然有参数以及他请求的路径那么请求路径呢request mapping先给他补充起来好了那接下来里面关注的就是我们的路径部分
[06:35] 好了user应该是user吧sysuser好了user upload没问题user upload没问题因为这个附录性已经写到上边了那好了接下来后面我们关注的是不是要传递一个ID过来我们是以get的形式传递过来的好了那接下来upload过来之后呢注意这里面我们的方法需要参数at pass variable死菌类型的ID那接下来
[07:09] at requestrequest就叫param了name等于fail好了这个name为什么要等于fail是这样的这个fail是你前端传递的这个文件的一个我们叫做名称在这儿各位来看你传递的这个名称在这儿传递的name名称是不是等于fail所以这个千万要写对要写对指的是你要传递一个文件这个文件的名称叫fail
[07:39] 当然了对于Spring来说我们这边可以是使用Multipart Fill来进行接收即可好了这样一来我们在这边Controller端的方法已经定义出来了接下来我们这个方法里面重点关注的事情其实就比较简单了首先第一件事我个人习惯我们要对这个文件进行处理那处理的逻辑全部留在思维当中去写我在这边直接调用即可所以我要做的第一件事
[08:07] 调用SERVICE保存图片那保存好了之后接下来呢我们直接返回数据即可那接下来我想跟各位说的是你保存图片归保存图片但是你需要把这个图片信息或者这个图片的请求路径你的请求地址要给我返回过来为啥要这样做是这样的就是说在我页面部分如果我上传成功之后
[08:36] 我还需要是不是一个回显那我们在前端页面回显的是不是就是你保存之后的路径没错吧各位所以对于我们来说保存图片之后要获取到图片的访问地址当然这个访问地址其实就是我们的一个Data URL或者是我们的一个HTTP地址没错吧好了接下来我们把代码给它补充完整通过User Service打点
[09:06] 我叫uploaduploadupload写意方法upload image那这upload image当中我接收两个参数第一个参数string类型的ID那各位这个ID是不是就应该是当前你完善图片它的user IDOK那第二个其实就是我们的fill那这样一来我们保存成功了之后得到的其实就是我们的一个请求UILOK那接下来我们构造返回结果即可
[09:39] return new一个resultresult code success代表成功OK那接下来把数据部分换成image URL即可OK那这样一来那这样一来我现在的图片其实已经在Controller层处理好了那只不过呢我Service层呢也需要添加这么一个方法所以在这边user Service里面添加对应的一个方法完成图片处理好了用户ID用户上传的
[10:13] 头像信息头像对文件OK那我们需要返回一个请求路径那好了接下来我们来看一下对于这个方法当中我们应该如何去做那么要做的事情呢其实比较简单如果说你这个文件上传成功了那上传成功是不是要对这个UIL地址进行一个修改对这个用户的头像信息别忘了我们这边用户加了一个字段
[10:43] 那这个字段代表是他的请求路径那这个请求路径我们是不是要把它进行一个更新啊没错吧所以对于我们而言要做的事情由于要更新用户所以第一步根据ID查询用户用户先准备好那接下来第二件事我们现在是使用DataURL的形式存储图片所以我们想方设法的对图片
[11:15] BAT输组进行叫做BASE64编码这是我们要做的第二件事编码之后其实得到的就是一个字幕串拿到了字幕串接下来第三件事这个字幕串注意它其实代表的就是你的请求UIL路径别忘了Data UL其实也是一个UIL所以我们要做的事情接着就是更新用户头像请求地址请求路径好了接下来第四件事并返回就可以了
[11:49] 好了接着我们一个一个的把代码补充完整首先我们的第一件事根据ID查询根据ID查询比较简单user.do打点我们user.do都有了find by ID把ID拿过来打点get这样一来我们得到了用户对象
[12:14] 好了用户对象已经得到了之后接下来呢我们想方设法的对Data UIL的数据进行一个处理那这个怎么处理呢很简单很简单我们可以借助一个工具类叫做base64注意啊这个base64呢各位别选错包有很多有很多我来找一下点EncodeOK各位来看Encode的时候实时接收的就是一个Beta数组
[12:48] 那我们现在要对图片信息里面的byte数组进行Base64处理那图片信息Multiple的fail里面可以通过打点get bytes这种形式得到byte数组当然了这边byte数组呢可能有一个异常我们处理一下那接下来我想跟各位说的是这样一来你得到的其实可以理解为是我们一个byte字幕串的后半部分Data UIO的后半部分
[13:16] 也就是说你前面这个图片你最终要展示的究竟是什么形式是不是一个Data UI还没有所以我们需要加一个前缀OK这边需要一个逗号需要一个逗号所以把这个前缀全部都补充完整之后我们其实就可以理解为它是一个Data UI了当然了我们一会儿可以把它进行一个打印看一下效果好了这样一来我们Data UI的形式图片咱们已经搞定了接下来就是更新头像
[13:53] 那user打点set好了那这个其实代表的就是我们的头像的一个请求路径虽然是data ul形式接着最后returnencodeok那这样一来我这个代码呢其实也已经写好了那写好了之后我重新启动一下我这个系统v服务我们一起来看一下是否能够把这个数据给我更新出来好了这边control了有一个问题啊这边pulltree异常没解决ok
[14:25] 没问题了接着重新启动重新启动OK服务呢已经启动成功了我们打开浏览器一起上传一个看一下效果当然了我这边呢先刷新一下我的数据这个先把它设置为空吧OK
[14:59] 好了我们可以随便的选择一张图片一起来看一下是否能够完成上传好了在这边的员工照片选择一张在今天第九天资料当中给各位来了一个001002任意选择一张即可打开好了这边打开了之后抱歉我把这个再删掉咱们再来一下看一下我们的请求与响应了001走各位发现请求成功并且也有响应的这个内容
[15:27] 那接着我们来看一下数据库是否有数据呢来刷新一下嗯数据库现在没有啊那我看一下我们的后台那各位来看其实后台呢也已经把这个图片呢给我们展示出来的没错吧那我们检查一下代码就是Service代码检进去看哦没错是这样的就是说呢在目前为止呢我这边只是把这个数据给它填写了但是没有完成更新没错吧所以U2DU打点see you
[15:58] OK把这个user更新进去好了接着我再去重启一下服务器这个就是代码写的稍微有点快出现一点点简单的问题好了这边再去重启我们耐心等待一下好了现在已经启动成功了接下来我们再去对这个用户进行一个头像的更新操作找到个人详情打开选择一张图片比如说我就用001走好了各位这回成功了来看一下数据库刷新一把
[16:31] 你会发现数据库当中具有了这么一条哎头像的一条信息OK那这样一来我整个头像的这个处理其实就已经成功了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 人事管理系统中，通过 Data URL 方式实现用户头像上传，并展示前后端代码实现过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程目录，当前选中“1.3 Data URL实现用户头像上传”，说明本节内容。
画面 2: 在 IntelliJ IDEA 中查看 User.java 类，展示用户实体类中包含的字段，如 username、mobile、deptId 等。
画面 3: 在浏览器地址栏中输入 localhost:8080，准备访问系统。
画面 4: 在文件资源管理器中，展示项目目录结构，选中 components 文件夹下的 imgUpload.Vue 文件。
画面 5: 在 IntelliJ IDEA 中，右键点击 User.java 文件，弹出菜单，准备进行操作。
画面 6: 在浏览器中打开 iHRM 系统的员工详情页，显示“请上传图片”提示。
画面 7: 在 IntelliJ IDEA 中，查看 UserController.java 文件，展示 @RequestMapping("/user/upload/{id}") 方法。
画面 8: 在 IntelliJ IDEA 中，为 UserController.java 文件添加 import 导入语句，准备使用 HttpServletResponse。
画面 9: 在 IntelliJ IDEA 中，查看 UserService.java 文件，展示 uploadImage 方法的实现，其中包含 userDao.findById(id).get()。
画面 10: 在 IntelliJ IDEA 中，展示多个窗口的分屏视图，包括项目结构、代码编辑器、数据库工具等。
画面 11: 在 IntelliJ IDEA 中，查看 UserController.java 文件，展示 upload 方法的实现，其中调用 userService.uploadImage。
画面 12: 在浏览器的开发者工具中，查看上传图片的响应，显示图片数据已成功返回。
画面 13: 在 IntelliJ IDEA 中，查看 UserService.java 文件，展示 uploadImage 方法的实现，其中包含 Hibernate SQL 语句。
画面 14: 在浏览器中，显示员工详情页，用户头像已成功上传并显示。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
private Integer inServiceStatus;
private String departmentName;
//level
String
saasAdmin, saas管理员所有权限
coadmin, 企业管理员（建建客户企业的时候添加）
user, 普通用户（需要添加）
private String level;
public User(Object [] values) {
//用户状态 1.在职 2.离职
this.username = values[1].toString();
this.mobile = values[2].toString();
this.workNumber = new DecimalFormat(pattern="#").format(values[3]);
this.timeEntry = (Date) values[6]; //部门编码
this.departmentId = values[6].toString(); //部门编码
}
```

画面 7:
```java
@RequestMapping(value="/sys")
public class UserController extends BaseController {
@Autowired
private UserService userService;
@Autowired
private PermissionService permissionService;
@Autowired
private JwtUtils jwtUtils;
@Autowired
private DepartmentFeignClient departmentFeignClient;
@RequestMapping("/user/upload/{id}")
public Result upload(@PathVariable String id, @RequestParam(name="file") {
}
```

画面 8:
```java
import org.springframework.http.HttpServletResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.multipart.commons.CommonsMultipartResolver;
import org.springframework.web.servlet.mvc.method.annotation.MvcUriComponentsBuilder;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;
import org.springframework.web.servlet.view.JstlView;
import org.springframework.web.servlet.view.RedirectView;
import org.springframework.web.servlet.view.UrlBasedViewResolver;

