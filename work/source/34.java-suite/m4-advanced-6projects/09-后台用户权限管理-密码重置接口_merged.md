# 09-后台用户权限管理-密码重置接口 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始讲解用户密码的重置接口

这里咱们提供了用户密码重置功能

目的是便于用户在忘记密码的时候

能够进行重置和恢复

重新登录到咱们的平台当中

这一块并非咱们的核心业务逻辑

那么咱们就快速实现对应的代码

首先咱们在Auxiliary User Service Implement下面

去增加一个接口

这个接口是重置用户密码接口

咱们将它拷贝到User Service当中

这里是一个重写

我们先将它去除

然后右键Reflect Home Members App

将它抽取上去

好

大家看一下

这个接口的描述

它是重置用户密码接口

它是重置用户密码接口

新生成的密码格式是账号

然后在这里再加上一个固定的支付串

咱们看一下它的具体处理实现逻辑是怎样

首先它要去查找用户

根据咱们传递过来的用户账号

查找在系统当中是否存在

接着的话

咱们要判断当前的用户

它是否具备管理员的权限

那么咱们是通过一个标示

就是用户表里面的以蛇的命

这个管理人员的标识来进行判断

如果它不是管理员

就不能进行相应的操作

要抛出对应的异常

接下来它就要生成新的加密密码

这个密码格式

就是刚才所讲的

由账号

听接一个固定支付串组成的

最后就要去数据层当中

将咱们的新生成的密码进行更新

它是通过这个方法

去做对应的实现

咱们将它实现一下

这个是在Authnusr

WebSuite里的接口下面

是一个自定义的接口

因为这涉及到自定义

社口的更新处理

咱们来看一下

这个Transactional注解的包

它在Split Framework下面

不要搞错了

下面是一个Modify的注解

因为咱们是要进行数据的更新操作

这个咱们要把它加上去

然后是具体的执行语句

这个Pyramid参数

咱们将它的包导入进来

是Split Framework下面的

这个和MyBattis就不一样

MyBattis是在MyBattis

iBattis的目录下面

最主要咱们来看一下这块的实现社口

它是通过一个AQL的面向对象的查询语句做的实现

它是要修改Authnusr的这个对象

将它的User Password改成咱们新生成的Password

条件是根据用户账号

做对应的查询

这里的参数并没有采用章位符

章位符之前咱们也做了讲解

比如说你要通过第一个参数

那么后面就根据对应的索引就可以

这里是根据参数的名称

这个是使用方式的差别

大家要理解清楚

好

那数据层的这个接口就已经实现

咱们再回到Service层当中

刚才的重置密码的方法

整个处理逻辑并不复杂

要做好相应的校验和判断

然后要注意新生成的密码

也要采用密文的方式进行存储

最后咱们再去实现它的Concurer接口层代码

咱们回到讲义当中

将Concurer层代码拷贝过去

放在Concurer User Concurer的接口下面

这里加上了它的Svog的注释说明

它的请求类型是支持Post的方式

接口路径是Lizzo的Password

参数只需要传递一个就是用户的账号

其他信息是不需要传递

在这里内部逻辑的时候

它会去校验当前的登录用户是否具备相应的权限

这个就是整个重置密码接口的具体实现

大家要注意一下

Transaction这个注解它是用于开启事物

如果是咱们采用自定义的搜索区修改

比如刚才所实现的用户重置密码的数据层接口

在这里面

加入了Modify

那么JPI要修改数据的时候

就需要开启事物

否则的话它会爆出异常

这个异常的话咱们可以看到它的提示信息

它说执行一个

修改或者删除

操作的时候

没有去开启对应的Transaction了

所以它是无法去正常执行的

后面咱们如果是要涉及到update或者delete操作的时候

要在接口上面加上对应的Transaction了的事物开启了

就会有一个大体的注解

最主要就是要确保JPI它是运行在一个有效的事务下面

好

这一讲就是对密码重置接口的讲解和实现

那这讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个基于 Spring Boot 的权限管理系统开发教程，具体讲解了“密码重置”功能的实现。讲师通过 IDE（IntelliJ IDEA）演示了从服务层（Service）到数据访问层（Repository）的完整代码逻辑。核心内容包括：
- 在服务层 `AuthorityUserServiceImpl` 中，实现 `resetPwd` 方法，用于重置指定用户的密码。
- 该方法首先检查用户是否存在，然后判断操作者是否为管理员，最后生成并更新密码。
- 数据访问层 `AuthorityUserRepository` 使用 JPA 的 `@Query` 注解定义了更新密码的 SQL 语句。
- 控制器层 `AuthorityUserController` 通过 `@ApiImplicitParam` 注解接收前端传入的参数，并调用服务层方法。
- 讲师特别强调了事务管理（`@Transactional`）的重要性，并演示了在没有事务时，JPA 操作会抛出 `TransactionRequiredException` 异常。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取视频的精确时间戳，以下章节基于画面内容和逻辑顺序进行划分：

- **章节 1: 服务层实现 (Service Layer Implementation)**
  - 画面显示 `AuthorityUserServiceImpl` 类中的 `resetPwd` 方法。
  - 逻辑：查找用户 -> 检查用户是否存在 -> 检查操作者是否为管理员 -> 生成新密码 -> 更新数据库。

- **章节 2: 数据访问层接口 (Repository Interface)**
  - 画面切换到 `AuthorityUserRepository` 接口。
  - 逻辑：使用 `@Query` 注解定义了更新用户密码的 SQL 语句，其中使用了 `@Param` 注解来绑定参数。

- **章节 3: 控制器层实现 (Controller Layer Implementation)**
  - 画面切换到 `AuthorityUserController`。
  - 逻辑：使用 `@ApiImplicitParam` 注解定义了 API 接口参数，调用服务层方法，并处理异常。

- **章节 4: 事务管理与异常处理 (Transaction Management & Exception Handling)**
  - 讲师在 `AuthorityUserRepository` 接口上添加了 `@Transactional` 注解。
  - 画面展示了在没有事务时，JPA 操作会抛出 `TransactionRequiredException` 异常。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **章节标题**: `1.6 密码重置接口`
- **功能描述**: “这里提供密码重置功能，以使用户忘记密码能够重置恢复，重新登陆。”
- **关键注解说明**:
  - `@ApiImplicitParam`: 用于 Swagger 文档注解，声明参数名称。
  - `@Validated`: 与参数校验注解配合使用。
  - `@Transactional`: 用于开启事务，JPA 修改操作需要事务，否则会报异常。

#### 代码关键内容

**1. 服务层代码 (`AuthorityUserServiceImpl.java`)**

```java
@Override
public void resetPwd(String userAccount, AuthorityUser loginUser) throws ComponentException {
    // 查找用户
    Optional<AuthorityUser> authorityUserOpt = authorityUserRepository.findone(eqUserName(userAccount));
    if (!authorityUserOpt.isPresent()) {
        throw new ComponentException(ApplicationErrorCodeEnum.ADMIN_USER_ACCOUNT_NOT_FOUND);
    }

    // 非管理员用户，不能进行此操作
    if (!GlobalConstants.STR_YES.equals(String.valueOf(loginUser.getIsAdmin()))) {
        throw new ComponentException(ApplicationErrorCodeEnum.ADMIN_NOT_ADMIN);
    }

    // 生成新的加密密码
    String newPwd = EncryptUtil.encryptSigned(userAccount + "123");
    
    // 调用数据访问层方法更新密码
    authorityUserRepository.updateUserPwdByAccount(userAccount, newPwd);
}
```

**2. 数据访问层代码 (`AuthorityUserRepository.java`)**

```java
@Repository
public interface AuthorityUserRepository extends PagingAndSortingRepository<AuthorityUser, Long>, JpaSpecificationExecutor<AuthorityUser> {

    /**
     * 根据账号修改用户密码
     * @param account
     * @param password
     * @return
     */
    @Transactional
    @Modifying
    @Query("update AuthorityUser usr set usr.userPassword = :password where usr.userAccount = :account")
    int updateUserPwdByAccount(@Param("account") String account, @Param("password") String password);
}
```

**3. 控制器层代码 (`AuthorityUserController.java`)**

```java
@PostMapping(value = "/resetPwd")
@ApiOperation(value = "重置密码接口", name = "account", dataType = "string", required = true)
public ApiRespResult resetPwd(String account) throws Exception {
    try {
        AuthorityUser loginUser = getUser();
        // 用户登陆处理
        authorityUserService.resetPwd(account, loginUser);
        return ApiRespResult.success();
    } catch (Exception e) {
        log.error(e.getMessage(), e);
        return ApiRespResult.sysError(e.getMessage());
    }
}
```

---

### 4) 关键场景与演示描述

- **场景 1: 服务层逻辑演示**
  - 讲师在 `AuthorityUserServiceImpl` 中逐步演示 `resetPwd` 方法的实现。
  - 他首先检查用户是否存在，如果不存在则抛出 `ADMIN_USER_ACCOUNT_NOT_FOUND` 异常。
  - 接着，他检查操作者是否为管理员，如果不是则抛出 `ADMIN_NOT_ADMIN` 异常。
  - 最后，他生成一个固定的加密密码（`userAccount + "123"`），并调用 `updateUserPwdByAccount` 方法更新数据库。

- **场景 2: 数据访问层事务演示**
  - 讲师在 `AuthorityUserRepository` 接口中添加了 `@Transactional` 注解。
  - 他强调了事务的重要性，指出 JPA 的更新操作必须在事务中执行。
  - 画面中展示了在没有事务时，会抛出 `TransactionRequiredException` 异常。

- **场景 3: 控制器层接口演示**
  - 讲师在 `AuthorityUserController` 中定义了 `resetPwd` 接口。
  - 他使用 `@ApiImplicitParam` 注解声明了 `account` 参数。
  - 他演示了如何在控制器中调用服务层方法，并处理异常。

- **场景 4: 异常处理演示**
  - 讲师在控制器中添加了 `try-catch` 块来捕获异常。
  - 他展示了如何将异常信息封装成 `ApiRespResult` 返回给前端。

---

以上是根据视频画面进行的结构化技术分析。
