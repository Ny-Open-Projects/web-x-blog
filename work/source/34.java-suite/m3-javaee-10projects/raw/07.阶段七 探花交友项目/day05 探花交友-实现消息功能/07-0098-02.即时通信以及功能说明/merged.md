# 02.即时通信以及功能说明

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\02.即时通信以及功能说明_【海量资源尽在 666java.com】.mp4
- 时长 4分48秒（音频 284s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下即时通讯那么什么是即时通讯呢其实我们对于即时通讯呢也并不陌生了因为我们每天的都会去使用这个微信啊或者说QQ啊等这样的一些通信的软件那么他们其实就是即时通讯啊那么下面呢我们来看一下这个呢是百度百科对于即时通讯的一个定义啊我们来看一下那么即时通讯的简称是叫IM啊
[00:29] 然后呢他是只能够去及时的去发送和接收我们互联网的一些消息的这样的一些业务那么从1998年呢就面试以来啊得到了迅速的一个这个发展那么集通讯的目前呢他不仅是单纯的一个聊天工具而且他集成了有很多的一些功能包括像什么这种邮件呢博客呢音乐啊等等这样的一些这个功能那么并且他也形成了这样的一个什么
[00:58] 平台啊那么也就是说它之前呢最早是一个用来我们直接可以聊天的一个工具而我们现在呢逐步的发展为是一个一体化的这样的一个平台因为上面会集成很多的一些这个东西包括有什么游戏呢电商呢资讯呢娱乐呢等等这样的一些内容呢会非常多啊并且呢是我们现在呢主要呢是在通过什么呢通过我们的手机也就是我们的移动端来使用我们的集通讯
[01:28] 那么这个呢发展也是非常非常迅猛的OK那么其实这个呢就是集通讯我们不需要去解释太多那么大家其实都了解都知道这个集通讯好那么接下来呢我们就来看一下在我们的碳花交友这个项目中它的功能是什么样的一些这个功能那么在我们的碳花交友这个项目中那么同样呢我们也是提供了这种类似微信的这样的一个聊天的功能那么我们的用户呢可以
[01:58] 选择和好友进行聊天那么也可以呢和陌生人进行做聊天当然了如果是陌生人的话那我们就需要通过这个聊一下这个功能进行打招呼如果对方同意之后那么就会成为好友然后就可以进行聊天了那么大致呢是在这个位置啊就说
[02:17] 那么我们去查看陌生人这个动态的时候呢下面的会有一个按钮叫做聊一下啊叫做聊一下那我点击这个聊一下呢就会去弹出一个框让我们去输入这个相关的问题而这个问题呢是对方所设置的问题那么我们输入之后呢呃然后点击提交那我们对方呢他就能够知道啊看到我们这个呃消息那么看到我们这个聊一下这个消息之后啊他点击这个聊一下
[02:46] 他愿意跟我们聊天那么这个时候就会成为好友那么成为好友之后啊那我们就可以进行做聊天了就是这样的一个功能啊这样的一个业务啊那么如果这个陌生人之间相互喜欢呢也会成为好友也可以聊天那么什么意思呢
[03:03] 那么在下面这个位置是不是还有一个这个按钮叫做什么叫做喜欢那么你点击这个喜欢啊你喜欢这个对方那么如果对方呢也点击喜欢你那这个时候呢你们两个之间呢也能够成为好友那么也是可以进行做聊天的啊所以说是这样的一个逻辑啊在里面
[03:23] 好那么在我们的消息这个界面中呢那我们可以啊不仅是可以给对方去发消息了发文字呢图片呢这个都可以啊那么并且呢我们还可以查看我们的一些点赞或者说评论啊喜欢公告啊等这样的一些消息啊那么我们来看他的一个页面呢是这样的一个页面啊那么在这个里面呢这个就是我们这个聊天的一个记录然后呢下面的这上面这个呢就是我们的一个点赞的一个消息列表
[03:51] 还有我们的什么评论的消息列表还有喜欢的这个消息列表公告的消息列表然后在这个位置啊可以去查看什么呢我们的联系人那么在联系人列表中呢可以点击联系人呢进行做一个聊天哎OK好那么下面这个呢就是我们聊天的一个界面啊是不是和我们的微信是不是非常的相像的然后呢可以看到在这个位置是不是可以去写这种一些发一些这个文字的
[04:19] 这个消息还可以去发送什么呢语音的消息还可以发送什么呢发送我们的这个图片的这个消息啊OK那么这个呢基本上就是我们所在我在我们的这个消息这个模块中呢所要完成的一些这个功能啊OK好那么关于我们的这个集资通讯啊以及我们的功能的一个说明那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解即时通讯功能的定义、功能说明及技术方案的初步内容。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“1.1、什么是即时通信？”章节，定义即时通信并列举其功能（如：短信、微信、腾讯、QQ、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Skype、ICQ、Yahoo、AOL、MSN、QQ、微信、微博、网易、阿里、腾讯、微博、微信、QQ、MSN、Sk

