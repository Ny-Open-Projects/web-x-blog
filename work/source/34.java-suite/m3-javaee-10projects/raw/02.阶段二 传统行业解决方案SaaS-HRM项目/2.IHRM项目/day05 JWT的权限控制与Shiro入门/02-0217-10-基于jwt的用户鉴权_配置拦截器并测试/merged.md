# 10-基于jwt的用户鉴权：配置拦截器并测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\10-基于jwt的用户鉴权：配置拦截器并测试_【海量资源尽在 ubkz.com】.mp4
- 时长 4分45秒（音频 285s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 拦截机的代码呢我们已经写好了但是这个拦截器呢目前来说还不能使用那我们接下来如何测试呢其实我们就是可以在这个系统微服务当中的它的登录和它的叫做profile我们的获取信息的方法当中我们做一个简单的测试就可以了刚才代码我们已经都改过了那接下来呢就是对这个拦截器做一个基本的配置那这个配置配置到哪呢其实很简单我们只需要在系统微服务下边
[00:30] 创建一个拦截器的一个配置文件就可以了或者我们的一个配置类那这个代码呢都是比较简单的一些内容并且它的套路都是一模一样的那在今天第五天的资料当中我这边有一个通用代码其实就是我们写好的这么两个文件注意这两个文件呢sysconfig是我们要用的配置类我可以把它Ctrl C拷到这边注意拷到System下边Ctrl V好那这个里面就是我们以配置文件的形式
[01:00] 去创建一个拦截器并且对它进行一个配置那里面配置的过程呢很简单configuration代表配置类那它呢需要去intense一个我们叫做webmvc configuration suppose好了那继承了之后我们就可以借助里面的重写add interceptor方法往我们的mvc工程当中添加一个我们自己定义好的jwt这个拦截器那如何定义呢首先就是添加add interceptor添加进来那接着add
[01:29] passpason那添加一个它匹配的UIL路径因为我们这个拦截器那可能是对某部分请求的链接或者某部分的API接口都要进行处理那所以批量的去配置它杠星星代表所有那接下来呢还有一个excludepasspason那这个代表的是我可能针对某一些我不需要进行拦截那比如说呢我们的登录就不需要比如说呢我们以后有注册也不需要
[01:55] 那比如说呢还有一些比如说退出那这些其实都不需要我们去做拦截的处理OK那这个配置文件我们说清楚了之后那接下来由于我这个工程用到了Spring Data JPA并且呢我真的用到了它的多对多的相应的一些操作那如果你用到了拦截器之后那通过拦截器它会造成一个问题就是会造成一个叫做No Session延迟加载No Session这么一个问题所以呢我需要去对这个No Session进行一个解决
[02:24] 那在今天资料当中呢也给各位准备了一个System Application那这里面呢我多添加了一句话就是艾塔宾那艾塔宾这个主要目的就是去解决我们的No Session问题呢好了这边我已经copy过来了No Session这个其实就是JPA的一个经典问题啊把它处理掉那好了这样一来呢我们的基本代码就已经全部都构造好了那构造好了之后呢我们去启动当前这个系统为服务启动它
[02:58] 好了这边微服务让它启动我能打开我的Postman咱们来测试一下我修改了这些代码之后它究竟还好不好使好了当然这个测试效果是为了更加直观的体现我就不连前端我在这边直接以Postman看一下能不能够第一个登录第二个能不能够去得到我的用户信息因为用户信息我们现在已经通过拦截器的形式得到ClamS然后通过ClamS是不是就去得到我们的用户ID
[03:27] OK代码呢改了很多那在这边呢咱们还遗留着之前测试的相关内容那这边呢有包袋那我们的发送的13800就这个就是我们数据库里面的第三位用户好了密码123456都没问题那接着走请求好了响应成功没问题数据token拿过来好了接着呢就是我们可以发送一个profile的这么一个请求注意我们要修改一下header那header添加上我们的token JWT数据
[03:56] 比尔开头加空格接着比尔空格扣过来好了send走那各位来看现在同样也能够得到我箱的这些数据的内容OK那这样一来呢我们就通过一个拦截器的形式统一的对这些我们的请求的内容做了一个处理当然了我们这拦截器里面还包括了其他的这么一项操作啊比如说呢这边我不发送
[04:24] 我们的bill不发送我们的请求头那我再去请求的话是不是我们这边就会告诉我没有登录啊来走你会发现他告诉我你还没登录OK那这样一来我们就通过拦截器的形式统一的对代码做了一个优化这是第一方面第二方面我们统一的对需要登录的接口进行了保护OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

