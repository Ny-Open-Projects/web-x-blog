# 画面线理解：12.环信用户系统集成之查询环信用户信息

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\12.环信用户系统集成之查询环信用户信息_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:35, 01:02, 01:31, 01:58, 02:32, 02:56, 03:13, 03:46, 04:13, 04:41, 04:59, 05:24, 05:47, 06:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:12:04

1) 这一组画面整体在讲如何在 Spring Boot 项目中编写一个用于查询用户信息的 RESTful 控制器，并通过模拟客户端测试其接口。

2) 按时间顺序列出每张画面的要点：

画面 1:
- 展示了 Mock 服务的界面，接口名称为“环信用户信息”，接口路径为 GET /huaxin/user。
- 返回数据包含 username 和 password 字段，其默认值分别为“用户名”和“用户密码”，示例值分别为 "123456" 和 "123456"。

画面 2:
- 展示了 IntelliJ IDEA 中的项目结构，当前打开的是 MyApplication.java。
- 代码内容：
  ```java
  package com.tanhua.sso;
  import ...
  @MapperScan("com.tanhua.sso.mapper") //设置mapper接口的扫描包
  @SpringBootApplication
  public class MyApplication {
      public static void main(String[] args) {
          SpringApplication.run(MyApplication.class, args);
      }
  }
  ```

画面 3:
- 展示了 IntelliJ IDEA 中的项目结构，当前打开的是 HuanXinController.java。
- 代码内容：
  ```java
  package com.tanhua.server.controller;
  import org.springframework.web.bind.annotation.RequestMapping;
  import org.springframework.web.bind.annotation.RestController;
  @RestController
  @RequestMapping("huanxin")
  public class HuanXinController {
  }
  ```

画面 4:
- 展示了 IntelliJ IDEA 中的项目结构，当前打开的是 HuanXinController.java。
- 代码内容：
  ```java
  import org.springframework.http.ResponseEntity;
  import org.springframework.web.bind.annotation.GetMapping;
  import org.springframework.web.bind.annotation.RestController;
  @RestController
  @RequestMapping("huanxin")
  public class HuanXinController {
      @GetMapping("user")
  }
  ```

画面 5:
- 展示了 IntelliJ IDEA 中的项目结构，当前打开的是 HuanXinController.java。
- 代码内容：
  ```java
  import org.springframework.http.ResponseEntity;
  import org.springframework.web.bind.annotation.GetMapping;
  import org.springframework.web.bind.annotation.RestController;
  @RestController
  @RequestMapping("huanxin")
  public class HuanXinController {
      @GetMapping("user")
      public ResponseEntity<HuanXinUser> queryUser() {
  }
  ```

画面 6:
- 展示了 IntelliJ IDEA 中的项目结构，当前打开的是 HuanXinController.java。
- 代码内容：
  ```java
  import org.springframework.http.ResponseEntity;
  import org.springframework.web.bind.annotation.GetMapping;
  import org.springframework.web.bind.annotation.RestController;
  @RestController
  @RequestMapping("huanxin")
  public class HuanXinController {
      @GetMapping("user")
      public ResponseEntity<HuanXinUser> queryUser() {
          return ResponseEntity.ok();
      }
  }
  ```

画面 7:
- 展示了 IntelliJ IDEA 中的项目结构，当前打开的是 HuanXinController.java。
- 代码内容：
  ```java
  import org.springframework.http.ResponseEntity;
  import org.springframework.web.bind.annotation.GetMapping;
  import org.springframework.web.bind.annotation.RestController;
  @RestController
  @RequestMapping("huanxin")
  public class HuanXinController {
      @GetMapping("user")
      public ResponseEntity<HuanXinUser> queryUser() {
          HuanXinUser huanXinUser = new HuanXinUser();
          return ResponseEntity.ok();
      }
  }
  ```

画面 8:
- 展示了 IntelliJ IDEA 中的项目结构，当前打开的是 HuanXinService.java。
- 代码内容：
  ```java
  try {
      HttpEntity<String> httpEntity = new HttpEntity<>(MAPPER.writeValueAsString(user));
      //发起请求
      ResponseEntity<String> responseEntity = this.restTemplate.postForObject(url, httpEntity, String.class);
      return responseEntity.getStatusCodeValue() == 200;
  } catch (Exception e) {
      e.printStackTrace();
      return false;
  }
  ```

画面 9:
- 展示了 IntelliJ IDEA 中的项目结构，当前打开的是 HuanXinController.java。
- 代码内容：
  ```java
  @GetMapping("user")
  public ResponseEntity<HuanXinUser> queryUser() {
      HuanXinUser huanXinUser = new HuanXinUser();
      User user = UserThreadLocal.get();
      huanXinUser.setUsername(user.getId().toString());
      huanXinUser.setPassword(DigestUtils.md5Hex(data + user.getId()));
      return ResponseEntity.ok(huanXinUser);
  }
  ```

画面 10:
- 展示了 IntelliJ IDEA 中的项目结构，当前打开的是 HuanXinController.java。
- 代码内容：
  ```java
  @GetMapping("user")
  public ResponseEntity<HuanXinUser> queryUser() {
      HuanXinUser huanXinUser = new HuanXinUser();
      User user = UserThreadLocal.get();
      huanXinUser.setUsername(user.getId().toString());
      huanXinUser.setPassword(DigestUtils.md5Hex(data + user.getId()));
      return ResponseEntity.ok(huanXinUser);
  }
  ```

画面 11:
- 展示了 Advanced REST Client 的界面，请求体为：
  ```json
  {
    "phone": "1766236965",
    "verificationCode": "123456"
  }
  ```
- 响应状态为 200，响应体为：
  ```json
  {
    "code": 0,
    "msg": "success",
    "data": {
      "id": 1,
      "username": "1766236965",
      "password": "e10adc3949ba59abbe56e057f20f883e"
    }
  }
  ```

画面 12:
- 展示了 Advanced REST Client 的界面，请求体为空。
- 响应状态为 200，响应体为空。

画面 13:
- 展示了 Advanced REST Client 的界面，地址栏中显示了多个接口地址，包括：
  - http://192.168.31.90
  - http://192.168.31.90/messages/announcements
  - http://192.168.31.90/messages/comments
  - http://192.168.31.90/messages/contacts
  - http://192.168.31.90/messages/contacts/keyword=1
  - http://192.168.31.90/user/huanxin/contacts/113
  - http://192.168.31.90/user/huanxin/contacts/114
  - http://192.168.31.90/user/huanxin/contacts/115
  - http://192.168.31.90/user/huanxin/contacts/116
  - http://192.168.31.90/user/huanxin/contacts/117
  - http://192.168.31.90/user/huanxin/contacts/118
  - http://192.168.31.90/user/huanxin/contacts/119
  - http://192.168.31.90/user/huanxin/contacts/120
  - http://192.168.31.90/user/huanxin/contacts/121
  - http://192.168.31.90/user/huanxin/contacts/122
  - http://192.168.31.90/user/huanxin/contacts/123
  - http://192.168.31.90/user/huanxin/contacts/124
  - http://192.168.31.90/user/huanxin/contacts/125
  - http://192.168.31.90/user/huanxin/contacts/126
  - http://192.168.31.90/user/huanxin/contacts/127
  - http://192.168.31.90/user/huanxin/contacts/128
  - http://192.168.31.90/user/huanxin/contacts/129
  - http://192.168.31.90/user/huanxin/contacts/130
  - http://192.168.31.90/user/huanxin/contacts/131
  - http://192.168.31.90/user/huanxin/contacts/132
  - http://192.168.31.90/user/huanxin/contacts/133
  -
