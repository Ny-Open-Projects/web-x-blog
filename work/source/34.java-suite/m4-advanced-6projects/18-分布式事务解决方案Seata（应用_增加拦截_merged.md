# 18-分布式事务解决方案Seata（应用_增加拦截 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那接下来呢

咱们继续来看CTA的应用

刚才呢我们是提供了一个过滤器

对吧

这个过滤器它起的作用呢

也是比较单一

就是什么呢

就是把我们这个全局的事物ID呢

给它绑定

实际上就是设置到我们这个

全局的上下文对象里面去了

对吧

那么设置好之后呢

接下来我们就需要来增加一个拦截器

这个拦截器它的作用就是什么呢

来拦截我们所有的FIN调用

因为我们这个微服务呢

在调用过程当中啊

咱们这边是不是全都是使用的

这种FIN接口这种方式来进行调用

而我们前面也一再强调

它在调用的时候呢

需要把这个XID是不是给它传播下去

就是每一次调用的时候呢

把它放到我们的请求头里面去

把它传播下去

所以说呢

我们现在要增加的这个拦截器

起的作用就是什么呢

就是把我们这个XID

给它放到我们的请求头里面去

那这样的话

我们就需要来拦截

所有的FIN

这些请求

那么怎么拦截这些请求呢

就需要来一个FIN的拦截器

我们只要实现这么一个接口

叫做Request Interceptor

Request Interceptor是谁呢

就是在我们Open FIN里边

这个包里边

你看有这么一个接口

只要是我们FIN接口调用

都会啊

都会被拦截

都会被拦截

那么拦截到之后呢

它就会先执行这一段逻辑

因为我们前面也

其实大家应该也都知道

拦截器

底层原理呢

就是基于什么呢

面向切面对吧

动态代理

其实就是对我们这些

FIN接口来进行代理

那么拦截它之后呢

先调用我们这一段代码

而这段代码呢

就是什么呢

就是把我们获取到的这个XID

调用这个Header方法对吧

把它放到我们的请求头里面去

然后呢

我们FIN是不是就真的去发一个请求

对吧

或者是get方式请求

或者是pose方式请求

请求下一个微服务

这样的话呢

我们这个全局的事务ID呢

就被通过请求头的方式

带到了下一个微服务

它其实就是通过我们这个

这种方式给它进行设置的

你看这儿啊

这是也说明了

创建一个FIN的拦截器

把我们这个root context中的XID

对吧

传递到我们这个调用链路上去

那么这个XID呢

我们前面也强调了

它是用来标识一个局部事务

属于哪个全局事务

对吧

需要在调用链路上呢

上下文件呢

当中来进行这个传递

所以说呢

我们只要把这个拦截器呢

给它创建好

就能够达到这样的效果

这个拦截器呢

也是放在哪呢

也是放在咱们这个common里边

PD common里边

在这儿呢

我其实都已经提供好了

别忘了

加一个component的注解

对吧

也就是说

也是需要交由Spring来管理的

这样的话

我们在进行FIN调用之前呢

先被这个拦截器拦截到

然后呢

我们再把这个值给它设置到请求头

好

这是我们当前这一步

这是增加一个拦截器

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频片段是关于分布式事务框架 Seata 的技术实现教学，重点讲解如何在微服务调用链路中传递全局事务 ID（XID）。讲师通过在 `pd-common` 模块中编写和配置两个拦截器——`RequestHeaderInterceptor`（用于 Feign 调用）和 `TxIdFilter`（用于 HTTP 请求过滤）——来确保 XID 能够在服务间传递。视频展示了如何在 Spring Boot 项目中使用 IntelliJ IDEA 编写、调试和管理这些拦截器代码，并最终在 `pd-druid` 模块中取消不必要的过滤器注册，以优化项目结构。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程引入，展示项目结构和当前章节“9. 增加拦截器”。
*   **00:05 - 00:15**: 讲解 `RequestHeaderInterceptor` 拦截器的代码逻辑，用于在 Feign 调用前将 XID 作为请求头 `TX_XID` 传递。
*   **00:15 - 00:25**: 讲解 `TxIdFilter` 过滤器的代码逻辑，用于在 HTTP 请求中获取 XID 并绑定到 `RootContext` 中，以便后续服务能访问。
*   **00:25 - 00:35**: 展示在 IntelliJ IDEA 中对 `TxIdFilter` 类的代码进行调试和修改。
*   **00:35 - 00:45**: 展示在 IntelliJ IDEA 中对 `RequestHeaderInterceptor` 类的代码进行调试和修改。
*   **00:45 - 00:55**: 讲解如何在 `pd-druid` 模块中取消 `TxIdFilter` 的注册，因为该模块不需要使用 Seata。
*   **00:55 - 01:05**: 总结本节内容，强调拦截器在分布式事务中的作用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **PPT / 图表**

*   **Seata 管理的分布式事务的典型生命周期**：
    *   **1. TM** 要求 TC 开始一项新的全局事务，TC 生成全局事务的 XID。
    *   **2. XID** 通过微服务的调用链传播。
    *   **3. RM** 将本地事务注册为 XID 到 TC 的相应全局事务的分支。
    *   **4. TM** 要求 TC 提交或回滚相应的 XID 全局事务。
    *   **5. TC** 驱动 XID 的相应全局事务下的所有分支事务以完成提交或回滚。
    *   **图示**：展示了 TM、TC、RM 三个角色以及它们与数据库（DB）之间的交互关系，通过 XID 进行事务协调。

#### **代码**

*   **`RequestHeaderInterceptor.java`** (Feign 拦截器)
    ```java
    package com.ithema.pinda.common.interceptors;

    import feign.RequestInterceptor;
    import feign.RequestTemplate;
    import io.seata.core.context.RootContext;
    import org.apache.commons.lang3.StringUtils;
    import org.springframework.stereotype.Component;

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
    *   **功能**：在 Feign 调用前，从 `RootContext` 获取 XID，并将其设置为请求头 `TX_XID`。

*   **`TxIdFilter.java`** (HTTP 过滤器)
    ```java
    package com.ithema.pinda.common.filter;

    import org.springframework.stereotype.Component;

    @Slf4j
    @Component
    public class TxIdFilter extends OncePerRequestFilter {
        @Override
        protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
            String xid = RootContext.getXID();
            String txId = request.getHeader("TX_XID");
            boolean bind = false;
            if (StringUtils.isBlank(xid) && StringUtils.isNotBlank(txId)) {
                RootContext.bind(txId);
                bind = true;
                log.debug("绑定 [" + txId + "] RootContext");
            }
            try {
                filterChain.doFilter(request, response);
            } finally {
                if (bind) {
                    String unbindId = RootContext.unbind();
                    log.debug("解绑 [" + unbindId + "] RootContext");
                    if (!txId.equalsIgnoreCase(unbindId)) {
                        log.warn("变更 [" + txId + "] --> [" + unbindId + "]");
                    }
                    if (unbindId == null) {
                        RootContext.bind(unbindId);
                        log.warn("绑定 [" + unbindId + "] 回 RootContext");
                    }
                }
            }
        }
    }
    ```
    *   **功能**：在 HTTP 请求进入时，如果当前上下文没有 XID 但请求头中有 `TX_XID`，则将其绑定到 `RootContext`；在请求结束后，将 XID 解绑，以确保事务上下文的正确管理。

---

### 4) 关键场景与演示描述

*   **场景一：创建 Feign 拦截器**
    *   **描述**：讲师在 `pd-common` 模块中创建了一个名为 `RequestHeaderInterceptor` 的类，该类实现了 `RequestInterceptor` 接口。在 `apply` 方法中，它从 `RootContext` 获取 XID，并将其设置为请求头 `TX_XID`。讲师在 IntelliJ IDEA 中展示了代码的编写和调试过程。

*   **场景二：创建 HTTP 过滤器**
    *   **描述**：讲师在 `pd-common` 模块中创建了一个名为 `TxIdFilter` 的类，该类继承自 `OncePerRequestFilter`。在 `doFilterInternal` 方法中，它首先获取当前上下文的 XID 和请求头中的 `TX_XID`，如果请求头中有 XID 且当前上下文没有，则将其绑定到 `RootContext`。在请求处理完成后，它将 XID 从 `RootContext` 中解绑。讲师在 IntelliJ IDEA 中展示了代码的编写和调试过程。

*   **场景三：取消过滤器注册**
    *   **描述**：讲师在 `pd-druid` 模块中，由于该模块不需要使用 Seata，因此需要取消 `TxIdFilter` 的注册。讲师在 IntelliJ IDEA 中展示了如何在配置文件中移除相关配置。

*   **场景四：调试与修改代码**
    *   **描述**：讲师在 IntelliJ IDEA 中对 `TxIdFilter` 和 `RequestHeaderInterceptor` 的代码进行了多次调试和修改，以确保其功能正确。讲师在代码中添加了日志输出，以便于调试和追踪。

---

以上是根据视频画面进行的结构化技术课程分析。
