---
title: "Swagger2 集成收官：swagger-bootstrap-ui 界面与 Gateway 聚合前的 OAuth2 启动器"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 智牛股]
tags: [Java, 项目实战, 权限管理]
---

# Swagger2 集成收官：swagger-bootstrap-ui 界面与 Gateway 聚合前的 OAuth2 启动器

上一篇把 Swagger2 封装成了自定义启动器，这一篇做两件事。其一把启动器真正接到后台管理服务上：让 Spring Data REST 的 HATEOAS 接口也进文档、换上 swagger-bootstrap-ui 界面、完成在线调试，Swagger2 集成至此收官。其二进入新的一章「OAuth2、Swagger 与 Gateway 整合」，先封装 OAuth2 自定义启动器并打通鉴权验证，为下一篇的 Gateway 聚合文档铺路。

## 先给结论

- 后台管理服务集成 Swagger2 只有三步：pom 引入自定义启动器依赖、bootstrap-dev.yml 配 swagger 属性、接口与参数对象加 @ApiOperation/@ApiImplicitParam/@ApiModel/@ApiModelProperty 注解。
- Swagger2 原生不支持扫描 Spring Data REST 接口；springfox-data-rest 2.9.2 内部编译依赖的 spring-data-rest-webmvc 是 2.6.13，与工程的 3.1.9 冲突，不想降级 WebMVC 就只能改源码适配。
- 源码只动两处：EntityContext 增加 getRemark() 读实体 @Api 注解的 value，SpringDataRestRequestHandler 的 groupName() 改为返回 getRemark()；同时启动类必须 @Import(SpringDataRestConfiguration.class)。
- swagger-bootstrap-ui 一个依赖完成换装，访问地址从 swagger-ui.html 变为 doc.html，左侧菜单右侧详情，还能直接在线调试接口。
- 后台运营人员与前端 APP 用户是两个用户数据源，OAuth2 密码模式只能指定一个数据源；演示阶段不搭两套认证服务，而是封装 OAuth2 自定义启动器，公用配置统一、免认证接口靠 ignore-urls 下放各服务。
- Swagger 在线调试受保护接口报 401，三种方案里选最简单的全局预置参数：securitySchemes 配 ApiKey("Authorization", "Authorization", "header")，token 值记得带 Bearer 前缀加空格。

## 后台管理服务集成 Swagger2：从依赖到界面验证

集成基于上一篇封好的启动器，pom 里加入依赖：

```xml
<!-- swagger 自定义启动器的依赖 -->
<dependency>
    <groupId>com.itcast.trade</groupId>
    <artifactId>stock-starter-swagger</artifactId>
    <version>${project.stock.version}</version>
</dependency>
```

Ctrl 点进去能找到依赖，说明配置加载成功。配置文件改 bootstrap-dev.yml 的开发环境（dev）：

```yaml
# Swagger界面内容配置
swagger:
  enabled: true
  title: 交易平台API接口文档
  description: 交易平台API接口文档
  version: 1.0.2
```

属性项与启动器里 SwaggerProperties 的定义一一对应：enabled 是 Swagger 文档的总开关，title、description、version 属于界面内容展示的描述信息。

接着给对外接口加注解，以保存角色权限接口为例。方法加 @ApiOperation，参数用 @ApiImplicitParam 描述，value 是参数说明，required 表示必填项：

```java
@PostMapping(value = "/savePrivileges")
@ApiOperation(value = "保存角色权限")
public ApiRespResult savePrivileges(
        @ApiImplicitParam(value = "权限信息", name = "roleAuth", required = true) @RequestParam("roleAuth") String roleAuth,
        @ApiImplicitParam(value = "角色ID", name = "roleId", required = true) @RequestParam("roleId") String roleId) {
```

参数是对象时走另一套注解。用户分配角色接口的入参 AuthorityUserRole 加 @ApiModel 做整体描述，属性加 @ApiModelProperty 做逐项描述：

```java
@ApiModel("AuthorityUserRole(用户与角色关联表)")
public class AuthorityUserRole extends BaseEntity {
    @ApiModelProperty(value = "用户ID", example = "1")
    private Long userId;
    @ApiModelProperty(value = "角色ID", example = "10171")
    private Long roleId;
    @ApiModelProperty(value = "机构ID", example = "10065")
    private Long institutionId;
    @ApiModelProperty(value = "机构名称", example = "御金汇公司")
    private String institutionName;
}
```

example 是在线测试时的默认值：不填的话调试参数默认为空，填了界面上会预填，比如 institutionId 预填 10065，保证接口能直接测起来。不想暴露的属性用 hidden = true 屏蔽——创建人这类字段既不会作为参数传过来，也不会作为返回信息暴露给客户端，直接藏掉。还有一个坑：Long 是包装类型，传具体值没问题，但前端传空值时无法转换处理；数值类型的属性建议都给 example 默认值，否则在线接口测试会报错。

启动后台管理服务验证，访问地址是服务地址加 swagger-ui.html 后缀（服务 context-path 为 admin）：`http://127.0.0.1:10691/admin/swagger-ui.html`。页面上 AuthorityLogicController 定义的两个接口——用户分配角色、保存角色权限——全部显示，参数描述与代码定义一致，必填项有标记；点开用户分配角色，AuthorityUserRole 的属性和默认值全部呈现，点击 try it out 能看到 institutionId 预填 10065。返回对象 ApiRespResult（code、message）没加 Swagger 注解，model 区没有中文描述，可以按同样方法补齐。但 Spring Data REST 暴露的接口一个都没出现：Swagger2 原生不支持对它的扫描，这是下一节要解决的问题。

## 让 Spring Data REST 接口进文档：版本冲突与源码改造

第一步，在 stock-starter-swagger 工程的 pom 里增加 Data REST 组件依赖；后台用户管理服务的启动类通过 @Import 导入 Spring Data REST 配置类，启动时扫描读取里面的配置。直接启动报错：调用的方法不存在，典型的依赖冲突。用 Maven Helper 插件分析 admin-user 工程的依赖树定位原因：springfox-data-rest 组件 2.9.2（讲义编写时的最新版本）内部依赖的 spring-data-rest-webmvc 编译版本是 2.6.13，而工程实际引用的是 3.1.9，版本不一致导致方法调用出错。降低工程的 WebMVC 版本不可取——很多服务依赖 Spring Boot WebMVC 做实现，降级等于对整个服务的公用核心依赖降级。所以只能改 springfox-data-rest 的源码，让它适配 webmvc 3.1.9。讲师已提前改好并拷贝到 stock-starter-swagger 工程。实际项目建议把修改后的源码重新打包成 jar 替换原包；教学演示直接放源码，同包结构下 Java 源码路径的扫描优先级最高，会先于 jar 里的 class 生效。

第二处改造解决可读性问题：HATEOAS 接口在 Swagger 上支持并不友好，CRUD 显示、返回结果描述都有欠缺，文档接口名称还用实体类名显示（如 AuthorityMenu），全英文、不直观。改两个类：

```java
// EntityContext 新增 getRemark()：读取实体上 @Api 注解的 value，为空则退回实体名
public String getRemark() {
    Api api = resource.getDomainType().getAnnotation(Api.class);
    if (api == null) {
        return getName();
    }
    return api.value();
}

// SpringDataRestRequestHandler.groupName()：原来返回 "%s Entity" 格式的实体名
@Override
public String groupName() {
    // return String.format("%s Entity", entityContext.getName());
    return String.format("%s", entityContext.getRemark());
}
```

groupName 的返回值最终就是文档里显示的接口分组名，原来取实体的 simpleName，现在改为取 getRemark()。@Api 注解加在数据层接口映射的实体上：

```java
@Api(value = "HATEOAS接口-菜单管理(AuthorityMenu)")
@Entity
@Table(name = "t_authority_menu")
public class AuthorityMenu extends BaseEntity {
```

Repository 方法上则照常加 @ApiOperation、@ApiImplicitParam 等描述。

重启验证时有个插曲：改完代码接口没出来。原因是 stock-admin-user 的启动类还没加 @Import(SpringDataRestConfiguration.class)——不加这个导入，Spring Data REST 定义的配置无法被扫描加载，自然识别不出它的接口。补上再重启，HATEOAS 相关接口全部呈现，分组名显示为注解定义的中文描述，相比全英文实体名清晰直观得多。另外注意，Spring Data REST 默认生成的增删改查接口（针对 AuthorityMenu 的 CRUD）没法完全展示出来——Swagger 对 Spring Data REST 的原生支持不友好所致，这并不影响使用，这些 CRUD 遵循 HATEOAS 规范操作即可。

## swagger-bootstrap-ui 换装与集成要点

第三方 UI 的集成成本几乎为零：stock-starter-swagger 的 pom 里、原生 swagger-ui 组件依赖旁边加一个 swagger-bootstrap-ui 依赖，重启服务即可。访问地址随之变化：不再是 swagger-ui.html，改为 doc.html——`http://127.0.0.1:10691/admin/doc.html`。新界面左侧是功能菜单（之前定义的接口列表），右侧是接口详情，包含参数信息、响应参数、响应示例和调试面板，比原生 UI 直观，也便于整个文档的维护和操作使用。

Swagger2 不只生成文档，还能直接调用调试。拿保存角色权限接口验证：点击调试，填 roleAuth（逗号分割的菜单与操作权限信息）、roleId = 10172（系统里创建好的默认角色），发送后返回成功报文，后台调用与 SQL 语句正常执行。在线文档调试就此跑通。

结合本章总结，集成要点收三句：自定义 starter 封装 Swagger2 启动器的价值在于便于复用、统一配置；Swagger 与 Spring Data REST 集成时，默认 HATEOAS rest 风格接口不会显示在文档中，不影响使用，遵循 HATEOAS 规范操作即可，文档只会显示自定义的逻辑接口，工程里额外添加的接口也能正常扫描识别显示；swagger-bootstrap-ui 相比默认 UI 更直观便于查看，实际工程项目建议用第三方 UI 替换原生界面。

## 聚合文档前置：OAuth2 自定义启动器与 Swagger2 鉴权

进入第四章「OAuth2、Swagger 与 Gateway 整合」，学习目标三点：实现自定义 OAuth2 启动器的封装与集成配置；实现 OAuth2 与 Swagger2 的集成使用；实现聚合文档——Swagger2 与 Spring Cloud Gateway 的集成使用。聚合文档指把所有微服务节点定义的 Swagger 接口聚合在一起，外部请求只访问 Gateway 一个地址，就能看到所有微服务节点下的接口信息。实现步骤五步：自定义 OAuth2 启动器、启动器与后台管理服务集成使用、实现 Swagger2 鉴权访问、Swagger2 与 Gateway 网关服务集成配置、集成功能验证。

先说清一个前提。后台管理服务给运营人员使用，前端 APP 客户量级大，两个层面的用户数据对应不同的表实体，属于两个用户数据源。之前实现的基于 APP 用户的 OAuth2 密码模式，其认证配置只能指定一个用户数据源；后台也要走密码模式的话，就得提供两套指向不同数据源的认证服务——实现一套之后两套三套都不是问题，但作为演示属于纯重复配置，没有太多技术学习意义，所以不同时采用。本章仍拿后台管理服务为例讲解；后面章节后台服务不接入 OAuth2 认证，改用 Spring Session 统一会话认证机制做鉴权——不采用 OAuth2 不代表放弃鉴权处理，至少要保障登录和菜单权限的鉴权流程正常运转。

封装 OAuth2 启动器还是 starter 套路：stock-starter 下新建模块 stock-starter-oauth2，包 com.itcast.trade.stock.starter.oauth2，依赖 spring-cloud-starter-oauth2 与 spring-cloud-starter-security，核心自动配置类：

```java
@Configuration
@EnableAutoConfiguration
@EnableResourceServer
@EnableGlobalMethodSecurity(prePostEnabled = true)
@ConditionalOnProperty(name = "security.oauth2.resource.token-info-uri")
public class AutoOAuth2Configuration implements ResourceServerConfigurer {

    @Autowired
    private RemoteTokenServices remoteTokenServices;

    @Autowired
    private RestTemplate lbRestTemplate;

    @Setter
    private List<String> ignoreUrls;

    @Override
    public void configure(HttpSecurity httpSecurity) throws Exception {
        ExpressionUrlAuthorizationConfigurer<HttpSecurity> registry = httpSecurity.csrf().disable()
                .authorizeRequests();

        // 设置无须认证的url路径（各服务个性化配置）
        if (null != ignoreUrls && ignoreUrls.size() > 0) {
            registry.antMatchers(ignoreUrls.toArray(new String[ignoreUrls.size()])).permitAll();
        }

        registry
            .antMatchers("/actuator/**", "/v2/**", "/doc.html", "/swagger-ui.html", "/css/**")
            .permitAll()
            .anyRequest().authenticated()
            .formLogin().loginPage("/login")
            .failureUrl("/login/error")
            .defaultSuccessUrl("/home");
    }
}
```

注解逐一说明：@EnableResourceServer 开启认证（资源）服务；@EnableGlobalMethodSecurity(prePostEnabled = true) 开启方法级别的安全扫描；@ConditionalOnProperty 按 security.oauth2.resource.token-info-uri 条件生效，配置了该属性下面的代码才会扫描生效；@ConfigurationProperties(prefix = "security.oauth2.client") 做属性自动注入——配置文件里前缀之下的 ignore-urls 会按名称匹配注入 ignoreUrls。封装思路是共性统一、个性预留：/actuator、/v2、doc.html、swagger-ui.html、/css 这些 Swagger 与静态资源路径全局放行，不做认证处理；统一登录页 /login、登录失败跳转 /login/error、成功跳转 /home 也是公用配置，各应用服务不用重复配置；各服务特有的免认证接口通过 ignore-urls 属性自行追加，保障每个服务的扩展性。lbRestTemplate 是支持负载均衡的 RestTemplate，以 HTTP 方式远程调用，注入到上面的配置里配合 RemoteTokenServices 远程校验 token。最后照例在 META-INF 下创建 spring.factories，注册配置类全路径（用 copy reference 拷贝，确保路径正确）。

后台管理服务接入两步：pom 引入启动器依赖，bootstrap-dev.yml 加认证配置：

```yaml
# spring security 配置
security:
  oauth2:
    resource:
      loadBalanced: true
      token-info-uri: http://trade-auth/oauth/check_token
    client:
      client-id: app
      client-secret: app
      scope: server
      access-token-uri: http://trade-auth/oauth/token
      user-authorization-uri: http://trade-auth/oauth/authorize

# 不需要认证扫描的接口路径
ignore-urls:
  - /webjars/**
  - /login/**
  - /swagger-resources/**
  - /csrf/**
```

OAuth2 认证地址与 client id 相关信息要保证正确；ignore-urls 本讲配置的是 Swagger 接口文档相关路径的放行，特殊免认证接口往下追加即可。

验证：同时启动认证服务（trade-auth）与后台管理服务，浏览器直接访问「根据机构预置类型获取所有菜单」接口，提示未认证、不能访问对应资源，说明接口已被 OAuth2 保护；用 Postman 向 9199 端口申请 token，把 token 以 access_token 参数追加到接口地址后再访问，认证保护提示消失，正常拿到接口数据——自定义启动器与后台管理服务的集成配置验证通过。

最后是 Swagger2 鉴权访问。资源受保护时，Swagger 在线调试会报错；不带 token 直接调用会出现 401 认证错误。三种方案：一是 Swagger2 集成 OAuth2 直接申请 token 访问，配置较复杂；二是自定义全局参数，每个接口自动在 header 上附带 Authorization 参数，但要逐个接口手动输入；三是全局预置参数，只填写一次 token，所有接口都能调用。取简单易用的第三种。修改 AutoSwaggerConfiguration 的 securitySchemes 方法：

```java
/**
 * 全局预置参数，不必每个方法都设置
 */
private List<ApiKey> securitySchemes() {
    return Arrays.asList(new ApiKey("Authorization", "Authorization", "header"));
}
```

ApiKey 的三个参数是名称、key、传递方式；后续要追加参数往 List 里加即可。重启后在接口文档的 Authorize 菜单能看到这个全局预制参数，key 与 name 和后台代码配置一致，传递方式是 header。把申请的 token 填进去保存，一次配置所有接口都附带生效。验证时先踩一个坑：填了 token 依然 401——token 是 Bearer token，值前面必须加 Bearer 加空格前缀。修正后再调「根据角色ID获取对应菜单信息」接口（传 10171），不带任何额外认证参数就能正常返回菜单数据。Swagger2 的鉴权访问与鉴权配置就此完成。

## 小结

- 集成三步走、注解四件套：pom 依赖、swagger 属性配置、@ApiOperation/@ApiImplicitParam/@ApiModel/@ApiModelProperty；example 既是示例又是在线测试默认值，Long 属性必须给默认值防止空值转换报错，不想暴露的属性用 hidden 屏蔽。
- Swagger2 支持 Spring Data REST 靠源码改造：先排掉 webmvc 2.6.13 与 3.1.9 的版本冲突，再改 EntityContext.getRemark() 与 groupName() 两处让接口分组支持 @Api 中文描述；启动类必须 @Import(SpringDataRestConfiguration.class) 才能扫描到 Data REST 配置。
- swagger-bootstrap-ui 一个依赖换装，地址从 swagger-ui.html 换成 doc.html，界面与在线调试体验优于原生 UI；实际项目建议替换原生界面。
- OAuth2 启动器封装遵循「共性统一、个性预留」：公共放行路径与登录跳转统一实现，各服务用 ignore-urls 追加免认证接口，最后 spring.factories 注册自动装配。
- Swagger 鉴权选全局预置参数方案：ApiKey("Authorization", "Authorization", "header")，token 值带 Bearer 前缀加空格，一次配置全接口生效。
