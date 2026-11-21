# 16-用户注册-服务层实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着的话呢

咱们开始讲解和实现用户注册功能的服务层代码

之前呢

咱们已经讲解并且实现了数据库的实体

还有它的数据层接口

以及呢

必要的功能

那接着的话呢

咱们就可以呢

将服务层代码呢

做个具体的编写

好

进入stop user service

在这里面呢

咱们去新加一个接口

这个呢

咱们写在上面

定义一个呢

用户注册的接口

user request

在这里面要传递什么对象呢

传递用户的信息

对不对

chad vio

那么chad user vio

这个对象呢

咱们可以看一下

在这里面呢

它是放在store common web下面

因为呢

可能会有很多其他服务节点呢

会需要用到呢

chad user用户的信息

它是继承了base vio

它的主要信息

就是用户注册

所填写的一些基本必要的资料

好

这个呢

是chad user vio的传输对象

好

那么呢

咱们还要将异常呢

抛出去

usr

我们之前呢

讲解的时候

是有工装两个异常

对不对

一个是业务异常

还有一个呢

是组件的异常

好

咱们把这两个异常呢

全部都带上

那咱们呢

先来看一下

整体的实现步骤是怎样

先加上呢

对应的注释

这个呢

是用户注册功能接口

那它的主要实现步骤呢

实现步骤是怎样呢

首先

我们要去判断这个用户呢

他是否已经注册了

对不对

如果是已经注册了

那接下来这个逻辑呢

就不用再接着去执行

然后呢

如果是没有注册

在这里呢

要对公司信息做校验

也就是说

你传递的公司呢

必须是合法的

是合法的

如果说你随便传一个公司呢

那这个肯定是不能通过的

这一点呢

要明白

然后呢

是

要构造去生成的

用户信息

咱们要把必要的一些那个信息呢

给它做一个构造

然后呢

生成我们要存储的用户对象

第四点呢

就是要完善并呢

拢于必要的用户信息

比如说你的公司的名称

对吧

还有你的机构类型等等

接着的话呢

就是注册即开户功能的实现

目的是要生成交易账户信息

好

这个呢

就是咱们主要的整体实现流程

当然

最后一步还必须要发送邮件通知

对不对

发送邮件呢

或是短信通知

但是在这里呢

咱们还没有去讲解和实现的阿里云短信

还有阿里云邮件的一个揭露功能

在这里咱们先暂时不用去实现

我们呢

可以将它标记为图度

后面呢

咱们实现了阿里云的通讯的时候呢

可以再把这块功能呢

再完善一下

那在这里呢

咱们测试是用户注册的整个

业务处理流程

好

接着的话呢

咱们就来对每一个步骤呢

做具体实现

首先呢

咱们要去创建一个

用户对象

这个话呢

是用于数据库保存的

用户对象

6

是一个新生成的用户

对不对

接着的话呢

咱们就要去做一个判断了

inert

check

就知道了

咱们只需要知道呢

它的查询的结果

我们就知道了

它是否已经注册成功

check

根据什么去判断呢

我们之前讲过了

有三个要素

对不对

一个呢

是用户编号

还有一个呢

是它的邮箱

check的user

muo.getphone

这个呢

就是咱们主流的一些必要信息

是邮箱

手机号

账户编号

接着的话呢

咱们就要做一个判断

check率照的呢

大于0

这个不等于说明是check率照的呢

说明是已经找到了

然后呢

我们还要去判断它的值

是不是大于0

对不对

如果说你查的结果呢

是0

有可能的话呢

你也是一个空查询

所以在这里呢

我们稳妥起见

还是呢

要给它做一个值的判断

好

给它抛出一个业务异常

因为这个呢

是业务处理的逻辑异常

application

给它一个错误码

这个错误码呢

是user

一个z

说明了

用户已经存在了

没法再进行注册

对不对

咱们可以看一下这个错误码

10005

用户已存在

好

接着的话呢

就要对公司信息做交易

检查呢

你所传递的公司是否合法的

因为找到的公司

咱们这个呢

是可以基于SaaS的运作

也就是说

任何的用户呢

在上面必须会有关联一个公司

如果你没有关联公司呢

你这个用户是一个不合法的用户

那我们来看一下

get company

要传递呢

它的公司ID

那么我们来做一个判断

如果是违控呢

说明是

没找到

对不对

那我没找到的话呢

你就是一个不合法的公司信息

我们也给它抛出一个异常

好

好

,我们要保存的用户底下

cad user

copy完成了

咱们别忘了

还得加上了一些必要的信息

就是你的用户编号

对不对

之前咱们讲过的全局序条生成方案

这个时候呢

就派上用场了

要去生成了

git

use number

全局唯一的用户编号

生成完这个之后呢

是不是还应该叫它的密码呢

也要做一个加密的保存

对吧

set user password

那么在这里呢

咱们就通过一个

加密工具

enquire youtube

点

enquire sign

传递呢

它的

密码信息

这个呢

是明文的

那么呢

为了保险起见

在数据库当中呢

咱们就要将它呢

以密文形式进行存储

那接着的话呢

我们还去完善一下

它的冗余信息

对不对

因为呢

用户资料

也是经常要去查询到的数据

为了减少呢

不必要的关联查询呢

咱们要将必要的信息呢

冗余一下

首先呢

是它的机构ID

机构ID

机构ID呢

就根据咱们之前所查到的

公司信息

对不对

这个时候呢

不仅可以做交易

在这里呢

冗余的时候

也派上用场了

get

instation

ID

然后new

chad user

点

set

instation

type ID

是一个类型

company

view

点

get

instation

type ID

这个咱们来看一下

到错了

看它的类型

是否正确

这个呢

是string类型

在这里呢

是一个long类型

这个呢

显然这个ID的话呢

它是一个long类型的

咱们要将这里呢

修改一下

long

好

这样的话呢

就没报酬

接着的话呢

还要去冗余它的公司名称

set company

这些的话呢

都是会经常用到的属性

好

用户信息生成完全之后呢

就可以了进行保存

stock

use the do

然后呢

隐私了

在这里面的话呢

还没有新增对不对

那咱们呢

把这个新增接口做个实现

你set

set user

给它加上一个注释

新增用户信息

接着的话呢

要给它一个map上面实现它的新增

sql

这个呢

有点长

那咱们呢

就直接拿之前实现过的代码来copy一下

找到stock user

查看找到对应的代码

直接copy到我们map文件当中

在这里呢

我们也可以采用那个mybets.generate

代码生成器呢

去生成对应的新增代码

它的一个新增的话呢

要注意

在这里呢

它会将所生成的ID呢

传递到我们这个key里面

看到没有

这个ID的话呢

并不是全局的用户编号

对不对

用户编号呢

是咱们通过方法去生成的

而这个ID的话呢

是通过买车口制增的生成的

我们把它新增一下

隐私的

newcred user

再往下面呢

咱们要实现注射及开户的功能

给它生成一个交易账户

咱们要拿到一个全局配置

判断呢

这个参数是否开启了

也就是说是否开启了注射

就给它生成一个交易账户

global

这个呢

是全局配置

好

类聚open

接着的话呢

咱们就来做一个判断

如果说这个值呢

过于空

shared

globalconfigure

并且呢

globalconfigure

它的值呢

是等于2

也就是说开启了

点get value

然后呢

对前面加上一个维护判断

防止出现一个控制成异常

那么呢

如果存在该项配置

并且值

那么就代表了注射及开户

好

咱们就要生成账户信息

怎么生成呢

shared account

给它创建一个account对象

new shared account

shared account.setaccountnumber

好呢

就要通过我们

全局序列号来生成一个交易账号

那shared account

在这里面的话

set user id

那new shared user id

这个呢

我们要调整一下

因为这个是生成全局用户笔号

这个是交易账户笔号

这两个是不一样的

对不对

那咱们呢

再copy一下

生成交易账户笔号

这个名称呢

改成user account

这个呢

也调整一下它的名称

user account number

这个呢也调整一下它的名称

这个呢也调整一下它的名称

这个呢也调整一下它的名称

这个呢也调整一下它的名称

好

生成规则呢

都一样的

但是呢

他们的那个传递的编号参数值呢

是不一样

然后呢

cad account

要去set它的group

组别

这个组别呢

咱们就默认为一

到时候咱们预制一条数据就可以了

先设置为系统默认

然后呢

还设置它的状态

它的状态呢

就是有效的

globe

默认是有效

点

ready

然后呢

咱们再设置一下它的

激活时间

这个呢就是

咱们系统生成的时间

再往下面呢就是

生成冗余信息的设置

好

要看

看一下它有哪些冗余信息呢

cad account.setinstitueid

这个呢

也是跟上面一样

将这个company view这一块呢

copy过来

那么下面的话呢

同样

把其他机构的那个冗余信息呢

直接夸比一下

company view

然后呢就是它的公司信息

set company id

company view.get id

再set它的username

username这个是new

trader

get name

set

trader group name

这个呢我们就采用系统默认主编

consistence

report group name

然后呢cad account.set balance

它的可用余额在这里呢就数字化为0

这个呢是长整形

最后呢咱们就可以了保存交易账号信息

cad account.insert do

这个话呢do还没有注入进来对不对

咱们再往上面呢

再把它注入一下

private

这些呢

先把它注入一下

再回到刚才的地方去保存交易账号

那么这个呢就是一些

咱们还没有去生成用户账号

直接呢将用户信息作为结果呢返回出来

好这个呢就是用户注册功能的业务接口具体的实现

在这里面的话呢

讲解了它的主要实验步骤

并且呢从代码上面呢做了编写

好那这一块呢就是咱们对用户注册的服务层的代码实现

最后呢咱们再回顾一下

在这里呢首先要先做用户检查

然后呢支持手机号和邮箱方式注册对不对

我们就要做重复判断

在这里呢用到了全局唯一虚拟号生产的用户偏好

通过买社口表方式呢去做的实现

那么结合拉斯廷斯的ID保障它的操作原子性

只影响了connection

可以防止了并发产生的问题

也就是说每个connection呢在这里面

它呢拉斯廷斯的ID

它只是受某个connection的影响对不对

这样呢就防止并发了产生的问题

最后呢校验通过之后保存了用户信息

邮件通知呢就在后面咱们呢实现了阿里云的对接呢

我们再把这块呢

进行完善

好那这一讲呢咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个股票交易系统（`bulls-stock-user`）的用户注册功能实现教程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了在服务层（`StockUserServiceImpl`）中如何实现用户注册的核心逻辑。主要内容包括：

*   **用户注册流程**：从接收前端传入的用户信息开始，到校验用户是否已存在、校验公司信息、生成唯一用户编号、构造用户对象、保存用户信息、生成交易账户并保存，最后返回新创建的用户对象。
*   **关键组件与技术**：
    *   **服务层**：`StockUserServiceImpl` 类中的 `userRegister` 方法。
    *   **数据访问层**：`StockUserDao` 用于数据库操作。
    *   **配置服务**：`ITradeGlobalConfigService` 用于获取全局配置，如用户编号的生成规则。
    *   **异常处理**：自定义 `BusinessException` 用于处理业务逻辑错误，如用户已存在或公司不存在。
    *   **工具类**：`BeanUtils` 用于属性拷贝，`String.format` 用于格式化用户编号。
*   **核心逻辑**：
    *   通过 `stockUserDao.checkRegister` 方法校验用户是否已注册。
    *   通过 `stockUserDao.getCompanyVoById` 方法校验公司信息。
    *   调用 `tradeGlobalConfigService.getNextSeqId` 获取全局唯一用户编号。
    *   调用 `stockUserDao.insert` 保存用户信息。
    *   调用 `tradeAccountDao.insert` 保存交易账户信息。

整个过程展示了如何在 Spring Boot 项目中实现一个完整的、包含校验和数据持久化的业务方法。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：展示项目结构和当前正在编辑的 `StockUserServiceImpl` 类，介绍本节目标是实现用户注册功能。
*   **00:06 - 00:15**：讲解 `userRegister` 方法的注解和参数，以及方法的总体流程。
*   **00:16 - 00:25**：演示第一步，调用 `stockUserDao.checkRegister` 方法校验用户是否已注册，并根据返回值抛出 `BusinessException`。
*   **00:26 - 00:35**：演示第二步，调用 `stockUserDao.getCompanyVoById` 方法校验公司信息，并根据返回值抛出 `BusinessException`。
*   **00:36 - 00:45**：演示第三步，使用 `BeanUtils.copyProperties` 将前端传入的 `tradeUserVo` 对象属性复制到 `newTradeUser` 对象中，并调用 `generateUserNo` 方法生成用户编号。
*   **00:46 - 00:55**：演示第四步，设置用户机构信息（`institutionId`, `institutionTypeId`, `companyName`），并调用 `stockUserDao.insert` 保存用户信息。
*   **00:56 - 01:05**：演示第五步，通过 `tradeGlobalConfigService` 获取全局配置，判断是否需要生成交易账户。
*   **01:06 - 01:15**：演示第五步的后半部分，如果需要生成交易账户，则创建 `TradeAccount` 对象，设置其属性（`setUserNo`, `setTradeGroupId`, `setStatus`, `setActiveTime`），并调用 `tradeAccountDao.insert` 保存。
*   **01:16 - 01:25**：演示第六步，返回新创建的 `newTradeUser` 对象。
*   **01:26 - 01:35**：展示 `generateUserNo` 方法的实现，说明其通过 `tradeGlobalConfigService.getNextSeqId` 获取序列号，并用 `String.format("%08d", nextUserNo)` 格式化为8位数字。
*   **01:36 - 01:45**：展示 `StockUserDao` 接口中的 `checkRegister` 和 `getCompanyVoById` 方法定义，说明其作用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **核心逻辑总结**：用户注册流程包括：1. 判断用户是否已注册；2. 校验公司信息；3. 生成用户编号；4. 构造并完善用户信息；5. 注册开户，生成交易账户信息；6. 发送邮件/短信通知。
    *   **技术细节**：
        *   “先做用户检查，支持手机号和邮箱注册，要重复判断。”
        *   “这里用到了全局唯一序列生成用户编号，通过Mysql表实现，结合last_insert_id函数，只影响Connection，防止并发问题。”
        *   “校验通过之后，保存用户信息。”
        *   “邮件通知待后面邮件功能实现完成之后再加上。”

*   **代码关键内容**：

    **1. `StockUserServiceImpl` 中的 `userRegister` 方法：**

    ```java
    public TradeUser userRegister(TradeUserVo tradeUserVo) throws BusinessException, ComponentException {
        // 1. 判断用户是否已经注册
        TradeUser newTradeUser = new TradeUser();
        Integer checkResult = stockUserDao.checkRegister(tradeUserVo.getUserNo(), tradeUserVo.getEmail(), tradeUserVo.getMobile());
        if (null != checkResult && checkResult > 0) {
            throw new BusinessException(ApplicationErrorCodeEnum.USER_EXISTS);
        }

        // 2. 对公司信息做校验
        CompanyVo companyVo = stockUserDao.getCompanyVoById(tradeUserVo.getCompanyId());
        if (null == companyVo) {
            throw new BusinessException(ApplicationErrorCodeEnum.USER_COMPANY_NOT_FOUND);
        }

        // 3. 构造生成用户信息
        BeanUtils.copyProperties(tradeUserVo, newTradeUser);
        newTradeUser.setUserId(generateUserNo()); // 调用生成用户编号的方法
        newTradeUser.setInstitutionId(companyVo.getInstitutionId());
        newTradeUser.setInstitutionTypeId(companyVo.getInstitutionTypeId());
        newTradeUser.setCompanyName(companyVo.getCompanyName());

        // 4. 保存用户信息
        stockUserDao.insert(newTradeUser);

        // 5. 注册开户，生成交易账户信息
        TradeGlobalConfig tradeGlobalConfig = tradeGlobalConfigService.getTradeGlobalConfigByCode(GlobalConstants.TRADE_ACCOUNT_CONFIG_CODE);
        if (null != tradeGlobalConfig && GlobalConfig.VALUE_TRUE.equals(tradeGlobalConfig.getValue())) {
            TradeAccount tradeAccount = new TradeAccount();
            tradeAccount.setAccountNo(generateUserNo()); // 生成交易账户编号
            tradeAccount.setUserId(newTradeUser.getId());
            tradeAccount.setTradeGroupId(1L); // 设置默认组
            tradeAccount.setStatus(GlobalConfig.STATUS_VALID); // 设置状态为有效
            tradeAccount.setActiveTime(new Date()); // 设置激活时间
            tradeAccountDao.insert(tradeAccount);
        }

        // 6. 返回新创建的用户对象
        return newTradeUser;
    }
    ```

    **2. `StockUserServiceImpl` 中的 `generateUserNo` 方法：**

    ```java
    private String generateUserNo() {
        // 获取用户账号
        Long nextUserNo = tradeGlobalConfigService.getNextSeqId(GlobalSeq.USER_NO);
        log.info("get the next userNo : " + nextUserNo);
        // 其中0表示前缀，后缀标识长度
        return String.format("%08d", nextUserNo);
    }
    ```

    **3. `StockUserDao` 接口中的方法：**

    ```java
    Integer checkRegister(@Param("userNo") String userNo, @Param("email") String email, @Param("mobile") String mobile);
    CompanyVo getCompanyVoById(@Param("id") Long id);
    ```

---

### 4) 关键场景与演示描述

*   **场景一：用户注册流程的开始**
    *   讲师在 `StockUserServiceImpl` 类中定位到 `userRegister` 方法。
    *   通过注释和代码，演示了方法的输入参数（`TradeUserVo`）和返回值（`TradeUser`）。
    *   展示了方法的总体流程注释，为后续代码编写提供指导。

*   **场景二：用户存在性校验**
    *   讲师调用 `stockUserDao.checkRegister` 方法，传入用户手机号、邮箱和用户名。
    *   通过 `if (null != checkResult && checkResult > 0)` 判断，如果返回值大于0，说明用户已存在。
    *   演示了抛出 `BusinessException(ApplicationErrorCodeEnum.USER_EXISTS)` 异常，阻止重复注册。

*   **场景三：公司信息校验**
    *   讲师调用 `stockUserDao.getCompanyVoById` 方法，传入公司ID。
    *   通过 `if (null == companyVo)` 判断，
