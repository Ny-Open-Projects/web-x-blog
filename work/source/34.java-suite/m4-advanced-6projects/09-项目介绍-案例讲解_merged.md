# 09-项目介绍-案例讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

为了让大家对这个工程更加熟悉,开发起来更加顺利,那我们挑一个案例详细讲解一下它的一个完整的数据走向流程。

好,那我这里就挑了一个品牌的一个查询的案例。

我们每次请求,第一步其实会将请求转发给我们的Nginx,Nginx拦截到之后会路由到我们后端微服网关,会经过Gateway。

不过我们这个案例这里就不讲Nginx了,直接讲Gateway这一块。

Gateway会根据你请求的路径去路由到后端的微服务,SQL Service里面指定的服务。

那这一块我对这个流程做了一个详细的图解。

请求这个地址先经过SQL Gateway,再经过SQL Service,下面的SQL Guest Service里面的brandcontrol.fundow方法。

这里有这个完整的图解,请求API brand。

那这个时候以Gate方式去提交,会经过SQL Gateway。

SQL Gateway。

会找到SQL Service里的SQL Guest里面的brandcontrol里面的fundow方法。

fundow查询需要转成brand对象。

brand对象是我们SQL API里面,SQL Guest API里面的brand对象。

这个图解是非常清楚的。

我们把这个案例给来讲解一下。

案例我们看一下。

请求第一步先经过Gateway微服网关。

在这一块请求是API brand。

它会被SQL Guest进行拦截处理,会路由到这里来。

好,路由之前呢,这里有一个过滤规则,会把我们请求的路径第一层路径给削掉,剔掉。

也就是你请求API brand的时候,

它真实过滤路由之后的一个地址。

所以是brand会把第一层给剔掉。

所以最终请求的其实是斜杠brand。

那么斜杠brand会路由到SQL Guest里面去。

那我们看一看SQL Guest。

在这一块,SQL Guest,这个,那SQL Guest会路由给这个微服务。

这个微服务呢,会找到brand对应的控制器。

那么brand对应的控制器,

那么brand对应的控制器,

那么brand对应的控制器,

就在这里。

而我们是以get提交,当前这里正好是以get去映射处理的一个方法,正好是fundwork。

那么这个时候就会调这个方法,调这个方法呢,会去调我们的fundwork,走到service来了。

service呢,你看它又会找谁,会找我们的service实现内,然后会找我们的brand map,这其实就是我们的图表。

那么这个就是这个通用map里面的了。

它继承了这个通用map,那所有的方法都在通用map里面有所实现。

好,这个我们就不再去讲解这一块了。

那我们把这个案例呢,来测试一次。

首先我们在浏览器上写一下这个测试。

log host,这个呢,换成微服网关的地址,8001 API BRAND。

回车一下。

报401,为什么会报401呢?

我们来介绍一下

用户请求过来,先经过Gateway这一块

简单看一下

到这一块来

目前是Gateway进行拦截

这里呢,其实有一个全局过滤器

这个过滤器我们看一下

所有的请求都会经过这个过滤器

它会对API User Login, API Admin Login

还有API Search进行一个放行

那不放行的它会做什么事情呢?

而我们刚才这个地址正好是没有放行的地址

因此它会走后面这个过程

后面这个过程呢

它会先去获取请求头里面的Authorization

这个会获取Authorization请求头

这其实就是我们的令牌数据

获取了之后,它会做一个判断

当这个令牌不为空的时候

那上面是为空,不为空的时候

才会放行

为空的话会继续去获取

获取Cookie里面有没有

如果Cookie里面没有

那这个时候就结束了整个程序

报401了

所以刚才报401是这一块的问题

那我们现在就来看看

我们这一块要想请求到这个地址

要么把刚才全区过滤器注释掉

要么添加一个令牌数据

好,我这里为了方便测试

我就直接用已经生成好的令牌就可以了

请求地址是这个地址

执行一次

可以了

好,因此我们这个整个案例就可以了

像这个是我当前这一块Ideal的编码问题

我没有去管它

在我们别的地方是不会有这个问题的

OK

这个是整个API Brand案例的一个数据完整走向的流程

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是“秒杀系统”系列课程中关于“秒杀商品维护”模块的讲解，重点在于演示如何通过 Spring Cloud Gateway 实现微服务的统一访问控制和权限校验。讲师首先回顾了项目的整体架构，然后深入到 `seckill-gateway` 服务，详细讲解了 `AuthorizeFilter` 全局过滤器的实现逻辑。该过滤器负责从请求头、URL 参数或 Cookie 中获取用户令牌（Authorization），并根据令牌的有效性决定是否放行请求。如果令牌无效或缺失，过滤器会返回 401 状态码拒绝访问。整个过程结合了代码演示、架构图和实际的 REST Client 调用，旨在帮助学员理解微服务网关在权限控制中的核心作用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:10**：课程开场，讲师介绍本节内容为“秒杀商品维护”模块，并展示项目整体架构图。
*   **00:10 - 00:25**：讲师切换至 `seckill-gateway` 服务的代码，讲解其 `bootstrap.yml` 配置文件，展示路由规则（如 `/api/brand` 路由到 `seckill-goods` 服务）。
*   **00:25 - 00:45**：讲师展示 `BrandController.java` 中的 `findALL()` 方法，说明其调用 `BrandService` 的 `findALL()` 方法来获取品牌列表。
*   **00:45 - 01:05**：讲师进入 `BrandService.java`，并展示 `BrandServiceImpl.java` 中的 `findALL()` 方法实现，强调其调用 `BrandMapper`。
*   **01:05 - 01:20**：讲师展示 `BrandMapper.java`，并讲解 `@Mapper` 注解的使用，以及 `Mapper<T>` 接口的继承关系。
*   **01:20 - 01:40**：讲师切换到 `AuthorizeFilter.java`，开始讲解全局过滤器的实现。
*   **01:40 - 02:00**：讲师展示 `AuthorizeFilter` 中的 `filter` 方法，讲解如何从请求头、URL 参数和 Cookie 中获取令牌。
*   **02:00 - 02:20**：讲师详细讲解 `if (StringUtils.isEmpty(token))` 条件下的逻辑，即从 Cookie 中获取令牌。
*   **02:20 - 02:40**：讲师讲解 `if (cookie==null && adminCookie==null)` 条件下的逻辑，即如果令牌无效则返回 401 状态码。
*   **02:40 - 03:00**：讲师讲解 `if (cookie!=null)` 条件下的逻辑，即从 Cookie 中获取令牌并设置到请求头中。
*   **03:00 - 03:20**：讲师展示 `REST Client` 工具，演示如何向 `/api/brand` 发起 GET 请求。
*   **03:20 - 03:40**：讲师总结 `AuthorizeFilter` 的工作流程，并强调其在微服务架构中的重要性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 图表**：
    *   **项目架构图**：展示了 `Nacos` 注册中心、`Gateway` 网关、`seckill-goods-service`、`seckill-order-service`、`seckill-user-service` 等服务之间的调用关系。
    *   **代码结构图**：展示了 `seckill-gateway` 服务的目录结构，包括 `src/main/java/com/seckill` 和 `src/main/resources`。
    *   **REST Client 请求截图**：展示了向 `http://localhost:8001/api/brand` 发起 GET 请求的界面。

*   **代码**：
    *   **`seckill-gateway/bootstrap.yml`**：
        ```yaml
        spring:
          cloud:
            gateway:
              routes:
                - id: goods_route
                  uri: lb://seckill-goods
                  predicates:
                    - Path=/api/skuAct/**, /api/activity/**, /api/brand/**, /api/category/**, /api/seckill
                  filters:
                    - StripPrefix=1
                - id: order_route
                  uri: lb://seckill-order
                  predicates:
                    - Path=/api/order/**
                  filters:
                    - StripPrefix=1
        ```
    *   **`BrandController.java`**：
        ```java
        @RestController
        @RequestMapping("/api/brand")
        public class BrandController {
            @Autowired
            private BrandService brandService;
            ...
            @GetMapping
            public Result<List<Brand>> findAll() {
                List<Brand> list = brandService.findAll();
                return new Result<List<Brand>>(flag: true, StatusCode.OK, message: "查询成功", list);
            }
        }
        ```
    *   **`BrandService.java`**：
        ```java
        public interface BrandService {
            List<Brand> findAll();
        }
        ```
    *   **`BrandServiceImpl.java`**：
        ```java
        @Service
        public class BrandServiceImpl implements BrandService {
            @Autowired
            private BrandMapper brandMapper;
            ...
            @Override
            public List<Brand> findAll() {
                return brandMapper.findAll();
            }
        }
        ```
    *   **`BrandMapper.java`**：
        ```java
        @Mapper
        public interface BrandMapper extends BaseMapper<Brand> {
            // 其他方法
        }
        ```
    *   **`AuthorizeFilter.java`**：
        ```java
        @Component
        public class AuthorizeFilter implements GlobalFilter, Ordered {
            private static final String AUTHORIZATION_TOKEN = "Authorization";
            private static final String ADMIN_AUTHORIZATION_TOKEN = "Admin-Token-itheima";
            ...
            @Override
            public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
                // 从请求头、URL 参数、Cookie 中获取令牌
                String token = request.getHeaders().getFirst(AUTHORIZATION_TOKEN);
                if (StringUtils.isEmpty(token)) {
                    token = request.getQueryParams().getFirst(AUTHORIZATION_TOKEN);
                }
                if (StringUtils.isEmpty(token)) {
                    HttpCookie cookie = request.getCookies().getFirst(AUTHORIZATION_TOKEN);
                    HttpCookie adminCookie = request.getCookies().getFirst(ADMIN_AUTHORIZATION_TOKEN);
                    if (cookie==null && adminCookie==null) {
                        response.setStatusCode(HttpStatus.UNAUTHORIZED);
                        return response.setComplete();
                    }
                    if (cookie!=null) {
                        token = cookie.getValue();
                    } else {
                        token = adminCookie.getValue();
                    }
                    request.mutate().header(AUTHORIZATION_TOKEN, "bearer " + token);
                }
                return chain.filter(exchange);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目架构展示**（00:00-00:10）
    *   讲师在 IDE 中打开项目结构，展示 `seckill-gateway`、`seckill-goods`、`seckill-order` 等服务。
    *   讲师切换到 `seckill-gateway` 服务的 `bootstrap.yml` 文件，展示其路由配置。

*   **场景二：控制器方法演示**（00:25-00:45）
    *   讲师在 `BrandController.java` 中高亮 `@GetMapping` 注解和 `findAll()` 方法。
    *   讲师在 `BrandService.java` 中高亮 `findAll()` 方法，并在 `BrandServiceImpl.java` 中高亮 `@Override` 注解和 `findAll()` 方法实现。

*   **场景三：全局过滤器实现**（01:20-03:20）
    *   讲师在 `AuthorizeFilter.java` 中高亮 `@Component` 注解和 `filter` 方法。
    *   讲师在 `filter` 方法中高亮 `if (StringUtils.isEmpty(token))` 条件，并演示如何从 Cookie 中获取令牌。
    *   讲师在 `filter` 方法中高亮 `if (cookie==null && adminCookie==null)` 条件，并演示如何返回 401 状态码。
    *   讲师在 `filter` 方法中高亮 `request.mutate().header(AUTHORIZATION_TOKEN, "bearer " + token);` 语句，并演示如何将令牌设置到请求头中。
    *   讲师在 `REST Client` 中高亮 `GET` 方法和 `http://localhost:8001/api/brand` 路径，并演示如何发起请求。

*   **场景四：权限校验逻辑总结**（03:20-03:40）
    *   讲师总结 `AuthorizeFilter` 的工作流程：从请求头、URL 参数、Cookie 中获取令牌，如果令牌无效或缺失，则返回 401 状态码，否则将令牌设置到请求头中并放行请求。
