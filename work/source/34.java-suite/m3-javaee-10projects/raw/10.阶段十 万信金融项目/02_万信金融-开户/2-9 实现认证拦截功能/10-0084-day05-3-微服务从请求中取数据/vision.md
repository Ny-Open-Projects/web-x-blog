# 画面线理解：day05-3-微服务从请求中取数据

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-9 实现认证拦截功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-9 实现认证拦截功能\day05-3-微服务从请求中取数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 00:45, 00:55, 05:41, 06:50, 07:14, 09:17, 09:53, 10:19, 10:36, 10:52, 11:05, 11:18, 11:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:58:24

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Cloud 微服务架构中，通过自定义拦截器（TokenInterceptor）和网关过滤器（AuthFilter）实现 JWT 认证与用户信息传递。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 IDE 中 AuthFilter.java 文件，代码中将 JSON Token 添加到请求参数中，用于后续服务调用。
画面 2: 同画面 1，无新增要点。
画面 3: 展示 PPT 中的系统架构图，包含接入方、网关、认证服务（UAAS）、微服务等模块及其交互关系。
画面 4: 显示项目文件夹，包含 AuthFilter.java、JWT令牌.png、LoginUser.java 等文件。
画面 5: IDE 中 AuthFilter.java 文件，高亮显示将 JSON Token 添加到请求参数的代码行。
画面 6: 播放器中展示 TokenInterceptor.java 代码，用于解析并设置用户登录信息。
画面 7: 播放器中展示 WebConfig.java 配置类，用于注册 TokenInterceptor 拦截器。
画面 8: 播放器中展示 TokenInterceptor.java 代码，光标位于设置属性的语句上。
画面 9: 播放器中展示 TokenInterceptor.java 代码，光标位于设置属性的语句上。
画面 10: 文件资源管理器中，选中 TokenInterceptor.java 文件。
画面 11: IDE 中 AuthFilter.java 文件，光标位于将 JSON Token 添加到请求参数的代码行。
画面 12: IDE 中 AuthFilter.java 文件，光标位于将 JSON Token 添加到请求参数的代码行。
画面 13: IDE 中 WebConfig.java 文件，显示配置类用于注册拦截器。
画面 14: 播放器中展示 TokenInterceptor.java 代码，光标位于设置属性的语句上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@AuthAuthentication authAuthentication(AuthAuthentication authentication;
Map<String, String> jsonToken = new HashMap<>();
(authAuthentication.getAuthRequest().getRequestParameters());
//3.将jsonToken加入转发服务的request，这样被服务就能通过
requestContext ctx = RequestContext.getCurrentContext();
HttpServletRequest request = ctx.getRequest();
request.getParameterMap(); // 关键步骤，一定要看一下，下面这行代码将能取到值
Map<String, List<String>> requestQueryParams = ctx.getRequestQueryParams();
if (requestQueryParams == null) {
    requestQueryParams = new HashMap<>();
}
List<String> arrayList = new ArrayList<>();
arrayList.add(EncryptUtil.encodeUTF8StringBase64(JSON.toJSONString(jsonToken)));
requestContext.put("jsonToken", arrayList);
ctx.setRequestQueryParams(requestQueryParams);
return null
```

画面 5:
```java
List<String> arrayList = new ArrayList<>();
arrayList.add(EncryptUtil.encodeUTF8StringBase64(JSON.toJSONString(jsonToken)));
requestContext.put("jsonToken", arrayList);
ctx.setRequestQueryParams(requestQueryParams);
return null
```

画面 6:
```java
/**
 * Token拦截处理
 */
public class TokenInterceptor implements HandlerInterceptor {

    @Override
    public boolean preHandle(HttpServletRequest httpServletRequest,
                             HttpServletResponse httpServletResponse, Object o) {
        String jsonToken = httpServletRequest.getParameter("jsonToken");
        if (StringUtils.isNotBlank(jsonToken)) {
            LoginUser loginUser = JSON
                    .parseObject(EncryptUtil.decodeUTF8StringBase64(jsonToken),
                            new TypeReference<LoginUser>() {
                            });
            httpServletRequest.setAttribute("jsonToken", loginUser);
        }
        return true;
    }
}
```

画面 7:
```java
@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new TokenInterceptor()).addPathPatterns("/**");
    }
}
```

画面 13:
```java
package cn.itcast.wanxingzp.consumer.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new TokenInterceptor()).addPathPatterns("/**");
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3: PPT 标题为“P2P项目认证架构图”，架构图包含以下模块及交互：
- 接入方（Web、移动端、第三方接入） → 网关 → 认证服务（UAAS） → 微服务1、微服务2、微服务3
- 认证服务（UAAS） → 统一账号服务
- 认证服务（UAAS） → 上传用户资产权限认证

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
