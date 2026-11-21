# 08.前台系统之搭建node.js服务进行测试

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\08.前台系统之搭建node.js服务进行测试【海量资源尽在 ubkz.com】.mp4
- 时长 9分39秒（音频 579s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来搭建啊刚刚我们所提到的这个API这个工程啊那么前面其实我们也说过啊就是我们的这个项目的前端团队啊他们在做开发的时候啊他们并没有采用这种MOOC的这种形式去做一些数据的模拟而是采用了使用这个Node.js他们开发了一个服务端然后呢为这个客户端呢去提供这样的一个服务的一个支撑
[00:25] 然后呢进行那些demo化的开发注意是一个demo化的开发啊它并不能够直接用于我们的一些生产所以呢我们在我们目前我们去做前后端整合开发的时候呢也有必要要把它的API这个工程呢也给它跑起来这样的话呢我们才能够便于我们开发至少你需要去看到它的一些
[00:48] 访问的地址包括一些想要的一些数据结构啊等等啊所以啊我们需要先把它先搭建起来哎OK好那么我们来看一下怎么样搭建呢我们一步一步来做一下啊首先第一步呢我们从我们资料中呢找到这样的一个压缩包然后把它解压到我们对应的这个位置啊我们来找一下找到我们资料中是不是有一个这个压缩包呀然后呢我们把它解压到刚刚的我们的这个位置和我们啊刚刚的这个浩克vib这个项目
[01:17] 一致的一个目录下面咱们去创建一个目录叫做-API然后我们把压缩包里面的一些相关的所有的内容我们把它解压到这个里面来这样做一个这样的一个解压解压到这那么解压完成之后我们就需要
[01:37] 去给他做一些这个配置啊配置由于呢我们现在做的这个呢他本身呢其实是一个服务端啊本身是个服务端他呢还涉及到一个数据库的一个交互啊所以呢我们先需要的是把他的这个数据库呢先给他创建好那么他的数据库呢我们创建一个叫myhome这样的一个数据库然后呢我们再去执行一些这个脚本那么我们先把这个数据库呢创建出来
[02:03] 在我们的这个55185这个下面呢我们去创建一个数据库啊那么在这儿创建一个新建一个数据库名字叫做myhome然后呢我们去找到下面有一个编码是U8然后点击这个确定那myhome这个数据库呢就创建出来了那么创建出来之后呢我们通过我们的资料中呢找到一个社会脚本那么我们来看一下这个社会脚本把这个内容呢我们全部都给他贴过来然后呢我们去
[02:31] 在这个里面的我们去点击这个查询新建的查询把这个内容抠过来抠过来之后啊那么我们就可以去就可以去做一个执行然后呢我们现在呢就把会把一些数据库啊就创建好了包括一些初始化的一些我们这个数据啊就搞定了那大概有这么多张表去支撑我们这个服务啊
[02:54] 好那么现在我们是不是就搞定了那么下面我们来看一下既然它是一个服务对不对所以我们就需要去修改它的配置让它去能够正确的去连接到我们服务数据库的服务埋伤口服务那么它的配置在哪里在这儿在这个位置在这个下面有一个叫configureconfig下面有这么多的配置这么多配置
[03:20] 那么我们修改哪个呢显然是不是应该修改这个config-dev这是我们的开发下面的一个配置那么为什么要修改它呢其实我们可以来看一下在我们的这个packager.json这个文件里面我们来找一下在这个文件中呢我们是不是要去最后把我们这个node.js服务跑起来那么跑起来呢我们需要执行一个命令就是run一个什么呢这个dev是我们的开发环境
[03:49] 我们可以看到他设置全局的一个这个环境变量是不是就是一个config.dev那么其实所对应的呢就是我们的这个啊就是我们刚刚所看到这个配置文件啊所以呢我们现在选择要先修改的是这个config.dev的这个配置文件那我们打开在这个里面的其他的我们先保持默认啊先不管他那么我们主要去需要去做一些修改的内容是不是在这个位置啊是不是db的这个配置
[04:16] 对吧OK这个modules的pass这个我们也不管他然后我们来看一下host这个172.165.85这个是不是我已经修改好我的这样的一个地址OK那么大家需要注意了这个内容就是这一块的这个内容这一块的内容这一块的内容是不是需要根据你自己的一些这个数据库的一个环境去做一些这个修改
[04:41] 那么这个是端口然后这个是host这个是端口然后type就是我们mysearch数据库用户名是root密码也是root数据库就是myhome跟我们这个数据跟我们这个信息要保持完全的一致ok那么现在我们这个配置就搞定了那么搞定之后我们就需要把这个服务跑起来那么这个服务怎么跑我们来看一下
[05:06] 在这个下面我们点击这个右键打开我们的一个命令行那个窗口那么我们依然是需要先通过这个NPM做一个install把一些相关的一些依赖包我们先下载下来然后我们再做一些启动所以我们先执行这个installok那么我现在把这个视频先暂停一下等待它的一个下载好那么现在相关的一些依赖都已经下载下来了
[05:32] 那么下载下来之后我们就需要把我们的一个服务跑起来服务怎么跑其实我们刚刚也说过在 package 下面是不是有一个 dv然后去运行我们 node运行我们 node 的一个服务然后我们在这个位置来一个命令就叫 npm什么的 run注意是 run 不是 start因为 start 我们并没有去写run 谁 run 一个 dv就对了注意 dv 所对的就是我们就他对就他ok
[06:01] 然后我们把它去做一个运行那么运行之后我们现在就已经运行了我们的一个node.js的一个服务就相当于是一个后端的一个服务那么接下来我们来看一下测试一下它的一个登录它的一个登录那么是否能够登录成功呢我们就需要去找一下我们的用户然后我们可以看到在us的表下面有这样的一些用户那么可以看到是不是用户名是不是 Tom
[06:30] 然后密码是123我们尝试的来输入一下这个Tom密码123我们点击这个登录看他是否能够登录成功的走那么我们可以看到现在是不是已经有登录成功了对吧登录成功了那么登录成功之后我们就看到我们的这个首页首页那么这个是我们的首页那么打开了这个图片现在展示还没有图片还没有图片那么我们可以看到它下面的一些内容还是把这个百分比缩小一下可以看到下面的内容
[06:59] 那么我们可以通过我们鼠标的滚轮是不是往下面去滚这个是不是相当于我们去操作我们的手机上面的一种操作对吧轮波图可以把它拖住这样左右是不是相当于我们手在屏幕手机上面屏幕是手在滑动的这样的一个效果ok这样的一个效果你可以看到这样的效果
[07:20] 然后下面还有一些我们的一些问答的数据还有一些楼盘的数据二手房的数据租房的一些数据等等然后下面这个位置是我们的一些菜单是我们的菜单我们可以看到有什么有资讯有微聊有我的个人中心等等一些相关的内容那么下面还有一些搜索OK这个就是我们前端所实现的这样的一个效果
[07:48] 好嘞那么我们到目前为止呢我们是不是已经把它的服务端跟它的前端的都已经搭建起来了哎呀OK好那么我们来看一下这个讲义啊讲义那么在我们的讲义中呢跟我们刚刚讲的呢是基本上是一样的啊那么我们修改配置文件呢就是这个配置文件然后呢把这个config呢这里面内容呢做一些这个修改然后呢我们在这呢强调一下啊所运行的这个dev呢其实就是在我们的package那个配置文件中是不是所
[08:18] 定义的是他呀哎OK这个就是我们的一个开发环境啊大家的同学说老师这个test和这个pro这两个我们现在要不要去修改它其实没有必要为什么呢大家想一想啊那么我到目前他已经到我们后端开发因为我们后端对不对到后端开发的这个阶段了我们就没有必要在我们的生产环境或者说我们的测试环境再去部署这样的一个服务来支撑
[08:44] 而应该是我们的后端为他提供这样的一个服务做一个支撑OK大家这个能够理解了吗那么其实这个node.js所提供这个服务仅仅用于什么呢用于前端团队在开发这个前端这个项目的时候做一个使用OK好嘞好那么这个呢我们就搞定了那么接下来呢我们是不是根据他的一个这个用户名和密码是不是做一个登录对吧做一个登录那么我们就可以发现啊可以是登录成功了
[09:13] 登录成功之后成功的是不是看到我们首页了ok好那么到这里我们首页就看到了或者说我们项目就搭建完成了就真正的搭建完成了可以看到这样的效果那么接下来后面我们是不是就需要基于我们现在搭建好的项目我们来开发它的功能对不对好那么关于我们的服务的一个启动那么我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何搭建一个基于 Node.js 的 API 服务端工程，包括解压资料、创建数据库、配置文件、安装依赖、启动服务并验证前端页面。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档“讲义.pdf”第15页，内容为“2.2、搭建api工程”，说明前端团队采用 node.js 开发服务端进行 demo 开发，第一步是将资料中的 haoke-web-api.zip 解压到项目目录。
画面2：展示 Windows 资源管理器，路径为“研发 > 好客程序 > day06”，显示了“haoke-web.zip”、“haoke-web-api.zip”和“myhome.sql”三个文件。
画面3：展示 PDF 文档“讲义.pdf”第16页，内容为“第二步，创建数据库”，要求创建 myhome 数据库并执行 myhome.sql 脚本，同时显示了数据库表结构（answers, chatinfos, homelings, homes, informations, map, menus, questions, swipes, users）。
画面4：展示 Navicat Premium 数据库管理工具，正在执行 SQL 脚本，内容包括：
INSERT INTO swipes VALUES ('1', 'public/1.png', 'pic-thumb2.png', null);
INSERT INTO swipes VALUES ('2', 'public/2.png', 'pic-thumb2.png', null);
INSERT INTO swipes VALUES ('3', 'public/3.png', 'pic-thumb2.png', null);
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  id int(11) NOT NULL AUTO_INCREMENT,
  username varchar(85) COLLATE utf8_bin DEFAULT NULL,
  password varchar(255) COLLATE utf8_bin DEFAULT NULL,
  mobile varchar(255) COLLATE utf8_bin DEFAULT NULL,
  address varchar(1051) COLLATE utf8_bin DEFAULT NULL,
  `status` int(11) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
INSERT INTO answers VALUES (1, '1天', 2, null, 11);
画面5：展示 Windows 资源管理器，路径为“研发 > 好客程序 > day06”，显示了“haoke-web.zip”、“haoke-web-api.zip”和“myhome.sql”三个文件。
画面6：展示 EditPlus 编辑器，打开并显示了“package.json”文件内容：
{
  "name": "myapi",
  "version": "1.0.0",
  "description": "",
  "main": "Index.js",
  "scripts": {
    "test": "cross-env NODE_ENV=config-test node app.js",
    "dev": "cross-env NODE_ENV=config-dev node app.js",
    "pro": "cross-env NODE_ENV=config-pro node app.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "busboy": "0.2.14",
    "is-extra": "6.0.0",
    "joi": "13.2.0",
    "jsonwebtoken": "8.2.1",
    "koa": "2.5.0",
    "koa-bodyparser": "4.2.0",
    "koa-jwt": "3.3.1",
    "koa-logger": "3.2.0",
    "koa-mount": "3.0.0",
    "koa-multer": "1.0.2",
    "koa-router": "7.4.0",
    "koa-static": "4.0.5",
    "koa2-cors": "2.0.5",
    "mysql": "2.16.0"
  }
}
画面7：展示 Windows 命令提示符窗口，执行了“npm install”命令，输出了安装依赖包的信息。
画面8：展示 EditPlus 编辑器，显示“package.json”文件，同时命令提示符窗口中执行了“npm run dev”命令。
画面9：展示 Chrome 浏览器，访问本地地址“localhost:9000/home”，显示了 React 应用的首页，包含“Carousel”组件和多个圆形图标。
画面10：展示 Chrome 浏览器，访问本地地址“localhost:9000/home”，显示了房屋列表页面，包含多个房屋信息卡片。
画面11：展示 Chrome 浏览器，访问本地地址“localhost:9000/home”，显示了加载中页面，中间有“Loading”文字和旋转图标。
画面12：展示 PDF 文档“讲义.pdf”第17页，内容为“npm install #安装依赖”、“npm run dev #启动dev脚本”，并附有“scripts”配置说明。
画面13：展示 PDF 文档“讲义.pdf”第17页，内容为“第四步，输入命令进行初始化和启动服务”，并附有“npm install #安装依赖”、“npm run dev #启动dev脚本”和“scripts”配置说明。
画面14：展示 PDF 文档“讲义.pdf”第17页，内容为“第四步，输入命令进行初始化和启动服务”，并附有“npm install #安装依赖”、“npm run dev #启动dev脚本”和“scripts”配置说明，同时显示了前端页面的截图，包含“二手房”、“新房”、“租房”、“海外”、“地图找房”、“看交”、“计算器”、“问答”等按钮，以及“好客问答”模块。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4 SQL：
INSERT INTO swipes VALUES ('1', 'public/1.png', 'pic-thumb2.png', null);
INSERT INTO swipes VALUES ('2', 'public/2.png', 'pic-thumb2.png', null);
INSERT INTO swipes VALUES ('3', 'public/3.png', 'pic-thumb2.png', null);
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  id int(11) NOT NULL AUTO_INCREMENT,
  username varchar(85) COLLATE utf8_bin DEFAULT NULL,
  password varchar(255) COLLATE utf8_bin DEFAULT NULL,
  mobile varchar(255) COLLATE utf8_bin DEFAULT NULL,
  address varchar(1051) COLLATE utf8_bin DEFAULT NULL,
  `status` int(11) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
INSERT INTO answers VALUES (1, '1天', 2, null, 11);

画面6 package.json：
{
  "name": "myapi",
  "version": "1.0.0",
  "description": "",
  "main": "Index.js",
  "scripts": {
    "test": "cross-env NODE_ENV=config-test node app.js",
    "dev": "cross-env NODE_ENV=config-dev node app.js",
    "pro": "cross-env NODE_ENV=config-pro node app.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "busboy": "0.2.14",
    "is-extra": "6.0.0",
    "joi": "13.2.0",
    "jsonwebtoken": "8.2.1",
    "koa": "2.5.0",
    "koa-bodyparser": "4.2.0",
    "koa-jwt": "3.3.1",
    "koa-logger": "3.2.0",
    "koa-mount": "3.0.0",
    "koa-multer": "1.0.2",
    "koa-router": "7.4.0",
    "koa-static": "4.0.5",
    "koa2-cors": "2.0.5",
    "mysql": "2.16.0"
  }
}

画面7 命令：
npm install
npm mysql@1.0.8 No description
npm mysql@1.0.8 No repository field.
added 413 packages from 397 contributors in 22.854s

画面8 命令：
npm run dev
cross-env NODE_ENV=config-dev node app.js

画面12、13、14 文本：
npm install #安装依赖
npm run dev #启动dev脚本
#脚本如下：
"test": "cross-env NODE_ENV=config-test node app.js", #设置环境变量
"dev": "cross-env NODE_ENV=config-dev node app.js", #设置环境变量
"pro": "cross-env NODE_ENV=config-pro node app.js", #设置环境变量

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1 标题：2.2、搭建api工程
画面3 标题：第二步，创建数据库
画面12、13、14 标题：第四步，输入命令进行初始化和启动服务
画面12、13、14 文本内容：npm install #

