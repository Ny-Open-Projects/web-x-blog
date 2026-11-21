# 19-分布式事务解决方案Seata（应用_取消过滤器 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那接下来呢我们继续来看

SITA的应用

刚才呢我们是增加了过滤器

又增加了拦截器对吧

这些呢全都是跟我们这个

分布式事物相关的

其实主要就是在处理什么呢

这个全局的事物ID对吧

让它在我们整个这个调用链上

能够传播下去

就是做这么一个事

那么我们只要给它传播下去就可以了

那么具体它内部怎么去提交

怎么去回滚对吧

它们怎么协调这个不用我们管

这是由我们SITA这个服务呢

它自己来协调的

所以我们只要按照它的要求

给它去传播这个XID就可以了

好那接下来呢

我们还需要来取消过滤器注册

因为什么呢

大家来看

我们前面也解释了PDJ的这个服务呢

因为它不需要使用到这个SITA对吧

但是呢我们前面是不是在

我们这个common当中增加的这个过滤器

那也就意味着

我们所有的

微服务呢

在启动的时候

其实都注册了这个什么呢

都注册了这个过滤器

而我们这个PDJ的又不需要对吧

就它特殊

因为它没有使用到J的

所以说呢

我们还需要干什么呢

把它已经注册好的这个filter呢

再给它取消掉

给它取消掉

其他的都用到

所以不需要取消

那么怎么取消呢

其实非常简单

我们其实就是提供这么一个

用于注册的bin

filter registration bin

对吧

然后呢

把我它已经注册的这个过滤器

给它注进来

注进来之后呢

然后调用set enable的

等于false

是不是就表示这个过滤器不可用

这样的话呢

相当于就有给它取消注册了

所以就这个PDJ的比较特殊

所以说呢

我们在这个地方来操作一下

PDJ的里边

你看

在config里边有一个apacheJ的

然后呢

通过这种

这个pdj的里边

对象这种方式

给它来取消

这个过滤器注册就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“品达物流TMS项目”的分布式事务解决方案（使用 Seata）的教学内容。核心主题是**如何在微服务架构中，通过自定义过滤器（Filter）和拦截器（Interceptor）来传递和管理全局事务的唯一标识符（XID）**。视频演示了两个关键步骤：
1.  **增加过滤器**：在 `pd-common` 模块中创建一个 `TxIdFilter`，用于在 HTTP 请求进入时，从请求头中获取 `TX_XID`，并将其绑定到 `RootContext` 中，以便在后续的调用链中传递。
2.  **取消过滤器注册**：在 `pd-druid` 模块中，通过一个 `ApacheDruid` 配置类，使用 `FilterRegistrationBean` 注册一个 `cancelMyFilterRegistration` 方法，将 `TxIdFilter` 的注册状态设置为禁用（`setEnabled(false)`），从而取消其过滤器功能。这通常是为了在特定服务（如 Druid）中避免不必要的 XID 传递，以防止事务污染或冲突。

整个过程展示了 Spring Boot 中如何通过 `@Component` 和 `FilterRegistrationBean` 来动态管理 Servlet 过滤器，是微服务中实现分布式事务上下文传递的典型实践。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从画面中获取精确的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

*   **00:00 - 00:05**: 课程大纲展示，定位到“第11章 TMS司机端、快递员端开发”下的“3.4 应用”部分。
*   **00:05 - 00:15**: 展示“8. 增加过滤器”章节内容，重点讲解 `TxIdFilter` 的代码实现。
*   **00:15 - 00:25**: 展示“10. 取消过滤器注册”章节内容，重点讲解 `ApacheDruid` 类中 `cancelMyFilterRegistration` 方法的代码实现。
*   **00:25 - 00:30**: 展示“11. 增加注解”章节内容，为后续步骤做铺垫。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **课程大纲**：
    *   项目名称：品达物流TMS项目。
    *   当前章节：第11章 TMS司机端、快递员端开发。
    *   子章节：3.4 应用。
    *   子章节列表：
        1.  建立数据库
        2.  启动Seata Server
        3.  修改registry.conf
        4.  修改file.conf
        5.  重启服务
        6.  引入seata依赖
        7.  增加Seata配置
        8.  增加过滤器
        9.  增加拦截器
        10. 取消过滤器注册
        11. 增加注解
        12. 测试

#### 代码关键内容

*   **`TxIdFilter` 过滤器 (位于 `pd-common` 模块)**

    ```java
    package com.itehima.pinda.common.filter;

    import io.seata.core.context.RootContext;
    import lombok.extern.slf4j.Slf4j;
    import org.apache.commons.lang3.StringUtils;
    import org.springframework.stereotype.Component;
    import javax.servlet.FilterChain;
    import javax.servlet.Filter;
    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;
    import java.io.IOException;

    /**
     * 创建一个Http Rest请求过滤器，用于把当前上下文中获取到的XID放到RootContext
     */
    @Component
    @Slf4j
    public class TxIdFilter extends OncePerRequestFilter {

        @Override
        protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
            String xid = RootContext.getXID();
            String txid = request.getHeader("TX_XID");
            boolean bind = false;
            if (StringUtils.isBlank(xid) && StringUtils.isNotBlank(txid)) {
                RootContext.bind(txid);
                bind = true;
                log.debug("绑定 [" + txid + "] 到 RootContext");
            }
            try {
                filterChain.doFilter(request, response);
            } finally {
                if (bind) {
                    String unbindid = RootContext.unbind();
                    log.debug("解绑 [" + unbindid + "] 从 RootContext");
                    if (!txid.equalsIgnoreCase(unbindid)) {
                        log.warn("变更 [" + txid + "] --> [" + unbindid + "]");
                        if (unbindid == null) {
                            RootContext.bind(unbindid);
                            log.warn("绑定 [" + unbindid + "] 到 RootContext");
                        }
                    }
                }
            }
        }
    }
    ```

*   **`RequestHeaderInterceptor` 拦截器 (位于 `pd-common` 模块)**

    ```java
    package com.itehima.pinda.common.interceptors;

    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.ServletRequestAttributes;
    import org.springframework.web.context.request.RequestAttributes;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web.context.request.RequestContextHolder;
    import org.springframework.web
