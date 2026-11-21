# 画面线理解：15-SpringBoot监控-actuator开启所有endpoint

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/2.SpringBoot 第二天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\2.SpringBoot 第二天\15-SpringBoot监控-actuator开启所有endpoint_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:56, 01:14, 01:33, 02:07, 02:46, 03:05, 03:43, 04:10, 04:20, 04:41, 05:07, 05:35, 06:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:04:18

1) 这一组画面整体在讲 Spring Boot Actuator 的健康检查和端点暴露配置，以及如何通过 HTTP 请求访问这些端点并查看其返回的 JSON 结构。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了访问 http://localhost:8080/actuator 返回的 JSON 数据，其中包含多个端点的链接，如 health、info、beans 等。
画面 2: 在 IDEA 中编辑 application.properties 文件，配置了健康检查的详细程度和暴露的端点。
画面 3: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "links" 部分。
画面 4: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "components" 部分。
画面 5: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "dependencies" 部分。
画面 6: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "beans" 部分。
画面 7: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "redisTemplate" 部分。
画面 8: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "conditions" 部分。
画面 9: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "info" 部分。
画面 10: 在 IDEA 中右键点击项目，选择“Build Module 'springboot-actuator'”进行构建。
画面 11: 在 IDEA 中查看 UserController.java 文件，其中包含一个 @RestController 和 @RequestMapping("/user") 注解。
画面 12: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "mappings" 部分。
画面 13: 在在线 JSON 解析器中查看了 /actuator 返回的 JSON 结构，重点是 "requestMappingConditions" 部分。
画面 14: 在浏览器中访问 http://localhost:8080/actuator 返回的 JSON 数据，其中包含多个端点的链接，如 health、info、beans 等。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 2:
```
info.name=shangsan
info.age=23
# 开启健康检查的详细信息
management.endpoint.health.show-details=ALWAYS
# 将所有监控端点暴露在默认路径下
management.endpoints.web.exposure.include=*
```

画面 9:
```
{
  "name": "applicationConfig",
  "properties": {
    "value": "shangsan",
    "origin": "class path resource (application.properties)"
  },
  "info.age": "23",
  "origin": "class path resource (application.properties)"
}
```

画面 11:
```
package com.ethan.springboottactuator;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/user")
public class UserController {
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无。

5) 无。
