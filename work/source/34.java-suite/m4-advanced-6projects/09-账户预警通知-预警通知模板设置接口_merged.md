# 09-账户预警通知-预警通知模板设置接口 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着咱们去实现预警通知模板的设置接口

用户预警通知是可以根据用户的偏好来设定不同的条件

去触发生成相应的通知

并且可以通过在内信邮件或者是短信的方式发送给用户

那常见的预警通知包含止盈止损通知

股票日内的涨跌幅

变动比例

以及价格等等

这里我们就以比较常见且主要的通知

止盈止损通知为例

做一个具体的讲解

首先咱们还是画下整个流程图

加深大家对整个流程的理解

首先咱们要去设定预警通知的模板

预警通知模板其实有很多种

在这里我们可以列出它的主要预警通知模板

比如说这个呢

是止盈止损

然后还有股票的日内涨跌幅

还可以有股票的变化价格

也就是它的涨跌价格

这里咱们就是侧重实现止盈止损的通知

其他类型的通知

大家有时间的话呢

可以借鉴止盈止损的通知去做相应的实现预警通知的模板

一般呢

是由管理人员去做相应的设置

APP用户

他是不能够去设置预警通知模板

这一点大家要理解清楚

他们是不同的身份

操作的功能是不一样的

那APP用户

他能够去设置账户的预警通知

这个账户就是针对于他个人

比如说他可以设定某只股票的止盈止损的价格

APP用户设置完成之后

咱们后台调度服务

就可以根据预警通知的模板

以及账户预警通知的条件去生成

相应的预警通知记录

预警通知记录是由交易调度服务生成

然后调度服务根据生成的预警通知记录

可以去实现预警通知的推送

预警通知推送

它包括两种处理方式

一种是我们常用的APP推送

另外一种就是离线方式的推送

这里我们是基于阿里云的短信邮件推送

好

这一块就是整体预警通知的处理流程

那咱们回到讲义当中

通知模板是由管理人员进行配置维护

它可以支持内线的变量

这样管理起来更为灵活

如果需要调整格式

不需要再去调整相应的实现代码

这里是我们模板设置的一个事例

那咱们看一下预警通知模板的整体表结构

这个是预警类型

预警类型我们在这里是分为止损和止盈

下面是通知方式

通知方式包括APP在内信

email邮件

SMS短信方式

下面是模板的内容

然后是消息的标题

这个是模板的状态

然后是管理员的信息

下面就是操作时间

接下来咱们看一下数据层的接口

这里我们是通过SpringData REST做的实现

咱们回到工程中

定义到相应的代码

整体实现比较简单

咱们就将代码直接引入进来

这里主要提供了三个接口

一个是根据消息类型

获取账户预警通知模板

接下来是根据ID来运行的

获取预警通知信息模板

这个是要获取完整的对象信息

这个接口我们可以看到

它可能会存在多条

那么只取其中一个对象

下面是保存数据接口

这里加入了缓存的处理

因为要提升处理效率

咱们在模板获取的时候

加入了缓存功能

所以在做数据保存的时候

需要更新对应的缓存

缓存的key A0是代表第一个闪烁

参数位是从0开始

采用参数名称作为key也可以

但是通过参数位

它可以防止参数为空出现的空子人异常

好

那咱们回到讲义当中

接下来就是对服务层接口的实现

服务层主要是提供了模板的设置与更新的接口

咱们可以回到工程当中

定位到具体的代码

咱们来看一下这个接口是如何处理的

首先是对传递的预警信息模板

并设置模板做一个判断

如果ID为空

说明是新增数据

在这里就要去校验数据的重复性

根据预警通知类型去做相应的判断处理

一般系统当中只会存在一个预警类型的模板

比如说指引类型一个模板

止损类型一个模板

如果是存在重复

要抛出相应的异常提示

接着就是对数据进行保存和更新

接下来咱们再来看一下web层的接口

account1,template,controller

咱们回到工程中

定位到controller

这个是SplintBoot实现的模板设置接口

通过SplintDataRest

也可以实现模板的设置接口

但是在这里它还会暴露相应的增删改查接口

如果是对于比较重要的业务接口

或者业务实现复杂度相对比较高一些

咱们就可以采用SplintBoot的接口做相应的解析

这里是提供了预警通知模板的保存接口

它只支持POST的方式调用

增加了SWOG注解

然后调用service的接口

对模板进行了保存

这里要将当前登录的用户信息作为参数传递进去

好,这一讲咱们就对预警通知模板设置接口做了一个讲解

整体实现代码并不复杂

大家要着重掌握预警通知的方式

整体处理流程

那这一讲的内容咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程聚焦于一个股票交易系统中“用户预警通知”功能的后端实现。讲师通过演示如何从零开始构建一个完整的预警通知模板管理模块，详细讲解了从数据库表结构设计、到数据访问层（Repository）、服务层（Service）再到控制器层（Controller）的完整开发流程。核心内容包括：定义预警模板的数据库表结构（如 `warnType`、`notifyType` 等字段）、实现数据持久化操作（如 `saveTemplate` 方法）、以及通过 Spring Boot 的 RESTful API 提供对外接口。整个过程旨在展示如何在实际项目中，通过分层架构和标准注解，实现一个可配置、可扩展的业务功能。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**：课程开场，讲师介绍本节将实现“预警通知模板设置接口”。
*   **00:15 - 00:35**：展示并讲解预警通知模板的数据库表结构，包括字段 `id`, `warnType`, `notifyType`, `content`, `title`, `status`, `lastUpdateBy` 等及其数据类型和注释。
*   **00:35 - 01:00**：进入代码实现阶段，首先展示 `AccountWarnTemplate` 实体类的定义，以及 `AccountWarnTemplateRepository` 接口中的 `getDistinctByWarnType` 方法。
*   **01:00 - 01:30**：讲解服务层 `AccountWarnTemplateServiceImpl` 的实现，重点是 `saveTemplate` 方法，其中包含对模板重复性的校验逻辑。
*   **01:30 - 02:00**：演示控制器层 `AccountWarnTemplateController` 的实现，展示如何通过 `@PostMapping` 注解暴露一个保存模板的 REST API。
*   **02:00 - 02:30**：总结本节内容，强调通过分层架构实现接口，并为后续的“账户预警通知”功能做铺垫。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **章节标题**：`3. 实现`，下设子章节 `3.1 实现预警通知模板设置接口`。
*   **模板示例**：`尊敬的客户，您所持有的产品${stockCode}，当前价格${stockPrice}元，已达到止损比例${stopProfitRate}，请您及时处理。`
*   **模板表结构**：
    *   **属性**：`id`, `warnType`, `notifyType`, `content`, `title`, `status`, `lastUpdateBy`。
    *   **名称**：主键标识、预警类型、通知方式、模板内容、消息标题、消息状态、最后跟新人id。
    *   **数据类型**：`bigint(19)`, `tinyint(3)`, `varchar(32)`, `varchar(2000)`, `varchar(255)`, `tinyint(3)`, `bigint(19)`。
    *   **是否为空**：`NO`, `NO`, `NO`, `YES`, `YES`, `YES`, `YES`。
    *   **注释**：主键标识、预警类型(0:止损, 1:止盈)、通知方式(APP:站内信, EMAIL:邮件, SMS:短信)、模板内容、消息标题、消息状态(0:启用, 1:禁用)、最后跟新人id。

#### 代码内容

*   **实体类 `AccountWarnTemplate`**：
    ```java
    @Api(value = "HATEOAS接口-菜单操作管理", ... )
    @Entity(name = "t_authority_menu_operation")
    public class AuthorityMenuOperation extends BaseEntity {
        private Long menuId;
        private String operationName;
    }
    ```
*   **数据访问层 `AccountWarnTemplateRepository`**：
    ```java
    @Override
    default public void customizeQuerydslBindings(bindings, QAccountWarnTemplate obj) {
        bindings.bind(obj.first(StringExpression::contains)); // 粗略查询
    }
    @ApiOperation(value = "根据ID获取预警通知信息模板")
    @ApiImplicitParam(value = "ID唯一标识", name = "id", dataType = "Long", required = true)
    AccountWarnTemplate getByID(@Param("id") Long id);
    ```
*   **服务层 `AccountWarnTemplateServiceImpl`**：
    ```java
    @Service
    public class AccountWarnTemplateServiceImpl implements IAccountWarnTemplateService {
        @Autowired
        private AccountWarnTemplateRepository accountWarnTemplateRepository;
        // 保存或更新模板
        @Override
        public void saveTemplate(AccountWarnTemplate accountWarnTemplate, AuthorityUser user) throws ComponentException {
            if (null == accountWarnTemplate.getId()) {
                accountWarnTemplate.setCreateTime(new Date());
            }
            // 检验数据的重复性
            AccountWarnTemplate accountWarnTemplateDB = accountWarnTemplateRepository.getDistinctByWarnType(accountWarnTemplate.getWarnType());
            if (null != accountWarnTemplateDB) {
                throw new ComponentException(ApplicationErrorCodeEnum.ACCOUNT_WARN_TEMPLATE_TYPE);
            }
            // 保存或更新数据
            accountWarnTemplate.setLastUpdateBy(user.getId());
            accountWarnTemplate.setLastUpdateTime(new Date());
            accountWarnTemplateRepository.save(accountWarnTemplate);
        }
    }
    ```
*   **控制器层 `AccountWarnTemplateController`**：
    ```java
    @RestController("/accountWarnTemplate")
    public class AccountWarnTemplateController extends BaseController {
        @Autowired
        private AccountWarnTemplateService accountWarnTemplateService;
        @PostMapping(value = "/saveTemplate")
        @ApiOperation(value = "保存预警通知模板")
        public ApiRespResult<String> saveTemplate(AccountWarnTemplate accountWarnTemplate) {
            ApiRespResult result = null;
            try {
                accountWarnTemplateService.saveTemplate(accountWarnTemplate, getUser());
                result = ApiRespResult.success();
            } catch (Exception e) {
                log.error(e.getMessage(), e);
                result = ApiRespResult.sysError(e.getMessage());
            }
            return result;
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：数据库表结构设计**（00:15 - 00:35）
    *   讲师在文档中滚动展示 `预警通知模板表结构` 的表格，逐行讲解每个字段的含义、数据类型和约束条件。特别强调了 `warnType` 字段用于区分“止损”和“止盈”，`notifyType` 字段用于区分通知方式（APP、EMAIL、SMS），以及 `status` 字段用于控制模板的启用/禁用状态。

*   **场景二：服务层代码实现**（01:00 - 01:30）
    *   讲师在 IDE 中打开 `AccountWarnTemplateServiceImpl.java` 文件，演示 `saveTemplate` 方法的实现。他重点讲解了如何通过 `getDistinctByWarnType` 方法查询数据库，以检查用户是否已存在相同类型的预警模板，从而避免数据重复。代码中包含了详细的注释，解释了每个步骤的目的。

*   **场景三：控制器层接口暴露**（01:30 - 02:00）
    *   讲师在 IDE 中打开 `AccountWarnTemplateController.java` 文件，演示如何使用 `@PostMapping` 注解定义一个 RESTful API。他解释了该接口的 URL 路径 `/saveTemplate`，并展示了如何将前端传来的 `AccountWarnTemplate` 对象和用户信息传递给服务层进行处理。同时，他强调了使用 `@ApiOperation` 和 `@ApiImplicitParam` 注解来为 Swagger 提供接口文档。

*   **场景四：代码调试与异常处理**（01:30 - 02:00）
    *   在演示服务层代码时，讲师在 `saveTemplate` 方法中添加了 `try-catch` 块，用于捕获可能发生的异常，并将异常信息封装成 `ApiRespResult.sysError` 返回给前端，以提供友好的错误提示。这体现了良好的异常处理和错误反馈机制。
