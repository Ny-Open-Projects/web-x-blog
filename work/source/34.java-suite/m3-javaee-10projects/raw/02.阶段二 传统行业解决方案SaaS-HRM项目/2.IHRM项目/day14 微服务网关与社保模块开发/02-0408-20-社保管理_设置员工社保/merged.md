# 20-社保管理：设置员工社保

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\20-社保管理：设置员工社保_【海量资源尽在 ubkz.com】.mp4
- 时长 16分2秒（音频 963s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们已经设置好了这个列表相应的展示这些数据那接下来呢按照我们之前画的这张图呢继续往下看那员工的列表我们已经做过了接下来呢咱们就可以对某一个刚入职的员工进行他的一个社保设置当了某些员工呢如果说到某一个时间节点范围可以对他提高一些薪水那就是涨工资了
[00:26] 那这个时候呢它的社保的一些缴纳的一些比例或者缴纳的一些基数也需要适应的做调整那我们接下来就开始做员工的这个社保的一个保存或者进行修改那我们要做的这一点呢先去找到我们的页面那我们可以通过在页面上点击其中某一个员工进入到他这个设置界面那我们可以来试一下点击进来之后呢这边报错是肯定的因为他会自动的请求我们的后单接口
[00:53] 那各位进入到页面各位就知道了那如果这个员工呢已经设置过了社保是不是会展示出他设置的社保数据如果没有这个社保咱们就可以填写上之后再做保存那如果之前有咱们是不是就做更新呀那我们看过了这个箱的页面那咱们来分析一下进入到页面他所需要的一些基本数据首先在上方页面呢上边显示的是员工的一些
[01:20] 员工数据员工信息也就是用户表里的信息比如说这个用户呢他的一个入职时间他的一个身份证号码比如说还有一些他的一些起本的一些情况那底下这一些显示的其实就是员工的社保相关的一些数据所以我想说的是咱们进入到页面首先得先把用户的数据给他查询出来没错吧那要查询这个用户数据我们可以打开F12一起来看一下他最终发送的请求是什么样子
[01:53] 好了这边呢发送了一个请求来找到header其实请求的就是我们的社保相应的这个模块当中后面加的是当前用户的ID那这get方式请求就是获取用户的社保数据那对于我们来说要做的事情就很简单了回到我们这边的代码部分咱们开始写对应的接口好了把这些不相关的全部都给它关掉好了接下来呢在这边咱们就开始我们要编写的第一个就是根据
[02:25] 用户ID来查询用户的社保数据好那从上面的Ctrl CCtrl VCopy一个方法下来那我们这边请求的路径呢注意这回请求的路径诶注意是不是就应该是这么一个ID啊好了请求的方式就是一个Get诶请求方式那这边我们就是FindBy IDOK那这边呢没有什么需要各位注意的就是一个At Pass Verbal
[02:59] 死菌类型的ID设置过去即可那注意这里面的咱们需要的数据呢刚才说过一共有两个部分的数据一部分代表的是用户表里的信息另一部分代表的是这个用户的一些参保的一些设置数据那我们要做的事情呢其实就分为两块那我们要查两次首先第一个就是要查询就是根据
[03:28] 用户ID查询我们的用户数据好那接下来第二个就是根据我们的用户ID查询这个社保数据最终构造成一个完整的数据是不是做出相应的响应啊OK好了那接下来呢就是说我们现在这需要两块数据一个是用户一个是我们的社保我们可以把它呢封装到一个MAP集合里面最终给它进行响应MAP等于new一个哈希MAP好了注意啊各位
[03:58] 我写的这些全部都是符合接口的一些规范符合接口的一些规则的主要是为了简单我这边用了一个map那我们这个map里面要put两块内容第一块是用户的user另一块就是用户的社保那这个user这个数据从哪来呢我们就可以通过fin请求我们的系统请求我们的系统微服和系统微服获取用户数据
[04:28] OK那好了接着我们在这边可以配置一个对应的请求份接口来一个包Client好了这个份接口呢其实很简单在我今天给各位提供的这个资料当中也给各位准备好了基本代码Client把这两个Ctrl C全部都拷过来那这两个呢首先第一个就是这边有一个System分Client各位来看请求的是我们系统微服SysUserID就是根据ID来进行查询
[05:07] 好了我们可以一起把这玩意儿注入进来放到最上方吧at all to where注入进来好了那接下来呢我们在底下就可以通过分client点find by id是把这个id传进去就可以调用我们的系统为服务得到用户数据那需要各位注意的是我们这回呢得到的是一个result这么一个对象
[05:38] result注意咱们可以找到系统为服务一起来找一下用户他怎么给我封装成的result完了用户里面找find by id在这边各位发现他最终的封装的是一个user result封装到result当中这里面的data部分是不是才应该是我们的用户数据所以在我们这边user所以在我们这边
[06:14] 请求的时候我们要想得到真正的用户对象object注意我这边就不转型了obgo那其实就应该是点datadata其实才是我们的用户对象那有了用户我们可以把这玩意点put到我们的map集合里比如说就叫userobgo好了那这个用户部分呢我们获取到了接下来呢就是要查询用户的社保那这个用户社保其实就是很简单了
[06:46] Service.findbyid好了这个ID传进去最终得到我们这个社保对象好了我写一下就是user社保这个对象user社保social社保对象uss等于OK好了接口少方法我们在接口当中配置一个新的方法就可以了好了就是根据
[07:41] id 来查询好了同样的逻辑do.findById把id传进去得到一个optional好了做一个判断returnoptional.express it好了optional.get那这边来一个这边来一个no即可好了那接下来呢我们可以在这边呢把这个代码给他
[08:18] 放到map集合当中u u s sok好那这样一来呢咱们这个方法就已经写好了注意啊这个方法相对来说呢比较简单我这边的就不再写一点错一点实在是太慢了那除了咱们这个获取了用户的这个社保数据之外接下来呢再来看这边的其实还有一个小小的细节问题需要各位要注意一下是这样的就是咱们对某一个用户去设置社保的时候呢
[08:51] 因为它不同的城市可能它设置的社保的项目是不一样的比如说北京可能就四险一金或者是上海可能是五险一金或者其他的城市六险七险并且每一个城市它的险种是不太一样所以在这边你选择参保城市的时候我们就需要向后台发送一个请求去查询一下当前这个城市它的一个社保它的一个参保项
[09:20] 所以这边呢还有这么一个接口也需要我们去做一下好了请求的是payment item那后面传递的是一个我们叫做城市IDOK好了咱们把这个接口呢也给它补充上啊Ctrl C拿到这边这个比较简单好了这个就是根据城市城市ID查询参保城城市的社保项参保项OK这边呢请求的是一个payment
[10:00] ID没什么问题这个就是find payment itemfind payment叫做item好了那这边传递的是一个我们的城市ID过来好了那接下来呢咱们要做的事情呢其实这样的ID已经有了同时之前跟各位介绍过的数据库表在我们的数据库表当中呢就有这么一个城市参保的一张表就是city payment item所以我们直接根据ID从这个表里面查出
[10:35] 对应的结果得到数据即可没错了所以我们可以一起来试一下那需要各位注意的是我们的数据库当中啊一个城市呢它可能有多个参保项有多个参保项所以在这边我们要查询Service查询是不是得到的应该是一个list集合没错吧那list集合里面装的就是citypaymentitemok好了那这边呢就是一个list集合等于
[11:06] 好了我们可以通过咱们之前预留的一个Service得到最终的成绩结果好了我们一起来找到这个Service就是payment Service点抱歉这个没有注入进来啊add all to where注入进来payment Service拿过来payment Service点咱们就是finderallbycity就ID吧
[11:47] 好了那接着把这个city id传进去那我们这边的直接return这个list就可以了那survey层少方法补充一个方法alt加回车补充一个新的方法就是根据根据城市id获取我们的缴费的缴费的这些项目好了那对于这个呢咱们就需要自己去写相关的这个代码了就可以return点find all
[12:17] Five City ID好了把这个ID继续传下去那需要各位注意的是DU层需要配置这么一个方法好了就是直接拷一下吧其实跟这个名字是一样的OK好那这样一来呢咱们对应的这些方法呢就已经都写好了好了那这个方法写好了之后啊这个我是不想再去重启了咱们再把最后一个方法也给它搞定是这样的
[12:59] 就是说呢在页面部分各位咱们可以做一些相对设置页面全部都设置好了之后我点击保存是不是就完成我整个数据的一个保存或者更新的这么一个操作呀好了我们可以一起来试一下打F12走那这边你会发现又请求的是这个接口只不过是以put的方式来进行提交没错吧所以对于我来说呢咱们要做的事啊就是配置一个
[13:28] 保存的一个方法这是一个流程咱们全部给它搞定就可以了好了这边呢咱们就是一个保存或更新用户社保好了那这边呢就是saveuser这个玩意儿好了那put的方式提交我们有一些相应的参数request包带那需要各位注意前端传递过来的就是这么一个咱们的社保这个对象
[14:05] 好了那到了这个程度呢咱们都知道做保存或者更新比较简单直接在这边的设置即可但是我们这边的需要设置一下setcompany点这个表里面没有company id咱们用户表里有那不需要设置了那我们直接通过user Service.sale把这个uss传递过去就可以了那最终直接return让他成功
[14:35] 这个就是一个常规的保存比较简单那这边少save方法那回到这边少一个save方法那在我们这边呢添加一个save方法就可以了同样是借助do.save.uss传递进去OK好了我们重新启动一下当前的这个vf1来重新启动一下这边呢Tomcat已经启动成功了回到我们的页面部分各位一起来看一下
[15:16] 那点击其中的第一条来进来哎各位发现当前这个用户的所有数据呢基本上都已经有了好了那接下来呢在这边我们可以对里面的数据呢做一些小小的修改比如说呢这边来北京好了什么首次采访或者非首次采访1000啊这边呢有对应的比例在这边呢可以设置一些数据好了可以设置123456好了来
[15:44] 当然这边北京也可以调当然我数据库里面只有北京好了咱们可以一起来看一下能不能把这个数据给它更新上12345走好了接着点击进来再来看一下12345XXX是不是都已经有了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Spring Boot + Feign 客户端调用远程服务，实现社保信息的查询与保存功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示社保信息管理页面，显示员工列表，可按部门、城市筛选，当前选中“test1”部门和“北京”城市。
画面2：在浏览器开发者工具 Network 面板中，显示对 localhost 的请求返回 304（未修改），表明页面静态资源已缓存。
画面3：在 IDEA 中查看 SocialSecurityController.java，展示 list 和 findById 两个接口的代码，用于分页查询和根据 ID 查询社保信息。
画面4：在 Windows 资源管理器中，浏览“课程资料”文件夹，显示“day/4.pdf”文件。
画面5：在 IDEA 中，对 SocialSecurityController.java 的 findById 方法进行修改，添加 @PathVariable 注解，用于接收路径参数。
画面6：在 IDEA 中，继续修改 findById 方法，将 systemFeignClient.findbyId(id) 的返回值存入 map，并返回。
画面7：在 IDEA 中，查看 UserSocialService.java，展示 findbyId 方法，通过 systemFeignClient 获取用户数据并封装返回。
画面8：在 IDEA 中，展示 UserSocialService.java 的 find 方法，用于分页查询用户数据，并调用 systemFeignClient。
画面9：在 Navicat 中，查看社保数据库表结构，展示 city_id、payment_item、social_company 等字段。
画面10：在 IDEA 中，查看 SocialSecurityController.java 的 @RestController 注解和 @Autowired 注解，用于配置 Feign 客户端。
画面11：在 IDEA 中，查看 SocialSecurityController.java 的 findPaymentItem 方法，用于根据城市 ID 查询支付项目。
画面12：在 IDEA 中，查看 SocialSecurityController.java 的 saveUserSocialSecurity 方法，用于保存用户社保信息。
画面13：在 IDEA 中，查看 SocialSecurityController.java 的 findPaymentItem 方法，用于根据支付项目 ID 查询具体项目。
画面14：展示社保信息详情页面，显示员工 itcast 的社保信息，包括参保城市、社保类型、基数、比例等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
@RequestMapping(value = "list",method = RequestMethod.POST)
public Result list(@RequestBody Map map) {
    Integer page = (Integer)map.get("page");
    Integer pageSize = (Integer)map.get("pageSize");
    //1.调用Service层
    PageResult pr = userSocialService.findAll(page,pageSize,companyId);
    return new Result(ResultCode.SUCCESS,pr);
}

//根据用户id查询用户的社保数据
@RequestMapping(value = "/{id}",method = RequestMethod.GET)
public Result findById(@PathVariable String id) {
    Integer page = (Integer)map.get("page");
    Integer pageSize = (Integer)map.get("pageSize");
    //1.调用Service层
    PageResult pr = userSocialService.findAll(page,pageSize,companyId);
    return new Result(ResultCode.SUCCESS,pr);
}
```

画面5：
```java
@PathVariable String id
```

画面6：
```java
Map map = new HashMap();
Object obj = systemFeignClient.findById(id).getData();
map.put("user",obj);
UserSocialSecurity uss = userSocialService.findById(id);
map.put("userSocialSecurity",uss);
return new Result(ResultCode.SUCCESS,map);
```

画面7：
```java
Map map = new HashMap();
//1.根据用户id查询用户数据
Object obj = systemFeignClient.findById(id).getData();
map.put("user",obj);
//2.根据用户id查询社保数据
UserSocialSecurity uss = userSocialService.findById(id);
map.put("userSocialSecurity",uss);
return new Result(ResultCode.SUCCESS,map);
```

画面8：
```java
//分页查询用户的社保数据
public PageResult find(@RequestParam Integer page, @RequestParam Integer pageSize) {
    //1.调用Service层
    PageResult pr = userSocialService.findAll(page,pageSize,companyId);
    return new Result(ResultCode.SUCCESS,pr);
}
```

画面10：
```java
@RestController("/social_security")
public class SocialSecurityController extends BaseController {
    @Autowired
    private CompanySettingsService companySettingsService;
    @Autowired
    private UserSocialService userSocialService;
    @Autowired
    private SystemFeignClient systemFeignClient;
```

画面11：
```java
@RequestMapping(value = "/payment_item/{id}",method = RequestMethod.GET)
public Result findPaymentItem(@PathVariable String id) {
    List<CityPaymentItem> list = paymentItemService.findAllByCityId(id);
    return new Result(ResultCode.SUCCESS,list);
}
```

画面12：
```java
//保存查询到的用户社保
public Result saveUserSocialSecurity(@RequestBody UserSocialSecurity uss) {
    //根据城市id查询该城市的所有参保项目
    List<CityPaymentItem> list = paymentItemService.findAllByCityId(uss.getCityId());
    //将参保项目存入uss对象中
    uss.setPaymentItemList(list);
    //调用Service层保存
    userSocialService.save(uss);
    return new Result(ResultCode.SUCCESS);
}
```

画面13：
```java
//根据用户id查询用户的社保数据
public Result findById(@PathVariable String id) {
    Map map = new HashMap();
    Object obj = systemFeignClient.findById(id).getData();
    map.put("user",obj);
    UserSocialSecurity uss = userSocialService.findById(id);
    map.put("userSocialSecurity",uss);
    return new Result(ResultCode.SUCCESS,map);
}

//保存查询到的用户社保
public Result saveUserSocialSecurity(@RequestBody UserSocialSecurity uss) {
    //根据城市id查询该城市的所有参保项目
    List<CityPaymentItem> list = paymentItemService.findAllByCityId(uss.getCityId());
    //将参保项目存入uss对象中
    uss.setPaymentItemList(list);
    //调用Service层保存
    userSocialService.save(uss);
    return new Result(ResultCode.SUCCESS);
}

//根据城市id查询参保项目
public Result findPaymentItem(@PathVariable String id) {
    List<CityPaymentItem> list = paymentItemService.findAllByCityId(id);
    return new Result(ResultCode.SUCCESS,list);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

