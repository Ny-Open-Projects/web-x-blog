# day11-18-满标放款-定义接口4

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-4 满标放款需求分析和接口定义
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-4 满标放款需求分析和接口定义\day11-18-满标放款-定义接口4_【海量资源尽在 666java.com】.mp4
- 时长 10分33秒（音频 633s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 咱把这个接口三定好之后呢接下来就是最后一个接口接口四对吧接口四呢主要就是启动还款就是先把还款的计划啊还款的名气啊先给它生成了再说那这里边呢主要就涉及到两个微服务大家看一看啊一个还是谁啊交易中心从这开始对不对然后直接远程请求到哪还款服务大家看是不是所以我们接下来呢应该先做一个准备工作什么准备工作
[00:29] 我们现在的微服务工程里边是不是还缺这个谁啊款款微服啊对不对我们需要把它导进来然后呢配置启动参数啊还要针对Apollo上做一些最基础的一些配置能把它先启动起来再说对不对再定义这个什么呀接口所以我们接下来首先先把这个准备工作做了啊我们看一下讲义对方跟大家说了这里边是涉及到款款微服务嘛所以先把它搭建起来导入工程啊配置启动参数还有什么Apollo
[00:58] 那咱看看吧这些呢咱大家都比较熟悉了啊前面都进行过好多次了我这就不再从头给大家演示了啊挑几个关键地方咱过一遍就行了大家看一下首先导入这个工程吧这个工程呢我们在资料文件夹里边有啊大家找一找找到之后呢你直接导进来就行了我这呢都已经导过了导进来之后呢你大概熟悉一下这个破文件啊看里边都导了哪些jar 包啊有些jar 包咱没有讲到呢但是呢将来会讲会用
[01:28] 然后手机手机这个配置文件这是这个APPID对吧这里边是什么呀Apollo上的名称空间吧这是这个应用程序的名字日志这个大家都很熟了然后就是这个加代码加代码这一块你看看啊这些好多包都是空包吗等着咱去开发呢这边咱提前给他放了一些工具类security youtube这个都见过了吧这些配置类不再说了大家都知道了提前给他准备了一些实体类
[02:01] 好这个蓝链器令牌蓝链器咱之前也都用过啊好这些一些这个模型对象啊封装好的还有这个还款的一些工具类对吧好这个什么呀启动类前面大家大概看一下吧这里边配了一些什么基本的一些配置对吧可烂他呀事务啊飞呀再说了这是第一步吧你得先把这个呃还款未服这个工程给先导进来
[02:30] 导进来之后呢我们就在这顺手把这个启动参数给他配了行参数的话你这里边看讲义吧看看讲义主要是配这个什么端口号啊环环微服的端口号是53080直接粘过来拿用就行了看到这吧对不对最后呢我们就需要在Apollo上因为我们所有的配置基本上都放到Apollo上了吧你要新建一个项目这个项目就是用来存储环环微服对应的一些配置
[03:02] 我这边这一操都已经进行完了因为他稍微麻烦一下你自己下去操作就行了这个大家比较熟大家看我在这是不是新建了一个项目咱大概过一遍这里边都需要进行哪些基础配置基本上都差不多你看application里面是不是就这两项smagger还有全局异常补货这个springboard http里边我们是不是主要配这个vif的基础访问路径然后再往下我们看看
[03:32] 有一个非Ribbon不再说了啊直接这个关联那个什么公共的那个名声空间啥都不用改就行了mp这一块mp这一块我们主要就是配的那个那个什么呀实体类那个包那进行扫描吗呃还有就是连接池这一块啊这块主要是配这个数据库连接字符刷对吧ip地址啊端口号数据库的名字再往下还有什么
[04:03] 这两个咱暂时用不着你先不用管了大概呢就这几点吧大家需要对它进行配置就OK了那配完之后呢我们最好是启动一下这个什么环绕微服看它能不能正常启动能不能正常的从阿卜罗上读取到这些配置我们启动一下我们主要是观察这个控制台有没有报错就行我看一下这块是不是就是从阿卜罗上在读取配置目前只要它启动没有问题吧我们觉得这个微服基本上是可以用的
[04:43] 你看这儿他说这样端口2553080对不对那咱这个准备工作吧咱就做到这儿做到这儿之后呢咱接下来是不是该定义第几个接口啊对最后一个接口就是启动还款这个接口我们说这个接口呢主要涉及到交易中心和什么呀还款这个微服那这个接口呢应该是定义在哪个地方应该定义在是不是还款微服这哪对吧由交易中心去访问这个接口
[05:10] 然后这边主要实现的功能就生成还款计划应受联系等这些数据啊做好准备工作了然后呢就启动还款成功嘛这边是不是就响应到前端了对不对整个这个过程就结束了啊所以我们接下来的应该是呃去API工程里边定义这个最后一个接口那由于呢这个还款微服是我们新增加的一个一个微服工程对吧所以说API工程里边我们需要新建一个repayment的包在这个包里边呢就是
[05:39] 我们去新建这个什么还款微服务相关的这个接口就行那我们找到这个谁呀API然后呢在这个地方新增一个包然后呢在这个包里面我们是不是新建一个接口叫repayment什么呀API接口接口这是咱们还款微服务的这个第一个接口对不对然后在这个接口里边咱就要定义一个方法叫start repayment就是
[06:19] 干什么启动还款咱把这个给它粘过来这我们定义的第一个方法这里面是不是缺一个类叫Project with Tenders什么DTO咱找一找这个类给它拷过来应该是这个对不对我们看看它应该拷到什么地方API里边还要建这么一个包MODL咱先把这个包建一下这个包咱还没建子包
[06:53] 建一个modl然后呢我们就把它给拷过来就行了这边会自动导报哎我没导导进来了反应稍微一段慢啊那咱看看这个方法名字叫startrepairment啊箭名之一就是启动还款那么这里边呢我们重点关注的就是这个参数啊这个参数里边都有什么内容呢咱点进去看看吧那这里边你看一下它主要应该就是你看看看图啊其实它这边你看
[07:28] 是不是交易中心往这边发请求吗他会传过来一些数据吧我们这边要接受一下那么就封装到这个什么呀project的v字tender的dtu里面你看这里面有标的的信息什么呀投标的记录对吧还有一些什么呀利率他要根据这些数据要干什么呀去生成缓缓计划还有这个什么呀应收明信这是一个数据的一个封装吧这个大家知道就行了到时候用的时候再说这是这个接口咱们定好接口定好之后咱们接下来是不是应该是
[07:57] 要去找一找Controller来生成一下这个方法Controller的话这应该就是还款微服这个工厂了啊这里边咱还没有Controller找一找还没有Controller是不是咱新建一个Controller名字呢咱跟讲义保持一致他的名字叫repayment Controller对不对这个类不存在你自己建吧扔过来然后我们加点出示这个应该是什么呀
[08:35] 还换微服务的什么呀c o n t的Controller对吧然后呢上面是不是要加一个注解叫restcontroller然后呢我们这个类是不是要实现呢刚才定义的这个接口就叫什么repaymentapi对吧repaymentapi
[09:05] 然后他就报错了因为我们里边是不是定义了一个方法然后咱接下来把这个方法呢给他生成一下这是咱们这个版款微服这control里边第一个方法然后咱参考讲义把相关的一些注解给他粘过来这一块然后呢还有这个谁啊request body好差不多咱一起看一看主要是看这个访问路径你看他也是什么开头的对L开头的说明他是给谁啊后台微服去访问的
[09:44] 那是不是呢看这个什么呀看这个图呗那这里边这个接口是谁去访问的呀交易中心嘛什么交易中心就是咱后台的一个微服务哎所以说呢这是L开头的这个大家需要注意的然后这是咱那个封装数据的那个参数对不对那这咱就把什么呀对咱这个满标放款业务当中的最后一个接口就定义好了这边大家需要注意的是你提前需要把这个还款微服务就环境整个给先搭建起来那这是目前吧咱们把
[10:14] 满标放款这个业务当中所涉及到的四个接口全部都定义好接口定义好之后呢接下来是不是前后端开始进行什么并行开发了那我们呢接下来就是分成四个阶段把这四个接口里边的功能挨个给它实现了就OK了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个还款服务的业务流程与代码实现，包括流程图、配置文件、API接口和数据模型。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示还款服务的流程图，包含多个步骤，如“放款成功”、“修改标的的状态”、“生成还款计划”等，流程图中包含“60%”的进度标识。
画面2：展示IDEA中`application.yml`配置文件，内容为：
app:
  id: repayment-Service
apollo:
  bootstrap:
    enabled: true
    namespaces: micro_service.spring-boot-dubbo,application.micro_service.spring-boot-http,micro_service.spring-boot-Eureka,micro_service.spring-cloud-feign
spring:
  application:
    name: repayment-Service
logging:
  config: classpath:log4j2-dev.xml
画面3：IDEA项目结构视图，显示`wanningzp-repayment-Service`模块下的`src/main/java`和`resources`目录结构。
画面4：Apollo配置中心界面，显示`application`配置项，包括`Swagger.enable`和`spring.mvc.throw-exception-if-no-handler-found`等键值对。
画面5：Apollo配置中心界面，显示`micro_service.spring-boot-dubbo`配置项，其中`spring.datasource.url`值为`jdbc:mysql://127.0.0.1:3306/wanpinzp_repayment?useUnicode=true&characterEncoding=utf8&useSSL=false`。
画面6：IDEA控制台输出日志，显示Spring Boot启动过程中的错误信息，如“Could not find meta server address”和“Sync config failed”。
画面7：展示还款服务的流程图，包含多个步骤，如“放款成功”、“修改标的的状态”、“生成还款计划”等，流程图中包含“45%”的进度标识。
画面8：IDEA项目结构视图，显示`wanningzp-api`模块下的`java`目录结构，并弹出“New Package”对话框，输入包名为“repayment”。
画面9：Windows资源管理器中，右键点击`ProjectWithTendersDTO.java`文件，弹出上下文菜单。
画面10：IDEA中打开`ProjectWithTendersDTO.java`文件，显示类定义，包含`project`、`tenders`、`commissionInvestorAnnualRate`和`commissionBorrowerAnnualRate`等字段。
画面11：IDEA中打开`RepaymentApi.java`文件，显示接口定义，包含`startRepayment`方法。
画面12：IDEA中打开`RepaymentController.java`文件，显示类定义，尚未编写代码。
画面13：IDEA中`RepaymentController.java`文件，显示`@RestController`注解和`@Override`方法，方法名为`startRepayment`，参数为`@RequestBody ProjectWithTendersDTO`，返回值为`null`。
画面14：展示还款服务的流程图，包含多个步骤，如“放款成功”、“修改标的的状态”、“生成还款计划”等，流程图中包含“45%”的进度标识。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
app:
  id: repayment-Service
apollo:
  bootstrap:
    enabled: true
    namespaces: micro_service.spring-boot-dubbo,application.micro_service.spring-boot-http,micro_service.spring-boot-Eureka,micro_service.spring-cloud-feign
spring:
  application:
    name: repayment-Service
logging:
  config: classpath:log4j2-dev.xml

画面5：
jdbc:mysql://127.0.0.1:3306/wanpinzp_repayment?useUnicode=true&characterEncoding=utf8&useSSL=false

画面10：
public class ProjectWithTendersDTO {
    /**
     * 标的的信息
     */
    private ProjectDTO project;
    /**
     * 标的对应的的所有投标记录
     */
    private List<TenderDTO> tenders;
    /**
     * 投资人年化利率（投资人让利）
     */
    private BigDecimal commissionInvestorAnnualRate;
    /**
     * 借款人年化利率（借款人让利）
     */
    private BigDecimal commissionBorrowerAnnualRate;
}

画面11：
package cn.itecast.wanpinzp.api;
import cn.itecast.wanpinzp.api.repayment.model.ProjectWithTendersDTO;
import cn.itecast.wanpinzp.common.domain.RestResponse;
public interface RepaymentApi {
    /**
     * 启动还款
     */
    @Operation(value = "projectWithTendersDTO", required = true, dataType = "ProjectWithTendersDTO", paramType = "body")
    @PostMapping("/start-repayment")
    public RestResponse<String> startRepayment(ProjectWithTendersDTO projectWithTendersDTO);
}

画面13：
@RestController
public class RepaymentController implements RepaymentApi {
    @Override
    @Operation(value = "projectWithTendersDTO", required = true, dataType = "ProjectWithTendersDTO", paramType = "body")
    @PostMapping("/start-repayment")
    public RestResponse<String> startRepayment(@RequestBody ProjectWithTendersDTO projectWithTendersDTO) {
        return null;
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、7、14：展示还款服务的流程图，包含多个步骤，如“放款成功”、“修改标的的状态”、“生成还款计划”等，流程图中包含“60%”和“45%”的进度标识。
画面4：Apollo配置中心界面，显示`application`配置项，包括`Swagger.enable`和`spring.mvc.throw-exception-if-no-handler-found`等键值对。
画面5：Apollo配置中心界面，显示`micro_service.spring-boot-dubbo`配置项，其中`spring.datasource.url`值为`jdbc:mysql://127.0.0.1:3306/wanpinzp_repayment?useUnicode=true&characterEncoding=utf8&useSSL=false`。
画面6：IDEA控制台输出日志，显示Spring Boot启动过程中的错误信息，如“Could not find meta server address”和“Sync config failed”。
画面10：IDEA中打开`ProjectWithTendersDTO.java`文件，显示类定义，包含`project`、`tenders`、`commissionInvestorAnnualRate`和`commissionBorrowerAnnualRate`等字段。
画面11：IDEA中打开`RepaymentApi.java`文件，显示接口定义，包含`startRepayment`方法。
画面12：IDEA中打开`RepaymentController.java`文件，显示类定义，尚未编写代码。
画面13：IDEA中`RepaymentController.java`文件，显示`@RestController`注解和`@Override`方法，方法名为`startRepayment`，参数为`@RequestBody ProjectWithTendersDTO`，返回值为`null`。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

