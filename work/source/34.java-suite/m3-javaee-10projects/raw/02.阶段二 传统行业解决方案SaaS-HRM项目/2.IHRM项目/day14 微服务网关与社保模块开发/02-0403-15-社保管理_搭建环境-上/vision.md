# 画面线理解：15-社保管理：搭建环境-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\15-社保管理：搭建环境-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:42, 01:33, 02:43, 04:07, 05:00, 06:08, 06:42, 07:28, 08:06, 08:53, 10:34, 11:59, 13:11, 14:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:19:27

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 和 Shiro 的人力资源社保系统模块的开发过程，包括项目结构、配置文件、实体类、服务层和控制器层的编写，以及数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示桌面，有“黑马程序员”和“博学谷”的标志，鼠标指针在桌面中央。
画面 2: IntelliJ IDEA 打开项目 `ihrm_parent`，显示项目结构，根目录下有 `ihrm_common_model`, `ihrm_company`, `ihrm_employee` 等子模块。
画面 3: 在项目结构中展开 `ihrm_social_security` 模块，显示其 `src/main/java` 和 `src/test/resources` 目录。
画面 4: 打开 `ShiroConfiguration.java` 文件，显示 Shiro 配置代码，包括 `filterFactory.setUnauthorizedUrl`、`filterMap.put` 和 `RedisManager` 的构造。
画面 5: 在项目结构中选中 `resources` 目录。
画面 6: 打开 `ArchiveDetail.java` 文件，显示 `@Entity` 注解和 `ArchiveDetail` 类的构造方法。
画面 7: Windows 资源管理器中显示 `dao` 文件夹，其中包含多个 `.java` 文件，如 `ArchiveDao.java`、`CityPaymentItemDao.java`。
画面 8: 资源管理器中显示 `dao` 文件夹内的文件列表。
画面 9: 打开 `ArchiveService.java` 文件，显示 `@Service` 注解和 `firstArchive` 方法。
画面 10: 弹出“New Package”对话框，提示输入新包名。
画面 11: 打开 `SocialSecurityController.java` 文件，显示 `@RestController` 注解和 `@RequestMapping`。
画面 12: SQLyog 数据库管理工具中显示 `ss_company_settings` 表的结构，包括字段 `company_id`、`set_type`、`data_month`。
画面 13: 在 `SocialSecurityController.java` 中，`settings` 方法中调用 `companySettingsService.findById(companyId)`。
画面 14: 打开 `CompanySettingsService.java` 文件，显示 `@Service` 注解和 `settings` 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```java
filterFactory.setUnauthorizedUrl("/autherror?code=2");
//登录后访问
filterMap.put("/sys/city/**","anon");
filterMap.put("/sys/facelogin/**","anon");
filterMap.put("/auther","anon");
//认证之后访问（登录）
filterMap.put("/","authc");
//路径（用户自定义配置路径）
filterFactory.setFilterChainDefinitionMap(filterMap);
return filterFactory;
```
```java
@Value("${spring.redis.host}")
private String host;
@Value("${spring.redis.port}")
private int port;
```
```java
public RedisManager redisManager() {
    RedisManager redisManager = new RedisManager();
    redisManager.setHost(host);
}
```
画面 6:
```java
@Entity
@Table(name = "ss_archive_detail")
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class ArchiveDetail implements Serializable {
    private static final long serialVersionUID = -5571487189954762991L;
    public void setUsersSocialSecurity(UsersSocialSecurity userSocialSecurity) {
        this.householdRegistrationId = userSocialSecurity.getHouseholdRegistrationId();
        this.participatingTheCity = userSocialSecurity.getParticipatingTheCity();
        this.providentFundCity = userSocialSecurity.getProvidentFundCity();
        this.providentFundNotes = userSocialSecurity.getProvidentFundNotes();
        this.providentFundBase = userSocialSecurity.getProvidentFundBase();
        this.socialSecurityBase = userSocialSecurity.getSocialSecurityBase();
        this.accumulationFundEnterprise = userSocialSecurity.getAccumulationFundEnterprise();
        this.proportionOfProvidentFundEnterprise = userSocialSecurity.getProportionOfProvidentFundEnterprise();
        this.individualProportionOfProvidentFund = userSocialSecurity.getIndividualProportionOfProvidentFund();
        this.providentFundEnterprise = userSocialSecurity.getEnterpriseProvidentFundPayment();
        this.totalProvidentFund = this.providentFundEnterprise.add(this.providentFundIndividual);
    }
```
画面 9:
```java
@Service
@Transactional
public class ArchiveService {
    @Autowired
    private ArchiveDetailDao archiveDetailDao;
    @Autowired
    private IdWorker idWorker;
    @Autowired
    private SystemFeignClient systemFeignClient;
    @Autowired
    private EmployeeFeignClient employeeFeignClient;
    @Autowired
    private UserSocialService userSocialService;
    @Autowired
    private PaymentItemService paymentItemService;
    public Boolean firstArchive(String companyId, String yearMonth) {
        Long count = archiveDao.countByCompanyIdAndYearsMonth(companyId, yearMonth);
        if (count > 0) {
            return false;
        }
        return true;
    }
}
```
画面 11:
```java
@RestController
@RequestMapping("/social_security")
public class SocialSecurityController {
    @Autowired
    private CompanySettingsService companySettingsService;
    @RequestMapping(value = "/settings", method = RequestMethod.GET)
    public Result settings() {
        CompanySettings cs = companySettingsService.findById(companyId);
        return new Result(ResultCode.SUCCESS, cs);
    }
}
```
画面 12:
```sql
CREATE TABLE `ss_company_settings` (
  `company_id` varchar(40) NOT NULL COMMENT '企业ID',
  `set_type` varchar(40) NOT NULL COMMENT '设置类型',
  `data_month` varchar(40) NOT NULL COMMENT '数据月份'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
画面 13:
```java
public Result settings() {
    CompanySettings cs = companySettingsService.findById(companyId);
    return new Result(ResultCode.SUCCESS, cs);
}
```
画面 14:
```java
@Service
public class CompanySettingsService {
    @Autowired
    private CompanySettingsDao companySettingsDao;
    @RequestMapping(value = "/settings", method = RequestMethod.GET)
    public Result settings() {
        CompanySettings cs = companySettingsService.findById(companyId);
        return new Result(ResultCode.SUCCESS, cs);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 7: 未显示 PPT 标题或架构图。
画面 12: SQLyog 中显示 `ss_company_settings` 表的结构，包含字段 `company_id`、`set_type`、`data_month`，以及表的创建语句。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
