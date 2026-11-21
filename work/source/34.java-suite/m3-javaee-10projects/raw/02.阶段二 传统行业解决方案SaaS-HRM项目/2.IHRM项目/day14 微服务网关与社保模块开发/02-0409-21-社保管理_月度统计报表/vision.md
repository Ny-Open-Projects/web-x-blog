# 画面线理解：21-社保管理：月度统计报表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\21-社保管理：月度统计报表_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:27, 03:16, 05:05, 06:45, 07:30, 09:07, 10:41, 11:12, 12:10, 13:25, 14:16, 15:05, 15:52, 16:47
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:24:07

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的社保缴费报表系统，从前端页面展示到后端代码实现，重点讲解了档案服务层（ArchiveService）中获取员工社保明细并计算总金额的逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示前端社保报表页面，显示员工社保信息，包含“社保表”、“导出”、“刷新”等操作按钮。
画面 2: 展示 SocialSecurityController.java 中的代码，包含保存用户社保信息、查询支付项、以及查询历史记录的接口。
画面 3: 展示 ArchiveService.java 中的代码，包含获取企业设置、保存企业设置、以及获取员工社保列表的接口。
画面 4: 展示 ArchiveService.java 中的代码，包含查找档案和查找档案详情的方法。
画面 5: 展示 ArchiveService.java 中的代码，正在为 ArchiveDao 和 ArchiveDetailDao 注入依赖。
画面 6: 展示 ArchiveService.java 中的代码，正在为 ArchiveDetailDao 注入依赖，并显示了 IDE 的自动补全建议。
画面 7: 展示项目文件夹结构，显示 service 目录下的 ArchiveService.java、CompanySettingsService.java、PaymentItemService.java 和 UserSocialService.java。
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
service
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
