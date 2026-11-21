# 59-规则引擎Drools-Spring整合Drools（Spring — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来咱们继续来看Spring整合DROs,刚刚我们完成的是Spring整合DROs,是这种简单整合方式,然后我们通过单元测试这种方式来进行的测试。

现在我们相当于是在原先的基础之上加入我们的Web模块,也就是加入了我们的Spring MVC,在我们一个Web工程里面来进行整合,然后我们在测试的时候也就不用再做单元测试了,而是直接启动我们的Tomcat服务器,然后我们可以通过Controller这种方式来访问它。

好,那接下来我们就来看根据步骤,按照步骤来整合一下。

第一步还是创建一个新的。

Maven工程,而这个Maven工程是不是就必须是这种WAR工程了,打包方式是WAR的,因为我们最终是一个Web工程,需要Tomcat来运行环境来支持。

咱们来创建一个新的工程,就叫DROs-SpringWeb。

好,在我们Idea这边,这个我们就不需要了,直接创建一个新的。

在这儿咱们是不是就需要来选择股价了,那么我们这儿选的股价是这个WebApp,这个。

好,同样这儿来指定一下,CAM点,IT黑码。

模块ID呢,就是这个DROs-SpringWeb。

好,这块呢我们来看一下,这个是没问题的,然后直接Next。

这是创建在这个目录下也不用改了。

好,在当前窗口打开我们这个新创建的工程。

稍微等待一下,因为呢它要下载一些东西。

好,这已经这个创建好了。

创建好之后啊,它其实自带了很多东西啊。

还有这个地方呢,它给我们指定的这个编译的版本呢,我们给它改一下,改成1.8的。

它生成的是1.7的。

好,它这些Dependency呢,我们给它干掉,不要。

包括呢,它生成的这些Build的这些东西呢,我们都不需要啊,所以都给它删掉。

好,从这儿呢,也能看到它的打包方式是这种挖包的方式啊。

好,把这里边这些东西呢,整个清理一下。

然后呢,我们。

来导入相关的这些依赖。

还有这个Properties里边啊,这些啊。

嗯。

前面这几个呢,已经有了,对吧。

然后呢,还是这一块呢,我先。

对应的拷过来。

这是指定我们框架啊,版本。

版本号的。

然后再往下呢,是不是就是相应的一些Dependency,Maven坐标了。

而这个坐标的话呢,前面这些啊。

跟我们刚才这种简单整合方式是完全一样的。

相当于它是在原先的基础之上,

我们加入了什么呢?

加入了一个是Spring-Web,

还有一个是Spring-WebMVC对吧。

也加入了这么两个坐标。

因为我们当前呢,是一个Web工程啊。

需要使用到Spring-WebMVC框架。

所以这个坐标呢,是在上一个工程的基础之上,

又加入了这么两个坐标。

好,这个呢,我们就不再解释了。

咱们对这个应该还是比较熟悉的。

然后再往下呢,是一个插件的配置。

因为一会儿呢,我们要使用TalmCAD插件啊。

所以在这儿呢,我们Build这个标签里面,

配置了一个TalmCAD插件。

那么基于TalmCAD插件这种方式呢,

来启动我们的TalmCAD服务器。

好,这个就已经考过来了。

我们使用的这个端口号呢,就是80。

但是这个呢,你可以自己指定成其他的都可以。

在这儿呢,我就不再改了。

就是80端口。

然后呢,请求路径就是一个斜线。

那就表示我们不用项目名访问啊。

直接来访问我们当前这个工程里边的Controller就可以了。

好,这是关于我们的这个工程的控制。

我们的POM文件呢,咱们就已经配置好了。

接下来呢,我们来配置一下web.tmr。

因为什么呢?我们要使用Spring MVC对吧?

所以我们需要在web.tmr里面呢,

来配置Spring MVC的这个Dispatcher ServerLate。

这个叫做前端控制器对吧?

好,需要把它配置一下。

打开我们的web.tmr。

好。

咱们在这儿呢,来配置一下。

关于这个配置呢,

我们就不再多说了。

直接把这个ServerLate是不是配置拷过来。

好,放到这儿来。

大家看,我们直接拷过来就可以。

然后呢,我们配置的是星点度对吧?

也就是说我们这些Controller啊,它的请求路径啊,

必须都是以这种点度结尾,

然后呢就可以请求到我们编写的这些Controller。

但这儿呢,也可以配置其他的。

那么我们还是习惯用这种星点度这种方式。

然后呢,它在启动的时候,

大家看,这儿我们配置了一个load on startup。

还记得这种用法吗?

这个是不是指的就是我们这个Talmokad的服务器启动的时候呢,

就会去加载我们当前这个ServerLate,

并且呢,去读取这个配置文件对吧?

现在它爆红,就是因为我们现在是不是还没有这个配置文件,

还不存在这个配置文件。

所以下一步呢,我们就需要把这个配置文件创建出来。

那这个配置文件应该放在哪儿呢?

是不是应该放在我们的这个resources下面。

而现在它有这个resources,

没有这个吗?

没有吧。

所以我们在这儿呢,需要来这个创建一下。

需要给它来创建一下。

咱们在这个Main下面,对吧?

Src Main,然后呢,下面我们来创建一个目录。

一个是什么呢?

Java,还有一个是resources。

把缺失的这个目录呢,给它来补全一下。

那么需要注意的是什么呢?

当前呢,它,这只是两个普通的文件夹,对吧?

像我们这个Java下面呢,是不是应该放的是我们的Java代码。

resources下面呢,放的是相关的一些配置文件,对吧?

所以呢,我们需要来修改一下。

怎么修改呢?

选中这个Java,点右键。

在这儿是不是有一个make directory as,

将我们当前这个目录设置成什么呢?

对于Java来说呢,是不是应该就是sources root。

好。

而对于resources这个目录呢,应该是什么呢?

就是resources root。

好。

那这个时候呢,我们就可以在resources下面来创建出来,

咱们这个Spring MVC的配置文件了。

好。

在这儿呢,我们来创建一下这个配置文件。

OK。

然后具体这个配置文件的内容呢,我们在这儿就不再编写了。

这些内容呢,我直接拷过来。

好。

直接拿过来。

然后呢,我们大概来看一下这些配置。

还是在这里边呢,我们是不是引入了这个KIE的这个namespace,对吧?

当然对应的呢,也有它的这个约束。

这个配置文件。

然后呢,这块配置咱们其实都见过了。

在我们刚才我们做的这个简单整合里边,其实就是这么配置的。

只不过呢,我现在是把它拿到了Spring MVC这个配置文件里面。

它其实本质上还是Spring的配置文件,对不对?

好。

所以这块拿过来没有做任何变动。

包括我们说的这个注解,对吧?

要支持我们那个KBase啊,KSession啊,那些注解使用。

那么在这个地方也需要把它拿过来。

然后再往下呢,

这个就是关于我们Spring MVC的一些配置。

比如说这个什么呢?

Component scan,对吧?

组件扫描。

然后它要扫描哪个包。

现在呢,它之所以爆红是因为我们现在还没有这个包呢,对吧?

一会儿我们给它创建出来就好了。

然后呢,这个是不是支持我们Spring的注解?

然后呢,这个是注解。

这个呢,是普通的注解支持。

这个呢,是MVC的。

你看,它是MVC这个名称空间下边的这个注解驱动。

其实啊,其实你如果引入了这个之后啊,

上面这个呢,你可以不引入。

就不是必须的了。

因为这个呢,相当于就把上面这些都已经包含掉了。

就是引入它的注解解析器。

好,那接下来呢,我们看它这儿爆红。

那我就需要把这个包呢,给它创建出来。

一会儿呢,它就会扫描我们这个包。

咱们把这个包创建出来,看我们的ITK码。

那么这个包创建出来,你看它这儿是不是就已经不爆红了。

这一步呢,我们就已经搞定了。

这是把我们的SpriteMVC这个配置文件给配置好。

当然如果说我们这个应用比较大的话呢,

我们是建议把这一块怎么着,把这块单独提出来。

提成一个单独的文件。

因为这块呢,都是关于我们DRoads的相关的一些配置。

对不对?

那么因为我们当前这个呢,没有做具体的业务。

主要还是展示我们这个整合的过程。

所以我们这些配置项呢,全都放在一块了。

如果说我们真正做项目,这个业务比较多的话呢,

我们肯定就需要来。

进行这个配置文件的拆分。

对吧?

配置文件的拆分。

然后呢,把同一类的这些配置项,拆分到一个文件里面去。

这是比较规范的一种做法。

那么当前呢,我们就可以直接这么来做了。

这些配置文件就已经搞定了。

再往下呢,咱们是不是需要来编写一个我们的规则文件呢?

这个规则文件呢,咱们还是来创建这个hello world.dll这个文件。

同样的,还是放在这个Ruler,Ruler4目录下。

因为我们在这是不是指定的还是Ruler4。

在这呢,先把这个Ruler4,这应该创建的是Ruler4目录了。

然后在这下边来创建我们的这个规则文件,叫hello world.dll。

这个文件呢,我们还是简单处理啊。

所以这个规则文件还是刚才那个文件,没什么变动。

好,直接拿过来,就可以了。

那这个规则文件就已经搞定了。

然后呢,这儿通过这个目录呢,你看。

也是一致的。

这样呢,我们就可以加载到这个规则了。

加载之后呢,我们需要来编写一个service。

因为前面的话,咱们其实都是通过单元测试的这种方式,对吧?

来获得我们的KBase啊,或是KSession啊。

然后呢,来调用规则引擎相关的API。

那么我们在真正的项目应用当中呢,一般都会去封装一个service。

然后呢,把规则引擎相关的这些操作呢,全都封装到这个service里面去。

好。

所以我们在这儿呢,就来创建一个service类啊。

咱们就叫Ruler Service吧。

好。

然后呢,这个类的话,应该是在我们那个service包下边,对吧?

所以咱们在这儿呢,来创建一个service包。

然后呢,下面创建这么一个类,叫Ruler Service。

好,直接OK。

这样的话呢,在我们service包下边,是不是就创建了这么一个Ruler Service。

然后呢,这个service呢,我希望让我们的Spring把它管理起来。

那也就意味着我需要在它这上面是不是加一个service注解。

加一个service注解,对吧?

这是我们Spring注解。

然后呢,你看它所出的这个包,是不是正好能扫描到它呀。

你看咱们是不是扫描的是cam.attk码。

然后它这下面所有的子包,对吧?

子包,那么都可以扫描到。

那这样的话呢,我们当前这个类是不是就扫描到了。

扫描到之后呢,就可以把这个Ruler Service是不是给创建出来了。

创建出来之后呢,我们希望给我们注进来一个什么对象呢?

注进来一个KBase对象。

而这个KBase呢,

还是通过我们这个注解,你看没有?

还是这个KBase注解。

把它注到我们的service里面来。

同样这个名称呢,KBase是来自于谁呢?

还是来自于这个地方,这个name。

这个对应关系大家要清楚。

这样的话,我们的KBase是不是就已经搞定了,就注进来了。

我们在这来写一下,这个是注入我们的KBase对象,KIE对象。

好。

这就注入了。

注入之后呢,咱们是不是就可以在这里面呢,来定义一个方法,就是触发规则的方法,对吧?

这个方法呢,就叫Ruler吧。

好。

然后这个代码呢,咱们其实就非常熟悉了。

只不过呢,是原先我们都是写在了单元测试方法里面,而现在呢,是写到我们service的这个方法里面去了。

好。

这是定义了这么一个方法,就叫Ruler。

然后在这里面呢,通过KBase来获得一个Session。

然后呢,然后呢,在这儿来触发规则,对吧?

最后呢,把Session给关闭掉。

好。

这是关于我们这个service的编写,还是比较简单的。

然后呢,最后我们是不是来创建一个Controller类啊?

在这儿来创建一个Controller。

直接放在我们这个Controller包下边。

类名呢,就叫HelloController。

同样的,这个呢,也是我们Spring的一个组件。

所以我在这儿是不是需要加一个Controller注解,对吧?

然后呢,这个地方呢,是不是需要来加一个RequestMapping。

咱们能访问到它了。

这个RequestMapping,我来给一个什么呢?

就叫Hello吧。

跟我们讲义保持一致。

好,Hello。

在这里边呢,我是不是需要注入我们的service,对吧?

注入我们的service。

所以,这下面呢,这就通过我们的AutoValue呢,

把刚才咱们定义的这个RulerService给注进来。

注进来之后呢,在我们Controller里边来编写一个方法,对吧?

在这个方法里边来调用我们的service。

好,这就是这么一个调用过程。

这些呢,我就不再写了。

都是比较简单的代码,直接拷过来。

好。

我们来调用一下。

你看,有一个就叫Ruler的方法。

然后呢,它的RequestMapping,对吧?

请求路径呢,就是-Ruler。

在这里边呢,咱们是不是直接来调用我们service的Ruler方法。

然后呢,在这里边,你看,它是不是就最终调用到我们工作这个规则引擎相关的API了。

好,最终把这个规则出发了。

好,那么最后返回一个OK就可以了。

到这儿的话,我们所有的代码是不是都已经写完了。

写完之后呢,咱们就可以一会儿再来测试一下。

好,那么关于我们的这个,

整合代码开发就已经完成了。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对《Spring整合Drools+web》技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程旨在指导学员如何将业务规则引擎Drools与Spring Web框架进行整合，构建一个可运行的Web应用。课程内容从项目初始化开始，逐步讲解了如何在Maven项目中引入必要的依赖（包括Drools和Spring），配置Web应用的部署描述符（`web.xml`）和Spring的配置文件（`springmvc.xml`），并在项目中创建DRL规则文件、服务层和控制器层，最终实现通过HTTP请求触发Drools规则的业务逻辑。整个过程强调了Spring框架在整合Drools中的核心作用，包括依赖注入、注解驱动和配置管理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 课程引言与本节目标。讲师介绍本节将演示如何整合Drools与Spring Web。
*   **00:16 - 00:45**: **第一步：创建Maven Web工程**。在IDE中新建名为 `drools_springweb` 的Maven Web项目，并在 `pom.xml` 文件中配置项目坐标和依赖。
*   **00:46 - 01:15**: **第二步：配置 `web.xml`**。在 `WEB-INF/web.xml` 中配置 `DispatcherServlet`，并指定其加载的Spring配置文件 `springmvc.xml`。
*   **01:16 - 01:45**: **第三步：配置Spring核心文件 `springmvc.xml`**。在 `src/main/resources/springmvc.xml` 中配置Drools的 `KModule`，定义 `KBase` 和 `KSession`，并启用Spring的注解驱动和组件扫描。
*   **01:46 - 02:15**: **第四步：创建DRL规则文件**。在 `src/main/resources/rules/` 目录下创建 `helloworld.drl` 文件，并编写一个简单的规则 `rule_helloworld`。
*   **02:16 - 02:45**: **第五步：创建服务层 `RuleService`**。在 `src/main/java/com.itheima/service/` 目录下创建 `RuleService.java` 类，用于封装调用Drools `KSession` 的逻辑。
*   **02:46 - 03:15**: **第六步：创建控制器层 `HelloController`**。在 `src/main/java/com.itheima/controller/` 目录下创建 `HelloController.java` 类，通过 `@RequestMapping` 映射URL，并调用 `RuleService` 中的方法来触发规则。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: `7.2 Spring整合Drools+web`
    *   **操作步骤**: 第一步：创建 `pom.xml` 导入依赖；第二步：配置 `web.xml`；第三步：配置 `springmvc.xml`。
    *   **依赖版本**: `drools.version=7.10.0.Final`, `spring.version=5.0.5.RELEASE`。
    *   **配置文件路径**: `src/main/resources/springmvc.xml`, `src/main/resources/rules/helloworld.drl`。

*   **关键代码片段**:

    *   **`pom.xml` 依赖配置**:
        ```xml
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
            <version>${spring.version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context-support</artifactId>
            <version>${spring.version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-test</artifactId>
            <version>${spring.version}</version>
        </dependency>
        <dependency>
            <groupId>org.drools</groupId>
            <artifactId>drools-core</artifactId>
            <version>${drools.version}</version>
        </dependency>
        ```

    *   **`web.xml` 配置**:
        ```xml
        <servlet>
            <servlet-name>springmvc</servlet-name>
            <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
            <init-param>
                <param-name>contextConfigLocation</param-name>
                <param-value>classpath:springmvc.xml</param-value>
            </init-param>
            <load-on-startup>1</load-on-startup>
        </servlet>
        <servlet-mapping>
            <servlet-name>springmvc</servlet-name>
            <url-pattern>*.do</url-pattern>
        </servlet-mapping>
        ```

    *   **`springmvc.xml` 配置**:
        ```xml
        <kie:kmodule id="kmodule">
            <kie:kbase name="kbase" packages="rules">
                <kie:ksession name="ksession"/>
            </kie:kbase>
        </kie:kmodule>

        <bean class="org.kie.spring.annotations.KModuleAnnotationPostProcessor"/>

        <context:component-scan base-package="com.itheima"/>
        <context:annotation-config/>
        <mvc:annotation-driven/>
        ```

    *   **DRL 规则文件 `helloworld.drl`**:
        ```drl
        package helloworld
        rule "rule_helloworld"
            when
                eval(true)
            then
                System.out.println("规则：rule_helloworld触发..");
            end
        ```

    *   **服务层 `RuleService.java`**:
        ```java
        package com.itheima.service;
        import org.springframework.stereotype.Service;
        @Service
        public class RuleService {
            // 服务方法体
        }
        ```

    *   **控制器层 `HelloController.java`**:
        ```java
        package com.itheima.controller;
        import org.springframework.web.bind.annotation.RequestMapping;
        import org.springframework.stereotype.Controller;
        import org.springframework.beans.factory.annotation.Autowired;
        @Controller
        @RequestMapping("/hello")
        public class HelloController {
            @Autowired
            private RuleService ruleService;
            @RequestMapping("/rule")
            public String rule() {
                ruleService.rule();
                return "OK";
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与依赖管理**
    *   **描述**: 讲师在IDE中创建了一个名为 `drools_springweb` 的Maven Web项目。随后，他打开了 `pom.xml` 文件，向观众展示了如何添加Drools和Spring框架的依赖，并指定了具体的版本号。演示中重点强调了 `spring-context`、`spring-context-support` 和 `drools-core` 等核心依赖。

*   **场景二：Web应用配置**
    *   **描述**: 讲师切换到 `WEB-INF/web.xml` 文件。他演示了如何配置 `DispatcherServlet`，并将其映射到 `*.do` 路径。同时，他通过注释解释了 `contextConfigLocation` 参数的作用，即指定Spring配置文件的位置。

*   **场景三：Spring核心配置**
    *   **描述**: 讲师打开了 `src/main/resources/springmvc.xml` 文件。他首先配置了Drools的 `KModule`，并定义了 `KBase` 和 `KSession`。接着，他配置了 `KModuleAnnotationPostProcessor` 以支持注解驱动。最后，他添加了 `component-scan` 和 `annotation-driven` 等配置，使Spring能够自动扫描和管理组件。

*   **场景四：规则文件与业务逻辑实现**
    *   **描述**: 讲师在 `src/main/resources/rules/` 目录下创建了 `helloworld.drl` 文件。他编写了一个简单的规则，该规则在条件 `eval(true)` 满足时，会打印一条日志信息。随后，他创建了 `RuleService` 服务类和 `HelloController` 控制器类，通过 `@Autowired` 注解将 `RuleService` 注入到控制器中，并在控制器的 `rule()` 方法中调用服务方法，从而触发Drools规则。

*   **场景五：项目结构与代码组织**
    *   **描述**: 讲师通过IDE的项目结构视图，向观众展示了整个项目的目录结构。他强调了 `src/main/resources/` 目录下存放配置文件和规则文件，`src/main/java/` 目录下存放Java源代码，并按照 `controller`、`service` 等模块进行组织，体现了良好的项目分层架构。
