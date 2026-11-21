# 画面线理解：20.功能开发之编写接口服务（整合前端测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\20.功能开发之编写接口服务（整合前端测试）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:42, 00:53, 01:35, 01:50, 02:23, 02:48, 03:06, 03:21, 04:00, 04:08, 04:23, 04:39, 05:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 19:11:04

1) 这一组画面整体在讲一个 Spring Boot 项目中短信验证码功能的后端实现与调试过程，包括代码逻辑、调试断点、服务调用以及移动端界面演示。

2) 按时间顺序列出每张画面的要点：
画面1：
- 显示 IntelliJ IDEA 中 MyApplication.java 的启动类代码。
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
- 控制台输出 Spring Boot 启动日志，显示 Tomcat 服务器启动成功。

画面2：
- 显示 SmsController.java 中 sendCheckCode 方法的代码，用于处理短信验证码请求。
- 代码内容：
  ```java
  @PostMapping("login")
  public ResponseEntityObject sendCheckCode(@RequestBody Map<String, Object> param) {
      ...
      int code = ((Integer) sendCheckCode.get("code")).intValue();
      if (code == 3) {
          return ResponseEntity.ok(null);
      } else if (code == 1) {
          ...
      }
  }
  ```
- 调试器显示当前执行位置在 sendCheckCode 方法内。

画面3：
- 与画面2类似，但调试器中变量窗口显示了参数和返回值，其中 code 值为 3。
- 代码内容：
  ```java
  int code = ((Integer) sendCheckCode.get("code")).intValue();
  if (code == 3) {
      return ResponseEntity.ok(null);
  } else if (code == 1) {
      ...
  }
  ```

画面4：
- 调试器中变量窗口显示了参数和返回值，其中 code 值为 1。
- 代码内容：
  ```java
  int code = ((Integer) sendCheckCode.get("code")).intValue();
  if (code == 3) {
      return ResponseEntity.ok(null);
  } else if (code == 1) {
      String msg = sendCheckCode.get("msg").toString();
      builder.errCode("000001").errMessage(msg);
  }
  ```

画面5：
- 显示 MobaXterm 终端界面，连接到 Ubuntu 服务器。
- 服务器信息：
  ```
  Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-145-generic x86_64)
  Last login: Thu Aug 1 09:20:32 2019 from 192.168.31.128
  root@itcast:~#
  ```

画面6：
- 在终端中执行 Docker 命令，创建并启动 Redis 和 RocketMQ 容器。
- 命令内容：
  ```bash
  docker create --name redis-node02 --net host -v redis-node02/data redis:5.0.2 --cluster-enable
  docker create --name redis-node03 --net host -v redis-node03/data redis:5.0.2 --cluster-enable
  docker ps
  docker exec -it redis-node01 /bin/bash
  docker create -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.rocketmq.namesrv.addr=192.168.31.81:9876 -Dcom.rocketmq.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -
