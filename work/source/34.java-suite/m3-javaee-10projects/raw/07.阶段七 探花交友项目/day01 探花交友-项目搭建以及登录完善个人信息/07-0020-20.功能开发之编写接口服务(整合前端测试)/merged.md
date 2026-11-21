# 20.功能开发之编写接口服务（整合前端测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\20.功能开发之编写接口服务（整合前端测试）_【海量资源尽在 666java.com】.mp4
- 时长 5分18秒（音频 319s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 那么接下来我们就来测试一下刚刚我们所启动的一个服务那么刚刚我是直接启动的其他后面我们是需要打断点的所以需要按照debug来做一个启动了然后我们找到刚刚我们所编写的Controller然后在这个位置来打一个断点来看一下它整个执行的过程我来打开我们的一个restclient去做一个测试
[00:23] 那么可以看到我们这个端口是18080那么前面这个地址是我这台机器的地址然后到后面就是我跟着所编写的路径叫用Loki然后发起post请求那么提交参数是一个手机号然后我们点击这个send去做一个发送走那么其实可以看到断点是不是已经进入了然后我们来看一下往下面走吧下面走走看一下拿到的手机号对不对没问题OK
[00:53] 然后往下面走等待他去发送那么看他会返回什么呢那么里面的逻辑呢我们就不跟着他去做一个执行了应该他是OK的一个逻辑那我们稍微等待一下第一次他是需要连接这个ready可能会稍微有点慢那么这个位置呢已经看到他说发送失败对吧发送失这个位置是我们我们要看这个看他已经是发送成功了然后往下面走走
[01:22] 走到这发送成功那么我来看一下我的手机有没有收到验证码已经收到了那么验证码是209951那么我们可以去执行往后通过走那么来看一下我们的响应在这个位置就是状态码就是200OK没有任何问题那么其实我们可以来检查一下检查一下就是我们刚刚所发送的验证码那么看它
[01:51] 我们来找一下然后我们进入到这个里面我们来看验证一下看我们的这个redis中的这个数据对不对干涉一下那么我们来get一个叫做checkcode然后手机号那么可以看到这个验证码就是我刚才所读的这个209951ok没有问题
[02:22] 好那么现在呢我们是不是基本上已经测试出我们这个所编写这个服务是OK的对吧那么接下来呢我们就需要通过我们的这个前端也就是我们那个安卓那个应用啊那我们来实际的来测试一下看它会怎么样那么之前我们所安装的这个呢是一个test这样的一个apk那么我们需要安装一个功能相对比较完善的一个apk是在这个位置啊
[02:50] 在这有一个在这就它那么把它呢我们来拖拽过来这样先把之前的那个先卸载掉那么找到之前这个探花那么鼠标N主然后把它拖拽到这个位置就卸载那么稍微等待一下是确定卸载好已经卸载掉了然后呢我们把它呢就直接拖过来那么来等待它的一个安装
[03:16] 好那么我这个应用呢就已经安装完成了那么接下来呢我们来看一下啊那么呃大家可以点击上面这个按钮啊就是在这个位置有一个修改呃服务API的一个地址那么点击它那么把这个地址可以修改掉那么呃如果采用这个Mock的话那么就可以把这个地址啊就是前面这个到164这个位置啊你填到这儿啊就可以了那么我这呢就直接就哎那我就那我就直接去使用它吧
[03:46] 保存一下然后我们点击登录注册OK好那么看到这样的一个页面了对吧然后我们输入手机号比如说我就输入我的手机号了然后点击获取验证码走你会发现请求是不是就来了然后往下面走走走走走走通过我们可能是
[04:18] 这个没有提醒啊那我们再来点一下吧OK那么可以看到刚刚我们所发送这个是不是就已经生效了对吧然后呢我们这样来测一下吧delete一下那么我把这个删除掉然后呢我们再来执行一下点击获取验证码轴哎是不是获取到了请输入这个验证码哎这样的话是不是我们第一个这个逻辑就已经跑通了那我们来看一下我们刚刚
[04:49] 的这个验证码有没有去重新发送呢那么可以看到我的手机已经是有了这个验证码了是563488来看一下对不对是不是563488OK这样的逻辑没有问题好那么到这里是不是我们已经就整合了我们的前端的逻辑已经就完成了整个的一个这样的一个测试了OK好那么关于我们这个短期验证码的一个发送和对接那就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个 Spring Boot 项目中短信验证码功能的后端实现与调试过程，包括代码逻辑、调试断点、服务调用以及移动端界面演示。

2) 按时间顺序列出每张画面的要点：
画面1：
- 显示 IntelliJ IDEA 中 MyApplication.java 的启动类代码。
- 代码内容：
  ```java
  package com.tanhua.sso;
  import ...
  @MapperScan("com.tanhua.sso.Mapper") //设置Mapper接口的扫描包
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
  Docker create --name redis-node02 --net host -v redis-node02/data redis:5.0.2 --cluster-enable
  Docker create --name redis-node03 --net host -v redis-node03/data redis:5.0.2 --cluster-enable
  Docker ps
  Docker exec -it redis-node01 /bin/bash
  Docker create -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -Dcom.RocketMQ.namesrv.addr=192.168.31.81:9876 -Dcom.RocketMQ.sendMessageWithVIPChannel=false -e JAVA_OPT_EXT=-server -Xms128m -Xmx128m -Xmn128m -

