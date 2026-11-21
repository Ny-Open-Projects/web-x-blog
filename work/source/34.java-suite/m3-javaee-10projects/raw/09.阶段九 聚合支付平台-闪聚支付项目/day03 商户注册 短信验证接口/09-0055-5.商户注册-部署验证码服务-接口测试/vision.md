# 画面线理解：5.商户注册-部署验证码服务-接口测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\5.商户注册-部署验证码服务-接口测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:22, 02:11, 04:02, 04:46, 05:23, 06:16, 07:00, 08:07, 09:13, 10:38, 11:33, 12:24, 12:58, 14:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:51:17

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Swagger UI 调用 Spring Boot 服务的验证码生成与校验接口，并展示相关的代码实现和 Redis 配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中“2.1 发送验证码”接口的参数说明，包括 name、payload、effectiveTime。
画面 2: 在 Swagger UI 中显示 /generate 接口的参数配置，包括 effectiveTime、name、payload。
画面 3: 在 IDEA 中展示 SeNumberVerificationHandler.java 文件的代码，包含注释和调用 smsService 的代码。
画面 4: 在 Swagger UI 中显示 /generate 接口的响应结果，返回 JSON 数据，包含 code、msg、result、content。
画面 5: 在 IDEA 中展示 SeNumberVerificationHandler.java 文件的代码，显示 Redis 连接异常的错误日志。
画面 6: 在 Windows 资源管理器中显示 redis-windows.conf 文件。
画面 7: 在 Redis Desktop Manager 中尝试连接 redis-01，弹出“确认”对话框。
画面 8: 在 Swagger UI 中显示 /generate 接口的 curl 命令和请求 URL。
画面 9: 在 Swagger UI 中显示 /verify 接口的参数配置，包括 name、verificationCode、verificationKey。
画面 10: 在 PDF 文档中显示“2.2 校验验证码”接口的参数说明，包括 name、verificationCode、verificationKey。
画面 11: 在 Swagger UI 中显示 /verify 接口的参数输入，填写了 name、verificationCode、verificationKey。
画面 12: 在 Swagger UI 中显示 /generate 接口的 curl 命令和请求 URL。
画面 13: 在 PDF 文档中显示“2.2 校验验证码”接口的参数说明，包括 name、verificationCode、verificationKey。
画面 14: 在 PDF 文档中显示“2.2 校验验证码”接口的参数说明，包括 name、verificationCode、verificationKey。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
String mobile = String.valueOf(payload.get("mobile"));
// 使用腾讯云发送短信
smsService.sendMobile(code, getEffectiveTime());
// 测试使用，在这里直接输出验证码
smsService.sendConsole(mobile, code, getEffectiveTime());
return null;
```

画面 5:
```java
// get a resource from the pool. nested exception is io.lettuce.core.RedisConnectionException: Unable to connect to localhost:6379
```

画面 6:
```
redis-windows.conf
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1:
- 标题：2.1 发送验证码
- 表格：
  | 参数名 | 参数类型 | 描述 |
  | --- | --- | --- |
  | name | string(query) | 业务名称(使用何种方式的验证码，可选的sms, img, mail等) |
  | payload | application/json | 业务携带参数，如手机号、邮箱 |
  | effectiveTime | string(query) | 验证信息有效期(秒) |

画面 10:
- 标题：2.2 校验验证码
- 表格：
  | 参数名 | 参数类型 | 描述 |
  | --- | --- | --- |
  | name | string(query) | 业务名称(使用何种方式的验证码，可选的sms, img, mail等) |
  | verificationCode | string(query) | 验证码 |
  | verificationKey | string(query) | 验证key |

画面 13:
- 标题：2.2 校验验证码
- 表格：
  | 参数名 | 参数类型 | 描述 |
  | --- | --- | --- |
  | name | string(query) | 业务名称(使用何种方式的验证码，可选的sms, img, mail等) |
  | verificationCode | string(query) | 验证码 |
  | verificationKey | string(query) | 验证key |

画面 14:
- 标题：2.2 校验验证码
- 表格：
  | 参数名 | 参数类型 | 描述 |
  | --- | --- | --- |
  | name | string(query) | 业务名称(使用何种方式的验证码，可选的sms, img, mail等) |
  | verificationCode | string(query) | 验证码 |
  | verificationKey | string(query) | 验证key |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
