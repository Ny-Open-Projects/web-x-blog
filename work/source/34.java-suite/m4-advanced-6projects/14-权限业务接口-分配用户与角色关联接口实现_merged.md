# 14-权限业务接口-分配用户与角色关联接口实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来咱们接着呢

去实现分配用户与角色关联关系接口

之前呢

咱们是实现了角色和菜单

以及呢操作关联的权限接口

那么有了之前这个接口的实现了

咱们就可以呢

将对应的角色分配给相应的用户

用户和角色呢

是一个多对多的关系

那咱们来看一下具体该如何去实现

回到咱们代码工程当中

找到业务实现类

那在下面呢

添加一个接口

public user assign loss

这里面要存进的参数呢

是authority user load

还有什么参数呢

还有对应的用户信息

authority user

然后呢要拋出对应的异常

加上对应的注释说明

这个呢是分配用户与角色的关联

关系接口

那首先呢

我们仍然是要打印了对应的日子

让这个类名呢

扣一下

然后咱们将他的参数呢

打印出来

因为这个呢

是用户和角色的关联

所以咱们打印这个关联的对象

在这里面呢

它会包含具体的信息

打印这个对象呢

就可以了

那我们看一下具体实现步骤是怎样的

第一步咱们是要查找用户

已分配的

角色信息

第二步呢

获取需要分配的角色详情

第三步呢

要校验用户呢

它是否存在多个

相同机构类型的角色

咱们之前做了讲解对不对

我们这个平台下面呢

会存在三种运营身份

一个呢是集团

另外一个是运营中心

还有呢就是交易商

一个用户呢

他可以拥有不同运营身份的角色

但是呢

他不能拥有相同运营身份的不同角色

也就是说他不能拥有在不同交易商下面的不同角色

他只能拥有了一个交易商所关联的角色

那么在这里要做必要的判断

第四个步骤呢

要保存用户与角色的关联关系

那咱们呢

主意对这些步骤呢

做个实现

我说的一体牛载肉

这个呢

是一个集合对象

这个呢

咱们要将那个数据层接口注入进来

在下面呢

添加一个来为的

保守一体

牛载肉

这个呢

是用户与角色的关联数据

接口

然后咱们还要注入一个呢

角色的数据层接口

这个角色

这个呢

已经有了

我们就不需要再注入

好

咱们回到代码当中呢

继续实现刚才的逻辑

保守内体

好

用着

肉

这个是一头的

饭的

哦

买优载的

这里呢

我们就将参数信息呢

传递进去

保守

有载肉

获取呢

传递的用户ID

那么拿到这个信息呢

进行之后呢

接着咱们还去查询了

角色相形

根据呢

ID来获取

获取呢

角色ID

然后这里呢

还在GET才能呢

获取真正的对象

接着呢

咱们就来做个判断

一个用户呢

他不能存在

相同机构的不同角色

那咱们呢

就要做一个便利处理

便利呢

他已经分配的角色信息

那么呢

那么拿到分配的角色信息之后呢

咱们就要判断了这个角色所对应的机构类型

也是推选

拍白地

演绎果实

这个呢

和要分配的机构类型呢

做一个对比

如果是相同的话呢

说明了这个用户

他是存在

相同

其后的不同角色不能进行保存

要抛出一场

这个呢

是咱们的系统结束

将这个异常错误码了

抛出返回给购物端

Element

User

Integration

Unical

这错误码呢

就是说

用户呢

他不能添加相同机构类型的角色

避免了一个用户

他关联了相同机构类型下面的不同角色权限

这样呢

咱们系统也不好去处理

好

最后呢

就是保存用户和角色的关联关系

这个保存起来呢

要将

AusleyUserLow的信息呢

要补充完善下

比如说他的

角色名称啊

这些信息咱们要将垄断

那么咱们呢

就从代码当中做一个copy

那么咱们再来看一下

他要保存哪个信息呢

这里呢

是角色名称

然后呢

是机构的类型

下面的是机构的名称

这里呢

就是他的创建信息

这个data呢

咱们将他给回来

好

最后呢

就是保存

调用了数据层的操作接口

对用户和角色的关联数据进行保存

这里呢

就是完善用户与角色的关联数据

好

接着话呢

咱们再从展示当中呢

对整个流程做一个回顾

后台这里呢

他是凑顺业务功能的实现

这里的参数还有常规的业务教验呢

就交由前端去判断控制

当然在实际生产环境当中呢

后台还是要加上这些必要性的教验

比如说你传递过来的参数

唯空的一些判断

然后他的一些说法性等等

这样呢

可以保持代码的健康性

那么整个的处理逻辑流程是怎样的

首先是要根据用户ID去查询的用户所分配的所有角色

那么拿到这些信息之后呢

接下来咱们就能做对应的对比

接着我们要去根据指派的角色ID要获取的角色详情

然后就是具体的对比和处理逻辑

检查指派的角色ID呢

他所对应的机构类型

然后呢

和我们这边所分配的角色的对应的机构类型的做一个判断

是否会存在重复

如果是重复呢

就要抛出一场

因为呢

系统是做了限制一个用户呢

他可以有多个角色

但是呢

机构类型是不能够重复的

最后呢

咱们就要去组装和完善了用户和角色的关联数据

然后呢

要用数据层接口进行了保存

好

接下来呢

还去实现concealer层的代码接口

那么咱们呢

将这个接口呢

就直接copy过去

找到咱们的concealer

咱们加上对应的注释

这个是分配用户

与角色关联关系接口

post mapping呢

是指示是post的方式调用

这个呢

是他的请求路径

API operation呢

是作为SWARC的注解描述说明

那么这个接口呢

咱们还没抽取出来

咱们回到刚才的时间内当中

右键

replac

form members up

将它呢

抽取出来

然后呢

点击replac

这样呢

他就抽取出来了

之后呢

加上了一个重写的注解

咱们回到controller省当中

这里呢

就没报错了

那么他要传递的参数呢

就是user load对象

user load对象呢

他的信息其实很简单

一个呢

是user ID

一个呢

是你要分配的角色ID

那么在这里呢

还有一个什么

get user

这个作用呢

我们也可以看到代码的实现

authorize user呢

他会将他的信息呢

放置到用户和角色的关联对象当中

也是呢

做了信息的一个记录

对他的创建人

他的修改人

那么controller省当中呢

这get user应该就是当前session操作的用户

我们呢

就将这个方法这个实现

获取用户信息呢

很多接口他都需要去使用

所以呢

要把它封装在basecontroller省下面

好

那在这里呢

咱们再创建一个

接口

这个就作为controller省的误类

然后呢

我们把这个get user方法呢

放置进去

如果是还有一些公用的方法

咱们呢都可以放在basecontroller省当中

回到刚才的logit

controller

然后呢

我们要做一个继承

继承了basecontroller

这样的话呢

就能够

要用呢get user方法

拿取呢

用户的信息

他的拿取来讲呢

也是比较简单

是直接呢

从session当中

获取呢

对应的user对象

如果是不存在呢

就刨除一场

下面的逻辑的话呢

就会被被用户继续处理

好

这一块呢

就是用户和爵士的分配业务接口的实现

那这一讲的知识呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“bulls-stock-admin-user”的 Spring Boot 项目中，实现“用户与角色分配”核心业务逻辑的教程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 `AuthorityLogicServiceImpl` 服务层中编写 `userAssignRoles` 方法。该方法的核心逻辑包括：1) 查询用户已分配的角色；2) 查询需要分配的角色详情；3) 校验用户是否在多个相同机构类型的角色；4) 保存用户与角色的关联数据。过程中，讲师还讲解了如何使用 `@Autowired` 注解注入 Repository、如何定义和使用自定义异常 `ApplicationErrorCodeEnum`，以及如何通过 HQL 语句进行跨表查询（虽然在本片段中未完整展示）。整个过程旨在教授如何实现一个健壮、可维护的权限分配服务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开场，展示课程大纲，定位到“3.7 权限核心逻辑接口实现（重要）”。
*   **00:00:05 - 00:00:15**: 展示 `AuthorityLogicService` 接口定义，包含 `userAssignRoles` 方法的签名，参数为 `AuthorityUserRole` 和 `AuthorityUser`，并抛出 `ComponentException`。
*   **00:00:15 - 00:00:30**: 切换到 `AuthorityLogicServiceImpl` 类，开始编写 `userAssignRoles` 方法的实现。
*   **00:00:30 - 00:00:45**: 讲解方法的第一步：通过 `authorityUserRoleRepository.findByUserId` 查询用户已分配的角色列表。
*   **00:00:45 - 00:01:00**: 讲解方法的第二步：通过 `authorityRoleRepository.findById` 查询需要分配的角色详情。
*   **00:01:00 - 00:01:15**: 讲解方法的第三步：遍历已分配角色列表，校验用户是否在多个相同机构类型的角色，若存在则抛出 `ComponentException`。
*   **00:01:15 - 00:01:30**: 讲解方法的第四步：为 `AuthorityUserRole` 对象设置角色名称、机构类型ID、机构ID、创建者、创建时间、更新者和更新时间等属性。
*   **00:01:30 - 00:01:45**: 讲解方法的第五步：调用 `authorityUserRoleRepository.save(authorityUserRole)` 保存用户与角色的关联数据。
*   **00:01:45 - 00:02:00**: 展示 `ApplicationErrorCodeEnum` 的定义，用于抛出自定义异常，例如 `ADMIN_USER_INSTITUTION_UNIQUE`。
*   **00:02:00 - 00:02:15**: 展示 `BaseController` 类，用于演示如何获取 `HttpSession`。
*   **00:02:15 - 00:02:30**: 展示 `AuthorityLogicService` 接口的完整定义，包括 `@Service` 注解和方法签名。
*   **00:02:30 - 00:02:45**: 展示 `AuthorityLogicServiceImpl` 类的完整实现，包括 `@Service` 注解和 `userAssignRoles` 方法。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：`3.7 权限核心逻辑接口实现（重要）`。
    *   接口定义：`AuthorityLogicService` 接口，方法签名 `public void userAssignRoles(AuthorityUserRole authorityUserRole, AuthorityUser authorityUser) throws ComponentException`。
    *   服务实现：`AuthorityLogicServiceImpl` 类，方法实现 `public void userAssignRoles(AuthorityUserRole authorityUserRole, AuthorityUser authorityUser) throws ComponentException`。
    *   异常枚举：`ApplicationErrorCodeEnum`，包含 `ADMIN_USER_INSTITUTION_UNIQUE` 等错误码。
    *   代码注释：`// 1. 查询用户已分配的角色信息`，`// 2. 获取需要分配的角色详情`，`// 3. 校验用户是否存在多个相同机构类型的角色`，`// 4. 保存用户与角色的关联关系`，`// 5. 保存用户角色数据`。

*   **代码关键内容**:

    **1. 接口定义 (AuthorityLogicService.java)**

    ```java
    public interface AuthorityLogicService {
        /**
         * 分配用户与角色的关联关系
         * @param authorityUserRole
         * @param authorityUser
         * @throws ComponentException
         */
        public void userAssignRoles(AuthorityUserRole authorityUserRole, AuthorityUser authorityUser) throws ComponentException;
    }
    ```

    **2. 服务实现 (AuthorityLogicServiceImpl.java)**

    ```java
    @Service
    public class AuthorityLogicServiceImpl implements AuthorityLogicService {

        @Autowired
        private AuthorityUserRoleRepository authorityUserRoleRepository;

        @Autowired
        private AuthorityRoleRepository authorityRoleRepository;

        @Override
        public void userAssignRoles(AuthorityUserRole authorityUserRole, AuthorityUser authorityUser) throws ComponentException {
            // 1. 查询用户已分配的角色信息
            List<AuthorityUserRole> authorityUserRoleList = authorityUserRoleRepository.findByUserId(authorityUserRole.getUserId());

            // 2. 获取需要分配的角色详情
            AuthorityRole authorityRole = authorityRoleRepository.findById(authorityUserRole.getRoleId());

            // 3. 校验用户是否存在多个相同机构类型的角色
            for (AuthorityUserRole userRole : authorityUserRoleList) {
                if (userRole.getInstitutionTypeId().equals(authorityRole.getInstitutionTypeId())) {
                    throw new ComponentException(ApplicationErrorCodeEnum.ADMIN_USER_INSTITUTION_UNIQUE);
                }
            }

            // 4. 保存用户与角色的关联关系
            authorityUserRole.setRoleName(authorityRole.getRoleName());
            authorityUserRole.setInstitutionTypeId(authorityRole.getInstitutionTypeId());
            authorityUserRole.setInstitutionId(authorityRole.getInstitutionId());
            if (null != authorityRole.getInstitutionVo()) {
                authorityUserRole.setInstitutionName(authorityRole.getInstitutionVo().getDetailInstitution());
            }
            authorityUserRole.setCreateBy(authorityUser.getId());
            authorityUserRole.setCreateTime(new Date());
            authorityUserRole.setLastUpdateUser(authorityUser.getUserName());
            authorityUserRole.setLastUpdateTime(new Date());

            // 5. 保存用户角色数据
            authorityUserRoleRepository.save(authorityUserRole);
        }
    }
    ```

    **3. 异常枚举 (ApplicationErrorCodeEnum.java)**

    ```java
    public enum ApplicationErrorCodeEnum {
        USER_PWD_ERROR("用户密码错误！", "100004"),
        USER_EXISTS("用户已存在！", "100005"),
        USER_COMPANY_NOT_FOUND("公司不存在！", "100006"),
        USER_FILE_NOT_FOUND("用户文件未找到！", "100007"),
        USER_ROLE_NOT_FOUND("用户角色未找到！", "100008"),
        ADMIN_USER_INSTITUTION_UNIQUE("用户在多个相同机构类型的角色，不能保存！", "200001"),
        ADMIN_USER_NEED_LOGIN("请重新登陆！", "200002");
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：接口定义与服务实现** (00:00:05 - 00:01:45)
    *   讲师首先在 IDE 中打开 `AuthorityLogicService` 接口文件，展示其方法签名。
    *   随后，讲师切换到 `AuthorityLogicServiceImpl` 文件，开始编写实现代码。
    *   讲师通过鼠标滚轮和点击，逐步展示代码的每一部分，包括查询已分配角色、查询需要分配的角色、校验逻辑和保存数据。
    *   在校验逻辑部分，讲师特别强调了 `ComponentException` 的抛出，并展示了 `ApplicationErrorCodeEnum` 中的 `ADMIN_USER_INSTITUTION_UNIQUE` 错误码。

*   **场景二：异常处理与代码注释** (00:01:00 - 00:01:30)
    *   讲师在代码中添加了详细的中文注释，如 `// 3. 校验用户是否存在多个相同机构类型的角色`，以帮助理解代码逻辑。
    *   讲师在 `for` 循环中添加了 `if` 条件判断，并在条件成立时抛出 `ComponentException`。

*   **场景三：数据保存与属性设置** (00:01:30 - 00:01:45)
    *   讲师演示了如何为 `AuthorityUserRole` 对象设置多个属性，包括角色名称、机构ID、创建者、创建时间等。
    *
