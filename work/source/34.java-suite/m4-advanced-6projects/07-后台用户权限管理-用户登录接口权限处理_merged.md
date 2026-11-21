# 07-后台用户权限管理-用户登录接口权限处理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始去实现了后台的用户登录接口

咱们来看一下它这一块的具体实现

那首先呢

咱们要在user service实现内当中呢

添加对应的接口

去实现用户登录处理的逻辑

好

在这里咱们回到代码当中

找到对应的service

authentic user service implement

之前的咱们实现了新增用户的接口

接着的话呢

咱们去添加新的接口

这个接口的话呢

是用户登录接口的处理

那咱们来做一个具体实现

首先呢

我们要梳理一下整个的实现流程

第一步呢

先要去查找用户

判断呢

用户是否存在

如果用户不存在呢

就抛出一场

也就没法处理呢

下面的逻辑

第二步呢

我们要去对用户登录密码

做校园判断

在这里呢

是采用加密的形式

去比较用户所传递过来的密码

第三步

咱们要记录

用户的登录信息

比如说用户的登录时间啊

登录IP啊

等等

第四步呢

咱们要获取

用户的角色权限

并且呢

要

拿取

最大的

最大的

角色权限信息

因为用户呢

可能会分配多个机构的角色权限

所以呢

咱们要从中呢

去查询

筛选出最大的角色权限

第五步呢

要获取用户的角色菜单操作权限信息

将它存录在Ladies环境当中

用于咱们后面的权限控制处理

好

那接着呢

咱们就来对代码做一个具体实现

虽然用户登录接口呢

看起来比较简单

就做一个登录操作

但是它实际上要做的事情呢

处理的内容还是比较多

首先呢

咱们就去通过数据层接口

拿到呢

用户对象

Ausility

User

Ausility User

在这里面呢

通过数据层接口

User

User

Find One

这里呢

仍然是采用之前呢

所实现的方法

根据呢

用户账号去获取到用户信息

然后呢

咱们加一个判断

这里呢

就要做一个不存在的判断

User

Is Present

然后呢

咱们要抛出一个异常

我们判断一个Safety

给它一个抽物码

Application Add Code

提示呢

账号不存在

没有找到

接下来呢

咱们就来去对这个用户密码呢

做一个交易判断

咱们呢

首先拿到用户对象

这里呢

咱们将名称调整下

改成了Operate

这个话呢

才是实际的用户对象信息

点Get

信息

并快开

Password

通过了咱们的加密工具

去将用户传递的密码呢

进行一个加密处理

然后呢

再和数据库当中

所查询的密码呢

做一个比较判断

Get User Password

如果是不一致呢

咱们要将异常的抛出

Compend Exception

给它一个抽码

提示呢

Add Me User

Count

密码呢

抽

接着的话呢

咱们就要记录了用户的登录信息

记录了它的最后的登录时间

就是当前的服务器时间

然后呢

设置它的

最后一次的登录IP

这个就是它NIP

可以从上

可以从上

从上层

Control层当中呢

通过Client IP参数进行传递

然后呢

就可以保存咱们的User对象

这里面呢

是一个更新处理

因为呢

这个Auxiliary User呢

是从数据库里面查询出来的

它会有一个ID

那么通过JPEG接口的话呢

如果是有ID

找到对应数据之后呢

它就会做更新

并不会新增

第四个步骤呢

要获取用户的角色选项

拿取最大的角色

首先咱们必须要查到呢

这个用户下面呢

所分配的所有角色

通过数据层接口

Auxiliary User Load

Libsitory去调用了

By User ID

那么我们也做一个围攻判断

如果是没找到呢

说明这个呢

权限分配

这个数据呢是存在问题的

让咱们要抛出对应的异常

给它一个错误码

提示呢

没有分配角色信息

那接着的话呢

我们看一下如何去获取

这里面所有角色

的最大权限呢

咱们先写一下这个代码

这个呢

我们先写一个空的方法

get

pair

获取最大右前期的角色权限

user load

然后呢

传入刚才的list

loadlist的集合

通过这个方法呢

它就会获取最大权限的

Auxiliary User Load对象

然后呢

我们就可以去拿到它的角色ID

咱们呢

就来对这个方法做个具体实现

创建方法

我们将它的返回对象呢

做个修改

加上对应的注释

这个是获取最大的权限角色

之前呢

咱们讲过整个平台当中的权限优先级呢

它的顺序是集团

集团下面的角色呢

是属于最高优先级

接着的话呢

是运营中心

再往下面呢

就是交易商

这个呢

是他们的一个优先级规则

那我们怎么去快速实现呢

我们就在这里呢

将这三个角色定义为三个产量

然后将这三个产量呢

加入到list的集合对象当中

那么加入的顺序呢

我们也按照它的优先级来

集团角色呢

就放在最前面

接着的话运营中心

然后是交易商

那么我们再根据呢

传递过来的用户角色做一个遍地判断

因为list呢

优先判断的是权限最大的

所以呢

如果是优先匹配到

咱们呢

就可以直接将对象呢

作为结果返回出来

好

那接着呢

我们再做个具体实现

首先咱们定义一个list的集合

给它加上一个说明

将平台角色权限呢

按优先级排列

转换成为集合

最大权限的角色呢

放在前面

通过alias as list

global consistence

institution

首先呢加入集团

接着呢咱们再加入运营中心

最后呢就是交易商

这样呢这个集合的第一个说明位置呢

就是最大的权限

也就是集团角色

好

然后呢咱们做一个

便利匹配处理

将用户的

角色

权限信息

做便利匹配处理

外层过循环

institution

然后呢咱们来做一个过滤处理

用这个我们定义

将用户传递过来的角色呢

做个便利

按流逝转换来进行处理

然后呢通过pill的方法进行了具体的过滤

item.getinstitutiontypeid

做个判断

然后呢find the first

将它的第一条记录呢做返回

对于它的这个成绩顺序

pill的方法呢是到这里为止

然后呢是find the first

然后呢我们做一个判断

也就是说如果是找到呢

咱们就将结果呢直接返回出去

否则如果没有pill到呢

咱们就

按默认来处理

就直接呢返回第一个结果

好这个呢

就是

获取用户最大的

权限角色的处理逻辑

那下面呢

还有一些逻辑要做对应的处理

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于一个名为 `bulls-stock-admin-user` 的 Spring Boot 项目中，后台用户登录接口的业务逻辑实现。讲师通过 IntelliJ IDEA 的代码编辑器，逐步演示了 `AuthorityUserServiceImpl` 类中 `userLogin` 方法的完整实现过程。该方法主要包含以下核心步骤：
1.  **用户存在性校验**：通过 `authorityUserRepository` 查询用户，若不存在则抛出 `ADMIN_USER_ACCOUNT_NOT_FOUND` 异常。
2.  **密码校验**：获取用户密码并进行加密后，与数据库中存储的加密密码进行比对，若不匹配则抛出 `ADMIN_USER_ACCOUNT_PASSWORD_ERROR` 异常。
3.  **登录信息记录与持久化**：更新用户的最后登录时间和 IP 地址，并将用户对象保存回数据库。
4.  **角色权限获取**：根据用户 ID 查询其拥有的角色列表，并调用 `getPriorityAuthorityUserRole` 方法获取具有最高权限的角色ID。
5.  **权限信息处理**：将角色ID转换为权限字符串列表，用于后续的权限控制。

整个过程展示了如何在服务层实现一个完整的、包含异常处理和数据持久化的用户登录功能。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，展示课程大纲，当前章节为“1.5 后台用户登陆接口实现”。
*   **00:00:05 - 00:00:15**：进入 `AuthorityUserServiceImpl` 类的代码编辑器，展示类的结构和注入的两个 Repository。
*   **00:00:15 - 00:00:30**：聚焦于 `userLogin` 方法的定义，展示方法的参数和注释。
*   **00:00:30 - 00:00:45**：演示第一步，通过 `authorityUserRepository.findone` 查询用户并进行存在性判断，若不存在则抛出 `ADMIN_USER_ACCOUNT_NOT_FOUND` 异常。
*   **00:00:45 - 00:01:00**：演示第二步，获取用户对象并进行密码校验，使用 `EncryptUtil.encryptSigned(password)` 对输入密码进行加密，并与数据库中的密码进行比对，若不匹配则抛出 `ADMIN_USER_ACCOUNT_PASSWORD_ERROR` 异常。
*   **00:01:00 - 00:01:15**：演示第三步，记录用户的登录时间和 IP，并将更新后的用户对象保存到数据库。
*   **00:01:15 - 00:01:30**：演示第四步，查询用户的角色列表，并调用 `getPriorityAuthorityUserRole` 方法获取最大权限的角色ID。
*   **00:01:30 - 00:01:45**：演示第五步，将角色ID转换为权限字符串列表，用于后续的权限控制。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **章节标题**：`1.5 后台用户登陆接口实现`
    *   **代码文件**：`AuthorityUserServiceImpl.java`
    *   **方法签名**：
        ```java
        public AuthorityUser userLogin(String userAccount, String password, String clientIp)
        ```
    *   **方法注释**：
        ```java
        /**
         * 用户登陆接口处理逻辑
         * @param username
         * @param password
         * @param clientIp
         * @throws ComponentException
         */
        ```

*   **关键代码片段**：

    *   **用户存在性校验**：
        ```java
        Optional<AuthorityUser> authorityUserOpt = authorityUserRepository.findone(equalsUsername);
        if (!authorityUserOpt.isPresent()) {
            throw new ComponentException(ApplicationErrorCodeEnum.ADMIN_USER_ACCOUNT_NOT_FOUND);
        }
        ```

    *   **密码校验**：
        ```java
        AuthorityUser authorityUser = authorityUserOpt.get();
        String encryptPassword = EncryptUtil.encryptSigned(password);
        if (!authorityUser.getPassword().equals(encryptPassword)) {
            throw new ComponentException(ApplicationErrorCodeEnum.ADMIN_USER_ACCOUNT_PASSWORD_ERROR);
        }
        ```

    *   **记录登录信息并保存**：
        ```java
        authorityUser.setLastLoginTime(new Date());
        authorityUser.setLastLoginIp(clientIp);
        authorityUserRepository.save(authorityUser);
        ```

    *   **获取角色权限**：
        ```java
        List<AuthorityUserRole> roleList = authorityUserRoleRepository.findByUserId(userId);
        if (null == roleList || roleList.size() < 1) {
            throw new ComponentException(ApplicationErrorCodeEnum.ADMIN_USER_NOT_ASSIGN);
        }
        Long roleId = getPriorityAuthorityUserRole(roleList).getRoleId();
        ```

    *   **获取权限字符串列表**：
        ```java
        String authResources = AuthResources.getAuthResources(roleId);
        List<String> authList = Arrays.asList(authResources.split(","));
        ```

---

### 4) 关键场景与演示描述

*   **场景一：方法定义与结构展示 (00:00:05-00:00:15)**
    *   讲师首先展示了 `AuthorityUserServiceImpl` 类的代码结构，重点介绍了其 `@Service` 注解和注入的两个 Repository：`AuthorityUserRepository` 和 `AuthorityMenuRepository`。这为后续的业务逻辑实现奠定了基础。

*   **场景二：用户存在性校验 (00:00:30-00:00:45)**
    *   讲师将光标移动到 `userLogin` 方法中，演示了如何使用 `authorityUserRepository.findone` 方法根据用户名查询用户。通过 `Optional` 类型的返回值，讲师展示了如何判断用户是否存在，并在不存在时抛出 `ADMIN_USER_ACCOUNT_NOT_FOUND` 异常。

*   **场景三：密码校验 (00:00:45-00:01:00)**
    *   讲师演示了如何获取用户对象，并使用 `EncryptUtil.encryptSigned(password)` 方法对输入的密码进行加密。接着，他将加密后的密码与数据库中存储的密码进行比对，若不匹配，则抛出 `ADMIN_USER_ACCOUNT_PASSWORD_ERROR` 异常。

*   **场景四：登录信息记录与持久化 (00:01:00-00:01:15)**
    *   讲师演示了如何更新用户的登录时间和 IP 地址，并调用 `authorityUserRepository.save(authorityUser)` 方法将更新后的用户对象保存回数据库，确保数据的一致性。

*   **场景五：角色权限获取 (00:01:15-00:01:30)**
    *   讲师演示了如何通过 `authorityUserRoleRepository.findByUserId(userId)` 查询用户的角色列表。他强调了对角色列表的校验，确保用户至少拥有一个角色。接着，他调用 `getPriorityAuthorityUserRole(roleList)` 方法，该方法会根据角色的优先级（如机构类型）返回具有最高权限的角色ID。

*   **场景六：权限信息处理 (00:01:30-00:01:45)**
    *   讲师演示了如何将角色ID转换为权限字符串列表。他调用 `AuthResources.getAuthResources(roleId)` 方法获取权限字符串，并使用 `Arrays.asList` 方法将其转换为 `List<String>`，以便后续用于权限控制。
