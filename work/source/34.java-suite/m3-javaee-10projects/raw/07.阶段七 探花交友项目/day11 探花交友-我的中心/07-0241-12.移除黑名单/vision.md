# 画面线理解：12.移除黑名单

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\12.移除黑名单_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:15, 00:27, 00:58, 01:07, 01:26, 02:03, 02:18, 02:38, 02:45, 02:54, 03:17, 03:43, 04:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:44:56

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中通过 UserController、UsersService 和 BlackListService 层级调用，使用 MyBatis-Plus 的 QueryWrapper 实现对黑名单数据的分页查询和删除功能，并通过 Mock 服务模拟接口和数据库验证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了通过 Advanced REST Client 发起的 HTTP 请求返回的 JSON 数据，内容为黑名单用户列表，包含 avatar、nickname、gender、age 等字段。
- JSON 数据：
```json
{
  "counts": 0,
  "pages": 0,
  "page": 1,
  "list": [
    {
      "id": 22,
      "avatar": "https://itcast-tanhuu.server-domain.aliyun.com/images/0g/10.jpg",
      "nickname": "laine_22",
      "gender": "mz",
      "age": 49
    },
    {
      "id": 23,
      "avatar": "https://itcast-tanhuu.server-domain.aliyun.com/images/0g/10.jpg",
      "nickname": "laine_23",
      "gender": "mz",
      "age": 27
    },
    {
      "id": 24,
      "avatar": "https://itcast-tanhuu.server-domain.aliyun.com/images/0g/2.jpg",
      "nickname": "laine_24",
      "gender": "mz",
      "age": 39
    }
  ]
}
```

画面 2：
- 展示了 Mock 服务（mock.boxegu.com）中接口的参数配置页面。
- 路径参数：`uid`
- Headers：
  - Content-Type: application/x-www-form-urlencoded
  - Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyIiwiaWF0IjoxNjMwMjUxNzQwLCJleHAiOjE2MzAyNTUzNDAsImF1ZCI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1YiI6ImF1dGhvcml0eSIsInN1
