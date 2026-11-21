# 06-考勤设置：代码实现-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\06-考勤设置：代码实现-下_【海量资源尽在 ubkz.com】.mp4
- 时长 9分58秒（音频 598s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们现在呢把这个烤芹呢查询已经给它写好了那除了查询之外那注意我这边呢全部把方法都写好再进行重新启动啊好了那接下来呢咱们就开始如果有了对应的烤芹之后这边随便填随便填随便填随便填那我一点保存是不是就是对我们已有的数据进行一个修改操作呀那注意我们可以打开F2一起来看一下
[00:30] 那点击这边可以还要填数据要填一下数据来各位他请求的方法就是CFG ATDE代表的是我要保存或者更新那这边也把所有的数据发送到我们的请求这边所以我想说这边发送的请求各位看到了其实就是我们这边对应的烤琴设置的对象所以我们要做的事情就是配置对应的这么一个方法
[01:05] 那接收put的请求那接收的参数注意是不是一个对象啊所以我们开始把这个代码呢给它补充出来好了来一份下来就是我们的保存靠近设置请求的路径呢就在这儿那请求方式是put那我们对应的请求参数就是我们这个对象OK好了接下来咱们开始改造一下改造一下这个就叫做seal那接下来里面呢接收的是一个参数
[01:45] at request bodyok那接下来呢我们这边调用就可以直接调用的方法来完成操作了Service.save attconfig那接着把这个对象呢传递过去完成操作那我们这边保存成功不需要其他的返回直接告他成功即可那我们这边呢Service 从手方法在Service当中添加一个新的方法过来就可以了好了这个就是我们的
[02:24] 保存或者更新我们的烤琴设置那需要各位一定要注意啊咱们保存或者更新那相应的这个烤琴设置的时候那你怎么就知道这回是在保存操作你怎么知道这回执行的就一定是更新操作呢所以对于我们来说呢依靠人家前端给你传递这些参数呢不太靠谱所以我们要做的事情呢首先第一个就是去查询是否存在
[02:55] 相应的叫做考勤记录好那接下来呢如果存在那代表的就是我们要更新那接着第三个如果不存在我们需要就是设置ID这回就做保存当然了不管是更新还是保存其实我们调用的方法都是一个叫做save没错吧OK好那接下来呢咱们就开始把这个箱的代码呢给它补充完整
[03:22] 那这边的查询是否存在相应的这个考勤记录那我们用什么查呢是这样的那页面传端传递过来的这边的是不是有部门ID并且我们当前能够得到这个操作人的起义ID所以我们要查询的其实就是根据起ID根据部门ID来查询当前的考勤那各位发现这个方法呢是我们之前就已经写好了所以把这玩意儿直接Ctrl C拿过来Ctrl VConfig点
[03:55] get company idconfig.get我们的部门ID那接下来呢这边呢得到返回值比如说我就起个名字就叫VO了那接着如果存在咱们就需要更新那注意判断一下VO等于等于不不等于那注意刚才我们说过之所以这边呢咱们要做这种判断是因为这边
[04:28] 请求过来的这个config或者你进行保存这个config没有ID如果有ID它直接自动的是不是就能保存和更新啊所以对于我们这边如果存在我们这边设置一下点set ID就是拿到我们查询的VO点get ID这样就来设置上ID了那一会儿因为有ID它会自动更新那接下来else如果不存在ID那我们这边代表的是要做保存所以这边点set
[04:57] ID那这个ID我们就需要自己生成一把ID workerNext ID没错吧好了这个就是如果不存在我们要设置ID那最终保存和更新全部体现在我们的DU当中直接调用save方法就可以了OK好了那咱们这个方法呢已经写好了那但是各位忽略了一个问题是这样的就是在我们进行保存的时候啊
[05:27] 保存的时候这个要用到企业ID那我们的企业ID在哪呢是不是这边就需要在你保存的时候把这个企业ID给我设置上点setcomedyid那这样一来我们这个完整的流程呢就已经写好了那好了接下来呢我们就可以把这个服务给它启动起来OK千万别抱错先给它启动起来找到当前工程找到对应的启动类来执行
[06:01] 好了这边的启动呢可能会有一点点时间啊我们在这点时间里面干嘛呢是这样的所有的请求咱们都应该给他抱歉这边call应该是IA是RMOK来重新启动一下找到我们这个模块重新启动一下刚才是编译没通过是call过来的时候有一个地方应该是call错了好了这边让他进行启动那接下来呢回到我们刚才的话题是这样的
[06:49] 我们现在所有的请求都应该要接入到网关所以在我们的网关层咱们就需要做相应的一些配置没错吧那做一些相应的配置把这个网关层从这边Ctrl Ccopy一段过来Ctrl V好了这边呢咱们请求的就是我们的唯一ID这个ID呢我们先叫这ID呢随便起来我叫CFG好了我们请求的前缀呢都是CFG开头的
[07:19] 那我们能把这个服务呢给它转发到哪个地方注意如果碰到CFG这种请求的是不是应该给它转发到我们这边新创建好的这个微服啊转发过来OK那接着我们可以重新启动一下我们的网关服务那网关服务呢之前我已经启动了在这边重新启动一下好了看一下我们当前的这个模块呢其实已经启动成功了靠近模块那我们等待
[08:09] 这个网关模块成功之后我们连接上前端页面咱们来做一个测试好了这边呢我已经启动成功了回到我们的前端页面咱们一起来试一下好了我们刷新一把那找到这边的设置哎找到这边的设置那点进来之后呢我们来看一下研发部他默认的已经有值了那接下来呢这边有测试部财务部哎各位会发现他这个考勤时间呢会有一些不同比如说这边八点那接下来研发部
[08:41] 0点没错吧那接下来呢我们这边修改能不能用呢好了我们这边呢随便添点就是1.05分让它进行上班来接着我们保存一把好了这边保存了之后我们再来看一下刚才改的应该是研发部各位来看1.05是不是也做了相的修改啊那这样一来咱们就已经完成了第一个咱们初期模块的设置
[09:08] 那其实出勤模块搞定了之后呢这边还有请假扣款加班等等这几个流程那这几个流程跟我们这个出勤管理呢其实是差不多的所以这几个模块呢留给各位去实现当了在今天资料当中我会把相应的这些代码呢给各位下发下去OK好了那到目前为止咱们今天的第二块功能也就是这块烤勤和各位做了一个简单的
[09:36] 说明其实对于考勤而言这个设置它的意义要大于它的代码因为代码其实比较简单主要希望各位要知道就是考勤设置在我们的一个人力资源管理系统当中它的一个必要性还有它涉及到的一些需求主要是跟我们计算薪资息息相关OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Spring Boot + Shiro + Eureka 实现考勤配置的前后端交互与服务间调用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- IDE中展示ConfigController.java文件，其中定义了获取考勤配置的POST接口。
- 代码片段：
  ```java
  @RestController
  @RequestMapping("/cfg")
  public class ConfigController extends BaseController {
      @Autowired
      private ConfigurationService configurationService;
      ...
      @RequestMapping(value = "/atte/item", method = RequestMethod.POST)
      public Result atteConfig(String departmentId) {
          AttendanceConfig ac = configurationService.getAtteConfig(companyId, departmentId);
          return new Result(ResultCode.SUCCESS, ac);
      }
  ```

画面2：
- 浏览器中展示考勤设置页面，显示“部门”为“人力资源部”，“出勤时间”为“08:20-09:30”。
- 网络面板显示POST请求的Payload，包含departmentId和多个时间字段。

画面3：
- IDE中展示ConfigController.java文件，与画面1相同，但光标位置不同。

画面4：
- 浏览器中展示考勤设置页面，与画面2相同，但页面左下角有IDE窗口的缩略图。

画面5：
- IDE中展示ConfigurationService.java文件，光标位于第44行，显示了AttendanceConfig的DAO方法定义。

画面6：
- IDE中展示ConfigurationService.java文件，光标位于第54行，显示了find方法的实现，包含条件判断和返回值。

画面7：
- IDE中展示项目结构，选中了“ihrm_common_model”模块，下方显示了多个应用的运行日志。

画面8：
- IDE中展示ShiroConfiguration.java文件，定义了Realm和SecurityManager的配置。

画面9：
- IDE中展示application.yml文件，配置了多个服务的路径和敏感头信息。

画面10：
- IDE中展示项目结构，选中了“ihrm_gate”模块，下方显示了application.yml文件的内容。

画面11：
- IDE中展示GateApplication.java文件，显示了Spring Boot的启动类和日志信息。

画面12：
- 浏览器中显示空白页面，URL为“localhost:8080/#/attendances/index”。

画面13：
- 浏览器中展示考勤设置页面，与画面2相同，但“部门”为“研发部”，“出勤时间”为“08:20-09:30”。

画面14：
- 展示了一个PDF阅读器界面，显示“day15”文档，内容为空白。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import org.springframework.web.bind.annotation.RestController;

/**
 * 配置考勤设置的Controller
 */
@RestController
@RequestMapping("/cfg")
public class ConfigController extends BaseController {
    @Autowired
    private ConfigurationService configurationService;

    /**
     * 获取考勤设置
     * cfg/atte/item
     * post
     * 参数 departmentId
     */
    @RequestMapping(value = "/atte/item", method = RequestMethod.POST)
    public Result atteConfig(String departmentId) {
        AttendanceConfig ac = configurationService.getAtteConfig(companyId, departmentId);
        return new Result(ResultCode.SUCCESS, ac);
    }
}
```

画面5：
```java
private ExtraDutyRuleDao extraDutyRuleDao;
private DayOffConfig dayOffConfigDao;
private IdWorker idWorker;
@Autowired
private ConfigurationService configurationService;

//保存或更新考勤设置
public void saveAtteConfig(AttendanceConfig attendanceConfig) {
    if (null != attendanceConfig) {
        attendanceConfig.setId(idWorker.nextId());
        attendanceConfig.setCompanyId(companyId);
        attendanceConfig.setDepartmentId(departmentId);
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendanceConfig.setCreateTime(new Date());
        attendanceConfig.setUpdateTime(new Date());
        attendanceConfig.setUpdateBy(userId);
        attendanceConfig.setCreateBy(userId);
        attendance

