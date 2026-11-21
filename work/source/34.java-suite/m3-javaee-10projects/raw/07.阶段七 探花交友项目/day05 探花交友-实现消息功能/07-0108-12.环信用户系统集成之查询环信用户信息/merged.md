# 12.环信用户系统集成之查询环信用户信息

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\12.环信用户系统集成之查询环信用户信息_【海量资源尽在 666java.com】.mp4
- 时长 6分30秒（音频 390s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么前面呢我们已经完成了将我们的用户信息呢注册到了环信那么接下来呢我们来看一下在我们的APP中啊其实我们是需要去查询到我们的用户名和密码进行登录这个环信的所以说呢在我们的这个APP这一段它并没有保存我们的用户名和密码的信息而这个用户名和密码信息呢是由我们后端所提供的
[00:28] 所以说呢我们需要为我们的前端呢去提供一个接口进行做查询那么这个接口的定义呢是在这个位置有一个叫做环信的一个用户信息查询环信User返回就返回这样的一个数据就可以了用户名和密码那么接下来呢我们就来编写一下我们这个环信的这样的一个接口信息那么我们打开我们这个工程啊然后我们找到找到我们的这个
[00:58] server这个工程接下来呢我们在我们的server这个工程中啊去来编写这个服务啊那么我们找到我们的Controller然后呢我们去创建一个类啊叫做环信环信Controller然后呢我们给它设置为这是一个restcontroller然后呢设置一个request mappingrequest mapping呢我们给它设置为这是一个这个环信
[01:31] 好然后呢下面我们哎这个我们是不是应该我们这个名字写的有点问题啊那我们就来改一下就叫这改成大写啊好累的要大写啊然后呢我们这个里面去写个方法那么我们返回值呢我们应该就返回的是我们的response啊response然后呢这个t呢就是我们的环性啊这个Ura这个对象啊
[02:00] 然后呢我们来看一下这个环线优越对象呢就是用户名和密码然后呢我们就需要呢去做一个这个query这个操作query这个user这个操作然后呢去写一个request mapping那么这个里面呢写一个叫做user我们应该叫写这么get mapping然后呢写一个这个user然后呢最后我们就可以去做一个
[02:29] 那么我们就直接去先拿到我们当前这个用户然后呢Url等于UrlUrlStateLocal点get去拿到一个Url然后呢我们去构造一个这个对象那我们就直接来做一个构造吧那我们就直接return这个responseresponse entity点ok中里面我们去放一个对象
[03:00] 那么放哪个对象呢就是这个叫做环信环信U了啊环信U了这个对象然后呢等于去new一个这个对象啊去new一个这个对象啊然后呢我们把这个对象呢就做一个返回啊那么他的用户名呢这个用户名啊U了name那就是这个U了点get id啊点to stream然后呢环信U了点set password啊
[03:31] 那么这个呢就是在前面我们写过的一个这个就是进行MD5加密之后的一个值啊那我们来找一下这个值我们把它拷贝过来在SSO里面我们找到这个Service那么有一个叫做环信啊这个Service然后这个里面呢我们找到这个代码的叫这啊这个就是我们的一个密码好那我们拷贝一下拷贝到我们的这个里面来放到这来
[03:57] 好那么这个UID呢那就是我们上面的这个UID啊然后呢去加一个他做一个MD5值的一个转化啊就可以了好这样的话呢我们已经就拿到了我们这个环境的这个信息那么通过我们这个接口呢就可以去返回回去了啊那我们来看一下我们的这个讲义的中的实现那么跟我们这个写的是不是也是一样的对吧然后呢这个是这个是我们的这个环境然后呢这个定一个U的
[04:26] 然后我们去定一个优对象最后做一个返回最后测试就会看到有这样的一个结果对吧好 那么接下来我们也来测试一下那么这个SSO就跑起来了我们这个就不用管它了然后我们再把我们这个server需要跑起来那么server要跑起来我们首先需要把double先跑起来对吧然后我们再去把这个server跑起来我们来找到我们这个double然后去run一下
[04:53] 好那我们来等待一下它的一个执行好那么现在我们就跑起来了下面我们就来测试一下那么首先呢我们还是需要通过我们这个就是我们刚刚所注册的这个用户然后呢我们去做这个登录然后呢我们发起发送这个验证码那么发送完成之后呢我们去做登录走好那么那么我们就把它去直接通过那么登录成功了那么登录成功之后啊那么就需要
[05:23] 去来做查询了来做查询呢我们就我们就找一个吧找一个他啊然后呢我们去把这个拷贝过来然后呢我们来改一下我们的这个就是请求的一个路径哦那么我们就直接来这个里面拷贝吧就是就是他的啊环信优惠好然后呢我们把它拷贝一下然后呢到这来好到这环信这个优惠然后呢去发起请求
[05:50] 走那么可以看到是不是就要返回了这样的一个数据就用户名是102然后密码是一个MD5加密的个值那么这样的话我们把这个接口提供给我们的APP那么APP通过这个接口就可以拿到这个用户信息然后拿到这个用户信息之后就可以去登录到环信然后去调用环信的一些
[06:12] 这个安卓的SDK来获取或者说发送接收一些这个消息了好那我们来看一下这个讲义讲义呢是不是也是这样的对吧能够去拿到这个信息了OK好那么关于我们这个查询环信用户信息的一个接口的一个编写那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  @MapperScan("com.tanhua.sso.Mapper") //设置Mapper接口的扫描包
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
  package com.tanhua.server.Controller;
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

