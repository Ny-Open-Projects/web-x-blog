# 15-社保管理：搭建环境-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\15-社保管理：搭建环境-上_【海量资源尽在 ubkz.com】.mp4
- 时长 14分30秒（音频 871s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们现在做好了社保模块对应的需求分析表结构说明那接下来呢我们就可以搭建一个新的模块咱们着手在新模块当中完成我们这个代码的开发那我们搭建的这个模块呢就是我们社保相应的这个模块那这边呢需要跟各位简单的说明一下由于我们之前学过了代码生成工具那其中的一些基本的代码呢我们就借助工具自动的生成出来比如说呢我们的实体类
[00:31] 比如说我们的DU层的相应的接口比如说呢还有一些基本的思维层相关的这些代码那这些内容呢我都已经给各位准备好了当然了各位如果说呢想自己生成那就生成一把如果不想生成用我今天给各位提供好的这个资料就可以了好了这边有社保资料里面有基本生成的一些相同代码还有一些可以直接使用的工具类OK
[00:58] 好了那这边呢咱们就开始去创建一个小小的工程接着把这些生成好的代码呢导入到工程当中哎让他跑起来搭建好这么一个环境那在这边呢咱们先去创建一个模块ok定位到复模块右键创建一个model那这个模块的名称究竟叫什么呢我在这边呢就跟讲义上保持一致了Ctrl C把这个模块名称拷过来拷到这边Ctrl V好了接着点击next哎finish
[01:34] 那这个模块我们创建出来了之后呢会有箱的坐标我们的依赖那接着在资料当中呢已经把这个箱的依赖呢给各位准备好了就是一个碰文件好了把这个所有的内容呢直接拷过去Ctrl C拿到这边Ctrl V好了那这样一来呢我们已经添加好了对应的坐标依赖那接下来在当前的这个工程当中
[02:03] 当前的这个工程当中我们要想呢让它能够启动起来咱们需要有相应的一些启动内以及对应的相对这些配置文件好了我在这边呢先去创建一个对应的包吧com.him.提一个名字socilok代表的是我们的社保模块点击ok那接着在这个包下我们去创建一个启动内接着去创建对应的一些咱们的Java代码
[02:33] 好在这边呢简单的先来搞一个启动类出来那启动类呢其实很简单了跟我们之前的这些代码呢基本上都是差不多的Ctrl C这边拿过来Ctrl V任意一个地方拷过来一份OK那拷过来之后呢简单的做一个小小的配置啊比如说这边Spring Boot的包扫描比如说我们这边要扫描的一些咱们的实体类那注意这个实体类扫描这边呢需要做一个小小的修改
[03:04] 为了方便我直接让他扫描笃闷这个包下了那剩下底下什么ERICA等等这些配置我就不再啰嗦了OK抱歉刚才call过来的时候这个应该给他起一个名字起个名字改一下名字好了我们就叫做社网模块吧SOCALS3SECURITYOK改一下名字
[03:33] 好了这个名字呢我们已经改好了当然了里面的这些内容里面这些内容其实什么JWT啊咱们其实已经没用了所以删掉呢也可以当然了我这边呢就直接保留了OK好了这样一来我们这个启动类呢其实已经配置好了那注意那除了这个启动类我们在这边呢是不是还引入过来了这么一个shadow配置文件这个shadow配置文件呢也需要做一个小的修改
[04:00] 好了注意这边呢还是跟之前一样我们就不去进行全线上面的一个验证了OK好了这边有个包引错了把它删掉OK好了这样一来呢咱们的启动内搞定了share相应的这个配置呢咱们也给它拿过来了那当然了我们还少一个就是我们的配置文件那这个配置文件也可以从一个地方呢咱们把它拷过来Ctrl C直接拿过来一份Ctrl V
[04:31] 那靠过来之后呢这个配置文件做一个修改首先Eureka这些没有问题那我们这边请求的端口呢就是9004了那接着我们请求的服务名称呢也做一个修改SOCIAL-SECURITY好了这个是我们代表的模块名称OK加S那这样一来呢咱们对应的基本的配置啊就已经都给它配置完成了那接下来呢在这边呢是这样的
[05:00] 还是之前的一句话我们之前学过了代码生成所以相应的一些基本代码咱们直接通过数据库自动生成就可以了这些代码包含我们的实体类包含我们的最基本的DO接口以及对应的一些基本Service那好了我们接下来就把生成好的这些文件给它copy到我们对应的工程当中首先这边就是我们的modelOK
[05:29] 那这些代码呢在资料当中呢都给各位准备好了基本代码好了有一个就是我们的domainOK就在这个位置Ctrl C靠过来好了打开idea找到我们的model目录在里面呢创建一个新的package创建一个包好了我们这个包名就是social下划线securitysCtrl V靠进去OK
[06:04] 好了这样子我们的实体类这几个呢就已经搞定了其实这几个类呢都比较简单就是根据数据库里面的字段一个一个的生成出来的而已好了实体类呢我们搞定了之后接下来呢还有就是对应的DAO以及对应的Service那这些代码呢全部都是生成好的我们开始同样创建一个包呢我们叫做DAO好了在里面再去创建一个包呢我们叫做SERVICE
[06:33] 那接着把对应的每一层的代码呢全部给它拷过去就可以了好了比如说呢我们这边会有DU层代码Ctrl C把DU全部拷过来Ctrl V拷进来那需要各位呢注意一下这么拷过来的这些代码里啊刚才这个实体类com.hmdomain这个包名是不是写错了好了这边呢我把这个包名呢做一个修改OK没问题了
[07:13] 好了那这几个都比较简单都比较简单全部都是一些最基础的一个代码里面没有任何的实现方法OK好了那接下来咱们有了DU是不是还应该有相应的Service那同样的也是把Service层的这些代码呢也给它拷过来Ctrl CCtrl V那需要各位注意一下这个Service里面的这些代码呢我做过一些基本的删减基本删减
[07:42] 对应的其实6个DU应该有6个Service但是我只需要4个其实就够了好抱歉这里面还有一些代码我把这些代码全部都干掉咱们就保留空的什么都不要好了同样的这边呢是一个空的没什么问题好了再来上边这里面呢也是把所有的这些代码呢全部都给它删掉ok好了这边还有一个错误啊好了那这样一来咱们对应的DU层Service层
[08:30] 还有对应的咱们的实体类这几个基本的这几个类呢咱们都已经创建出来了那好了接下来在这边呢咱们来验证一下可以写一个Controller咱们简单的来验证一下我们创建的这些工程呢究竟能不能够访问过来OK好了在这边呢我们可以去创建一个对应的我们的Controller层来一个包c1trol11rcontroller那在里面呢咱们可以定义对应的一个Controller方法
[08:59] 好了来右键创建一个class那这个Controller呢咱们就叫做社保吧socalsecurityscontrollerok好了呢这边呢咱们可以做一些最最最最基本的一些配置啊比如说呢第一个ata rest Controller好了这是我们需要的接着第二个ata request我们叫做myping
[09:34] 那这边呢我们简单的说一下就是说现在我们请求的所有的副路径呢都是就叫社保跟我们这边的请求路径是一致的那我可以从这边呢直接拷一段过去啊拷一段过去OK拿过来好了这个是我们请求的副路径那接下来呢咱们可以随便的写一个控制器的方法哎完成咱们这个测试功能
[10:03] 那比如说呢在我们这个系统当中啊有一项啊就是回到这张图来看比如说我们这张有一个功能是这样就是查询一下这个企业呢是否设置过这个社保的这个月份比如说有这么一个功能那我们要做的事情呢就是在这边呢给他配置一个方法就是查询企业是否设置过我们这个社保
[10:31] 那这个呢应该怎么去做呢很简单首先来一个ata requestmapping指定的是我们的请求路径好了我的路径呢就叫做settings这边呢哎已经有了好了那接着我们的请求方法呢就是method等于我们叫做get用get的方式请求过来其实就是做一个小小的查询那我们最终返回的结果全部都是result这个各位应该还有印象而已suata result
[11:01] 好了这个方法名称叫什么其实无所谓就叫做setty好了为了不报错先return一个num那接下来呢我想说一下咱们要查询企业是否设置过社保那我们之前说过这是一个sas系统那不同的企业可能是不一样的那我们要想得到企业ID很简单只需要在上边继承我们公共的base Controller哎就可以了啊那这边呢我们就可以通过base Controller当中
[11:33] 拿到对应的我们的company id好了这个我就不写了好那这样一来呢我们其实已经得到了企业对应的企业的这个id那我们要做的事情请求过来之后我们是不是拿到企业id去查一下当前这个月是否企业设置过设保那查的是哪个表各位应该还有印象我们的数据库呢其实就是company settings这个表比较简单注意来看
[12:05] 这个表呢比较简单一共就三个字段company idsettings还有datamonth其中呢第一个company id呢是我们的permit key主件所以我们这边要做的就是根据id根据这个company id是主件就是根据主件去查一下有没有数据有数据返回是不是就可以了所以在我们这个方法呢要做的事情很简单我们用到了Service就注入serviceoutware private
[12:34] 那我们刚才自己call过来了一个就是company setting我们的Service好了company settingservicecompany settingservice那么要做的事情借助Service根据ID来查find by ID那这个ID是不是就是我们的企业IDCM company ID传进去就可以了那这样一来呢我们就能得到一个company setting司的这么一个对象CS
[13:06] 等于好了最终我们构造返回值就是new一个result好了success接下来第二个把这个cs传进去即可我们都知道现在的思维层少一个方法我们就直接在思维层中补充一个方法就可以了好了这个是什么就是根据企业id来进行查询
[13:38] 那我们这个思维层的方法呢就是借助do层层的向下传递过去点find by id把id设置上他们的id好了接着点get好了那这边呢我们可以做一个判断if settings等于等于not好了主要是为了页面显示的更加来友好一些当然了这个你其实不写其实也可以的好了那我这边就
[14:15] 不写了直接returnOK那这样一来呢我们第一个方法呢就已经写好了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

