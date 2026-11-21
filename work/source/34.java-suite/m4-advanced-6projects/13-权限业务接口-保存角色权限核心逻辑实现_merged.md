# 13-权限业务接口-保存角色权限核心逻辑实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着的话呢

咱们继续实现角色和权限的管理保存接口

上一讲呢

咱们对外层做了一个实现

那么这一讲呢

咱们就来实现它内层的具体处理逻辑

回到咱们代码当中

下面呢

咱们就去创建对应的方法

我们给它定一个方法名称

这个呢是私有的

void

将名称的copy过来

传递的参数呢

一个是角色ID

然后呢是角色所分配的

转线信息

接着的话呢咱们打印对应的日志

说明呢

它已经进入到指方法当中

进行逻辑处理

然后将这个方法名称呢打印提示出来

这个呢是它的参数

这里打印出角色ID就可以了

那接着的话呢

我们来实现它整体的处理流程

首先第一步

我们要过滤

low-auth

参数

输入数据

它的规范呢

我们上一章节呢也做了讲解

M呢

开头的是菜单对不对

O开头的是代表操作

我们在这里呢加上注释说明

以M开头的

代表的是菜单

菜单信息

以O开头的

代表的是操作信息

通过逗号进行分割

通过逗号进行分割

팅点

内容

方案

这里呢我们选这个

记录

可以那个

这个

简单的

然后呢,是派的

咱们在这里呢,是以逗号进行分割

第二步呢

咱们要对

权限信息呢,做去从处理

做去从

好,那我们看一下

该怎么去做呢

给它定义一个list的对象

so auth list

通过stream方式

做流逝转换处理

auth array

其实team呢,做去从

然后呢,我们重新将它呢

转换成为一个list对象

这样呢,就可以防止

前端的话呢,出现一些重复的

权限数据

那么接着的话呢,咱们就可以进行

权限的保存和分配

但是在进行权限保存分配之前呢

咱们要先删除角色原有的

菜单

菜单

和操作权限信息

那咱们呢,要将数据层接口注入进来

数据层接口呢

我们定义两个

第一个呢

是菜单的

另外一个呢,是操作的

authority

应该是

load menu

另外呢,authority

然后呢,是一个load operation

我们呢,将它们注入进来

加上对应的注释说明

这个呢,是角色

菜单

关联

数据层接口

这个呢,是

角色

和

菜单

操作的

关联

数据层接口

定义完成之后呢

我们就来标明它的删除方法

authority

咱们首先呢,去删除最末层的数据

也就是

菜单的操作层数据

elite

or

id

咱们要注意,删除数据的时候呢

咱们要从最末级进行删除

这样呢,避免一些关联所产生的一些数据问题

然后呢

authority

load menu

looksatory

然后呢,delete

这里呢,有调用对应的方法

咱们可以看到

这个数据层接口

它是

删除呢

角色

所

关联的

数据信息

对不对

那在这里呢

它是删除什么

角色

所

关联的

菜单操作

在这里呢

咱们可以看到

我们是采用自定义的circle进行了实现

对不对

那么自定义circle呢

它是删除了

角色

所关联的菜单操作

那么自定义circle编写起来了

其实也并不复杂

又跟咱们写不同circle一样的

要传递了对应的参数

对于没有特殊需求的话呢

咱们就采用

普通的增删改查接口

去做操作就可以了

这个呢

相当于就可以实现一个什么

批量的删除

在这下面呢

角色

和菜单的

操作数据层接口

也是同样的处理方式

再往下面呢

要去

重新

进行了

角色

和权限

信息的保护

然后呢

我们可以看到

这个

这个

这个

这个

这个

这个

这个

这个

这个

这个

因为咱们在这里

有多个

权限数据

所以呢

要去

遍力

展现信息

如个

进行

保存处理

首先呢

我们在对外层

定意呢

对应的 Ä

在这里面呢

我们在定意

一个

角色

和菜单的

对象

然后呢

我们就做

便利处理

拿到

权限

ID信息

去给他呢 放进一个新的对价

这样的好处呢 就在于每次循环的时候呢 都不用再去创建一个引用 节省了一定的资源开销

oswit low menu

那我们来看具体的处理 首先的话呢 我们要做一个判断 判断呢 它是否包含menu的表示

我们现在最上面呢 第一两个长量标识 public

bundle

menu of flag 这个话呢 是一个操作表示 我们再靠底下 下面呢 我们再创建一个

菜单的表示 给他呢 加上对应的都是网线分配

菜单的操作表示 下面的话呢

是网线分配菜单表示 我们再回到刚才的国际

这个呢 就是判断它是否包含了菜单操作的程序表示

那么如果它是菜单的操作呢 我们就要进行对菜单操作进行保存

那么怎么保存呢 我们要去给他设置相关的信息

set operation id 这个呢 做一个转换可以知道

id

点对face

让他的前对呢 做个计划menu of flag

计划为空

将空格呢 去除 接着话呢 我们要去设置呢 他的表示id

set load id 最后呢 咱们就交用数据层结构进行保存 再往下面呢 就是对菜单的判断

同样的 要判断他的前对

这个呢 就是对菜单进行操作保存

同样的

咱们呢 要给这个菜单对象呢 设置对应的信息 首先呢 设置他的菜单id

让点可以使用 做一个替换 将他的menu前对呢 去除去去除空格

然后呢 设置他的角色对象 最后呢 就调用数据层结构进行保存

最后呢

咱们再写另外一个

这个判断

如果都不匹配的情况下呢 咱们就要打出一个警告日志

onload menu

我update

让他id呢 排出来 这个呢 就是角色和权限的内存处理逻辑 咱们呢 加上对应的注释

这个就是保存角色和权限的关联关系

好 接着呢 咱们再回到讲一当中 对整个逻辑流程呢 再做一次回顾

我们看呀 整体处理逻辑 首先的话呢 我们要做便利循环处理

支持呢 多个角色id对应的权限信息分配

方法上面呢 要加上失误图解 加上transaction

因为呢 我们会采用jp进行了数据层的操作jp呢 他是依赖于失误才能进行操作

接着话呢 咱们要做交易处理检查了权利的角色id

是否存在 然后咱们就要开始保存角色和公配的权限信息

调用了c5 low reveal ledges 传现处理方法 根据指定分割符的解析传递的传递数据

然后low aus的这个规范呢 咱们要明白清楚

这个格式呢 是m开头或者是o开头的 以m开头呢 代表的是菜单id 以o开头的代表的是操作id

他们之间呢 可以通过ZO号进行分割 支持了多个传递

针对权限数据呢 可以做过滤去重处理 因为咱们不能保证全前端传递的数据呢是百分之百的正确 对不对

如果是他重复勾选或者说前端的话呢 没有控制严格 那么后台呢 我们可以做一个过滤去重 同时呢

也可以保证咱们后台接口处理逻辑的建创性 接着话呢 咱们要先删除原有的操作和菜单数据

这种方法来的话更直接和简单

因为的话呢 你要跟原有数据进行一个比对

然后再做一个添加 这样呢 操作起来会比较麻烦 而且呢 不容易保证整个数据的正确性

所以呢 咱们要先清除原有的操作和菜单 然后呢 按你新传递的数据进行保存就可以了

删除的时候呢 咱们要注意它的顺序 一般呢 我们要把关联的数据放在前面去处理

接着话呢 咱们去解析传递的权限数据

根据指定的标识呢 去区分菜单还是呢 具体的菜单操作 最后呢 分别

保存数据至角色和操作的关联表 以及呢 角色和菜单的关联表 主要呢 就这两张角色对应的权限关联表

最后呢 还有对kentura层接口呢 做一个实现 让咱们呢 就来快速创建一下

在kentura层接口

咱们呢 去创建一个cast 名称呢 就叫authority logic control了 咱们呢 就将代码呢 直接拨并过来

将service录入进去 这个service呢 咱们要抽取一下

取标右键reflag

然后以strate

在这里面 选择inoffice 这个呢 是咱们的接口名称 必须要implement 然后在这里呢 copy 选择我们要抽象的方法

好reflag 选择yes

这样呢 我们可以看到生成了一个接口 对不对 这个接口的话呢 前置我们要改一下

然后在这里呢 要做个保证 我们要将实现内呢 最好放在它的纸包下面implement

这样子 代码的话 移到里面去reflag

这个名称呢 我们add shift再加r

我们点击右键reflag

uset 这里选择inoffice

这个呢 是定义接口名称 以i进行开头

不需要implement 在这里选择copy 然后呢 是选择咱们需要抽象的接口 点击reflag

好 这个呢 yes

那么这个接口呢 就已经抽取完成

咱们呢 还是创建一个纸包packageimplement 将实现内呢 放在implement包下面

好 咱们回到刚才的接口层

在这里呢 将service注入进来 然后呢 加上对应的注解

再给它呢 加上control的注解 定义请求入境 请求入境呢 就叫authority

ogic

好 在这里呢 我们就实现了它的controller这个程

这一讲呢 咱们就对权限核心国际接口的实现了 做了一个具体的讲解 那这一讲呢 咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段为一个关于 Spring Boot 后台管理系统权限控制模块开发的实战教学。讲师通过 IntelliJ IDEA 开发环境，详细演示了如何实现一个核心的权限分配接口 `savePrivileges`。该接口的核心功能是：接收一个角色ID和一个包含菜单ID与操作ID的字符串（如 `"M_100_O_200"`），然后将这些权限信息批量保存到数据库中。实现过程包括：参数校验、权限字符串解析、数据清理（删除旧权限）、以及分情况保存菜单权限和操作权限。整个过程体现了面向对象设计、Spring Data JPA 的使用、以及事务管理等核心开发理念。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，展示项目结构和当前正在编辑的 `AuthorityLogicServiceImpl` 类。
*   **00:00:05 - 00:00:15**：讲师介绍 `savePrivileges` 方法的总体功能和参数。
*   **00:00:15 - 00:00:30**：演示如何通过 `@Transactional` 注解开启事务，并对传入的角色ID进行校验，若不存在则抛出 `BusinessException`。
*   **00:00:30 - 00:00:45**：讲解 `saveRolePrivileges` 方法，用于保存角色与权限的关联关系。
*   **00:00:45 - 00:01:00**：演示如何对传入的权限字符串 `roleAuth` 进行预处理，包括替换非法字符、去除空格、并按分隔符 `","` 分割成字符串数组 `roleAuthList`。
*   **00:01:00 - 00:01:15**：在 `saveRolePrivileges` 方法中，先删除角色原有的所有菜单和操作权限，为新权限腾出空间。
*   **00:01:15 - 00:01:30**：进入核心的权限保存逻辑，遍历 `roleAuthList` 数组，对每个权限字符串进行解析。
*   **00:01:30 - 00:01:45**：根据权限字符串的前缀，判断是菜单权限还是操作权限，并分别创建对应的实体对象 `AuthorityRoleOperation` 或 `AuthorityRoleMenu`。
*   **00:01:45 - 00:02:00**：对菜单权限，设置 `menuId` 和 `roleId`，然后调用 `authorityRoleMenuRepository.save()` 保存。
*   **00:02:00 - 00:02:15**：对操作权限，设置 `operationId` 和 `roleId`，然后调用 `authorityRoleOperationRepository.save()` 保存。
*   **00:02:15 - 00:02:30**：演示如何处理未知的权限类型，并记录日志。
*   **00:02:30 - 00:02:45**：总结整个方法的实现逻辑，并在 PPT 上列出关键步骤。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT 内容

*   **左侧大纲**：显示了课程的结构，当前章节为“3.7 权限核心逻辑接口实现（重要）”，并列出了该章节的子项。
*   **右侧总结**：在视频末尾，PPT 上列出了 `savePrivileges` 方法的六个关键步骤：
    1.  先遍历循环处理，支持多个角色ID的权限信息分配，方法 `@Transactional`。
    2.  做校验处理，检查传递的角色ID是否存在。
    3.  保存角色和分配的权限信息。
    4.  `saveRolePrivileges` 权限处理方法，根据指定分隔符，解析传递的权限数据。
    5.  `roleAuth` 的规范，格式为 `"M_ID_O_ID"`，以 `M` 开头的代表菜单ID，以 `O` 开头的代表操作ID，通过逗号进行分隔。
    6.  针对权限数据做过滤去重处理。

#### 代码关键内容

*   **`savePrivileges` 方法（主方法）**：
    ```java
    @Transactional(rollbackFor = Exception.class)
    public void savePrivileges(String roleAuth, String... roleIds) {
        log.info("Process in AuthorityLogicServiceImpl.savePrivileges method params, roleAuth: " + roleAuth + ", roleIds: " + Arrays.toString(roleIds));
        // 1. 保存多个角色的权限信息，支持批量方式处理（参数由前端传递）
        for (String roleId : roleIds) {
            // 2. 将roleId信息转换，校验角色信息是否存在
            Long roleIdLong = Long.valueOf(roleId);
            Optional<AuthorityRole> authorityRoleOpt = authorityRoleRepository.findById(roleIdLong);
            if (!authorityRoleOpt.isPresent()) {
                throw new BusinessException(ApplicationErrorCodeEnum.USER_ROLE_NOT_FOUND);
            }
            // 3. 保存角色与权限的关联关系
            saveRolePrivileges(roleIdLong, roleAuth);
        }
    }
    ```

*   **`saveRolePrivileges` 方法（核心权限处理）**：
    ```java
    private void saveRolePrivileges(Long roleId, String roleAuth) {
        log.info("Process in AuthorityLogicServiceImpl.saveRolePrivileges method. roleId: " + roleId + ", roleAuth: " + roleAuth);
        // 1. 过滤roleAuth参数的数据，规范为“M_ID_O_ID”，以M开头的代表的是菜单ID，以O开头的代表的是操作ID，通过逗号进行分隔。
        String[] roleAuthArr = roleAuth.replace(" ", "").trim().split(",");
        // 2. 对权限参数信息去重处理
        List<String> roleAuthList = Stream.of(roleAuthArr).distinct().collect(Collectors.toList());
        // 3. 先删除角色原有的菜单和操作权限信息
        authorityRoleOperationRepository.deleteAllByRoleId(roleId);
        authorityRoleMenuRepository.deleteAllByRoleId(roleId);
        // 4. 重新进行角色和权限信息的保存，遍历权限信息，逐个进行保存处理
        for (String id : roleAuthList) {
            // 5. 判断是菜单权限还是操作权限
            if (id.contains(MENU_OPT_FLAG)) {
                // 菜单的操作保存
                authorityRoleOperation.setOperationId(Long.parseLong(id.replace(MENU_OPT_FLAG, "").trim()));
                authorityRoleOperation.setRoleId(roleId);
                authorityRoleOperationRepository.save(authorityRoleOperation);
            } else if (id.contains(MENU_FLAG)) {
                // 菜单的操作保存
                authorityRoleMenu.setMenuId(Long.parseLong(id.replace(MENU_FLAG, "").trim()));
                authorityRoleMenu.setRoleId(roleId);
                authorityRoleMenuRepository.save(authorityRoleMenu);
            } else {
                log.warn("unknown menu opt id: " + id);
            }
        }
    }
    ```

*   **常量定义**：
    ```java
    public final static String MENU_OPT_FLAG = "O";
    public final static String MENU_FLAG = "M";
    ```

---

### 4) 关键场景与演示描述

*   **场景一：方法入口与事务管理**：讲师首先展示了 `savePrivileges` 方法的入口，并强调了 `@Transactional` 注解的作用，确保整个权限分配过程的原子性。
*   **场景二：角色ID校验**：讲师通过 `authorityRoleRepository.findById(roleIdLong)` 查询数据库，若未找到则抛出 `BusinessException`，演示了如何进行数据校验。
*   **场景三：权限字符串解析**：讲师演示了如何使用 `String.replace()` 和 `String.split()` 方法，将传入的权限字符串 `roleAuth` 拆分为一个字符串数组 `roleAuthArr`，并使用 `Stream` 进行去重处理，得到 `roleAuthList`。
*   **场景四：数据清理**：在保存新权限前，讲师演示了如何调用 `deleteAllByRoleId` 方法，先删除角色原有的所有菜单和操作权限，避免数据冗余。
*   **场景五：权限类型判断与保存**：讲师通过 `if (id.contains(MENU_OPT_FLAG))` 和 `else if (id.contains(MENU_FLAG))` 两个条件判断，分别创建 `AuthorityRoleOperation` 和 `AuthorityRoleMenu` 实体对象，并调用对应的 Repository 方法进行保存。
*   **场景六：异常处理与日志**：对于无法识别的权限ID，讲师演示了如何记录警告日志 `log.warn("unknown menu opt id: " + id);`，确保程序的健壮性。
*   **场景七：PPT总结**：在视频末尾，讲师将整个实现过程总结在 PPT 上，清晰地列出了六个关键步骤，帮助观众系统性地理解整个逻辑。
