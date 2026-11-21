# 27-声明式缓存（声明式缓存代码实现_编写拦截 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

导入了这么几个工具类对吧

这几个工具类呢

咱们后续呢都会使用到它

那接下来呢我们来看下一个小节

就是编写拦截器

这个呢应该是我们

整个这个声明式缓存啊

实现过程当中非常非常重要的一环

这个呢我们前面在做

这个实现思路的时候呢

也提到了对吧

这里边呢我们会涉及到这么一个拦截器

而这个拦截器呢

它是用于拦截什么呢

加入缓存相关注解的这些control的方法的

同时呢这个拦截器呢

它其实本质上又是一个AOP的切面

又是一个切面

好那接下来呢

我们就把这个拦截器呢来创建出来

这个拦截器呢

我们把它放到哪呢

咱们来在这呢来创建一个

在我们J2Catch下边来创建一个包

就叫做AOP

因为整个这一套呢

我们其实全都是基于Spring的AOP啊

来实现的

所以我们在这呢创建这么一个包

然后在这个包下边来创建咱们这个拦截器

这个拦截器的名字呢

我就直接从这来复制了一下

叫做CatchMap

Asset Interceptor

好直接把它粘贴在这

这是我们的缓存

在这来写一下缓存操作的这个拦截器

然后刚才提到了

这个拦截器的话呢

它之所以是拦截器呢

必须要实现我们这个拦截器接口

对吧

Interceptor

不要导错了

你看这个拦截器有很多

对吧

咱们导的是这个

Spring什么AOP

AOP

Alice对吧

在这个包下边这个拦截器

好

然后呢刚才提到了

这个拦截器呢

它同时呢又是作为我们AOP的切面存在的

对吧

所以说呢我们在这呢需要指定一个什么呢

就是SPEC的

这个表示当前这个类呢

是一个切面类

同时呢这个类呢也是需要实力化的

所以我们需要给它加一个Component注解

这个都没什么好说的

然后接下来呢

我们需要来指定什么呢

就是我们这个AOP啊

在这个地方呢

底层它会使用一个AOP框架

就是SPEC的J

所以我们在这呢需要来使用

这个Enable SPEC的J Autoproxy

其实就是基于这个什么呢

SPEC的J框架来自动产生代理

那么为谁产生代理呢

咱们一会儿是不是需要指定

就是通过来判断什么呢

我们Controller方法上是否有那个什么呢

Catch注解

是不是来产生代理

说白了它就是为我们的Controller来创建代理

那么创建代理呢

那么创建代理的时候呢

它是有两种创建方式对吧

两种创建方式

一种是基于JDK动态代理

还有一种呢就是CGlib

而我们这个地方呢需要指定什么呢

使用CGlib

那么如何指定呢

其实就是通过这个Proxy Target Class等于True

字面翻译呢

你看Proxy就是代理

Target就是目标对吧

目标类

也就是为目标类创建代理

这个值是不是等于True啊

而我们CGlib呢

它的这个代理的原理其实是什么呢

就是为我们的Controller这个类

来创建子类对象

也就是说我们这个代理跟目标

跟目标类之间呢

是一个继承的关系

所以这个地方呢

我们需要这个是指定什么呢

指定使用CGlib吧

这种方式

为我们的这个Controller

是不是来创建代理对象

然后呢代理对象呢

这个代理对象

其实是我们这个目标对象

就是我们那个Controller对象

它的一个

它的一个什么呢

它的子类

他们之间是这么一个继承关系

这个我们前面如果讲过

大家学过这个SpringAOP

应该也都知道

那么这个地方为什么我们强调

一定要使用这种CGlib代理方式呢

就是因为另外的

比如说我们使用JDK动态代理呢

它其实是什么呢

是基于接口来创建代理对象

也就是我们这个代理对象呢

是必须要实现什么呢

实现一个接口的

这个接口呢

同时又是我们目标对象实现的一个接口

也就是说我们这个

如果使用这个JDK动态代理的话

它创建出来的这个代理类呢

跟我们目标类之间

它们是一个并列的关系

它们拥有共同的接口

而我们Controller呢

往往是没有接口的

对吧

所以说这个地方呢

要保证我们这个代理对象能够创建成功

这个地方呢

我们使用这种CGlib这种方式肯定是没有问题的

好

所以在这呢

这是指定啊

使用我们这个SPECJ

它的自动代理

同时呢

指定这个代理创建的方式

好

然后呢

这个地方还有一个小的细节呢

就是我们在这需要通过import呢

来引入什么呢

刚才咱们导入的这个工具类

就是这个SpringApplicationContactUtils

这个工具类

那么为什么要引入这个工具类呢

我现在在这来写一下

先把它导入一下

好

那么为什么一定要引入我们这个工具类呢

是因为啊

你看我们这个工具类上面是不是加了这个component的注解

对吧

也就是说我们当前这个类呢

也是需要Spring容器来管理

同时呢

把Spring这个上样文对象是不是给我们注进来

那么因为我们当前这个所在的包呢

是我们这个什么呢

J2CatchAOP这个包下边

那么可能在有很多情况下呢

我们这个SpringBoot呢

并没有扫描到我们这个工具类

也就是说根本就没有扫描到这个类的存在

那么如果扫描不到它的话呢

那你这个AutoVar的注解肯定它也就注不进来了

对不对

也就注不进来了

那这样的话呢

我们再调用这个getApplicationContext的方法

它返回的这个对象呢

它是不是就是一个空的呀

它就是一个空的

所以说呢

我们在这呢

要保证什么呢

这个对象能够这个注入成功

就需要让Spring容器能够扫描到这个类

那这个时候呢

我们在这加一个import

只要它能扫描到我们这个拦截器

那么我们这个类呢

是不是也就会被引进来

那么这样的话Spring就能感知到它

好

这是咱们这个interceptor

好

然后呢

我们大体的框架已经定义好了

接下来呢

我们就需要在这呢

来定义两个方法

你看这两个方法是干什么呢

就是加入我们这个around

around是不是就是一个环绕通知

这么一个注解

大家再来回想一下

我们前面在讲这个AOP的时候呢

是不是我们讲过有切面

对吧

有切点

还有什么通知

这些概念

对象目标对象

对吧

一大堆的这种术语

好

而我们这个地方呢

就会使用这个around

这叫做环绕通知

对吧

来指定

所以我们在这呢

需要先来定义一个方法

定义一个方法

确切的来说呢

应该是定义两个方法

为什么呢

因为我们在这是不是

指定了两个注解

对吧

指定两个注解

要对这两个注解进行拦截

也就是说

我们controller方法上

加了这两个注解

这个时候呢

就需要拦截这个controller

好

因为是两个注解

所以我们给它分开定义

定义成对应的两个方法

这样呢

就比较明确了

好

public

然后返回值呢

一般就是定义成object

然后这个方法名

其实可以任意

这个方法名定义成什么都可以

我在这呢

来看一下

咱们这个简易上

是怎么定义的

叫做invoke

什么catch all method

对吧

然后呢

关键是什么呢

关键就是这个方法呀

它需要指定参数

这个参数呢

就是我们这个

这个参数呢

就是我们这个

这个参数呢

就是我们这个

连接点

连接点

叫做什么呢

proceeding

proceeding

joint point

proceeding

joint point

对吧

可执行连接点

proceeding

joint point

proceeding

joint point

这叫可执行连接点

然后呢

我们需要给这个方法

来干什么呢

加入刚才我提到的

那个around

这叫做环绕通知

这叫做环绕通知

对吧

这么一个注解

然后呢

在这里边来指定什么呢

我们要拦截哪一个注解

拦截哪个注解

拦截哪个注解

拦截哪个注解

拦截哪个注解呢

拦截哪个注解呢

咱们这个地方呢

来拦截的就是

这个catch注解

拦截哪个注解呢

咱们这个地方呢

来拦截的就是

这个catch注解

所以有时候

我们把它复制过来

你看

好

你看

这是不是就是咱们定义的

所定义的这个catch注解

对吧

只要这个control的方法上

加的是这个注解

那这个时候呢

就会被我们

拦截到

并且呢

就会拦截到之后呢

它就会执行我们当前这个方法

执行当前这个方法

然后呢

这个是我们的环绕通知

环绕通知

大家还记得吧

除了我们的环绕通知

其实还有另外几种通知的类型

对吧

比如说我们的这个什么

前置通知

什么后置通知

对吧

包括这个环绕通知

还有什么异常通知

等等这些

那么这个呢

是环绕通知

也就是说

当我们control的方法上

加了这个注解之后呢

就会被拦截到

然后呢

就会执行当前这个方法

然后呢

这个方法呢

如果我想放行

对吧

我想直接去放行

然后调用我们的目标对象

那么怎么调用呢

其实就是通过调用我们这个proceeding

它的这个什么呢

它的这个proceed的方法吧

看这有一个叫做proceed的方法

是不是来这个获得

所以说呢我们在这个地方呢

就可以直接

如果要是放行的话呢

我们直接调用这个proceeding

join point的连接点对象的一个proceed的方法

然后呢

有可能需要把这个参数给它传回去

对吧

那么咱们这个control的方法一边都有参数

而这个参数呢

通过它呢也能够获得到

直接通过连接点.get什么呢

args对吧

其实这就是获得它的这个

获得它的这个参数

然后这个异常信息呢

我们就可以直接简单抛一下就可以了

往外抛

throws

从这往外抛一下

这个呢

这就是通过反射呢

是不是去放行了

这个其实就是放行了

我们的这个调用我们目标对象了啊

但是在调用目标对象之前呢

我们可以在这来先说出一句话

具体怎么处理这个缓存对吧

怎么去解析这个缓存

一会儿怎么去解析这个注解

我们一会再说

咱们先把这个流程跑起来

就是看看什么呢

我们这个拦截器到底能不能起作用

到底能不能真正拦截对吧

如果能够测试通过能够真正的拦截

然后我们再做进一步的这个缓存相关的处理

所以说呢

我们现在这呢

简单来一个输出语句啊

这个就是什么呢

我们这个缓存拦截器对吧

那么

执行了啊

简单的在这儿来输出一下就可以啊

这个方法呢

他就是拦截什么呢

这是拦截我们这个方法上使用这个什么呢

catch注解的这个control

然后呢

除了这个之外呢

咱们是不是需要再来

复制一份

这个是干什么呢

这个是不是就是

把这个给他改一下

这个叫做什么catch evict对吧

也就是改成这个注解

刚才也提到了

我们需要提供两个方法对吧

这个呢

就是处理什么呢

就是我们这个方法上有这个注解

这就表示我们要清理缓存了对吧

所以说呢

我们这个地方呢

这里面呢

就是要清理缓存

这个地方呢

就是要设置缓存

好

然后呢

这个方法名呢

咱们给他改一下啊

现在是方法名是冲突了啊

这个invoke catch evict all method

好

现在呢

咱们大体这个架子呢

就是已经搭起来了

对吧

只不过在这个地方是有一句

只是有一个输出语句

一会呢

我们再去完善它

那接下来呢

我们就想来测试一下

对吧

看看我们当前这个什么呢

这个拦截器

他到底能不能起作用

好

现在呢

咱们可以这样啊

嗯

在我们这个controller当中

找一下我们这边

这是不是有个controller

对吧

然后呢

我们就直接啊

嗯

来复制一个controller

来简单测试一下

咱们这个就叫j2catch controller吧

好

j2catch controller

然后呢

我们在这里边呢

来测试一下

好

这呢

改成j2catch

好

或者就叫catch也行

好

简单一点

然后这里边呢

咱们可以给他指定几个方法

对吧

指定几个方法

这里边这些东西呢

都不要了

都不要了

好

然后呢

我们可以把这些方法都给他去掉

好

只保留一个方法

一会我们把这个方法呢

给他改造一下

这些都不要了

都去掉

然后呢

比如这个方法呢

还叫这个detail

对吧

然后呢

这个地方还是addressbook

然后呢

这个地方还是ID

这里边呢

还是addressbook

里边呢

都不要

好

咱们这呢

可以直接来

我们就不再去访问数据库了

咱们怎么做呢

直接自己来造一个数据就可以了

造一个假数据

假设呢

就是从我们这个数据库里面来

这个查出来的

对吧

假设就是从数据库里面查出来的

然后呢

把这个addressbook

给他返回一下

好

返回的时候呢

我们来设置一下

他的这个ID啊

这个ID呢

就是我们传过来的

这个ID

好

然后呢

addressbook.set

他什么呢

address

好

这个呢

来一个北京

好

其他的属性我就不再一个一个设置了

假设这段代码呢

这就相当于我们是从数据库里面

那么查出来的数据

对吧

然后呢

最后把它返回

这个就是我们的查询数据库

好

OK

然后呢

我们给这个方法来加一个注解

加一个什么呢

catch注解

对吧

加一个catch注解

好

然后呢

在这儿来指定什么呢

region对吧

比如这个region呢

我就来一个addressbook

好

然后呢

这个key呢

我就来一个什么呢

ab

好

然后呢

这个parameter呢

我就来一个ID

好

咱们这个注解是不是已经加上了

然后按照我们刚才提到的

只要这个controller方法上呢

加了这个注解之后啊

他应该就可以拦截到

对吧

那接下来呢

我们来测试一下

看看他到底能不能拦截到

如果要是能拦截到我们这个方法

那也就是说

我们这个方法

执行之前

先要执行这个拦截器的这个方法

对吧

拦截器的这个方法

那这个时候呢

我们应该在控制台能够看到这句话

好

那接下来呢

咱们把这个项目呢

来启动一下

好

咱们现在这个项目呢

已经跑起来了

那接下来我们来测试一下

看看他到底能不能

执行到我们这个拦截器

这个拦截器到底能不能起作用

其实我跟大家说

这个拦截器呢

现在是不能起作用的

咱们先来看一下

然后我们再来说啊

他为什么不起作用

好

那么我们可以通过咱们这个

SWAG来测试一下

Localhost

然后端口号呢

是8189

就这个

找到我们这个D2Cache

对吧

这个

然后呢

这里面有一个Detail这个

然后我们Try it out

对吧

然后呢

在这个地方来输入

随便输入一个123吧

点

执行

看我们控制台

你看查询数据库

对吧

然后呢

并没有看到这句话

然后呢

我们可以在这加一个断点

对吧

因为我现在是debug方式来启动的

然后再来执行

你会发现啊

他控制台又输出了

查询数据库

说明我们control的方法没有问题

执行了

但是呢

这个地方并没有过来

也就是说我们当前这个什么呢

这个拦截器其实并没有起作用

哎

这个是为什么呢

我们现在写的代码都没有问题啊

为什么他还还不能起作用呢

其实就是因为什么呢

就是因为我们当前的

这个拦截器

sprint框架根本就没有感知到

哎

更确切的说呢

根本就没有扫描到他

哎

你看我们当前这个拦截器

他是放在哪个包下边啊

他是不是在我们这个j2cache

在我们这个j2cache

aop这个包下边

对吧

而我们的启动类呢

是在这个品达这个下边

那这样的话呢

他默认情况下

是不是只会扫描我们这个品达下边

或者跟他评级的这些包里面的

这些类

而我们这个j2cache呢

这里边这些类呢

根本就没有扫描到

哎

所以说呢

这个框架根本就没有扫描到我们这个类

那他怎么可能起作用啊

对不对

所以说呢

我们这个地方呢

需要哎

让我们这个框架能够知道

能够感知到我们这个类的存在

也就是能够扫描到他

然后呢

才能相应的进行实力化

对不对

然后这个时候他才能起作用

好

所以一会呢

我们可以来改造一下

大家可以想一想啊

我们应该如何能够让我们的sprint框架

能够扫描到这个类

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面，进行的结构化中文输出：

---

### 1) 视频摘要

本视频课程聚焦于 Spring 框架中如何实现基于注解的缓存功能。讲师通过一个名为 `j2cache` 的项目，详细演示了如何自定义一个缓存拦截器（`CacheMethodInterceptor`）。核心内容包括：编写拦截器类、注入 Spring 上下文工具类、使用 `@Around` 注解实现环绕通知、以及如何通过 `@Cache` 注解标记需要缓存的方法。视频通过代码编写、注释说明和控制台日志输出，完整地展示了缓存拦截器的实现逻辑和工作流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，展示项目结构和当前学习的章节：`6.2.4 编写拦截器`。
*   **00:05 - 00:15**: 讲师在 `CacheMethodInterceptor.java` 文件中，开始编写拦截器类，并导入必要的依赖包，如 `org.aopalliance.intercept.Interceptor` 和 `org.aspectj.lang.annotation.Aspect`。
*   **00:15 - 00:25**: 讲师引入 `SpringApplicationContextUtils` 工具类，用于获取 Spring 的 `ApplicationContext`，并用 `@Component` 注解将其标记为 Spring Bean。
*   **00:25 - 00:35**: 讲师在 `CacheMethodInterceptor` 类中添加 `@Component` 和 `@Aspect` 注解，使其成为一个 Spring 的组件和切面。
*   **00:35 - 00:45**: 讲师使用 `@EnableAspectJAutoProxy(proxyTargetClass = true)` 注解，指定使用 CGLIB 方式创建代理对象，以支持对 `@Controller` 等类的代理。
*   **00:45 - 00:55**: 讲师编写 `@Around` 环绕通知方法 `invokeCacheAllMethod`，并使用 `@Cache` 注解作为切入点。
*   **00:55 - 01:05**: 讲师在方法中打印日志“缓存拦截器执行了...”，并调用 `proceedingJoinPoint.proceed()` 继续执行原始方法。
*   **01:05 - 01:15**: 讲师在 `J2CacheController` 中，为 `detail` 方法添加 `@Cache` 注解，并演示如何通过 `cacheChannel` 获取缓存数据。
*   **01:15 - 01:25**: 讲师运行程序，通过控制台日志观察缓存拦截器的执行过程，验证其功能。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲显示当前章节为 `6.2.4 编写拦截器`。
    *   代码文件 `CacheMethodInterceptor.java` 和 `SpringApplicationContextUtils.java` 的结构和注释。
*   **关键代码**:
    *   **拦截器类定义**:
        ```java
        @Aspect
        @Component
        @EnableAspectJAutoProxy(proxyTargetClass = true)
        @Import(SpringApplicationContextUtils.class)
        public class CacheMethodInterceptor implements Interceptor {
        ```
    *   **环绕通知方法**:
        ```java
        @Around("@annotation(com.itehima.j2cache.annotation.Cache)")
        public Object invokeCacheAllMethod(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
            System.out.println("缓存拦截器执行了...");
            return proceedingJoinPoint.proceed(proceedingJoinPoint.getArgs());
        }
        ```
    *   **工具类 `SpringApplicationContextUtils`**:
        ```java
        @Component
        @Primary
        public class SpringApplicationContextUtils {
            @Autowired
            private ApplicationContext applicationContext;
            @PostConstruct
            private void init() { springContext = applicationContext; }
            public static ApplicationContext getApplicationContext() {
                return springContext;
            }
        }
        ```
    *   **控制器方法**:
        ```java
        @GetMapping("detail/{id}")
        @Cache
        public AddressBook detail(@PathVariable(name = "id") String id) {
            // 查询缓存
            CacheObject cacheObject = cacheChannel.get(region, id);
            if (cacheObject.getValue() != null) {
                return cacheObject.getValue();
            }
            // 查询数据库
            AddressBook addressBook = addressBookService.findById(id);
            cacheChannel.set(region, entity.getId(), entity);
            return addressBook;
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建拦截器类** (00:05-00:15)
    *   讲师在 `CacheMethodInterceptor.java` 文件中，创建一个实现了 `Interceptor` 接口的类。
    *   他导入了 `org.aopalliance.intercept.Interceptor` 和 `org.aspectj.lang.annotation.Aspect` 等必要的包。
    *   他添加了 `@Aspect` 注解，表明这是一个切面。

*   **场景二：注入 Spring 上下文** (00:15-00:25)
    *   讲师展示了 `SpringApplicationContextUtils.java` 文件，这是一个工具类。
    *   他使用 `@Autowired` 注解注入 `ApplicationContext`，并用 `@PostConstruct` 初始化静态变量 `springContext`。
    *   他通过 `@Import` 注解将该工具类导入到拦截器中，以便在拦截器中获取 Spring 上下文。

*   **场景三：编写环绕通知** (00:45-01:05)
    *   讲师在 `CacheMethodInterceptor` 类中，编写了 `@Around` 注解的方法。
    *   他使用 `@annotation(com.itehima.j2cache.annotation.Cache)` 指定切入点为所有带有 `@Cache` 注解的方法。
    *   在方法体内，他打印日志“缓存拦截器执行了...”，然后调用 `proceedingJoinPoint.proceed()` 继续执行原始方法。

*   **场景四：应用注解与测试** (01:05-01:25)
    *   讲师在 `J2CacheController` 中，为 `detail` 方法添加了 `@Cache` 注解。
    *   他演示了如何通过 `cacheChannel` 获取缓存数据，如果缓存中没有，则查询数据库并设置缓存。
    *   他运行程序，控制台日志显示“缓存拦截器执行了...”，验证了拦截器成功生效。

---
