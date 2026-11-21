# 画面线理解：17-社保管理：企业设置

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\17-社保管理：企业设置_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:31, 01:38, 02:04, 02:17, 03:19, 04:08, 04:45, 05:15, 06:02, 06:58, 07:36, 08:25, 08:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:20:43

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 系统中实现企业社保设置功能，包括前端页面展示、后端 Controller 和 Service 层代码编写、以及数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了课程 PPT 的第 3.4.1 节“企业社保设置”，内容为获取企业社保设置的 Controller 方法。
- 代码片段：
```java
/**
 * 获取企业是否设置社保
 * @return
 */
@RequestMapping(value = "/settings", method = RequestMethod.GET)
public Result getSettings() throws Exception {
    CompanySettings companySettings = companySettingsService.findById(companyId);
    return new Result(ResultCode.SUCCESS, companySettings);
}
```

画面2：
- 展示了前端 Vue 项目在 Visual Studio Code 中运行成功，提示“Your application is running here: http://localhost:8889”。

画面3：
- 展示了 iHRM 系统的“社保”页面，显示了部门、社保城市等筛选条件，但当前无数据。

画面4：
- 展示了 IntelliJ IDEA 中的终端日志，显示 Spring Boot 应用启动成功，包含 Eureka 服务注册和负载均衡信息。

画面5：
- 展示了多窗口切换界面，包括 PPT、代码编辑器、数据库工具等，用于说明开发环境。

画面6：
- 展示了 IntelliJ IDEA 中的 `CompanySettingsService.java` 文件，代码中使用了 `Optional` 类处理可能为空的查询结果。

画面7：
- 展示了 IntelliJ IDEA 中的项目结构，当前选中的是 `SocialSecurityApplication`。

画面8：
- 展示了 iHRM 系统的“社保”页面，浏览器显示“Request failed with status code 404”，表示请求失败。

画面9：
- 展示了 IntelliJ IDEA 中的异常堆栈信息，显示了 `404 Not Found` 的错误处理过程。

画面10：
- 展示了 `SocialSecurityController.java` 文件，其中定义了 `getSettings` 和 `saveSettings` 两个方法。

画面11：
- 展示了 `CompanySettingsService.java` 文件，代码中使用了 `Optional` 类处理查询结果，并添加了保存方法。

画面12：
- 展示了 `CompanySettings.java` 文件，代码中定义了 `setCompanyId` 方法，用于设置公司 ID。

画面13：
- 展示了 iHRM 系统的“社保”页面，页面加载中，显示“正在请求...”。

画面14：
- 展示了 iHRM 系统的“社保”页面，页面加载完成，显示“社保”标题和导航菜单。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 获取企业是否设置社保
 * @return
 */
@RequestMapping(value = "/settings", method = RequestMethod.GET)
public Result getSettings() throws Exception {
    CompanySettings companySettings = companySettingsService.findById(companyId);
    return new Result(ResultCode.SUCCESS, companySettings);
}
```

画面6：
```java
package com.ihrm.social.service;

import com.ihrm.social.domain.CompanySettings;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CompanySettingsService {

    @Autowired
    private CompanySettingsDao companySettingsDao;

    //根据企业id查询
    public CompanySettings findById(String companyId) {
        Optional<CompanySettings> optional = companySettingsDao.findById(companyId);
        return optional.isPresent() ? optional.get() : null;
    }
}
```

画面10：
```java
public class SocialSecurityController extends BaseController {

    @Autowired
    private CompanySettingsService companySettingsService;

    /**
     * 查询企业是否设置社保
     */
    @RequestMapping(value = "/settings", method = RequestMethod.GET)
    public Result getSettings() {
        CompanySettings cs = companySettingsService.findById(companyId);
        return new Result(ResultCode.SUCCESS, cs);
    }

    /**
     * 保存企业设置
     */
    @RequestMapping(value = "/settings", method = RequestMethod.POST)
    public Result saveSettings(@RequestBody CompanySettings cs) {
        CompanySettings cs1 = companySettingsService.findById(companyId);
        return new Result(ResultCode.SUCCESS, cs1);
    }
}
```

画面11：
```java
public void save(CompanySettings companySettings) {
    companySettings.setCompanyId(companyId);
    companySettingsDao.save(companySettings);
}
```

画面12：
```java
public class CompanySettings {
    // ... 其他属性和方法
    public void setCompanyId(String companyId) {
        this.companyId = companyId;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
- PPT 标题：“3.4.1 企业社保设置”
- 内容：“企业第一次进入社保页面，会要求输入制作社保记录的日期”

画面5：
- 展示了多个窗口，包括 PPT、代码编辑器、数据库工具等，用于说明开发环境。

5) 不要评价画面美观，不要输出与课程无关的内容。
（以上内容已按要求输出）
