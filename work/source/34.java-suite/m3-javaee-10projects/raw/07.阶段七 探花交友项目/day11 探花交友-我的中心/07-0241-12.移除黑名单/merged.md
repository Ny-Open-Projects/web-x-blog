# 12.移除黑名单

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\12.移除黑名单_【海量资源尽在 666java.com】.mp4
- 时长 4分20秒（音频 261s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下移除黑名单那么我们找到这个接口啊那么是在这个位置啊那么它发起的是一个delete请求然后呢传递一个用户的ID然后呢下面呢这个是用户ID然后呢响应数据呢是没有的好那么下面我们就来实现啊这个接口那么首先呢我们把这个Controller呢我们来拷贝一下然后呢把它丢到我们的这个serverus Controller下面来
[00:29] 然后在这里面我再一丢好那么我们可以看到我们通过一个delete mapping去指定我们接收的是一个delete请求然后我们去接收的是一个uid这个是我们的一个占卜服然后下面是有一个用户id然后我们去做一个delete这个操作接下来我们就在我们的userservice中去做一个实现
[00:55] 那么首先呢我们先拿到我们的user等于user3local.get去拿到user然后呢我们就调用我们的这个叫做blacklist Service做一个delete那就叫delete这个blacklist吧然后呢我们传递需要传递两个参数一个呢就是我这个当前这个用户的一个ID然后呢我们再去传递一个
[01:25] 要删除的一个目标的一个这个ID然后这样的话呢就可以了那么接下来呢我们就在这个里面去做一个删除的操作那么这个是UID那么我们其实这个呢是不是我们应该叫UID而这个呢应该叫Black UID对吧然后呢这个list然后呢UID
[01:54] 或者我们就叫叫它吧好然后呢我们就去做一个删除那么通过this.map然后呢做一个delete的操作通过一个这个wrap去做一个删除那么我们就还是定义吧直接来写一下叫querywrap然后呢叫blocklist然后呢querywrap等于new一个queryquerywrap然后呢我们去把它呢传递给它
[02:24] 然后我们需要设置有两个参数对吧第一个是EQ那就是我们上面这个UID然后把这个UID给它传递过来这是第一个参数第二个参数我们是需要去按的去设置一个那就是直接EQ就是按的那么然后就是我们的一个黑名单那么我们来看一下黑名单的这个ID那我们来找一下它就是那就这个之段了
[02:55] 这个字段然后呢叫black yoda id好把它传递给他那么这样的话呢我们就实现了一个这个删除那么我们这个方法是不是应该去给他返回一个布尔值啊对吧返回布尔值这样会好一些那么return一个他的delete之后他是返回我们删除的一个数量那么如果他
[03:24] 大于0的话那么这样的话就代表删除了这个数据了对吧然后呢我们来看一下我们的这个Service我们那个Service呢然后找一下我们那个Service在这那么它其实不需要处理了直接去做调用dict就可以了好那么接下来呢我们来重启来测试一下好那么接下来呢我们就直接整合到我们的app里面来做一个测试然后呢进入到我的这个模块然后呢找到通用设置然后呢有一个黑名单
[03:54] 那么这个里面有222324那么比如说我们把这个24呢给它取消掉我们点一下这个取消啊是不是就已经取消掉了然后呢再次进入呢就没有了那我们再去进入到我们这个表里面我们来查看一下那么刷新一下是不是就变成两条数据了那就说明刚刚我们所编写这个代码是OK的对吧好那么这个呢就是我们的一个移除黑名单的啊这样的一个功能的一个实现

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

