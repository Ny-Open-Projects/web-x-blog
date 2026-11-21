# 17-社保管理：企业设置

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\17-社保管理：企业设置_【海量资源尽在 ubkz.com】.mp4
- 时长 8分59秒（音频 539s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了现在呢我们已经完成了这个环境搭建那搭建好了之后呢就是根据我们今天一上来说的这张图咱们一个一个功能给它实现出来那首先呢看的就是第一个可以让一个企业呢去设置我们的社保月份那这边呢简单的来说一下这些呢所有的页面在今天的资料当中呢都已经给各位准备好了还是那句话咱们这个系统的页面呢都是大同小异的基本上都是差不多的
[00:32] 那我们现在要做的是社保相的模块那社保模块呢我们把所有的代码都放到了src好了接着找到底下有一个模块呢就是我们的社保模块的model s-critics那这里面是我们的所有社保模块的一些代码当了对应的一些请求API呢我们把它放到了ihrm当中放到就是社保的一个API就是通过API去调用的远程端接口
[01:00] 那这边呢咱们来看一下首先呢是这样的左侧链接为点击社保它会进入到一个页面不知道各位看到了吗进入到这么一个页面好了这个界面就在干嘛呢就是一点击社保它会去查询一下数据库看一下当前这个企业有没有设置过社保如果设置过了它会进入到当前这个月份当中的内容
[01:28] 如果没有设置过它会让你去输入你要去设置哪个月的社保那我们可以这样来做一下啊回到我这边的数据库找到这张表叫做company setting里面表数据呢现在只有这么一条那我把这个数据呢给它删掉好了删掉那删掉之后回到这边再点击社保你会发现哎各位发现现在呢它就进不去了当然了这边说了一个什么
[02:01] 系统繁忙请稍后再试啊我们来看一下是不是报错了来刷新一把好了这边呢他发送过来了一个请求啊这边呢这是有一个咱们这个代码处理的时候有一天不太好啊就是我们写这个代码处理的不太好是这样的就是我们这个代码如果他呢没有查询过来之后呢没有查询过来他后面不能用直接get我把这个代码呢简单的再来调整一下OK
[02:57] 好那接下来呢咱们就做一个小小的处理点is a present代表什么含义就是看一下查询出来之后有没有结果如果有结果的话我们就可以通过这玩意打点get得到对应的数据如果没有结果呢我们返回一个那就是这么一个含义啊OK这个把它删掉了那接着重新启动一下这个微服务让它报错了
[03:32] 好了其实这边这个服务咱们已经改正了其实这个效果各位已经看出来了我从数据库删除了一条记录这回我再点击是网模块你发现没有查询是不是就让你去手动输入你要去制作哪个月份的社保没错吧所以咱们先去完成今天的第一项功能第一项功能如果你设置过它会自动的进入到列表界面
[04:01] 如果没有设置过你需要在这边填写好之后把设置的这些内容给它保存到对应的数据库当中好了这是我们第一个事情好了咱们刷新一下一起来试一下好了这边呢不会再报错了不会再报错了没问题好了那接下来那接下来我们数据库里面没有记录那我们这边就可以输入一下比如说我要制作2019年比如说呢088月份的社保
[04:35] 我一点确定好了各位发现这边抱歉呢请稍后重视这出现了一个错误为什么是这样的呢咱们可以一起来试一下他究竟做了什么好了201908好了我一点击确定你会发现他又调用了一下这个setting这一回请求的是一个pose请求好了那注意这回做什么其实各位应该都知道了
[05:04] 微点确定之后它会自动的向这个数据库当中给我们保存一条记录好了接下来咱们就把这个方法给它搞定回到我们这边的代码里这些全部都清空它会请求到我们的社保微服务请求到我们的Controller当中好了刚才是先查查询完成我们输入之后就是保存保存这个企业设置
[05:34] 那请求的路径刚才我们看过跟这个其实是一模一样的只不过我们现在请求的变成了postOK那Ctrl C Ctrl V这边起一个名字就是C有setting好了这边呢会有相的参数那我这边呢就是其实逻辑都很简单这边就稍微快一点那这边的参数呢就是一个atresponse about atrequest about好了请求的其实就是咱们的这个settingsettingsOK
[06:13] 那对象呢传递了过来过了之后呢我们就可以借助 Service 完成保存点 see 接着把这个 setting 给他传递进去哎 Service好了这边直接返回成功哎即可那这边的 Service 找方法调用在 Service 层当中补充一个方法就是保存企业设置那这个呢就更加简单了直接咱们可以调借助 do 点
[06:48] C5把这个company setting传递进去好了那在我们进行保存之前呢这边呢还需要设置一个参数就是设置一下好了它有一个叫做is settings这是我们的一个参数这个参数主要是说一下在我们这个数据库当中有说明主要是说明一下当前这个月份呢是否是已经设置或者是未设置这个状态那我们这边呢既然它设置了是不是应该给它改成1是不是就可以了所以这边给它填一个
[07:18] 我们对应的参数就是1代表的是已经完成设置设置set is setting就是一个已设置一个未设置把它设置上就可以了好了接着再去完成保存操作好这边应该是set好了那接下来呢咱们就可以一起启动起来来看一下这个效果好了现在呢我们的程序已经启动成功了那目前的数据库呢
[08:12] 咱们还没有进行任何设置所以在这边我们可以设置一把先刷新一下看一下效果现在还没有所以接下来呢我们可以填一个2019比如说就是7月份的社保那接着点击确定好了这边已经过来了那我们来看一下数据库当中是否有这条记录好了之前什么都没有那刷新一把你会发现是不是多了我们刚才的记录2019-07没错吧OK好了那这样一来呢咱们就已经完成了这个
[08:43] 进入社保里面的第一项就是设置那各位会发现如果已经设置过了它是不是直接就进入到这个报表的一个列表界面没错吧如果没设置就需要重新设置一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package com.ihrm.social.Service;

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

