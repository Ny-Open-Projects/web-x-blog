# 19.部署后台系统的前端系统（nginx配置）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\19.部署后台系统的前端系统（nginx配置）【海量资源尽在 ubkz.com】.mp4
- 时长 6分41秒（音频 401s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续那么前面呢我们已经把NJAX呢是不是有安装好了对吧那么接下来呢我们就需要把我们刚刚呢去就是打包构建之后的一个静态页面呢去发布到我们的一个这个我们的服务器上面然后去做一个访问那么发布的路径呢我们把它放到我们这个叫Hawker下面有个publish然后下面呢有一个manage web那么把它发到这个下面来那么我这边刷新一下
[00:30] 这边刷新一下它应该是没有任何内容的那么我们进入这个manage web然后呢我们会把我们的一些这个就是我们刚刚啊打包之后的一些静态页面呢我们去找到然后呢去做一个发布这个下面有一个dist那有这么多然后呢把它拖到这个里面来那么第一步呢我们就即将完成就是把我们的这个静态页面啊去发布到我们的这个生产环境好
[00:57] 这样的话呢就有了静态页面了这个里面呢有一个比较关键的一个内容呢就是index.html那么重点我们访问他就可以了好那么这是第一个第一个这个问题解决了那么第二个问题呢就是我们需要来配置ngx的一个配置文件那么我们来看一下ngx配置文件呢它其实是在这个里面对吧那么我们需要给它设置什么呢设置一个这个server它默认的是这样的一个server对吧那么默认它去访问的是
[01:27] root指向的是我们html这个页面那么其实我们现在不需要它指定这个页面那我们需要它指定的是我们刚刚所上传的这个目录其实也就是这个目录那我们来看一下它应该怎么去做呢我们把这个server就全部都给它删除掉然后我们自己去添加一个那么要注意的是接下来我们来看一下我们的讲义那在讲义中给大家去写好的这样的一个配置那我们来看一下这个中的配置我们就先直接拷贝过来
[01:56] 然后呢我们再来看一下这个里面的一些这个内容那么我们把它丢到这OK那么这个呢其实就是我们的一个配置啊就是我们的配置server的一个配置那么看一下啊是不是少了一个少了一个S啊少了一个S啊加一个Sserver那么检查一下看有没有问题啊那么这个里面它应该是有S的啊server好那么这个server呢下面呢我们可以看到它所监听的端口呢是80端口
[02:25] 然后我们sername是我们去指向的一个域名要么要注意这个域名其实是一个虚拟的域名那么我们想要通过域名去访问还需要在我们本地通过一个host去做一个配合所以我在这个位置去指定了我本地的host是通过managerhawk.com去指向到我这台机器就是18那么其实就是我所发布的这台机器就它OK
[02:49] 然后呢继续往下面看那么下面我其实写了两个规则就是如果我们去请求的是以我们的好客这个开头的话那么我们将要去把我们这个请求代理到我们的一个我们的后台的服务这个呢其实所实现的效果呢就是我们之前呢在convex中所配置的一个代理找一下是在这个位置啊配置这个代理这个大家应该还记得啊我们配置这样的代理就是
[03:17] 我们所请求的是他的话那么就会去代理到这个位置来而我们现在已经把它发布到生产环境是不能够使用这个污名所提供的代理这种功能那么我们需要通过NGX来完成那么首先需要注意的是那么我们这个地址呢是比如说我们来举个例子那么我们去访问我们地址呢我们通过比如说我们通过这个叫做什么呢就是比如说叫19268
[03:47] 然后呢我们随便写一个啊然后呢他呢其实其实是要通过什么呢通过这个号客然后呢下面呢再去做一个访问大家注意那么访问地址中其实多了一个号客但是呢我们如果做代理的话把后面这个地址传递给我们真正的我们这个后台服务的话那么显然他是不对的因为
[04:09] 我们后台服务中是没有这个浩克这个地址的啊那么就是这个地址那么我们为什么要去加这个浩克这个地址呢原因是在我们的这个系统中呢我们为了去区分我们是请求我们自己的还是我们去请求我们后台的一个服务所以说呢我们添加了浩克这个地址那么我们想要去解决这个问题呢非常简单那么只需要注意只需要在我们的这个代理的地址的最后面啊
[04:36] 添加一个斜杠注意这个斜杠非常非常关键那么有了这个斜杠之后呢他就会去拿到我们这个浩克下面后面的内容注意也不是说这个括号是他后面请求内容去添加到这个后面来那么如果没有这个斜杠呢他就会拿到我们这个浩克包含这个浩克这个路径然后呢去给他写到这个位置来那么要注意的是这个斜杠非常非常的关键OK
[05:04] 好那么如果不是以这个浩克这个目录开头的话那么我们就请求到这个地址来ok就是这样的一个配置啊然后呢我们进入了这个sbin这个目录然后呢执行一个ngx-s reload那么这样的话呢我们就可以来查看一下那么我们就可以通过什么呢由于我本地的这个虚拟域名呢做了一个映射那我就可以通过这个manager然后呢这个浩克.com去做一个访问
[05:34] 那么会发现呢这个呢是我们去请求这个current user这个我们并没有去实现啊那我们可以来点击一下这个房源管理中的一个房源管理来看一下那么你会发现呢这个房源管理可以正常去查询数据了要注意的是这个数据它的来源呢其实是我们的这个1.7上面的18080这个端口的服务由于刚刚我们在agents这个位置去做了一个这样的一个带领
[06:01] 那么他就能够去请求到我们的数据啊这个一点一定要注意啊那么由于我们能看到这个页面呢其实是他是通过下面的这个呢去看到我们这个页面的啊这个一定要注意一下好那么我们可以看一下功能啊基本上应该是ok的跟我们在做开发测试的时候是一样的没有任何问题哎ok好那么大概可以看一下啊没有问题然后呢也可以去新增房源也是没有任何问题的哎ok好嘞那么其实到目前为止呢我们就已经
[06:31] 把我们后台系统的一个前台系统呢就已经跑起来了哎呦ok好那么这样的话呢我们通过这个ngx的配置那么就跑起来了好嘞

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何配置 Nginx 代理，使前端项目（itcast-haoke-manage-web）能通过域名 manage.haoke.com 访问，并展示其功能页面。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 Typora 文档中关于 Nginx 配置的说明，以及 Nginx 安装命令和配置文件路径。
画面2: 在远程服务器终端中，进入 manage-web 项目目录。
画面3: 在终端中列出 manage-web 项目目录下的文件，显示了多个 .js、.css 文件和 manifest.json。
画面4: 在终端中编辑 Nginx 配置文件，配置了 server 块和 location 块，用于静态资源服务。
画面5: 浏览器访问 manage.haoke.com/haoke/，显示 Google 搜索首页，表明域名未正确解析或代理未生效。
画面6: 在终端中编辑 Nginx 配置文件，配置了 proxy_pass 指向后端服务 192.168.1.7:18080。
画面7: 在终端中编辑 Nginx 配置文件，修改 listen 端口为 80。
画面8: 在 IntelliJ IDEA 中查看前端项目配置文件 config.js，其中包含 lessLoaderOptions 和 modules 配置。
画面9: 浏览器访问 manage.haoke.com/haoke/，显示 Google 搜索首页。
画面10: 浏览器地址栏输入 manage.haoke.com/house/resources，准备访问资源。
画面11: 浏览器访问 manage.haoke.com/house/resource，显示“房源管理”页面，包含搜索和操作按钮。
画面12: 浏览器访问 manage.haoke.com/house/resource，显示房源列表数据，包含房源编号、标题、面积等信息。
画面13: 浏览器访问 manage.haoke.com/house/resource，弹出一个红色的加载框，提示“正在加载...”。
画面14: 展示 Typora 文档中关于 Nginx 配置的说明，与画面1相同。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```
#安装Nginx
apt install libpcre3 libpcre3-dev zlib1bg-dev openssl libssl-dev
./configure
make install
#安装
cd /usr/local/Nginx/sbin/
./Nginx
```

画面2:
```
root@itcast02:publish# pwd
root@itcast02:publish# ll
total 12
drwxr-xr-x 3 root root 4096 Feb 28 23:48 ./
drwxr-xr-x 8 root root 4096 Mar 1 00:09 manage-web/
root@itcast02:publish# cd manage-web/
root@itcast02:manage-web# 
```

画面3:
```
-rw-rw-r-- 1 root root 51  Mar 1 00:11 1.chunk.css
-rw-rw-r-- 1 root root 5895 Mar 1 00:11 2.chunk.css
-rw-rw-r-- 1 root root 1862 Mar 1 00:11 3.chunk.css
-rw-rw-r-- 1 root root 1899 Mar 1 00:11 4.chunk.css
-rw-rw-r-- 1 root root 2849 Mar 1 00:11 5.chunk.css
-rw-rw-r-- 1 root root 1613 Mar 1 00:11 55.async.css
-rw-rw-r-- 1 root root 3114 Mar 1 00:11 57.async.css
-rw-rw-r-- 1 root root 2455 Mar 1 00:11 58.async.css
-rw-rw-r-- 1 root root 3095 Mar 1 00:11 59.async.css
-rw-rw-r-- 1 root root 1167 Mar 1 00:11 6.chunk.css
-rw-rw-r-- 1 root root 2154 Mar 1 00:11 60.async.js
-rw-rw-r-- 1 root root 1728 Mar 1 00:11 61.async.js
-rw-rw-r-- 1 root root 457 Mar 1 00:11 62.async.js
-rw-rw-r-- 1 root root 777 Mar 1 00:11 63.async.js
-rw-rw-r-- 1 root root 676 Mar 1 00:11 64.async.js
-rw-rw-r-- 1 root root 654 Mar 1 00:11 65.async.js
-rw-rw-r-- 1 root root 2916 Mar 1 00:11 66.async.js
-rw-rw-r-- 1 root root 266819 Mar 1 00:11 asset-manifest.json
-rw-rw-r-- 1 root root 1159 Mar 1 00:11 color.less
-rw-rw-r-- 1 root root 631 Mar 1 00:11 index.html
-rw-rw-r-- 1 root root 58141 Mar 1 00:11 index.css
-rw-rw-r-- 1 root root 1251050 Mar 1 00:11 umi.js
```

画面4:
```
#zip on;
server {
    listen 80;
    server_name localhost;
    #charset koi8-r;
    #access_log logs/host.access.log main;
    location / {
        root html;
        index index.html index.htm;
    }
    #error_page 404  /404.html;
    # redirect server error pages to the static page /50x.html
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root html;
    }
}
```

画面6:
```
server {
    listen 80;
    server_name manage.haoke.com;
    #charset koi8-r;
    #access_log logs/host.access.log main;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Server $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    location ~ ^/haoke/ {
        proxy_pass http://192.168.1.7:18080/;
        proxy_connect_timeout 600;
        proxy_read_timeout 600;
    }
    location / {
        root /haoke/publish/manage-web;
    }
}
```

画面7:
```
#keepalive_timeout 0;
keepalive_timeout 65;
#gzip on;
server {
    listen 80;
    server_name manage.haoke.com;
    #charset koi8-r;
    #access_log logs/host.access.log main;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Server $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    location ~ ^/haoke/ {
        proxy_pass http://192.168.1.7:18080/;
        proxy_connect_timeout 600;
        proxy_read_timeout 600;
    }
}
```

画面8:
```
ignoreMomentLocale: true,
lessLoaderOptions: {
    javascriptEnabled: true,
},
disableRedirectHoist: true,
cssLoaderOptions: {
    modules: true,
    getLocalIdent: (context, localIdentName, localName) => {
        if (context.resourcePath.includes('node_modules') ||
            context.resourcePath.includes('ant_design.pro.less') ||
            context.resourcePath.includes('global_less')) {
            return localName;
        }
        const match = context.resourcePath.match(/src(.*)/);
        if (match && match[1]) {
            const antdProPath = match[1].replace('.less', '');
            return `${antdProPath}-${localName}`;
        }
        return localName;
    }
},
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1: PPT 标题为“3.3. itcast-haoke-manage-web系统的Nginx配置”，内容为 Nginx 配置说明。
画面4: Nginx 配置文件结构，包含 server 块和 location 块。
画面6: Nginx 配置文件结构，包含 server 块和 location 块。
画面7: Nginx 配置文件结构，包含 server 块和 location 块。
画面8: 前端项目配置文件 config.js，包含 lessLoaderOptions 和 modules 配置

