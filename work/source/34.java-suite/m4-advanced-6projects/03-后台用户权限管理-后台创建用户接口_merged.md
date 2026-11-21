# 03-后台用户权限管理-后台创建用户接口 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来呢,咱们就对实现上做一个说明,以及呢,去实现后台创建用户接口的功能。

那咱们呢,回顾一下,之前章节呢,是实现了全线管理的基本与核心接口,对不对?

但是呢,咱们还缺少了登录接口,创建用户接口,以及呢,后台产品管理相关的接口。

这些呢,都是一些基础核心的数据,因为咱们后面的核心功能的话呢,还需要依赖于这些接口上的数据。

有了用户创建接口与登录接口呢,还需要去实现了全局的拦截器,实现全线和菜单的验证功能。

有了这些,咱们就可以呢,来验证了整个全线功能模块。

好,那接下来呢,咱们就来实现后台创建用户的接口。

首先呢,咱们要去创建用户实体,Authentic User,这个呢,是这个实体的代码。

在这里呢,咱们来看一下,它有哪些核心属性呢?

咱们回到代码工程当中,在这里呢,找到Authentic User。

咱们可以看到呢,这个User对象,它包括呢,用户的登录账号,机构类型,机构ID,用户密码,用户姓名,

它相关的一些资料信息,还有呢,它的账号。

然后呢,这个Authentic User的创建以及呢,登录记录信息。

咱们呢,要注意呢,它头部上的注解。

在这里呢,API是可以作为一个PATO OS接口,对外呢,提供增传改查的接口功能。

这个NT的话呢,是JP的映射注解,然后这个Table的话呢,映射的是咱们的T-Authentic User这个表。

API Model呢,是咱们对这个Authentic User对象呢,做了一个具体的属性描述。

然后下面的API Model,

就对每个属性呢,做了一个详细的说明。

如果是咱们呢,不需要展示出来的属性,可以通过Hidden去做一个隐藏。

好,实体创建完成之后呢,接着就要去创建它的数据层接口,Repository,

在Admin User管理服务工程下面。

在这里有个Authentic User Repository的数据层接口。

它是基层了Paging and Sorting,分页和排序的接口,以及JP的规范接口。

咱们可以看到呢,这里并没有具体的方法实现,对不对?

那在下面的Service逻辑处理过程当中呢,咱们会教大家如何去通过JP这个接口呢,去实现自定义的动态查询。

好,那接着的话呢,咱们就去创建一个Service。

咱们回到讲义当中。

数据层呢,已经创建完成。

那么接着的话呢,我们就创建它的Service层的实现。

在这里呢,右键。

New Java Class。

点击OK。

创建完成之后,咱们加上它对应的注解。

Service。

然后呢,咱们将它必要的属性注入进来。

直接从代码档中copy进来。

接着呢,咱们就来侧重它的核心接口的业务逻辑实现。

咱们定一个接口。

首先的话呢,去实现它的新增用户的方法。

为什么咱们不通过Libsytory这个数据层?

黑头OS它自身提供了新增用户的接口方法呢。

因为在这里呢,它只会将客户端传递过来的数据直接进行保存。

并不能做任。

并不能做相应的业务逻辑的校验以及逻辑方面的判断处理。

那么所以呢,咱们在这里会去自定义实现一个新增用户的接口。

因为下面咱们还要去处理对应的逻辑。

给它定一个传入的。

一个传入的阐述对象。

AuthenticUser。

在这里面的话呢,就是它当前的征入对象。

AuthenticUser。

LoginUser。

因为你创建的话呢,必须要有一个操作人员。

这个LoginUser呢,就是相应的操作人员。

然后咱们呢,要抛出对应的组成一长。

给它呢,加上对应的注释。

这个呢是新增用户的逻辑。

新增用户接口。

然后咱们看一下它具体的处理逻辑是怎样的。

首先第一步。

咱们呢要根据用户账号来查找对应的用户信息。

这个目的是为了校验用户账号是否已存在。

如果是不存在呢,接着咱们再处理下面的逻辑。

在这里呢,我们要去对后台管理用户。

后台管理用户。

对新增的后台管理用户密码呢。

进行加密处理。

再往下面呢,咱们就要去组装和拢于呢,用户后台管理用户信息。

第四点呢。

就是要开始保存后台管理用户的数据。

好,那咱们呢,就从代码层面做具体的实现。

首先呢,第一步。

咱们呢,给它定一个opinion。

这里面的话呢,是Authentic user。

咱们呢,就要去通过它的接口。

Authentic user repository。

在这里面呢,去放的一条记录。

这个记录的话呢,咱们来看一下该怎么去查询呢。

它是要根据用户账号来查找呢,对应的用户记录。

对不对?好。

咱们呢,先把方法名称呢,写上去。

if username。

然后呢,将它的账户信息呢,传递进去。

user account。

接着呢,咱们就来去实现了if username这个方法。

create method。

咱们呢,加上它追的注释。

这个是根据账号获取的用户对象。

再往下面呢,咱们就对它代码做一个编写。

return。

然后呢,要给它创建一个specification。

这个对象的话呢,它会去重写to-predicate的方法。

让咱们看一下,怎么就实现了。

通过tweet-coder.equal然后root.get。

在这里面呢,咱们要传递它的user account。

然后呢,user account。

做一个delay。

就是跟咱们这里的参数做一个值得比较。

如果是匹配呢,那么呢,它就符合对应的条件。

这个呢,是jpeg的一个规范对象。

这个条件呢,并不能去随便拼接,也不能去到随便哪一个对象返回。

这个呢,是jpeg下面的包。

大家可以看到。

这里呢,要加上一个结束符号。

这样呢,咱们就完成了根据用户信息去查找了对应的用户记录。

然后呢,咱们就要做个判断。

一呼。

Authlete。

user.ping.ien。

png.ien。

isPresent。

如果呢,它已经存在了。

那么呢,咱们要把它异常拷出来。

compandException。

在这里呢,给它一个错误码。

application.addcode.animal。

点。

这个错误码呢,咱们就叫做admin.user.account.exist。

然后呢,咱们要对密码进行加密处理。

user.setUserPassword.

通过咱们的加密工具,includeUtil,要用includeSign方法。

将用户的密码呢,传递进去。

然后呢,咱们就要去组装。

并且呢,将相关的信息拢移到用户信息当中。

首先呢,咱们创建一个日期。

new date。

然后呢,咱们将它拢移信息呢,加入进来。

在这里呢,咱们就从讲义当中呢,进行copy。

好。咱们可以看到呢。

它拢移了哪些信息呢?

在这里,它加入了机构类型信息。

然后呢,创建人相关的信息。

咱们可以看到,这个创建人呢,就是当前登录的用户。

然后这个呢,是它的一个状态。

默认的话呢,是处于一个激活可用的状态。

接下来呢,咱们就要调用接口,去保存后台管理用户。

authority.user.lipocitli.sign。

将user呢,传递进去。

好。这样呢,咱们就实现了,新建用户的业务处理逻辑。

咱们呢,再回到讲义当中,做一次回顾。

它的整体步骤呢,咱们可以看到,先根据传递来的账号,去查找呢,用户是否存在。

如果是存在呢,它就抛出对应的异常。

然后呢,密码,在数据库当中的存储,是采用密文的形式。

咱们需要对注册的密码呢,进行加密。

咱们需要对注册的密码呢,进行加密。

接着的话呢,咱们就要记录创建人相关的信息。

接着的话呢,咱们就要记录创建人相关的信息。

要保存用户数据,将用户的一些冗余信息啊,机构类型啊,加入进去。

要保存用户数据,将用户的一些冗余信息啊,机构类型啊,加入进去。

上面呢,是通过用户账号获取用户。

上面呢,是通过用户账号获取用户。

是依赖于呢,JP,Splashification,以及是Qt这个接口呢,来实现的自定义查询。

是依赖于呢,JP,Splashification,以及是Qt这个接口呢,来实现的自定义查询。

是依赖于呢,JP,Splashification,以及是Qt这个接口呢,来实现的自定义查询。

具体实现逻辑呢,刚才呢,也做了一个讲解,对不对。

具体实现逻辑呢,刚才呢,也做了一个讲解,对不对。

具体实现逻辑呢,刚才呢,也做了一个讲解,对不对。

如果说咱们呢,还想去实现其他的条件查询,那么在这里呢,咱们再去扩展,增加其他的属性就可以了。

如果说咱们呢,还想去实现其他的条件查询,那么在这里呢,咱们再去扩展,增加其他的属性就可以了。

如果说咱们呢,还想去实现其他的条件查询,那么在这里呢,咱们再去扩展,增加其他的属性就可以了。

如果说咱们呢,还想去实现其他的条件查询,那么在这里呢,咱们再去扩展,增加其他的属性就可以了。

如果说咱们呢,还想去实现其他的条件查询,那么在这里呢,咱们再去扩展,增加其他的属性就可以了。

那么在这里呢,咱们再去扩展增加了其他的属性就可以了。

这样呢,就比较灵活,可以呢,实现了动态条件的查询。

它实际上呢,是可以支持多个条件,多种操作户的查询,比如like都可以支持。

在这里呢,咱们就不进行赘述,大家有时间的话呢,可以再去参考JPA的规范操作,实现了多种条件的查询功能。

Service成接口实现完成之后呢,接下来就要去实现了Controller成接口。

那咱们呢,就来做个实现。

在咱们的admin user下面,Controller这个包,去创建一个class。

这Controller接口成处理呢,就没有过多的逻辑,咱们呢,将它直接copy过来。

将它的注解呢,也copy进来。

咱们呢,要将它的service注入进去。

这个service呢,咱们还没抽取出来。

那么右键。

reflect is checked。

然后在这里呢,咱们把它抽取出interface。

quotient add user。

点击copy。

reflect。

好,这样呢,它就把咱们的接口呢,抽取出来。

咱们将它的路径呢,改一下。

抽取完成之后呢,咱们可以看到,user下面呢,就会有新增用户的接口定义。

那咱们呢,再回到Controller成当中。

将这个接口呢,引入进来。

authority user service。

然后呢,做个注入,autowide。

这个呢,就是用户服务层接口。

在这里呢,它还调用了getuser。

因为呢,它还传递当前的登录用户,对不对?

所以呢,咱们还去继承了utens base controller。

好,Controller成代码呢,就已经编写完成。

咱们呢,再来讲解一下。

在这里呢,增加了API注解。

将它闹到SWOG接口文档当中。

然后呢,rest controller request mapping。

是它的一个请求。

然后呢,就设定了一个访问接口。

是作为访问接口,访问路径的定义。

下面呢,validate。

这个呢,是要做一个教验。

咱们呢,要对传递过来的参数,authority user呢,做一个教验。

咱们要注意呢,要加上两个注解。

第一个呢,是在内的上面呢,加上validate注解。

第二个呢,如果你的参数是一个对象。

那么要在参数对象前面呢,加上一个validate注解。

authority user呢,咱们可以看到,它具体的一个选项。

它具体的一个选项。

它具体的一个选项。

authority user呢,咱们可以看到,它具体的一个定义。

authority user呢,咱们可以看到,它具体的一个定义。

比如说你要对它的一些属性,做一些约束性,

比如说你要对它的一些属性,做一些约束性,

或者是一些胶原性的处理呢,

那么我们可以加上像一些Northen凹。

好像一些Northen凹。

对应的注解。

还有一些呢,像这个size、约束性的一些注解。

还有一些呢,像这个size、约束性的一些注解。

之前呢,咱们也做了讲解。

大家可以再去参照之前的代码实现。

大家可以再去参照之前的代码实现。

可以看到咱们是在

Common Web下面通过

Habitat Validator这个组件

做了对应的约束性交易

好

咱们再回到刚才的

陈秋乐城代码当中

他的一个处理逻辑来讲

首先是要获取到

对应的登录用户信息

然后再去通过Service的

Add User的这个切入口

去创建了新的管理用户

处理成功之后会将他的结果

返回给客户端

那如果是失败呢

会对这些异常做一个包装处理

这个就是陈秋乐城

他整体的一个处理逻辑

好

那咱们再回到讲义当中

这些说明的话大家要注意一下

陈秋乐城的方法该怎么去处理

通过Check Catch的

补活异常

然后Swork文档的一个注解说明配置

还有交易器的

注解使用

这些大家都按照代码当中的配置

来做具体的实现

好

那这一讲呢

对后台创建用户接口的实现呢

就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是“交易平台 - Day 11”课程的一部分，主要讲解如何在 Spring Boot 项目中实现后台用户的创建与登录功能，作为权限管理模块的核心组成部分。讲师通过 IntelliJ IDEA 开发环境，逐步演示了从定义用户实体类（`AuthorityUser`），到实现服务层（`AuthorityUserServiceImpl`）的用户创建逻辑，再到控制器层（`AuthorityUserController`）的接口暴露。整个过程强调了使用 Spring Data JPA 的 `Specification` 接口进行自定义查询、Spring Cache 的集成、以及异常处理和 Swagger 文档注解的规范。视频内容聚焦于后端开发，技术栈包括 Spring Boot、Spring Data JPA、Spring Cache、Spring Session、Lombok 和 Swagger。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 视频开场，展示课程大纲和学习目标，明确本节要实现“后台创建用户接口”和“Spring Session Redis 实现分布式会话”。
*   **00:16 - 00:35**: 讲师在 `AuthorityUser` 实体类中定义了用户账号、机构类型、机构ID和密码等字段，并使用 `@ApiModelProperty` 注解进行文档说明。
*   **00:36 - 01:00**: 讲师进入 `AuthorityUserServiceImpl` 服务层，定义了 `addUser` 方法，该方法接收两个 `AuthorityUser` 对象：一个用于创建新用户，另一个用于登录验证。
*   **01:01 - 01:25**: 讲师在 `addUser` 方法中，使用 `CriteriaBuilder` 构建一个 `Predicate`，用于根据用户账号查询数据库，检查该账号是否已存在。
*   **01:26 - 01:45**: 讲师演示了如何在 `addUser` 方法中抛出 `ComponentException` 异常，用于处理用户账号已存在的业务逻辑。
*   **01:46 - 02:05**: 讲师在 `AuthorityUserController` 控制器层中，定义了 `@PostMapping("/addUser")` 接口，用于接收前端的用户创建请求。
*   **02:06 - 02:25**: 讲师在控制器中调用 `authorityUserService.addUser(user, loginUser)` 方法，并将结果封装为 `ApiRespResult` 返回给前端。
*   **02:26 - 02:45**: 讲师在控制器中添加了 `try-catch` 异常处理块，用于捕获并处理服务层抛出的异常，并将错误信息封装到 `ApiRespResult` 中返回。
*   **02:46 - 03:05**: 讲师在控制器中添加了 Swagger 文档注解 `@Api` 和 `@ApiOperation`，并为 `AuthorityUser` 参数对象添加了 `@Validated` 注解，以确保参数校验生效。
*   **03:06 - 03:25**: 讲师切换到 `AuthorityUserServiceImpl` 服务层，开始讲解如何使用 `Spring Session` 和 `Redis` 实现分布式会话，为后续的登录功能做准备。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **学习目标**: “第1章 后台用户权限管理功能”，包含“目标”、“步骤”、“实现”三个部分。
    *   **章节标题**: “3. 实现”，下设“1.1 后台创建用户接口实现”、“1.2 Spring Session Redis实现分布式会话”等子章节。
    *   **关键说明**: “上一章实现了权限管理的基本与核心接口，但还缺少登陆接口，创建用户接口，后台产品管理接口。”
    *   **关键说明**: “有用户创建接口与登陆接口，还需要全局权限拦截器，实现权限与菜单验证功能，有这些，我们就可以来验证整个权限模块。”

*   **代码关键内容**:

    *   **实体类 `AuthorityUser.java`**:
        ```java
        @ApiModelProperty(value="用户账号", required = true)
        private String userAccount;

        @ApiModelProperty(value="机构类型", required = true)
        private String institutionTypeId;

        @ApiModelProperty(value="机构ID", required = true)
        private Long institutionId;

        @ApiModelProperty(value="用户密码", required = true)
        @JsonIgnore
        private String userPassword;
        ```

    *   **服务层 `AuthorityUserServiceImpl.java`**:
        ```java
        @Autowired
        private AuthorityUserRoleRepository authorityUserRoleRepository;

        @Autowired
        private CacheManager cacheManager;

        public void addUser(AuthorityUser user, AuthorityUser loginUser) throws ComponentException {
            // 1. 根据用户账号查找对应的用户信息，校验用户账号是否已存在
            CriteriaBuilder criteriaBuilder = entityManager.getCriteriaBuilder();
            CriteriaQuery<AuthorityUser> criteriaQuery = criteriaBuilder.createQuery(AuthorityUser.class);
            Root<AuthorityUser> root = criteriaQuery.from(AuthorityUser.class);
            Predicate predicate = criteriaBuilder.equal(root.get("userAccount"), userAccount);
            criteriaQuery.select(root).where(predicate);
            List<AuthorityUser> list = entityManager.createQuery(criteriaQuery).getResultList();
            if (list.size() > 0) {
                throw new ComponentException(ApplicationCodeEnum.USER_ACCOUNT_EXIST);
            }
            // 2. 对新增的后台管理用户，密码进行加密处理
            // 3. 组装和冗余后台管理用户信息
            // ... (后续代码)
        }
        ```

    *   **控制器层 `AuthorityUserController.java`**:
        ```java
        @Api(value = "用户管理接口", tags = "用户管理接口")
        @RestController
        @RequestMapping("/authorityUser")
        @Log4j2
        @Validated
        public class AuthorityUserController extends BaseController {

            @Autowired
            private IAuthorityUserService authorityUserService;

            @PostMapping(value = "/addUser")
            @ApiOperation(value = "新建用户接口")
            public ApiRespResult addUser(@Valid AuthorityUser user) {
                ApiRespResult result = null;
                try {
                    AuthorityUser loginUser = getUser();
                    // 用户登陆处理
                    authorityUserService.addUser(user, loginUser);
                    result = ApiRespResult.success();
                } catch (ComponentException e) {
                    log.error(e.getMessage(), e);
                    result = ApiRespResult.error(e.getErrorCodeEnum());
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

*   **场景一：定义用户实体类**
    *   **描述**: 讲师在 `AuthorityUser` 实体类中，使用 `@ApiModelProperty` 注解为每个字段添加了描述，并使用 `@JsonIgnore` 注解隐藏了密码字段，以防止在 API 响应中暴露敏感信息。
    *   **技术点**: 使用 Lombok 注解简化代码，如 `@Data`、`@NoArgsConstructor`、`@AllArgsConstructor`，并使用 Swagger 注解进行 API 文档化。

*   **场景二：实现服务层的用户创建逻辑**
    *   **描述**: 讲师在 `AuthorityUserServiceImpl` 中，通过 `CriteriaBuilder` 构建了一个 `Predicate`，用于根据用户账号查询数据库。如果查询结果不为空，则抛出 `ComponentException` 异常，提示用户账号已存在。
    *   **技术点**: 使用 Spring Data JPA 的 `CriteriaQuery` 进行自定义查询，实现灵活的业务逻辑。

*   **场景三：控制器层接口暴露**
    *   **描述**: 讲师在 `AuthorityUserController` 中，定义了一个 `@PostMapping("/addUser")` 接口，接收前端传来的 `AuthorityUser` 对象。在方法内部，调用 `authorityUserService.addUser(user, loginUser)` 方法进行业务处理，并将结果封装为 `ApiRespResult` 返回。
    *   **技术点**: 使用 Spring MVC 的 `@RestController` 和 `@RequestMapping` 注解定义 RESTful API，使用 `@Validated` 注解进行参数校验，使用 `@Log4j2` 注解进行日志记录。

*   **场景四：异常处理与 Swagger 文档**
    *   **描述**: 讲师在控制器方法中添加了 `try-catch` 块，用于捕获并处理服务层抛出的异常。同时，为 `AuthorityUser` 参数对象添加了 `@Validated` 注解，并在类上添加了 `@Api` 和 `@ApiOperation` 注解，以便在 Swagger UI 中生成清晰的 API 文档。
    *   **技术点**: 使用 `ApiRespResult` 统一返回格式，使用 `@Validated` 注解进行参数校验，使用 Swagger 注解进行 API 文档化。

*   **场景五：引入 Spring Session 和 Redis**
    *   **描述**: 讲师在服务层代码中，开始讲解如何使用 `Spring Session` 和 `Redis` 实现
