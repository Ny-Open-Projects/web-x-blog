# 24-swagger2集成-spring data rest对api注解支 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

下面我们开始去修改SpringFoxDataRest

让它能够支持API的入件

从而能够将SpringDataRest的接口

呈现在SWOG文档当中

HOS在SWOG上面

支持并不是十分友好

比如说CRUID的操作接口的显示

还有返回结果的描述

但是文档接口名称

它是用实体内名进行显示

这个是非常不友好

咱们要去修改它的原码

让它能够支持API的注解

就是上面的话

可以增加对应的描述信息

同时也能够将对应的接口呈现出来

咱们来看一下

具体的修改方法是怎么去实现的

回到咱们的代码当中

在这里咱们将原码

拖比到SWOG之第一启动工程当中

咱们要对它原码进行相应的修改

当然在实际

项目生产应用当中

咱们可以把修改后的原码

再重新打包成为一个价包

就是替换了原来的价

这里咱们是测试

如何去修改对应的原码

去支持相应的功能

那么我们是直接将原码拖比到工程当中

它的优先级会比较高

如果工程当中既引用了价

又采用了原码的包结构

那么它会优先扫描

咱们原码路径下面的代码

然后才是扫描的代码

加里面的原码

这个是优先级的一个关系

那么咱们来看一下

具体该如何去修改的

首先咱们在这里去修改

它的getDemark的

自定义文档属性结构的方法

咱们回到代码当中

在原码的包下面

咱们找到ntcontext

然后我们找到

getDemark方法

这个是自定义文档的属性

在这里它对API注解

做一个pandas

我们选择

如果是唯空

就直接去读取它的名称

就是getName

或许比如说你这个接口上面的话

定义了一个是delay

那么它对应的就是拿这个类的名称

如果你在上面的话

配置的值它就会拿到你在这里面定义的value

咱们可以看一下splint.let的接口

找到libscript里

咱们随便拿一个接口可以看一下

在这里面我们是定义了APIOperation

对不对?

我们并没有发现API的注解的定义

这个是定义在哪里呢?

它是定义在auth menu

也就是这个数学层接口所映射的实体类当中

咱们可以看到

在这里定义了一个value

对不对?

所以swog2它就会去读取这里面的value的值

然后作为名称显示在接口当中

咱们再回到刚才的原码当中

ntcontext

这个是它的一个自定义文档属性的处理逻辑

这一段方法在原码当中是不存在的

咱们可以找到之前的原码

这个是splintbox.letrest的主件

咱们拿到它之前的原码

版本是2.9.2

我们可以看一下ntcontext

点击查看文件

咱们往下面看

在这里并没有刚才所定义的方法

对不对?getName

它只有getName

好

咱们看一下

这个方法它是用于哪里的

我们看一下它的引用

enew

它的引用是在splintdata.letrestHandle这个类当中去使用的

我们可以看到它这里面有个groupName

groupName它最终的话就会显示在swog2的文档接口当中

它的格式是怎么处理的

在这里它直接是拿到ntcontext里面定义的remark的返回值

remark就是刚才API里面的话定义的value属性值

这样就是它最终接口返回的信息名称

咱们可以对比一下它原码

原来的代码它怎么去处理了

我们找到request.letrestHandle

点击查看文件

找到了groupName

它原来的话就是拿到nt的内名

这getName它取的就是它的simpleName

对不对?

也就是说回到咱们代码当中

它就会去拿到这个内的gitName

内名称当作为显示

这样它就没有这种注释来的更为直观一点

全部显示英文的实体名称

易读性非常大

对不对?

这个是咱们对它原码做的一个调整

主要就修改这两处原码就可以了

第一个咱们先实现它的getRemark的框桃

然后拿到API里面定义的value值

接着的话咱们在groupName里面去修改它原来的代码

将它的getName改成

从getRemark里面去读取对应的属性描述

最后大家就不要忘了

在咱们的数据层所映射的实例当中

要加上API注解描述

这样它才能真正生效

咱们就来重启服务

验证一下实际的结果是怎样

重新启动咱们的user服务

启动成功

咱们刷新一下文档接口地址

可以看到这个并没有生效

对不对?

咱们没有看到HVS相关的接口

SpringDataRest的依赖也已经是加入进来了

为什么它没有呈现出来呢?

大家要注意一下

咱们在stockadmin user的启动内容当中

要加上一个配置

这个配置就是import

让它导入SpringDataRest的配置内

咱们再重新启动服务

因为你不加上这个注解

在这里面SpringDataRest所定义的配置信息

它无法去扫描

无法去加载

就不能识别出SpringDataRest的接口

所以它在SpringDataRest当中就不能呈现出来

所以这一点咱们要明白清楚

重启服务完成之后

咱们再来刷新访问一下这个接口地址

这个时候可以看到

HVS相关的接口就全部呈现出来了

而且这些名称也是按照咱们的注解上面所定义的主性值进行了呈现

好

这个就是对SpringFoxDataRest的增加的API注解的知识

如果是不加这个注解

它在之前的接口访问当中

就会呈现出这样的英文的实体信息

非常不直观

在这里面咱们可以看到

这个是咱们修改原码后的描述信息

那么相比之前的话

就有很大的一个改善

对不对

看起来的话就会更为清晰和直观

那咱们回到这个原码后的描述信息

这个接口地址当中

可以看到咱们自己定义的那些属性接口都可以呈现出来

比如说AuthleticMenu

这个是菜单管理接口

在这里面LegallySettling

下面咱们是定义了两个接口

一个是根据机构预制进行获取所有菜单

下面的话是根据JSID来查找对应菜单信息

那么我们要注意一下

默认的话

它其实还提供了增长改查接口

就是针对于AuthleticMenu提供的增长改查

因为Swog对SplitDataList的原生知识并不是十分友好

所以对于CRUID的接口呈现

它没法进行了完全的展示

但是这个也没有关系

咱们理解清楚就可以

因为这个CRUID都是按照黑透OS的规范进行对应的操作

好

这一讲咱们就完成了SplitFoxDataList对API注解的修改知识

这讲咱们就先讲到这里

谢谢大家

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频课程聚焦于如何改进 Spring Data REST 框架与 Swagger2 文档集成时的用户体验。核心问题是：默认的 HATEOAS 接口在 Swagger 文档中显示的名称（如 `AuthorityMenu`）不够语义化，不利于开发者理解。讲师通过修改 Spring Data REST 的核心类 `SpringDataRestRequestHandler` 和 `EntityContext`，实现了自定义接口名称的功能。最终，通过在实体类上添加 `@Api` 注解，使 Swagger 文档中的接口名称能够显示为更具业务含义的描述，如“HATEOAS接口-菜单管理(AuthorityMenu)”。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师展示了一个 Swagger 文档界面，指出当前 HATEOAS 接口的显示名称（如 `AuthorityMenu`）不够友好。
*   **00:05 - 00:15**: 讲师在 PPT 中阐述了修改目标：通过修改 Spring Data REST 的源码，使其支持 `@Api` 注解，从而在 Swagger 文档中显示更友好的接口名称。
*   **00:15 - 00:30**: 讲师切换到代码编辑器，展示 `AutoSwaggerConfiguration.java` 文件，重点讲解了如何配置默认的排除路径（如 `/error`, `/actuator`）。
*   **00:30 - 00:45**: 讲师在 PPT 中详细说明了修改 `SpringDataRestRequestHandler` 类的 `groupName()` 方法，将返回值从实体名改为自定义的 `entityContext.getRemark()`。
*   **00:45 - 00:55**: 讲师在代码编辑器中展示 `EntityContext.java` 文件，讲解了如何自定义 `getRemark()` 方法，通过读取实体类上的 `@Api` 注解来获取自定义的描述。
*   **00:55 - 01:05**: 讲师在 PPT 中展示了修改后的 `SpringDataRestRequestHandler` 类的 `groupName()` 方法代码。
*   **01:05 - 01:15**: 讲师在代码编辑器中展示 `AuthorityMenuRepository` 接口，说明需要在实体类上添加 `@Api` 注解。
*   **01:15 - 01:25**: 讲师在 PPT 中展示了最终的实体类 `AuthorityMenu` 的代码，其中包含了 `@Api(value = "HATEOAS接口-菜单管理(AuthorityMenu)")` 注解。
*   **01:25 - 01:35**: 讲师在 PPT 中展示了修改后的 Swagger 文档界面，接口名称已更新为“HATEOAS接口-菜单管理(AuthorityMenu)”，并展示了其对应的 GET 和 POST 方法。
*   **01:35 - 01:45**: 讲师在 PPT 中总结了本次修改，强调了通过自定义 `@Api` 注解可以显著提升 Swagger 文档的可读性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 关键内容**:
    *   **章节标题**: “3.5 修改Springfox-Data-Rest支持@Api注解”。
    *   **问题描述**: “HATEOAS在Swagger上面支持不是十分友好，比如CRUD的显示，返回结果的描述等，但文档接口名称是用实体类名显示，这非常不好”。
    *   **修改方案**: “通过springfox.documentation.spring.data.rest.SpringDataRestRequestHandler类的groupName()方法来显示接口名称，做修改”。
    *   **修改代码片段**:
        ```java
        @Override
        public String groupName() {
            // return String.format("%s Entity", entityContext.getName());
            return String.format("%s", entityContext.getRemark());
        }
        ```
    *   **修改代码片段**:
        ```java
        public String getRemark() {
            Api api = resource.getDomainType().getAnnotation(Api.class);
            if (api == null) {
                return getName();
            }
            return api.value();
        }
        ```
    *   **最终效果**: “最后在要暴露接口的实体上面增加@Api注解”。
    *   **最终效果**: “HATEOAS接口-菜单管理(AuthorityMenu)”。
    *   **总结**: “通过自定义@Api注解，可以显著提升Swagger文档的可读性”。

*   **代码关键内容**:
    *   **`AutoSwaggerConfiguration.java`**:
        ```java
        DEFAULT_EXCLUDE_PATH = Arrays.asList("/error", "/actuator/**");
        ```
    *   **`EntityContext.java`**:
        ```java
        public String getRemark() {
            Api api = resource.getDomainType().getAnnotation(Api.class);
            if (api == null) {
                return getName();
            }
            return api.value();
        }
        ```
    *   **`SpringDataRestRequestHandler.java`**:
        ```java
        @Override
        public String groupName() {
            return String.format("%s", entityContext.getRemark());
        }
        ```
    *   **`AuthorityMenu.java`**:
        ```java
        @Api(value = "HATEOAS接口-菜单管理(AuthorityMenu)")
        @Entity
        @Table(name="t_authority_menu")
        public class AuthorityMenu extends BaseEntity {
            ...
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：问题展示 (00:00-00:05)**:
    *   **描述**: 讲师首先展示了一个 Swagger 文档的截图，其中 HATEOAS 接口的名称显示为 `AuthorityMenu`，并用红色框标出，指出这种显示方式不够友好，不利于开发者理解接口的实际用途。

*   **场景二：修改方案讲解 (00:05-00:15)**:
    *   **描述**: 讲师在 PPT 上详细讲解了修改方案，即通过修改 Spring Data REST 的源码，使其支持 `@Api` 注解，从而在 Swagger 文档中显示更友好的接口名称。

*   **场景三：代码修改演示 (00:15-00:45)**:
    *   **描述**: 讲师在代码编辑器中展示了 `AutoSwaggerConfiguration.java` 文件，并讲解了如何配置默认的排除路径。随后，讲师在 PPT 上展示了修改 `SpringDataRestRequestHandler` 类的 `groupName()` 方法的代码，并在代码编辑器中进行了相应的修改。

*   **场景四：自定义属性实现 (00:45-01:05)**:
    *   **描述**: 讲师在 PPT 上展示了修改 `EntityContext` 类的 `getRemark()` 方法的代码，并在代码编辑器中进行了相应的修改。该方法通过读取实体类上的 `@Api` 注解来获取自定义的描述。

*   **场景五：最终效果演示 (01:05-01:25)**:
    *   **描述**: 讲师在 PPT 上展示了最终的实体类 `AuthorityMenu` 的代码，其中包含了 `@Api(value = "HATEOAS接口-菜单管理(AuthorityMenu)")` 注解。随后，讲师在 PPT 上展示了修改后的 Swagger 文档界面，接口名称已更新为“HATEOAS接口-菜单管理(AuthorityMenu)”，并展示了其对应的 GET 和 POST 方法。

*   **场景六：总结 (01:25-01:45)**:
    *   **描述**: 讲师在 PPT 上总结了本次修改，强调了通过自定义 `@Api` 注解可以显著提升 Swagger 文档的可读性，并鼓励观众在自己的项目中应用此方案。
