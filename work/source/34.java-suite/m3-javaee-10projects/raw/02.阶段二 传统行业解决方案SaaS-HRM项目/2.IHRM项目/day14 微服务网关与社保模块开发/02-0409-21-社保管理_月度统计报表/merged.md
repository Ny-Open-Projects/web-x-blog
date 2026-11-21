# 21-社保管理：月度统计报表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\21-社保管理：月度统计报表_【海量资源尽在 ubkz.com】.mp4
- 时长 16分52秒（音频 1013s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好我们现在完成了对应的报表的一个展示还有员工参保数据的一个设置那接下来呢就是在这边当一个月份啊他们的所有的这个社保计算已经都够完成了之后我们可以统计一下当月这个报表的一个数据好了咱们点进去可以来看一下上方呢你设置的是几月份上面就会给你设置出当前几月份的报表那我们点进去来一起来看一下
[00:28] 那点进来之后呢这边其实也是一个查询当了这回查询的数据相对来说呢就比较多了里面这边还涉及到什么他的员工姓名这边还涉及到员工的一些公积金基数还有真正的他缴纳公积金的一些比例还有他具体涉及到多少钱好了当了这边呢还有很多的公金备注等等等等所有内容那这个其实就是我们整个报表最详细的一部分内容做说明
[00:55] 那这块内容报表我们如果验证了没有问题的话在这边可以就对当前7月份数据的报表进行归档就做一个历史性的一个备份那如果归档了之后接下来再做其实就变成8月份新的报表了那我们先来看第一个事情就是在这边我们可以先去查询出当前7月份社保的报表数据那么可以打开F12一起来看一下那我点击刷新找到我们这边
[01:27] 那发送的请求呢其实就是底下发送到了我们history什么当前月份这么一个参数后面还加上一个of type那需要各位注意这个of type如果是一指的是当前的这个报表数据那如果是其他的数据指的是历史归档的一些详细数据所以这边呢咱们做这个代码处理的时候希望各位要注意
[01:55] 那好了接下来呢我们就可以对照着当前这边呢配置一个新的方法回到我们的代码部分好了这个就是查询归档查询我们的月数月份的月份数据报表好了链接拷过来那这边呢有一个参数叫做OPTAP那这个OPTAP1代表的是当月数据当月数据啥意思指的是没有归档的数据那注意这边呢如果是其他
[02:30] 其他指的就是历史归档的详细记录OK那接着我们把这个代码呢给他先写账考过来一份好了请求的是history那后边呢就是y e a rmouseOK请求方式是get也没问题那接下来呢这边的请求呢会有一个参数啊咱们就是year mouse好了那接下来呢还有就是我们说过了还有一个参数
[03:08] 就是一个死菌类型的叫做OPtab当然了我们可以这边定义成int类型其实也可以OK那注意在我们这个代码的里面写的时候呢需要做一个判断ifOPtab等于等于一要走一个逻辑else要走一个逻辑那接下来呢就有的朋友会有疑问了这边先不抱错说一下有的朋友就会有疑问为什么要有两个逻辑是这样的
[03:40] 那如果不等于呢这边是其实就是我们的归档的以归档的数据那如果是1的话就是我们还未归档未归档要查询的是当月的这个详细数据能理解吧因为是这样的就是归档的数据在一个我们的归档数据库表未归档这个就比较麻烦了我们需要拼接完整的数据构造成我们的数据列表并且返回
[04:12] 好我们先来把这个相对来说简单一点的这个业务流程呢先给它搞定就是这个已归档的数据啊如果已归档的话那在我们的数据库当中呢特别是这两个表一个表呢就是我们这个社保归档的这个表还有一个就是我们的明细表就在里面产生相当记录那我们来看一下当前这个归档历史的这个表先看一下这个表里面有没有数据如果有我们再去查明细就可以了好了那这边呢回到我们的ID当中把这个代码呢给它实现一下首先第一个
[04:42] 就是我们需要根据你这个月份月和我们的企业ID去查询归档的历史好了如果归档如果归档历史存在那接下来我们就是查询归档名系OK这个相对来说比较简单我们需要相应的Service我们来看一下Service已经引进来了我们就可以通过Service归档点find就叫find find by
[05:14] by什么呀那就就find就叫归档吧OK那我们说了需要两个参数第一个参数就是comedyID那接下来第二个参数就是我们的一个year month没错接下来拿过来那注意这样一来呢我们就能够得到一个归档的历史这么一个对象啊OK好了那接下来引下包别引错我们是社保模块的好了接下来呢如果归档历史存在我们就可以if判断一下
[05:47] 不等于呢就是我们查询出来这个规档历史接下来我们去想方设法查询对应的明细记录那在这边呢我去定义了一个list一个集合那这个list集合就应该是从明细记录里面来进行获取的点find all detailsdetail by好了注意我们要查怎么查呢是这样的就是说我们有一个规档历史是吧还有规档明细规档历史
[06:15] 和归档名系是一个一对多那我们就需要用归档历史的ID来查所以我就Find By归档历史IDID来进行查询那接着我们在边把ID传递过去点GetID那好了这边呢需要两条serve两个查询我们一个一个把它补充上来第一个查询接下来第二个查询那这两个查询呢相对来说没有那么难啊
[06:49] 好了那接下来呢我们一起来看好了首先看第一个就是根据企业ID还有我们这个年月去查询归党历史OK那这边我们需要借助DEO所以我把DEO呢给它引进来别引错别引错包啊AOOKDEOat all to win好了那除了这个之外呢还有再来一个我们有一个历史有一个归党的名系Detail
[07:35] 哎,DU,别进错包OK,那接下来呢,咱们开始一个一个完成首先第一个,就是通过借助DU点Find注意我们这边查询呢其实就可以按照我们之前说的它这种别名的产业方式啊FindByP,C-U-M,P,C-U-M,P-N,YID,AND好了,叫做这个EarMouseOK,把这个Company ID传进去把这个EarMouse
[08:10] 哎传进去好了直接return即可那这边do少方法我们在do当中添加对应的一个方法出来好了因为我们这种是SpringDataGPA的查询方式所以这边呢它有一个这种名称查询那种思路就是说呢你这个如果跟啊表当中的属性名称保持一致它自动就会查咱们不需要写任何的搜据啊ok好了这一个查询咱们写好了接下来第二个就是根据归档的这个历史归档历史ID
[08:43] 查询我们的归档名信那这个相对来说呢也很简单好了直接呢在这边拿到我们的DU点FindBy就是直接ID了好了ID传进去这一特那同样的我们在这边呢也需要写一个方法各位来看
[09:14] 好了这个方法呢我们之前已经给各位引进来了其实已经写好了OK好了那这样一来咱们这个基本的这两个方法呢咱就已经写好了那注意这个是比较简单的一部分那还有一个部分呢就是未归档的这个数据那对于未归档的数据来说呢这个就稍微会有一点点麻烦我们通过我们的Service来进行查询其实也可以啊我们可以通过Service点调用的方法get
[09:47] get reportsget reports好了接着把这个参数的传递过去那这回呢就需要我们进行一个手动的查询了好了那接着我说一下这个方法呢相对来说会有一点点复杂并且里面的逻辑呢比较多那我们这边的简单的和各位做一个小小的说明就是说呀我要去查询当前的这个月的这个报表呢我需要有对应的姓名入职时间
[10:20] 手机号那注意后面的还有一大堆比如说学历开网什么什么工作程式等等那注意再往后面是对应的我们社保的具体的一些数据所以我想说我们这边查询的数据来源比较多也比较复杂那这个方法的内容比较多那在今天资料当中呢我已经把这个代码给各位准备好了咱们拿过来简单的看一下哎就可以了打开今天的这个资料在这个基本代码里面我们在归档设备当中
[10:50] 配置好了一个方法我把它已经打开了好了我们要做的事情呢就是把这个两个方法呢给它Ctrl C 靠到我们的代码当中靠到思路下边OK好了呢需要各位注意的是靠过来之后呢这边会有一些需要我们注入的一些对象啊At AutoValve 给它注入进来好了那接着我简单的解释一下这个方法究竟在做什么除了这个之外呢还有一个OK好了那简单的说一下
[11:31] 我这边调用的其实就是我们刚才写好的这个getReports方法这个getReports方法各位来看那传递过来一个年月传递过我们企业名称那注意我在这边首先做的第一件事就是去查询我们用户的这个社保列表那注意这个方法呢是我们之前在DO当中查询列表写好的一个方法注意这个分页参数我写的是None代表的是不分页我要查询全部那这样一来就能查询出了我们所有的
[12:01] 用户和一些基本的社保数据那这个查好了之后接下来底下我们说过了得到的是一个map集合那这个map集合我们重要是为了获取里面的user主要是为了获取我们查询出来的用户mobile等等等等这些基本数据开始去构造明细因为我们说过了我们现在查询的是当业的还没有归档所以这些数据我们自己要构造比较复杂那用户设置好了之后那别忘了
[12:30] 我们当前归档的数据还有一部分是用户或者说员工他的一些个人信息员工个人信息我们通过发送这种份请求的方式调用了一个我们的API各位来看这个其实就是我们的份发送了一个API请求得到雇员所有的明细数据因为只有在雇员里面才有他的学历才有他的什么开户行等等
[12:58] 其实这个就是我们这个方法的它的一个主要目的其实这个方法呢你说难吗不难但是它比较繁琐比较啰嗦并且里面的代码设计的点呢相对来说这边比较多这边还少一些东西我把它都注入进来OK好那接下来咱们来看那在刚才这个方法当中呢咱们说过了统计了用户数据统计了个人的一些
[13:42] 信息那接下来呢还有一些社保信息我又调用的是get other date这个方法来进行统计那注意这个为什么要专门又写这个方法进行统计呢是这样的因为在我们这个页面上需要当前一个企业他这个员工他对这个员工所支付的社保还有公积金总的一些费用当然还包含员工自费他的社保
[14:09] 和公积金它的总的费用所以我们这边就需要做一个相加的这么一个处理所以这边其实就是做了一个加法把两个加到一起比如说员工部分社保交了100那员工部分公积交了一部分那就是200企业当然也需要支付相应的这些总金额的一些数量OK好了那在这边呢需要各位注意一个点就是我们这边统计金额全部都是用的这种商业的数据类型就是big sample
[14:38] OK好了这个方法没有什么可说的那我们这边呢可以一起重新启动一下Tomcat我们来看一下这个页面效果OK刷新一把这个会稍微有点点慢各位耐心等待一下那启动报了一个错误我们一起来查一下这个错误好了years and months这边应该是某一个do里面写错了好了我们的归档的实际库表
[15:31] 这边存的是EarsMouse我这边写的是Ears这边加一个SOK那我们的Service呢也需要做一个修改方法名变了嘛OK再启动好了这边呢已经启动成功了成功了回到我们的页面一起来刷新一下504这个应该是网关还没有响应过来啊OK那各位来看现在这些数据就已经有了其中IDcastHMN贞号这些数据还是比较完整的
[16:13] 那注意啊其他的这些比如说ZBZ LL为啥没这些其实是这样的就是我们说过了这里面是员工的一些明细的数据比如说ZBZ我们可以对它进行一个设置个人信息里面可以这些数据各位看到都没有啊我们可以做一个相应的设置好了比如说1234567890好了接着底下我这边奖卡号电脑社保号就是X11随便写几个咱们来看一下这回
[16:44] 社保点进去报表刚才我们改的CBC是不是相关的数据已经有了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的社保缴费报表系统，从前端页面展示到后端代码实现，重点讲解了档案服务层（ArchiveService）中获取员工社保明细并计算总金额的逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示前端社保报表页面，显示员工社保信息，包含“社保表”、“导出”、“刷新”等操作按钮。
画面 2: 展示 SocialSecurityController.java 中的代码，包含保存用户社保信息、查询支付项、以及查询历史记录的接口。
画面 3: 展示 ArchiveService.java 中的代码，包含获取企业设置、保存企业设置、以及获取员工社保列表的接口。
画面 4: 展示 ArchiveService.java 中的代码，包含查找档案和查找档案详情的方法。
画面 5: 展示 ArchiveService.java 中的代码，正在为 ArchiveDao 和 ArchiveDetailDao 注入依赖。
画面 6: 展示 ArchiveService.java 中的代码，正在为 ArchiveDetailDao 注入依赖，并显示了 IDE 的自动补全建议。
画面 7: 展示项目文件夹结构，显示 Service 目录下的 ArchiveService.java、CompanySettingsService.java、PaymentItemService.java 和 UserSocialService.java。
画面 8: 展示 ArchiveService.java 中的代码，正在实现 getReports 方法，用于获取社保明细。
画面 9: 展示 ArchiveService.java 中的代码，正在实现 getReports 方法，处理员工个人信息并设置到 ArchiveDetail 对象中。
画面 10: 展示 ArchiveService.java 中的代码，正在实现 getReports 方法，包含获取其他数据的辅助方法。
画面 11: 展示 ArchiveService.java 中的代码，正在实现 getReports 方法，计算社保公司和个人缴纳金额。
画面 12: 展示 Spring Boot 启动日志，显示 PropertyReferenceException，提示找不到 yearMonth 属性。
画面 13: 展示 SocialSecurityApplication.java 中的代码，显示 Spring Boot 启动日志，提示没有激活的配置文件。
画面 14: 展示前端社保报表页面，显示员工社保信息，包含“社保表”、“导出”、“刷新”等操作按钮。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
@RequestMapping(value = "/{id}", method = RequestMethod.PUT)
public Result saveUserSocialSecurity(@RequestBody UserSocialSecurity uss) {
    userSocialService.save(uss);
    return new Result(ResultCode.SUCCESS);
}

// 根据企业id查询多保单的多保项目
@RequestMapping(value = "/payment_item/{id}", method = RequestMethod.GET)
public Result findPaymentItem(@PathVariable String id) {
    List<CityPaymentItem> list = paymentItemService.findAllByCityId(id);
    return new Result(ResultCode.SUCCESS, list);
}

// 查询月份流水表
// /history/201907/yearMonth=201907&optType=1
// optType: 1(当月流水)
// 其他(历史月份的详细记录)
@RequestMapping(value = "/history/{yearMonth}", method = RequestMethod.GET)
public Result historyDetail(@PathVariable String yearMonth, int optType) {
    return new Result(ResultCode.SUCCESS);
}
```

画面 3:
```java
@Autowired
private ArchiveService archiveService;

// 查询企业是否设置过社保
@RequestMapping(value = "/settings", method = RequestMethod.GET)
public Result settings() {
    CompanySettings cs = companySettingsService.findById(companyId);
    return new Result(ResultCode.SUCCESS, cs);
}

// 保存企业设置
@RequestMapping(value = "/settings", method = RequestMethod.POST)
public Result saveSettings(@RequestBody CompanySettings companySettings) {
    companySettings.setCompanyId(companyId);
    companySettingsService.save(companySettings);
    return new Result(ResultCode.SUCCESS);
}

// 查询企业员工的社保信息列表
@RequestMapping(value = "/list", method = RequestMethod.POST)
public Result list(@RequestBody Map map) {
    // 获取请求参数
    return new Result(ResultCode.SUCCESS);
}
```

画面 4:
```java
import org.apache.commons.lang.StringUtils;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Map;

@Service
@Transactional
public class ArchiveService {

    @Autowired
    private ArchiveDao archiveDao;

    @Autowired
    private ArchiveDetailDao archiveDetailDao;

    public Archive findArchive(String companyId, String yearMonth) {
        return archiveDao.findByCompanyAndYearMonth(companyId, yearMonth);
    }

    public List<ArchiveDetail> findAllDetailByArchiveId(String id) {
        return archiveDetailDao.findByArchiveId(id);
    }
}
```

画面 5:
```java
@Service
@Transactional
public class ArchiveService {

    @Autowired
    private ArchiveDao archiveDao;

    @Autowired
    private ArchiveDetailDao archiveDetailDao;

    // 查询档案历史
    public Archive findArchive(String companyId, String yearMonth) {
        return archiveDao.findByCompanyAndYearMonth(companyId, yearMonth);
    }

    // 根据档案id，查询详细明细
    public List<ArchiveDetail> findAllDetailByArchiveId(String id) {
        return archiveDetailDao.findByArchiveId(id);
    }
}
```

画面 6:
```java
@Service
@Transactional
public class ArchiveService {

    @Autowired
    private ArchiveDao archiveDao;

    @Autowired
    private ArchiveDetailDao archiveDetailDao;

    // 查询档案历史
    public Archive findArchive(String companyId, String yearMonth) {
        return archiveDao.findByCompanyAndYearMonth(companyId, yearMonth);
    }

    // 根据档案id，查询详细明细
    public List<ArchiveDetail> findAllDetailByArchiveId(String id) {
        return archiveDetailDao.findByArchiveId(id);
    }
}
```

画面 7:
```
Service
├── ArchiveService.java
├── CompanySettingsService.java
├── PaymentItemService.java
├── UserSocialService.java
```

画面 8:
```java
@Service
@Transactional
public class ArchiveService {

    @Autowired
    private ArchiveDao archiveDao;

    @Autowired
    private ArchiveDetailDao archiveDetailDao;

    // 查询档案历史
    public Archive findArchive(String companyId, String yearMonth) {
        return archiveDao.findByCompanyAndYearMonth(companyId, yearMonth);
    }

    // 根据档案id，查询详细明细
    public List<ArchiveDetail> findAllDetailByArchiveId(String id) {
        return archiveDetailDao.findByArchiveId(id);
    }

    public List<ArchiveDetail> getReports(String yearMonth, String companyId) throws Exception {
        Page<Map> userSocialSecurityItemPage = userSocialSecurityDao.findPage(companyId, pageable: null);
        List<ArchiveDetail> list = new ArrayList<>();
        for (Map map : userSocialSecurityItemPage) {
            String userId = (String) map.get("userId");
            String mobile = (String) map.get("mobile");
            String username = (String) map.get("username");
            String departmentName = (String) map.get("departmentName");
            ArchiveDetail vo = new ArchiveDetail(userId, mobile, username, departmentName);
            vo.setTimeOfEntry((Date) map.get("timeOfEntry"));
            Result personalResult = employeeFeignClient.findPersonalInfo(vo.getUserId());
            if (personalResult.isSuccess()) {
                UserCompanyPersonal userCompanyPersonal = JSON.parseObject(JSON.toJSONString(personalResult.getData()), UserCompanyPersonal.class);
                vo.setUserCompanyPersonal(userCompanyPersonal);
            }
            // 获取其他信息
            getOtherData(vo, yearMonth);
            list.add(vo);
        }
        return list;
    }
}
```

画面 9:
```java
@Service
@Transactional
public class ArchiveService {

    @Autowired
    private ArchiveDao archiveDao;

    @Autowired
    private ArchiveDetailDao archiveDetailDao;

    // 查询档案历史
    public Archive findArchive(String companyId, String yearMonth) {
        return archiveDao.findByCompanyAndYearMonth(companyId, yearMonth);
    }

    // 根据档案id，查询详细明细
    public List<ArchiveDetail> findAllDetailByArchiveId(String id) {
        return archiveDetailDao.findByArchiveId(id);
    }

    public List<ArchiveDetail> getReports(String yearMonth, String companyId) throws Exception {
        Page<Map> userSocialSecurityItemPage = userSocialSecurityDao.findPage(companyId, pageable: null);
        List<ArchiveDetail> list = new ArrayList<>();
        for (Map map : userSocialSecurityItemPage) {
            String userId = (String) map.get("userId");
            String mobile = (String) map.get("mobile");
            String username = (String) map.get("username");
            String departmentName = (String) map.get("departmentName");
            ArchiveDetail vo = new ArchiveDetail(userId, mobile, username, departmentName);
            vo.setTimeOfEntry((Date) map.get("timeOfEntry"));
            Result personalResult = employeeFeignClient.findPersonalInfo(vo.getUserId());
            if (personalResult.isSuccess()) {
                UserCompanyPersonal userCompanyPersonal = JSON.parseObject(JSON.toJSONString(personalResult.getData()), UserCompanyPersonal.class);
                vo.setUserCompanyPersonal(userCompanyPersonal);
            }
            //

