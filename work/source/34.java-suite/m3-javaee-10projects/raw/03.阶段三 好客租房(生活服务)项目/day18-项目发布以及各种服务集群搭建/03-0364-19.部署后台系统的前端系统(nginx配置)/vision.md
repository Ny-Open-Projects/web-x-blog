# 画面线理解：19.部署后台系统的前端系统（nginx配置）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\19.部署后台系统的前端系统（nginx配置）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:36, 00:58, 01:23, 01:49, 02:00, 02:23, 03:09, 03:44, 04:15, 05:44, 06:07, 06:19, 06:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:59:24

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
#安装nginx
apt install libpcre3 libpcre3-dev zlib1bg-dev openssl libssl-dev
./configure
make install
#安装
cd /usr/local/nginx/sbin/
./nginx
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
画面1: PPT 标题为“3.3. itcast-haoke-manage-web系统的nginx配置”，内容为 Nginx 配置说明。
画面4: Nginx 配置文件结构，包含 server 块和 location 块。
画面6: Nginx 配置文件结构，包含 server 块和 location 块。
画面7: Nginx 配置文件结构，包含 server 块和 location 块。
画面8: 前端项目配置文件 config.js，包含 lessLoaderOptions 和 modules 配置
