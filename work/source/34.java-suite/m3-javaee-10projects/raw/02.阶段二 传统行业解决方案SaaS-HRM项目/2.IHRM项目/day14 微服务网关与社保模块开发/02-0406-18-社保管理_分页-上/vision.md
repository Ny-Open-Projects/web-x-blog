# 画面线理解：18-社保管理：分页-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\18-社保管理：分页-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:40, 01:01, 01:28, 02:07, 02:56, 03:28, 03:37, 04:29, 04:40, 05:11, 05:34, 06:12, 06:31, 07:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:21:29

1) 这一组画面整体在讲如何在 iHRM 项目中实现企业社保信息的增删改查功能，包括前端页面、后端控制器、服务层代码及数据库操作。

2) 按时间顺序列出每张画面的要点：
画面1：前端页面展示“本月：社保在缴 公积金在缴 员工 诚聘 入职 离职”功能模块，显示部门、社保城市、公积金城市等筛选条件。
画面2：浏览器开发者工具 Network 标签页，显示请求头信息，包含 Authorization Bearer Token 和 Content-Type。
画面3：IntelliJ IDEA 中展示 SocialSecurityController.java 文件，包含 @GetMapping("/settings") 和 @PostMapping("/settings") 方法。
画面4：IntelliJ IDEA 中展示 SocialSecurityController.java 文件，正在编写 @PostMapping("/list") 方法。
画面5：IntelliJ IDEA 中展示 SocialSecurityController.java 文件，正在编写 @PostMapping("/list") 方法，使用 Map 获取请求参数。
画面6：IntelliJ IDEA 中展示 SocialSecurityController.java 文件，正在编写 @PostMapping("/list") 方法，使用 Integer 类型获取 page 和 pageSize。
画面7：IntelliJ IDEA 中展示 SocialSecurityController.java 文件，正在编写 @PostMapping("/list") 方法，使用 Integer 类型获取 page 和 pageSize。
画面8：Windows 桌面多窗口视图，显示 SQLyog、IntelliJ IDEA、Postman 等工具窗口。
画面9：IntelliJ IDEA 中展示 SocialSecurityController.java 文件，正在编写 @PostMapping("/settings") 方法，使用 @Autowired 注解注入 UserSocialService。
画面10：IntelliJ IDEA 中展示 SocialSecurityController.java 文件，正在编写 @PostMapping("/list") 方法，使用 @Autowired 注解注入 UserSocialService。
画面11：IntelliJ IDEA 中展示 SocialSecurityController.java 文件，正在编写 @PostMapping("/list") 方法，使用 PageRequest 和 Pageable 分页查询。
画面12：SQLyog 数据库管理工具，显示 user_social_company 表数据，包含 user_id、enterprises_pay_social_security_this_month、enterprises_pay_the_provider_this_month 等字段。
画面13：浏览器开发者工具 Network 标签页，显示请求头信息，包含 Authorization Bearer Token 和 Request Payload。
画面14：IntelliJ IDEA 中展示 UserSocialService.java 文件，正在编写 findAll 方法，注释说明需要使用 Feign 调用远程服务获取用户数据。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面3：
```java
public class SocialSecurityController extends BaseController {

    @Autowired
    private CompanySettingsService companySettingsService;

    /**
     * 查询企业是否设置过社保
     */
    @RequestMapping(value = "/settings", method = RequestMethod.GET)
    public Result settings() {
        CompanySettings cs = companySettingsService.findById(companyId);
        return new Result(ResultCode.SUCCESS, cs);
    }

    /**
     * 保存企业设置
     */
    @RequestMapping(value = "/settings", method = RequestMethod.POST)
    public Result saveSettings(@RequestBody CompanySettings companySettings) {
        companySettings.setCompanyId(companyId);
        companySettingsService.save(companySettings);
        return new Result(ResultCode.SUCCESS);
    }

    /**
     * 查询企业员工的社保信息列表
     */
    @RequestMapping(value = "/list", method = RequestMethod.POST)
    public Result list(@RequestBody Map map) {
        // 获取请求参数
        Integer page = map.get("page");
        Integer pageSize = map.get("pageSize");
        // 使用 service 查询
        userSocialService.findAll(page, pageSize, companyId);
        return new Result(ResultCode.SUCCESS);
    }
}
```

画面4：
```java
/**
 * 查询企业员工的社保信息列表
 */
@RequestMapping(value = "/list", method = RequestMethod.POST)
public Result list(@RequestBody Map map) {
    // 获取请求参数
    Integer page = map.get("page");
    Integer pageSize = map.get("pageSize");
    // 使用 service 查询
    userSocialService.findAll(page, pageSize, companyId);
    return new Result(ResultCode.SUCCESS);
}
```

画面5：
```java
/**
 * 查询企业员工的社保信息列表
 */
@RequestMapping(value = "/list", method = RequestMethod.POST)
public Result list(@RequestBody Map map) {
    // 获取请求参数
    Integer page = map.get("page");
    Integer pageSize = map.get("pageSize");
    // 使用 service 查询
    userSocialService.findAll(page, pageSize, companyId);
    return new Result(ResultCode.SUCCESS);
}
```

画面6：
```java
/**
 * 查询企业员工的社保信息列表
 */
@RequestMapping(value = "/list", method = RequestMethod.POST)
public Result list(@RequestBody Map map) {
    // 获取请求参数
    Integer page = map.get("page");
    Integer pageSize = map.get("pageSize");
    // 使用 service 查询
    userSocialService.findAll(page, pageSize, companyId);
    return new Result(ResultCode.SUCCESS);
}
```

画面7：
```java
/**
 * 查询企业员工的社保信息列表
 */
@RequestMapping(value = "/list", method = RequestMethod.POST)
public Result list(@RequestBody Map map) {
    // 获取请求参数
    Integer page = map.get("page");
    Integer pageSize = map.get("pageSize");
    // 使用 service 查询
    userSocialService.findAll(page, pageSize, companyId);
    return new Result(ResultCode.SUCCESS);
}
```

画面9：
```java
import com.ihrm.social.service;

@Service
public class UserSocialService {

    @Autowired
    private UserSocialSecurityDao userSocialSecurityDao;

    /**
     * 分页查询用户社保数据
     */
    public PageResult findAll(Integer page, Integer pageSize, String companyId) {
        // 需要借助 Feign 调用远程服务获取用户数据
        // 直接在本地获取社保信息
    }
}
```

画面10：
```java
import com.ihrm.social.service;

@Service
public class UserSocialService {

    @Autowired
    private UserSocialSecurityDao userSocialSecurityDao;

    /**
     * 分页查询用户社保数据
     */
    public PageResult findAll(Integer page, Integer pageSize, String companyId) {
        // 需要借助 Feign 调用远程服务获取用户数据
        // 直接在本地获取社保信息
    }
}
```

画面11：
```java
/**
 * 查询企业员工的社保信息列表
 */
@RequestMapping(value = "/list", method = RequestMethod.POST)
public Result list(@RequestBody Map map) {
    // 获取请求参数
    Integer page = map.get("page");
    Integer pageSize = map.get("pageSize");
    // 使用 service 查询
    userSocialService.findAll(page, pageSize, companyId);
    return new Result(ResultCode.SUCCESS);
}
```

画面12：
```sql
SELECT user_id, enterprises_pay_social_security_this_month, enterprises_pay_the_provider_this_month, participating_in
FROM user_social_company
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
