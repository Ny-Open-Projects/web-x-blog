# 画面线理解：day01-19-Swagger常用注解

- 阶段：10.阶段十 万信金融项目
- 章节：01_万信金融-项目介绍和开发环境搭建
- 源文件：10.阶段十 万信金融项目\01_万信金融-项目介绍和开发环境搭建\day01-19-Swagger常用注解_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:57, 03:20, 04:04, 04:20, 05:14, 05:56, 07:11, 07:35, 08:11, 08:20, 08:37, 08:50, 09:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:11:44

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 Spring Boot 项目中使用 Swagger 注解来生成 API 文档，重点演示了 @ApiImplicitParam 注解的使用方法和参数配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 IntelliJ IDEA 中的项目结构，选中了 ConsumerController.java 文件，准备编写代码。
画面 2: 展示了 PDF 文档中关于 Swagger 常用注解的介绍，包括 @Api、@ApiOperation、@ApiParam 等。
画面 3: PDF 文档继续展示 Swagger 注解，重点是 @ApiModelProperty、@ApiResponse、@ApiIgnore。
画面 4: PDF 文档中展示了 @ApiImplicitParam 注解的属性表格，包括 paramType、dataType、name、value、required 等。
画面 5: PDF 文档中再次展示 @ApiImplicitParam 注解的属性表格，内容与画面 4 相同。
画面 6: 在 IDEA 中，展示了 ConsumerController.java 文件的初始代码，包含 @RestController 和 @Api 注解。
画面 7: 屏幕截图显示了多个窗口，包括 PDF 文档和 IDEA，用于说明如何查看和使用 Swagger 文档。
画面 8: PDF 文档中再次展示 Swagger 注解的介绍，内容与画面 2 相同。
画面 9: PDF 文档中再次展示 @ApiImplicitParam 注解的属性表格，内容与画面 4 相同。
画面 10: 在 IDEA 中，展示了 ConsumerController.java 文件中添加了 @ApiImplicitParam 注解的代码，用于接收参数 name。
画面 11: 在 IDEA 中，展示了 ConsumerController.java 文件中添加了 @ApiImplicitParam 注解的代码，参数 required 设置为 true。
画面 12: PDF 文档中再次展示 @ApiImplicitParam 注解的属性表格，内容与画面 4 相同。
画面 13: 在 IDEA 中，展示了 ConsumerController.java 文件中添加了 @ApiImplicitParam 注解的代码，参数 dataType 设置为 "String"。
画面 14: 在 IDEA 中，展示了 ConsumerController.java 文件中添加了 @ApiImplicitParam 注解的代码，参数 required 设置为 true，dataType 设置为 "String"。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6 代码：
```java
package cn.itcast.wanxingzp.consumer.controller;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "用户服务的Controller", tags = "Consumer", description = "用户服务API")
@RestController
public class ConsumerController {

    @ApiOperation("测试hello")
    @GetMapping(path = "/hello")
    public String hello(){
        return "hello";
    }
}
```

画面 10 代码：
```java
@ApiImplicitParam(name = "name", value = "姓名", required = "true")
public String hi(String name){
    return "hi,"+name;
}
```

画面 11 代码：
```java
@ApiImplicitParam(name = "name", value = "姓名", required = true)
public String hi(String name){
    return "hi,"+name;
}
```

画面 13 代码：
```java
@ApiImplicitParam(name = "name", value = "姓名", required = true, dataType = "String")
public String hi(String name){
    return "hi,"+name;
}
```

画面 14 代码：
```java
@ApiImplicitParam(name = "name", value = "姓名", required = true, dataType = "String")
public String hi(String name){
    return "hi,"+name;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2、3、8、9、12: PPT 标题为“2.1.3 Swagger常用注解”，内容包括：
- @Api：修饰整个类，描述Controller的作用
- @ApiOperation：描述一个类的一个方法，或者说明一个接口
- @ApiParam：单个参数的描述信息
- @ApiModelProperty：用对象接收参数时，描述对象的一个字段
- @ApiResponse：HTTP响应其中1个描述
- @ApiIgnore：使用该注解忽略这个API
- @ApiError：发生错误返回的信息
- @ApiImplicitParam：一个请求参数
- @ApiImplicitParams：多个请求参数的描述信息

画面 4、5、9、12: PPT 表格数据：
| 属性       | 取值     | 作用                     |
|------------|----------|--------------------------|
| paramType  | path     | 以地址的形式提交数据     |
|            | query    | 直接跟参数完成自动映射赋值 |
|            | body     | 以流的形式提交 仅支持POST |
|            | header   | 参数在request headers 里边提交 |
|            | form     | 以form表单的形式提交 仅支持POST |
| dataType   | Long     | 参数的数据类型 只作为标志说明，并没有实际验证 |
|            | String   |                          |
| name       |          | 接收参数名               |
| value      |          | 接收参数的意义描述       |
| required   | true     | 参数是否必填             |
|            | false    | 非必填                   |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
