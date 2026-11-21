# 画面线理解：20-社保管理：设置员工社保

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\20-社保管理：设置员工社保_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:52, 03:03, 04:47, 05:28, 06:20, 07:11, 08:10, 10:37, 11:27, 12:52, 14:04, 15:11, 15:56
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:23:04

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
    //1.调用service层
    PageResult pr = userSocialService.findAll(page,pageSize,companyId);
    return new Result(ResultCode.SUCCESS,pr);
}

//根据用户id查询用户的社保数据
@RequestMapping(value = "/{id}",method = RequestMethod.GET)
public Result findById(@PathVariable String id) {
    Integer page = (Integer)map.get("page");
    Integer pageSize = (Integer)map.get("pageSize");
    //1.调用service层
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
    //1.调用service层
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
    //调用service层保存
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
    //调用service层保存
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
