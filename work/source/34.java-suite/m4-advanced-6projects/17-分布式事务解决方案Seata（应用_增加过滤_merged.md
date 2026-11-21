# 17-分布式事务解决方案Seata（应用_增加过滤 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

咱们继续来看Cita的应用

前面呢我们是已经在程序当中

演入了Cita的相关的Maven坐标

对吧

并且呢在Nux当中来增加了Cita的相关配置

这个配置文件

好那这个过程下一个过程呢

就是什么呢

我们需要来增加一个过滤器

这个过滤器呢就是把什么呢

把我们这个XID呢

把它放到一个叫做RootContext的

这么一个对象里面去

那么为什么要把它放进去呢

大家还记得吧

这个XID呢我们说

它是标识了一个

唯一标识了一个分布式事物

对不对

而这个ID呢是需要在我们

这个Fint调用的过程当中

传播下去的

咱们前面呢在讲这个生命周期的时候

也提到过

你看在这个整个这个

一个分布式啊

一个完整的分布式调用过程当中

它为了标识

这个分布式事物对吧

那么它会啊

每次这个调用的过程当中啊

都会去传播这么一个对象

这么一个

其实就是一个字符串对吧

就是个标识

叫做XID

你看XID通过微服务的调用链传播

而我们这个调用链呢

是通过什么方式去调用呢

是不是就是通过我们的Fint接口

这种方式来进行调用

所以它在调用的过程当中啊

就需要把这个XID给它传播下去

给它传播下去

说的更清晰一点呢

其实就是什么呢

更直白一点

就是什么呢

我们在发送这个请求的时候

需要把这个XID呢

把它放到我们的请求头里面去

然后这边这个微服务呢

就可以从请求头里面

把这个XID呢给它取出来

所以它是通过请求头这种方式

来传递参数

最终把XID呢给它带过去

而现在我们增加的这个过滤器呢

就是什么呢

需要先把这个XID给它获取到

然后放到root context里面去

放好之后呢

在后边我们还要增加一个拦截器

这个拦截器呢

就是干什么呢

就是把我们拿到的这个XID

给它放到什么呢

header

就是请求头里面去

这样的话呢

我们下一个微服务呢

就能够从请求头里面把它取出来

好

所以我们现在先来看这个过滤器

对吧

当然这段代码的话呢

不需要我们自己去编写

因为都属于什么呢

官方提供的一些模板化的代码

所以说呢

我们直接把这个代码拷过来

你只要知道它在做什么事情

就可以了

你看这个地方

我们是不是获得了

一个什么呢

获得了一个这个XID

当然因为我们当前是在过滤器

这个位置

它很有可能是获取不出来的

那这个时候呢

我们就做什么呢

从这个请求头里面来获得一个TXXID

对吧

那么往往这个TXXID呢

它不是空的

因为呢

什么呢

我们其实是通过什么代理技术啊

后边我们知道

它其实是通过代理技术

这个代理对象呢

会给我们这个获取到

这么一个全局的事物ID

然后呢

我们通过这个

root context.bound

是不是就是绑定

然后呢

把这个TXXID给它绑定

这样的话呢

我们到后边这个拦截器的地方呢

就可以把它取出来

然后给它放到哪呢

放到请求头里面去

其实呢

这个root context

大家应该也能猜出来啊

我们一般呢

在进行这种全局这种方式来

这个绑定数据的时候呢

往往都会使用到什么呢

thread local

所以说呢

我们可以简单来看一下啊

它其实就是把这个XID呢

给它通过这种本地现成的方式

来进行绑定

这样的话

我们在程序的任意位置呢

都可以把它取出来

注意看啊

是在哪呢

是在我们这个IO什么什么theta

这个标语下边

对吧

然后呢

它这里边是不是有一个方法

叫做bound

对吧

bound的话呢

它实际上就是调的这个方法

调的这个对象

它的put

对吧

而这个对象呢

就是这个对象

而这个对象是怎么获得的呢

是通过调用什么contact call loader

点load的方法来获得的

而这个方法呢

你看它是不是返回的

就是这个instance对象

而这个instance对象怎么来的呢

它其实最终你看

是不是new的一个这个对象

而这个对象呢

来看一下

它实际上呢

对应的就是谁呢

就是用的这个成员变量

叫做什么呢

叫做这个thread local

对吧

所以它这个封装的是比较深的

其实是一个thread local

然后里边是一个map

这样的话

通过这种方式

来表示我们这个上下文

对吧

这样的话

我们在程序任意位置呢

都可以通过这个上下文对象

把我们这个什么xid呢

给它取出来

好

当然了

我们这一段代码的话呢

就不用自己编写了

咱们只要知道

它起的什么作用就可以了

你看它其实是一个过滤器

对不对

是一个过滤器

那这样的话

我们针对这些微服务

所有的请求

对吧

那么都会经过这个过滤器

来进行处理

好

都会经过这个过滤器处理

所以它的处理的时候呢

首先把我们

这个xid对吧

给它绑定

绑定到我们上下文当中来

然后呢

在这是不是来do filter

是不是表示放行

放行完之后呢

一放行

其实就是我们整个调用链

是不是就调通了

调通了之后呢

最后别忘了

去干什么呢

unbound

是不是就解绑

对吧

解绑

好

这是这个过滤器

它起的作用

那这样的话

我们这个过滤器

应该放在什么地方呢

其实我们这些微服务呢

是不是都会使用到

所以说呢

我们给它放在哪呢

放在我们这个common里面

我在这呢

其实已经放好了

咱们直接来看一下就行了

包括这个代码

大家也不用自己去编写

好

那么你看

在这儿有一个filter

对吧

这里边就有我们这个什么

txxid filter

好

然后呢

这个过滤器

其实是继承了

这么一个过滤器啊

叫vanspr

什么request

这个是谁提供的

实际上就是我们这个

supreme mvc的

对吧

这个

然后呢

直接给它放在这儿

我们拿过来用就可以

别忘了

我们去加

加一个component的注解

也就是说这个过滤器对象呢

也是需要交由supreme来管理的

好

那到这儿的话呢

咱们这个过滤器呢

就已经解释完了

直接烤进来用就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是关于“品达物流TMS项目”第11章“分布式事务解决方案Seata”的技术教学视频。主要内容是讲解如何在Seata框架中，通过自定义过滤器和拦截器，实现将事务上下文（XID）在服务调用链路中进行传递，从而支持分布式事务的全局一致性。视频通过展示代码和PPT，详细说明了如何在`pd-common`模块中创建一个HTTP过滤器（`TxidFilter`）和一个Feign拦截器（`RequestHeaderInterceptor`），并将XID绑定到`RootContext`中，以便在后续的调用中被传递和识别。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开始，展示PPT大纲，当前章节为“8. 增加过滤器”。
*   **00:00:05 - 00:00:15**：讲解“8. 增加过滤器”章节，展示`TxidFilter`类的代码，说明其作用是将HTTP请求头中的`TX_XID`设置到`RootContext`中。
*   **00:00:15 - 00:00:25**：切换到“9. 增加拦截器”章节，展示`RequestHeaderInterceptor`类的代码，说明其作用是将`RootContext`中的XID作为请求头传递给下游服务。
*   **00:00:25 - 00:00:35**：展示`RootContext`类的源码，解释其内部使用`ThreadLocal`来存储和管理上下文数据。
*   **00:00:35 - 00:00:45**：展示`bootstrap-dev.yml`配置文件，说明MyBatis Plus的配置项。
*   **00:00:45 - 00:00:55**：展示`RootContext`类的`bind`和`unbind`方法，说明其如何将XID绑定到当前线程上下文，并在请求结束时解除绑定。
*   **00:00:55 - 00:01:05**：回到`TxidFilter`的代码，重点讲解`finally`块中的`unbind`逻辑，说明其如何确保XID在请求结束时被正确清理。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 大纲**：
    *   项目名称：品达物流TMS项目。
    *   当前章节：第11章 TMS司机端、快递员端开发。
    *   子章节：8. 增加过滤器；9. 增加拦截器。
*   **代码**：
    *   **`TxidFilter` 过滤器**：
        ```java
        @Component
        @Slf4j
        public class TxidFilter extends OncePerRequestFilter {
            @Override
            protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
                String xid = RootContext.getXID();
                String txid = request.getHeader("TX_XID");
                boolean bind = false;
                if (StringUtils.isBlank(xid) && StringUtils.isNotBlank(txid)) {
                    RootContext.bind(txid);
                    bind = true;
                    log.debug("绑定 [" + txid + "] RootContext");
                }
                try {
                    filterChain.doFilter(request, response);
                } finally {
                    if (bind) {
                        String unbindxid = RootContext.unbind();
                        log.debug("解除 [" + unbindxid + "] RootContext");
                        if (txid.equalsIgnoreCase(unbindxid)) {
                            log.warn("变更 [" + txid + "] --> [" + unbindxid + "]");
                            if (unbindxid == null) {
                                RootContext.bind(unbindxid);
                                log.warn("绑定 [" + unbindxid + "] RootContext");
                            }
                        }
                    }
                }
            }
        }
        ```
    *   **`RequestHeaderInterceptor` 拦截器**：
        ```java
        @Component
        public class RequestHeaderInterceptor implements RequestInterceptor {
            @Override
            public void apply(RequestTemplate template) {
                String xid = RootContext.getXID();
                if (StringUtils.isNotBlank(xid)) {
                    template.header("TX_XID", xid);
                }
            }
        }
        ```
    *   **`RootContext` 类**：
        ```java
        public class ThreadLocalContextCore implements ContextCore {
            private ThreadLocal<Map<String, String>> threadLocal = initialValue() -> new HashMap<>();
            public ThreadLocalContextCore() {
            }
            public String put(String key, String value) { return (String)(Map)this.threadLocal.get().put(key, value); }
            public String get(String key) { return (String)(Map)this.threadLocal.get().get(key); }
            public String remove(String key) { return (String)(Map)this.threadLocal.get().remove(key); }
            public Map<String, String> entries() { return (Map)this.threadLocal.get(); }
        }
        ```
    *   **`bootstrap-dev.yml` 配置文件**：
        ```yaml
        # 原生配置
        configuration:
          map-underscore-to-camel-case: ${mybatis-plus.configuration.map-underscore-to-camel-case}
          cache-enabled: ${mybatis-plus.configuration.cache-enabled}
          call-setters-on-nulls: ${mybatis-plus.configuration.call-setters-on-nulls}
          jdbc-type-for-null: ${mybatis-plus.configuration.jdbc-type-for-null}
          log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建过滤器** (00:00:05-00:00:15)
    *   讲师在PPT上展示`TxidFilter`类的代码。
    *   代码中，过滤器首先获取当前线程的XID（`RootContext.getXID()`），然后从HTTP请求头中获取`TX_XID`。
    *   如果当前线程没有XID，且请求头中有XID，则将请求头中的XID绑定到`RootContext`中。
    *   通过`log.debug`输出绑定成功的日志。
*   **场景二：创建拦截器** (00:00:15-00:00:25)
    *   讲师切换到“9. 增加拦截器”章节。
    *   展示`RequestHeaderInterceptor`类的代码。
    *   该拦截器从`RootContext`中获取XID，并将其设置为请求头`TX_XID`，以便在Feign调用时传递给下游服务。
*   **场景三：查看上下文实现** (00:00:25-00:00:35)
    *   讲师展示`RootContext`类的源码。
    *   代码显示`RootContext`内部使用`ThreadLocal`来存储和管理上下文数据。
    *   通过`put`、`get`、`remove`等方法，可以对上下文进行操作。
*   **场景四：绑定与解除绑定** (00:00:45-00:00:55)
    *   讲师展示`RootContext`类的`bind`和`unbind`方法。
    *   `bind`方法将XID存储到当前线程的上下文中。
    *   `unbind`方法从当前线程的上下文中移除XID。
*   **场景五：过滤器的finally块** (00:00:55-00:01:05)
    *   讲师重点讲解`TxidFilter`中的`finally`块。
    *   无论请求处理是否成功，都会执行`unbind`操作，确保XID在请求结束时被正确清理。
    *   代码中还包含了对XID变更的警告日志，以确保XID在调用链路中的一致性。
