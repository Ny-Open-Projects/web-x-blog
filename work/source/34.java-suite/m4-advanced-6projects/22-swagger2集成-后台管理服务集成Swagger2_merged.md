# 22-swagger2集成-后台管理服务集成Swagger2 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

下面咱们开始去实现了后台管理服务集成的SWG2文

那怎么去实现呢

咱们来看一下

首先我们在POM上面增加对应的依赖

将我们制定封装的SWG2启动器

这个依赖加入进去

放到咱们的后台管理服务工程当中

找到POM文件

放在Defenses标签下面

对这个名称我们做个调整

放上了

Boss开头了

好

Control看一下

可以找到依赖

说明了它是配置加载成功

咱们再回到讲义当中

接着的话呢

我们就要去配置文件当中的增加SWG2的配置

具体呢

就是去修改Bootstrap它的配置文件

在我的Mint User下面找到Resource

咱们呢去修改它的开发环境配置

在这里呢

咱们指向的就是开发环境

看到没有DV

好

那么SWG2的这个注解呢

咱们在这里呢

已经加入进去了

咱们可以看到这个属性配置呢

跟咱们之前呢

所定义的SWG

Properties里面的属性配置呢

都是一致的

也就是在这里面的话呢

咱们是需要配置哪些属性呢

就将这些属性定义在咱们的配置文件当中

也在这里面

比如说是否要开启SWG文档

这个呢相当于就是它的总开关

然后呢

是它的

标题描述

这些的话呢

都是相关的一些描述信息

好

这个呢

是SWG2文档的界面内容展示配置

这个配置完成之后呢

咱们就来给对外的接口呢

去加上SWG的注解

在这里呢

咱们以保存角色权限的这个接口

作为例子进行讲解

咱们找到保存角色权限接口

Ctrl H

好

找到对应的方法

在这里呢

我们可以看到

这个接口呢

并没有SWG2相关的注解说明

那咱们呢

要把它加入进去

首先呢

我们要定义API operation

这个是给这个接口呢

加上一个注释说明

它的接口的名称呢

就叫保存角色权限

然后的话呢

咱们还给它的参数

加上对应的注释说明

那咱们看一下

这个参数怎么定义呢

定义在具体的参数中

这个参数呢

在这个参数属性之前

这个参数属性呢

是可以支持多个注解的

那咱们可以看到

这里定义了一个API headmet

这个value呢

就是对这个属性的描述

然后这个require呢

是代表它是一个必填项

那同样的话呢

咱们也把下面这个参数的SWG2的配置呢

加入进去

好

这个呢

就给了它一个具体的描述

就是角色ID

那这样呢

咱们就完成了接口的SWG2的文档的注解定义

对于传递的参数

如果是一个对象

并非具体的属性

那么该怎么去定义SWG2的文档配置呢

咱们再回到讲解当中

咱们就以用户分配角色操作接口为例

来做一个讲解说明

咱们同样找到这个接口

咱们要找到它的入口

在control的程式当中

在这里同样

我们可以看到了

有一个API operation的注解

这个呢

是对该接口呢

做一个解决

的描述

那么对应的参数呢

它是如何去配置呢

咱们进入内部

可以看到在这里呢

定义了两个注解

API这个注解呢

是作为一个接口描述的定义

因为咱们下面了会通过SWG2的SWG2做一个集成

这个API注解呢

比如咱们是要提供HOS接口

那么呢

就需要把它们加入上去

那下面这个API model呢

代表的就是参数对象或者是返回对象的

注解说明

这个呢

是对整个对象的一个描述

咱们给了它一个描述

就是用户和角色的环境表

下面呢

有很多的属性

对不对

那么我们要给这些属性呢

再加上具体的描述

在这里呢

就是通过API model properties

做对应的配置

咱们可以看到这个呢

是用户ID的描述

一个sample是什么意思呢

一个sample它的意思呢

就是给了它一个默认的值

也就是说用户可以把这个页面的页面

做成一个模式

也就是说用户可以把这个页面的页面

可以通过SWOG2这个文档上面呢

进行在线的接口测试

那么在线接口测试呢

要传递了一些参数值

对不对

这个参数值呢

如果是咱们不填写这个

它默认的就是会空

如果咱们填写了一个example呢

它的在线测试结果上面

就会给它一个默认值

就是为1

下面的话呢

角色ID也是同样的

这个呢

就可以根据咱们的实际需要

去设置了不同的默认值

能够呢

让这个接口实现了正常的测试

就可以了

下面呢

也是对其他属性的一些描述

咱们呢

都可以看到

那么

如果说有些属性呢

咱们不想通过SWOG2暴露出来

那怎么去做呢

它就会通过一个属性hidden

去做对应的标识处理

比如说

CreditBuy创建人相关的信息

这些话呢

没必要暴露出去

对不对

因为这些呢

既不会作为参数传递过来

也不会呢

作为返回信息

暴露给客户端

所以呢

我们可以把这个属性呢

将它屏蔽掉

就通过hidden的input

对不对

做对应的设置

那另外还有一点呢

大家要注意一下

对于这种

Long数值类型

这个呢

是一个包装对象

对不对

这个包装对象呢

如果是传递为一个Long

这个呢

是没关系

比如说

它传递的是一个Long值

包装对象的话呢

它可以将Long设置进去

但是呢

如果说前端

它传递的是一个空值

那么这个Long的话呢

是无法支持的

所以呢

在这个时候

咱们要给它呢

一个默认的值

明白吗

否则的话呢

如果咱们都不给

前端的值

前端传过来的话呢

就是一个空值

即便你是包装的对象

它也无法进行转换处理

就会出现了

在线接口

测试调用出现了异常

好

这一点呢

大家要明白清楚

接下来呢

咱们再回到讲义当中

这些呢

就是刚才咱们结合代码呢

做的一些具体详解

这些属性的话呢

也做了对应的说明

以及呢

它的注意的地方

如果是数值类型的话呢

在这里建议

要给一个JAMP呢

赋予一个

默认值

否则呢

会出现包错

那接下来呢

咱们就来启动

后台管理服务工程

来验证呢

SWOG2接口文档

能否呢

正常显示出来

咱们找到启动内

右键

run运行

好

启动完成之后呢

咱们拿到这个

接口地址

进行访问

这个呢

是SWOG

它的接口文档的

访问地址

前面呢

是我们的

服务名称

咱们在配置文件当中呢

可以看到

这个呢

咱们的context bus呢

是admin

对不对

后面呢

只要跟上

它对应的

SWOG UI

与TML的

这个后缀路径

就可以呢

访问对应的

SWOG接口文档

咱们呢

来访问测试一下

好

这个时候呢

咱们可以看到

SWOG2的文档呢

它就可以正常显示出来

而且呢

可以看到

Authentic

Logic

Controller

这个接口

Controller层当中呢

咱们是定义了两个接口

在这里呢

都可以显示出来

咱们呢

可以回到Controller层当中

好

在这里呢

咱们定义了一个

用户分配角色操作

另外呢

是保存角色

权限的接口

咱们可以看到

两个接口呢

都已经展示出来了

对不对

那咱们来看一下

这个接口的参数

能否正常显示出来呢

点击保存角色权限

可以看到呢

这两个参数呢

都已经显示出来

而且描述的话呢

跟咱们在代码当中的定义呢

都是一致的

对不对

在这里呢

它都会显示出

它的一个配置要求

就是这个呢

是必填项

require的

接着的话呢

咱们再看一下

用户分配角色操作

这个接口

能否正常显示

在这里呢

它传递的是一个

参数对象

authority user load

对不对

那咱们呢

来具体看一下

好

在这里呢

我们就可以看到

它会将

authority user load

它的属性呢

全部呈现出来

那么

咱们在下面呢

定义了

它的一些属性描述

对不对

像机构ID啊

机构名称

然后呢

也定义了一些默认词

那我们来看一下

点击try it out

好

在这里呢

咱们就可以看到

institution ID呢

它就展示出

它对应的默认词

我们回到代码当中

找到institution ID

可以看到

它默认词呢

是10065

对不对

也就是说

通过咱们

在代码当中

对参数对象的定义呢

它可以正常解析

或生效

点击cancel

再往下面看呢

是它的一些

model信息

这个model信息呢

它显示出来一个

API

response result

这个对应的是什么呢

就是咱们

conclude层当中的

在这里面呢

返回对象

可以看到是

API

response result

对不对

它会呢

将这些信息的话呢

呈现出来

因为咱们在这里呢

没有给大家上

sword2的

诸简说明

所以在这里呢

没有看到它对应的

中文描述信息

对不对

这个呢

大家可以

利用闲余时间

再把这些

扩展信息的

事情去完善一下

参照了咱们

刚才所讲的

方法

去做对应的实现

好

在这里呢

就是

对

sword2

后台管理服务的

集成配置

咱们可以看到

它可以根据

咱们sword2的

配置定义

显示出

对应的接口

但是呢

spring data rest的

暴露接口呢

它就不能显示处理

咱们可以回到代码当中

再来看一下

微博sit里

在这里呢

咱们也定义了

很多的一些接口

对不对

这些呢

也加上了

对应的注释

但是它为什么

没有呈现出来呢

这个呢

是因为

sword2呢

它原生并不支持

spring data rest的

接口的

阻描

所以呢

它无法进行

正常的呈现

下面章节呢

咱们再来解决

这个问题

好

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程为“第3章 Swagger2集成使用”的第2部分，主要讲解如何将Swagger2集成到后台管理服务中，并解决Spring Data REST接口在Swagger UI中无法正常显示的问题。讲师通过IDEA开发环境，演示了在`pom.xml`中添加Swagger2依赖、在配置文件`bootstrap-dev.yml`中配置Swagger属性、以及如何通过`@ApiModel`和`@ApiModelProperty`注解为实体类添加Swagger文档描述。最后，讲师启动项目并访问Swagger UI，展示了集成后的API文档界面，并指出Spring Data REST接口的缺失问题，为后续章节做铺垫。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师在Typora中展示课程大纲，明确本节内容为“3.2 后台管理服务集成Swagger2”。
*   **00:05 - 00:15**: 讲师在IDEA中打开`pom.xml`文件，演示如何添加Swagger2的依赖项。
*   **00:15 - 00:25**: 讲师切换到`bootstrap-dev.yml`配置文件，演示如何配置Swagger的`enabled`、`title`、`description`和`version`等属性。
*   **00:25 - 00:35**: 讲师在`SwaggerProperties`类中展示如何配置全局的Swagger属性，如`host`和`authRegex`。
*   **00:35 - 00:45**: 讲师在`AuthorityLogicController`控制器中展示一个保存角色权限的接口`@PostMapping("/savePrivileges")`。
*   **00:45 - 00:55**: 讲师在`AuthorityUserRole`实体类中，使用`@ApiModel`和`@ApiModelProperty`注解为字段添加Swagger文档描述。
*   **00:55 - 01:05**: 讲师在IDEA中展示`AuthorityUserRole`类中`institutionId`字段的注解，并通过鼠标悬停查看其在Swagger UI中的显示效果。
*   **01:05 - 01:15**: 讲师在Typora中展示课程大纲，进入“3.3 让Swagger支持Spring data Rest接口”章节。
*   **01:15 - 01:25**: 讲师在Swagger UI界面中展示已集成的接口，包括`/authorityLogic/savePrivileges`和`/authorityLogic/userAssignRoles`。
*   **01:25 - 01:35**: 讲师在Swagger UI中点击`/authorityLogic/userAssignRoles`接口，展示其参数列表。
*   **01:35 - 01:45**: 讲师在IDEA中展示`ApiRespResult`类，说明其作为统一返回对象的作用。
*   **01:45 - 01:55**: 讲师在Typora中展示课程大纲，指出Spring Data REST接口在Swagger UI中无法显示的问题。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲：`第3章 Swagger2集成使用`，包含子章节`3.1 自定义Swagger2启动器`、`3.2 后台管理服务集成Swagger2`、`3.3 让Swagger支持Spring data Rest接口`等。
    *   配置文件说明：`# Swagger界面内容配置`，包含`enabled: true`、`title: 交易平台API接口文档`、`description: 交易平台API接口文档`、`version: 1.0.2`。
    *   问题提示：`能够看到我们的接口，但是Spring data rest暴露的接口却不能显示处理，下面我们来解决此问题。`

*   **代码关键内容**:
    *   **Maven依赖 (pom.xml)**:
        ```xml
        <!-- swagger 自定义启动器的依赖 -->
        <dependency>
            <groupId>com.itcast.trade</groupId>
            <artifactId>stock-starter-swagger</artifactId>
            <version>${project.stock.version}</version>
        </dependency>
        ```
    *   **配置文件 (bootstrap-dev.yml)**:
        ```yaml
        # Swagger界面内容配置
        swagger:
          enabled: true
          title: 交易平台API接口文档
          description: 交易平台API接口文档
          version: 1.0.2
        ```
    *   **实体类注解 (AuthorityUserRole.java)**:
        ```java
        @ApiModel("AuthorityUserRole(用户与角色关联表)")
        public class AuthorityUserRole extends BaseEntity {
            @ApiModelProperty(value = "用户ID", example = "1")
            private Long userId;
            @ApiModelProperty(value = "角色ID", example = "10171")
            private Long roleId;
            @ApiModelProperty(value = "角色名称")
            private String roleName;
            @ApiModelProperty(value = "机构类型", example = "COMPANY")
            private String institutionType;
            @ApiModelProperty(value = "机构ID", example = "10065")
            private Long institutionId;
            @ApiModelProperty(value = "机构名称", example = "御金汇公司")
            private String institutionName;
        }
        ```
    *   **控制器方法 (AuthorityLogicController.java)**:
        ```java
        @PostMapping(value = "/savePrivileges")
        public ApiRespResult savePrivileges(@RequestParam("roleAuth") String roleAuth,
                                            @RequestParam("roleId") String roleId) {
            ApiRespResult result = null;
            try {
                authorityLogicService.savePrivileges(roleAuth, roleId);
                result = ApiRespResult.success();
            } catch (Exception e) {
                log.error(e.getMessage(), e);
                result = ApiRespResult.sysError(e.getMessage());
            }
            return result;
        }
        ```
    *   **返回对象 (ApiRespResult.java)**:
        ```java
        public class ApiRespResult<T> implements Serializable {
            private static final long serialVersionUID = -1L;
            private String code;
            private String message;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：集成Swagger2依赖** (00:05 - 00:15)
    *   **描述**: 讲师在IDEA中打开`pom.xml`，将`stock-starter-swagger`依赖项添加到`<dependencies>`标签内，并展示其`groupId`、`artifactId`和`version`的配置。
    *   **技术要点**: 通过Maven管理依赖，确保Swagger2相关组件能被项目正确引入。

*   **场景二：配置Swagger属性** (00:15 - 00:25)
    *   **描述**: 讲师切换到`bootstrap-dev.yml`文件，修改`swagger`配置块，设置`enabled`为`true`，并配置`title`、`description`和`version`。
    *   **技术要点**: 通过配置文件控制Swagger UI的显示和文档元数据，使其符合项目需求。

*   **场景三：为实体类添加Swagger注解** (00:45 - 00:55)
    *   **描述**: 讲师在`AuthorityUserRole`实体类中，为每个字段添加`@ApiModelProperty`注解，并设置`value`和`example`属性。
    *   **技术要点**: 使用Swagger注解为实体类字段生成详细的API文档，提升接口文档的可读性和专业性。

*   **场景四：展示Swagger UI界面** (01:15 - 01:25)
    *   **描述**: 讲师启动项目后，在浏览器中访问`http://127.0.0.1:10691/admin/swagger-ui.html`，展示Swagger UI界面。
    *   **技术要点**: 验证Swagger2集成成功，查看已注册的接口和模型，确认文档生成效果。

*   **场景五：指出Spring Data REST接口问题** (01:45 - 01:55)
    *   **描述**: 讲师在Typora中展示课程大纲，明确指出Spring Data REST接口在Swagger UI中无法显示的问题，并预告下一节将解决此问题。
    *   **技术要点**: 识别并记录当前集成的局限性，为后续学习提供明确的方向。
