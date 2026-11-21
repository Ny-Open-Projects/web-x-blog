# 画面线理解：day06-15-开户第一阶段-遗留功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-15-开户第一阶段-遗留功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:18, 01:02, 01:55, 02:04, 02:22, 02:50, 03:01, 03:20, 03:53, 04:43, 05:17, 05:44, 06:04, 06:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:23:48

1) 这一组画面整体在讲如何通过 Spring MVC 拦截器在网关层处理用户登录凭证（access_token），并将其转换为 JSON 格式传递给下游微服务。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示课程 PPT 第 1.4.5 节标题“微服务获取请求中的数据”，并引出问题：如何从请求中取出用户信息？解决方案是采用 Spring MVC 拦截器。
画面 2: 展示系统架构图，说明接入方（WEB、移动端、第三方）通过网关访问资源，认证服务（UAA）负责用户认证。
画面 3: 展示 IDEA 中项目结构，定位到网关服务的 `pom.xml` 文件。
画面 4: 展示网关服务中 `AuthFilter.java` 文件的代码，其中包含将 `jsonToken` 参数转换为 JSON 字符串并放入请求参数的逻辑。
画面 5: 展示系统架构图，标注了请求流程：接入方请求网关，网关转发至认证服务，认证服务返回 access_token，网关将 token 转发给微服务。
画面 6: 展示消费者服务中 `TokenInterceptor.java` 文件的代码，其中包含将 `jsonToken` 参数转换为 JSON 对象并放入请求属性的逻辑。
画面 7: 展示消费者服务中 `LoginUser.java` 类的代码，定义了用户信息的 Java Bean。
画面 8: 展示消费者服务中 `ConsumerController.java` 文件的代码，包含测试接口 `hello` 和 `hi`。
画面 9: 展示消费者服务中 `TokenInterceptor.java` 文件的代码，其中包含拦截器的 `preHandle` 方法，用于解析并设置登录用户信息。
画面 10: 展示系统架构图，与画面 5 相同，用于说明认证流程。
画面 11: 展示系统架构图，与画面 5 相同，同时在左下角显示了终端窗口，提示用户输入 `curl` 命令。
画面 12: 展示消费者服务中 `TokenInterceptor.java` 文件的代码，与画面 9 相同，用于解析并设置登录用户信息。
画面 13: 展示消费者服务中 `SecurityUtil.java` 文件的代码，其中包含从请求属性中获取登录用户信息的方法。
画面 14: 展示消费者服务中 `ConsumerController.java` 文件的代码，包含创建用户和测试接口的逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4 代码：
```java
//2.将jsonToken写入转发财务请求中，这样微服务就能通过
requestContext ctx = RequestContext.getCurrentContext();
HttpServletRequest request = ctx.getRequest();
request.getParameterMap(); //关键步骤，一定要get一下，下面这行代码才能取到值
Map<String, List<String>> request = ctx.getQueryParams();
if (requestQueryParams == null) {
    requestQueryParams = new HashMap<>();
}
List<String> arrayList = new ArrayList<>();
arrayList.add(EncryptUtil.encodeUTF8StringBase64( jsonToken));
requestQueryParams.put("jsonToken", arrayList);
ctx.setRequestQueryParams(requestQueryParams);
return null;
```

画面 6 代码：
```java
//2.将jsonToken写入转发财务请求中，这样微服务就能通过
requestContext ctx = RequestContext.getCurrentContext();
HttpServletRequest request = ctx.getRequest();
request.getParameterMap(); //关键步骤，一定要get一下，下面这行代码才能取到值
Map<String, List<String>> request = ctx.getQueryParams();
if (requestQueryParams == null) {
    requestQueryParams = new HashMap<>();
}
List<String> arrayList = new ArrayList<>();
arrayList.add(EncryptUtil.encodeUTF8StringBase64( jsonToken));
requestQueryParams.put("jsonToken", arrayList);
ctx.setRequestQueryParams(requestQueryParams);
return null;
```

画面 7 代码：
```java
package cn.itcast.wanning2p.api.account.model;

/**
 * 当前登录用户
 */
@Data
public class LoginUser {

    /**
     * tenantId : 1
     * departmentId : 1
     * payload : "W111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
