---
title: "Gateway 聚合文档实战：网关集成 Swagger2 与权限管理章总结"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 智牛股]
tags: [Java, 项目实战, 权限管理]
---

# Gateway 聚合文档实战：网关集成 Swagger2 与权限管理章总结

权限管理章的最后一步，是把散在各微服务里的 Swagger 文档收拢到网关：Spring Cloud Gateway 通过路由定义自动发现各服务的文档节点，聚合到一个 doc.html 地址统一访问调试。本篇先走通 Gateway 聚合文档的完整链路——依赖、聚合配置类、转发控制器、集成验证，再对整个权限管理章做收口总结。

## 先给结论

- 网关引入 swagger 组件依赖必须排除 spring-boot-starter-data-rest：它内部依赖 Spring MVC 主线，会激活内置 Tomcat 容器；网关基于 Netty 做转发，Tomcat 一启动就和网关服务冲突。
- 聚合文档不手工维护各服务地址：实现 SwaggerResourcesProvider，注入 RouteLocator，从路由配置拿 service ID，按 host + path 拼 Swagger 资源地址，Set 按完整路径去重多节点。
- 服务带 context-path 时聚合地址会丢前缀：把 context-path 写进路由 URI（lb://stock-admin-user/admin），聚合文档能正常识别，也不影响路由转发。
- 网关要补一个 @RequestMapping("/swagger-resources") 的控制器：Swagger UI 页面背后是对 swagger-resources 的 XHR 请求，@GetMapping("") 映射路径必须为空、请求方式 GET，否则扫不出服务节点。
- 后台管理服务因 context-path 会扫出两个节点，有效的是带 -admin 后缀的最后一个；只想保留一个，取 URI 完整路径比对并剔除 lb 前缀。
- FAQ：Swagger2 2.9.2 版本不再支持 Guava 18.0，启动报错，把 Guava 依赖升级到 20.0。

## 网关聚合的三块拼装：依赖、聚合配置类、路由

网关服务的 pom 里引入 swagger 组件依赖，重点是 exclusions：

```xml
<!-- swagger 组件依赖 -->
<dependency>
    <groupId>com.itcast.trade</groupId>
    <artifactId>bulls-stock-starter-swagger</artifactId>
    <version>${project.stock.version}</version>
    <exclusions>
        <exclusion>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-rest</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

排除 spring-boot-starter-data-rest 的原因要记牢：它内部依赖 Spring MVC 主线，会激活内置 Tomcat 容器，Spring Boot 服务启动时加载 Tomcat；而网关服务基于 Netty 实现转发，Tomcat 启动就和网关服务冲突。

接着添加聚合文档配置类 StockSwaggerProvider，实现 SwaggerResourcesProvider 并注入 RouteLocator：

```java
@Autowired
public StockSwaggerProvider(RouteLocator routeLocator) {
    this.routeLocator = routeLocator;
}

@Override
public List<SwaggerResource> get() {
    List<SwaggerResource> resources = new ArrayList<>();
    List<String> routeHosts = new ArrayList<>();
    // 获取所有可用 service id，拼接 host + path + swagger 资源后缀，去重后封装 SwaggerResource
}
```

配置类里还定义了 Swagger2 默认的 URL 后缀（/v2/api-docs）、网关应用名称，以及需要排除的服务——微服务节点众多，有些服务不暴露 Swagger 接口或不提供对外访问接口，把服务名称加进排除列表即可。聚合逻辑的关键点有三个：

1. 获取所有可用的 service ID，也就是配置文件里定义的服务名称。网关采用负载均衡的处理方式，不可能通过 IP 直接调用，必须拿到 service ID。
2. URL 拼接格式是 host 加服务访问路径，服务访问名称与 service ID 一致，通过服务名称就能在 Nacos 上拿到服务的具体访问信息；网关通过这个地址调用时，由负载均衡寻找对应的 IP 信息。
3. 一个服务开启多个节点时，同一应用会在 Nacos 注册多个实例，网关会全部检测到，不去重就会出现重复接口。用 Set 集合记录已添加到网关的服务信息（service ID 加 /v2/api-docs 完整路径），配合排除指定服务与服务集群的规则，保证网关扫描到的都是可用的、具备 Swagger 接口的服务节点。

为什么从 route 定义自动获取，而不是逐个收集？每个微服务都有自己的文档接口地址，聚合就要逐个添加配置，比较麻烦，而且每次调整都要跟着改；采用 Gateway 的 route 定义信息自动获取，就不用专门维护各微服务各自的接口地址，直接根据 Gateway 里定义的路由信息拿到对应的服务节点信息。但拼接会产生一个新问题：有的微服务设置了 context-path（前置访问路径），有的没有，只扫描到 service ID 时，聚合地址会丢失 context-path。统一维护要借助路由 URI 信息处理，把 host 与 path 拼接起来作为 context-path 的访问路径。

落到配置上，就是给后台管理服务增加路由时，把 context-path 写在 URI 路径后面：

```yaml
server:
  port: 10680
spring:
  application:
    name: stock-gateway
  cloud:
    nacos:
      server-addr: 127.0.0.1:8848
    gateway:
      discovery:
        locator:
          enabled: true
      routes:
        - id: stock-user
          uri: lb://stock-user
          predicates:
            - Path=/user/**
        - id: stock-admin-user
          uri: lb://stock-admin-user/admin
          predicates:
            - Path=/admin/**
```

stock-admin-user 的路由 URI 是 lb://stock-admin-user/admin：通过负载均衡访问服务名称，后缀 /admin 就是它的 context-path。这样聚合文档能正常获取识别，也不影响路由转发——admin 下面的所有路径都会进行路由转发。

## 转发控制器与聚合验证

Gateway 做聚合文档，实际上做的是转发调用。看 Swagger2 文档页面背后的请求就明白了：打开浏览器 F12 面板刷新页面，XHR 请求的是 swagger-resources 访问路径，此外还有安全性访问配置、UI 访问接口等请求。所以网关要补一个 SwaggerController（放在 config 目录下）：

```java
@RestController
@RequestMapping("/swagger-resources")
public class StockSwaggerController {
    @Autowired(required = false)
    private SecurityConfiguration securityConfiguration;
    @Autowired(required = false)
    private UiConfiguration uiConfiguration;
    private final SwaggerResourcesProvider swaggerResources;

    @GetMapping("/configuration/ui")
    public Mono<ResponseEntity<UiConfiguration>> uiConfiguration() {
        return Mono.just(new ResponseEntity<>(
            Optional.ofNullable(uiConfiguration).orElse(UiConfigurationBuilder.builder().build()),
            HttpStatus.OK));
    }

    @GetMapping("")
    public Mono<ResponseEntity> swaggerResources() {
        // 返回聚合的 Swagger 服务节点资源
    }
}
```

两个注意点：swagger-resources 的 @GetMapping 映射路径必须为空，这样网关才能扫描到下面所有的 Swagger 服务节点信息——配置了指定路径反而无法访问，因为默认路径的后缀就是 swagger-resources，后面没有其他信息；请求方式是 GET，通过浏览器访问文档都是 GET 请求。返回值用 Mono，适配网关的响应式调用。

启动网关服务（端口 10680），访问 `http://127.0.0.1:10680/doc.html`。左侧下拉框列出所有服务节点信息：stock-user 用户服务、stock-admin-user 后台管理服务。后台管理服务出现了两个条目，因为它配置了 /admin 后缀访问路径——网关配置时是对所有路由信息做扫描，扫描范围就是配置文件里定义的内容；去重规则按完整 URI 路径执行，只要名称不重复，节点信息都会呈现，真正有效的是最后一个 stock-admin-user-admin。想只展示一个节点，就在配置里拿 URI 完整路径做比对判断，剔除前面的 lb 前缀再处理；出现重复聚合地址时，按需要选择对应的服务节点访问即可。

功能验证：选后台管理服务的菜单管理接口调试，roleId 传 10172，返回 401——后台管理服务的 OAuth2 认证还没有拿掉。在全局参数里配置 Authorization（大写），值为 Bearer 加空格加申请好的 token，保存后再访问，接口正常返回数据。Spring Cloud Gateway 对 Swagger2 的集成配置完成，聚合文档的呈现与使用就此跑通。

## 章总结：权限管理的收口与 FAQ

回顾本章三个学习目标：实现自定义 OAuth2 启动器的封装和配置；实现 OAuth2 与 Swagger2 的集成使用；实现聚合文档，Swagger2 跟 Spring Cloud Gateway 的集成使用。整章内容收成一张表：

| 模块 | 关键实现 | 要点 |
| --- | --- | --- |
| 实现说明 | 两个用户数据源 | APP 用户的 OAuth2 密码模式只能指定一个数据源；两套认证服务属于重复配置不做演示，但登录和菜单权限的鉴权保障不放弃，后续章节用 Spring Session 实现 |
| OAuth2 启动器 | stock-starter-oauth2 | 公用配置统一处理；个性化部分读取项目配置独立处理，免认证接口用 ignore-urls 属性指定 |
| 启动器与后台服务集成 | pom 依赖 + security.oauth2 配置 | 掌握实际项目中的使用方式，token 访问验证通过 |
| Swagger2 鉴权 | 三种方案 | 集成 OAuth2、自定义全局参数、全局预置参数；按业务需要灵活选择，本章采用最简单易用的第三种 |
| Gateway 聚合 | RouteLocator 扫描 + Controller 映射 | 基于路由转发信息自动扫描 Swagger 文档节点，无需在配置文件里做特殊定义；Swagger 的 Controller 接口必须增加，否则无法访问和加载服务节点信息 |

验证环节的两个细节值得单独强调：后台管理服务加了后缀路径，聚合下拉里真正有效的节点是最后一个；Swagger 文档接口地址背后是多个路径请求的组合（F12 刷新可见多个 XHR 请求），Controller 层的接口映射缺失会直接导致文档加载不出来。整章对聚合服务文档的有效性做了完整测试，各服务接口都能正常调用。

FAQ 两条：Swagger2 2.9.2 版本不再支持 Guava 18.0，启动会报错，把 Guava 依赖升级到 20.0 即可；需要扩展 Spring Data REST 相关知识点，可以参考课程附的链接地址自行研究。

## 小结

- 聚合文档的核心是自动发现：依赖 RouteLocator 从路由配置反推服务节点，service ID 拼 /v2/api-docs 得到资源地址，Set 按完整路径去重，多节点、context-path、排除服务三类边界都收在聚合配置类里处理。
- 网关侧两个必做项：exclusions 排除 data-rest 防 Tomcat 与 Netty 冲突；补 /swagger-resources 控制器（空映射、GET、Mono 返回）承接文档页面的底层请求。
- 验证链路完整走一遍才有说服力：10680/doc.html 看节点下拉、识别 context-path 造成的重复节点、401 时配全局 Authorization 参数（Bearer 加 token）调通菜单接口。
- 整章方法论落点：starter 封装让公用配置复用、个性配置（ignore-urls）下放各服务；鉴权方案按需选择不追求统一；聚合靠路由约定而非手工维护地址，Gateway 根据路由转发信息自动扫描文档节点，便于维护和使用。
