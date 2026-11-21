# 画面线理解：10-基于jwt的用户鉴权：配置拦截器并测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\10-基于jwt的用户鉴权：配置拦截器并测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:38, 00:50, 00:54, 02:15, 02:26, 02:35, 02:55, 03:04, 03:09, 03:29, 03:37, 03:51, 03:57, 04:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:14:01

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中配置拦截器、JWT 认证、权限控制，并通过 Postman 发送请求测试接口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中，展示 `JwtInterceptor.java` 代码，用于处理 JWT 认证，从请求头中提取 token 并解析。
画面 2: 在 Windows 资源管理器中，显示项目目录 `ihrm > days5 > 通用代码`，其中包含 `SystemApplication.java` 和 `SystemConfig.java`。
画面 3: 在 IntelliJ IDEA 中，弹出“Copy file”对话框，准备将 `SystemConfig.java` 复制到项目目录 `.../ihrm_system/src/main/java/com/ihrm/system/`。
画面 4: 在 IntelliJ IDEA 中，展示 `SystemConfig.java` 代码，该类继承 `WebMvcConfigurationSupport`，用于添加拦截器并排除登录注册路径。
画面 5: 在 Windows 资源管理器中，显示 `ihrm > days5 > 通用代码` 目录，与画面 2 相同。
画面 6: 在 Visual Studio Code 中，展示 `permission.js` 文件，用于定义权限点和方法，如 `show` 和 `doQuery`。
画面 7: 在 IntelliJ IDEA 中，展示 `SystemApplication.java` 代码，包含主方法、`@Bean` 注解的 `IdWorker` 和 `JwtUtils` 实例。
画面 8: 在 Windows 开始菜单中，鼠标悬停在 Firefox 浏览器图标上，准备打开浏览器。
画面 9: 在 IntelliJ IDEA 中，鼠标悬停在 `SystemApplication.java` 的 `@Bean` 注解上，显示其作用。
画面 10: 在 Postman 中，设置请求为 POST，地址为 `http://localhost:9002/sys/profile`，准备发送请求。
画面 11: 在 SQLyog 中，执行 SQL 查询语句，查询用户和权限表的数据。
画面 12: 在 Postman 中，切换到“Headers”选项卡，准备设置请求头。
画面 13: 在 Postman 中，设置请求头 `Authorization` 的值为 `Bearer`。
画面 14: 在 Postman 中，发送请求后，显示响应结果，包含用户信息和权限点。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Autowired
private JwtUtils jwtUtils;

@Override
public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
    String authorization = request.getHeader("Authorization");
    if (StringUtils.isEmpty(authorization) && authorization.startsWith("Bearer")) {
        //获取token
        String token = authorization.replace(target="Bearer", replacement = "");
        Claims claims = jwtUtils.parseJwt(token);
        if (claims != null) {
            request.setAttribute("user_claims", claims);
            return true;
        }
        throw new CommonException(ResultCode.UNAUTHENTICATED);
    }
}
```

画面 4:
```java
package com.ihrm.system;
import org.springframework.context.annotation.Configuration;
@Configuration
public class SystemConfig extends WebMvcConfigurationSupport {
    @Autowired
    private JwtInterceptor jwtInterceptor;

    @Override
    protected void addInterceptors(InterceptorRegistry registry) {
        //1.添加自定义拦截器
        registry.addInterceptor(jwtInterceptor)
                .addPathPatterns("/**")//2.指定拦截的url地址
                .excludePathPatterns("/sys/login","/frame/register/**");//3.指定不拦截的url地址
    }
}
```

画面 6:
```javascript
import {hasPermissionPoint} from '@/utils/permission'
export default {
    names: 'employeeAdd',
    components: {
        PageTool,
        employeesAdd,
        addRole,
        baseData: constantApi,
        dataList: [],
        counts: '',
        requestParameters: {
            page: 1,
            size: 10
        },
    },
    data() {
        return {
            employeesAdd: 'employeesAdd',
            addRole: 'addRole',
            baseData: constantApi,
            dataList: [],
            counts: '',
            requestParameters: {
                page: 1,
                size: 10
            }
        }
    },
    methods: {
        show(name) {
            return hasPermissionPoint(name)
        },
        doQuery(params) {
            list(this.requestParameters)
                .then(res => {
```

画面 7:
```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication(scanBasePackages = "com.ihrm")
@ComponentScan(value = "com.ihrm.domain.system")
public class SystemApplication {
    public static void main(String[] args) {
        SpringApplication.run(SystemApplication.class, args);
    }

    @Bean
    public IdWorker idWorker() {
        return new IdWorker();
    }

    @Bean
    public JwtUtils jwtUtils() {
        return new JwtUtils();
    }

    @Bean
    public EntityManagerInViewFilter openEntityManagerInViewFilter() {
        return new EntityManagerInViewFilter();
    }
}
```

画面 11:
```sql
SELECT p.*, p.name AS pname, p.code AS pcode, p.type AS ptype, p.role_id AS pr_id, p.permission_id AS ppermission_id, p.permission_code AS ppermission_code, p.permission_description AS ppermission_description, p.permission_visible AS ppermission_visible
FROM sys_permission p
WHERE p.id = pr_id AND p.role_id = role_id AND p.permission_id = permission_id
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
