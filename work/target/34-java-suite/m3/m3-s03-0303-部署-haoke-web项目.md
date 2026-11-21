---
title: "haoke-web 前台系统上线：改地址、跑 Node 服务、静态站交给 Nginx"
date: 2026-11-18
categories: [Java后端进阶全套, M3 十大中级项目, 阶段三 好客租房(生活服务)项目]
tags: [Java, 项目实战]
---

# haoke-web 前台系统上线：改地址、跑 Node 服务、静态站交给 Nginx

后台 manage-web 已经在 18 这台机器上跑通，前台 haoke-web 还停在开发机里。它是标准的前后端分离 React 工程：本地 `npm start` 一切正常，源码直接搬上服务器却跑不起来；就算勉强构建出页面，接口请求和 WebSocket 也全是死路。症结集中在两处：代码里写死的 `127.0.0.1`，以及只在开发机上有意义的 Node 开发服务。

这一课把前台系统的发布走完：先在服务器上把前端自带的接口服务跑起来，再把散落各处的硬编码地址全部替换，`npm run build` 构建出静态页面，最后在 Nginx 里新增一个 server 块托管，浏览器按域名访问验证。

## 先给结论

- 前台的发布物是 `npm run build` 产出的静态文件，Nginx 托管即可，线上页面不依赖 Node 进程撑着。
- 发布前两件事缺一不可：在服务器上跑起前端自带的 Node 接口服务，承接那批尚未实现的后端接口；把代码里的硬编码地址全部替换。
- 三类地址各有去处：`127.0.0.1` 换成真实服务器 `192.168.1.7`；`18080` 的接口换成 `api.manage.haoke.com`；`18081` 的 WebSocket 换成 `im.haoke.com`。
- 改完先本地 `npm run start` 自测，确认链路通了再构建；产物是 `build` 目录，上传解压重命名后交给 Nginx。
- `www.haoke.com` 是虚拟域名，本机 hosts 指向 18，`nginx -s reload` 生效后按域名访问验证。

## 一、前台与后台，部署差在哪

后台 manage-web 用 umi 构建，前台 haoke-web 是 create-react-app 体系的 React 工程，目录结构一眼可辨：`public` 放模板，`src` 放源码，`node_modules` 是依赖，构建产物落在 `build` 目录。两套工程的部署思路完全一致：构建出静态页面，发布到服务器，Nginx 托管。

差异也有两处，都决定了这一课不能照搬后台的流程：

**第一，前台有一批接口的后端还没实现。** 开发期靠工程自带的 Node 接口服务顶着，页面里 `/mock/infos/list`、`/mock/my/info` 这类请求就落在它上面。上线时这个 Node 服务也得跟着部署到服务器，否则对应功能直接挂掉。

**第二，地址写死得更散。** 后台的地址集中在 `config.js` 一处，前台除了集中配置，`home.js`、`find.js`、`my.js` 这些组件文件里还一个个写着 axios 请求的完整 URL，漏改一处就是一个白屏或报错。

## 二、先把 Node.js 接口服务在服务器上跑起来

这个 Node 服务在开发期通过 `npm run dev` 启动，部署它同样走「打包、上传、解压、启动」四步。前提是服务器上装好 Node.js 环境，资料包里带了安装包，解压后配好环境变量即可。服务所在模块按业务命名为 `haoke-web-api`，把它打成 zip 包上传到 1.7 的 `/haoke/publish/haoke` 目录：

```bash
cd /haoke/publish/haoke
unzip haoke-web-api.zip
cd haoke-web-api
npm run dev
```

启动当场报错。原因在启动脚本：`package.json` 里 dev 脚本用 cross-env 设置环境变量再启动，这套写法是按 Windows 环境配的，放到 Linux 服务器上直接失败。处理办法是把这个 dev 脚本删掉，改成本机可用的启动命令，服务随即正常跑起来。跑起来后页面里那些 mock 接口就有着落了，这一步完成的是「第二件事」里的服务器侧准备。

## 三、替换硬编码地址：全局搜 127.0.0.1

地址替换从集中配置开始。前台工程的 `src/commonjs/config.js` 定义了三个基础地址，改造后如下：

```javascript
export default {
  // imgBaseUrl: 'http://47.96.21.88:8086/',
  // apiBaseUrl: 'http://47.96.21.88:8086/',
  // wsBaseUrl: 'ws://47.96.21.88:8087';
  imgBaseUrl: 'http://192.168.1.7:8086/',
  apiBaseUrl: 'http://192.168.1.7:8086/',
  wsBaseUrl: 'ws://im.haoke.com/ws'
}
```

`wsBaseUrl` 指向 `im.haoke.com`，这个域名在之前配置 Nginx 反向代理 WebSocket 时已经就位，端口也不再写 18081，走 80 由 Nginx 转发。

集中配置之外，用 IDE 的全局搜索把 `127.0.0.1` 揪出来逐个处理，命中点分布在 `home.js`、`find.js`、`my.js` 等组件里，分两类改法：

```javascript
// home.js：写死 18080 的接口，换成后台接口域名
axios.get('http://api.manage.haoke.com/ad/');

// find.js：房源列表，落在 Node 接口服务的 mock 路径上
axios.get('http://api.manage.haoke.com/mock/infos/list?type=1');

// my.js：当前用户信息，带上本地存储的用户 id
axios.get('http://api.manage.haoke.com/mock/my/info', {
  user_id: localStorage.getItem('uid')
}).then((res) => {
  this.setState({
    avatar: res.data.avatar,
    openAvatar: true
  });
});
```

替换规则只有两条：写 `18080` 的真实接口，全部换成 `api.manage.haoke.com`，这个域名指向 1.7 上的 api-server，早已由 Nginx 配好；写 `18081` 的用户查询、微聊相关请求，全部换成 `im.haoke.com`。替换完再全局搜一遍 `127.0.0.1`，确认归零才算改干净，这一步靠的就是耐心，没有捷径。

## 四、构建、本地自测，再打包上传

`package.json` 的 scripts 里现成有 build 脚本，构建就是一条命令：

```bash
npm run build   # 产物输出到 build 目录
npm run start   # 本地把改造后的工程跑起来自测
```

构建完成，`build` 目录里就是要发布的全部静态文件。上传之前先在本地把改造后的工程跑一遍：登录用户 tom、密码 123，提交后请求打到 1.7 上刚跑起来的 Node 服务，登录成功，首页轮播与房源数据都能查到。数据能回来，说明改造后的地址链路是通的，这一步自测值回票价，很多地址替换的遗漏都是在这里暴露的。

确认无误，把 `build` 目录打成 zip，上传到 18 这台机器（manage-web 的静态站也在这上面，前端产物统一放一起）：

```bash
cd /haoke/publish
mkdir haoke-web
# 上传 build.zip 后解压，得到 build 目录
unzip build.zip -d haoke-web
cd haoke-web
mv build/* .     # 把产物平铺到发布目录，或直接把 build 重命名为最终目录名
```

发布目录里是一堆带 hash 的静态文件，结构与 create-react-app 的产物一致：

```text
/haoke/publish/haoke-web
├── index.html            # 唯一入口
├── asset-manifest.json   # 产物清单
├── manifest.json
├── service-worker.js
├── favicon.ico
└── static/               # 带 hash 的 js 与 css
```

## 五、Nginx 新增 server 块与域名验证

进到 `/usr/local/nginx/conf/` 打开 `nginx.conf`，在文件末尾新增 server 块。做法是拷贝 manage.haoke.com 那段配置作模板，改三处：`server_name` 换成 `www.haoke.com`，删掉原来的接口代理段，`root` 指向前台发布目录：

```nginx
server {
    listen       80;
    server_name  www.haoke.com;

    access_log logs/host.access.log main;

    location / {
        root /haoke/publish/haoke-web;
    }
}
```

比后台那份配置简单得多：前台页面自己不发带 `/haoke` 前缀的接口请求，接口走 `api.manage.haoke.com`、WebSocket 走 `im.haoke.com`，各自早有 server 块处理，前台这一块只干一件事，把请求按静态文件应答。

进入 `sbin` 目录热加载，再给开发机配上 hosts 映射：

```bash
cd /usr/local/nginx/sbin/
./nginx -s reload
```

```text
192.168.1.18 www.haoke.com
```

浏览器访问 `www.haoke.com`，页面出来了，样式与本地一致。登录 tom、123，登录成功，首页数据、房源详情都能拿到，与本地开发环境的表现完全相同。到这里前台系统上线完成，整个项目的部署也画上了句号。

整条发布链路串起来看：

```mermaid
flowchart LR
    A["替换硬编码地址"] --> B["npm run build"]
    B --> C["build 静态产物"]
    C --> D["打包 zip 上传 18"]
    D --> E["解压平铺到 /haoke/publish/haoke-web"]
    E --> F["Nginx 新增 server 块 root 指向"]
    F --> G["nginx -s reload"]
    G --> H["本机 hosts 指向 18"]
    H --> I["浏览器访问 www.haoke.com 验证"]
```

图里最容易被省略的是最左边的「替换地址」和最右边的「hosts 验证」，一头一尾都不产生可见的中间产物，却分别决定了构建出来的页面能不能用、以及最后能不能访问到。

## 常见误区

- **拿 `npm run dev` 当部署。** dev 起的是开发服务器，带热更新与 mock 能力，性能与稳定性都不适合线上；线上要的是 build 产物加 Nginx 托管，Node 服务只保留给那批未实现的 mock 接口。
- **只改 `config.js`，漏掉组件里散落的地址。** 集中配置只是地址的一部分，`home.js`、`find.js`、`my.js` 里各写死了完整 URL，全局搜索加复搜归零是唯一保险的做法。
- **Windows 的启动脚本原样搬上 Linux。** cross-env 设置环境变量再启动的脚本写法跨不过系统差异，直接报错；部署脚本要按目标系统写。
- **hosts 忘了配或指错机器。** `www.haoke.com` 是虚拟域名，必须指向 Nginx 所在的 18，指到 1.7 页面根本打不开；hosts 不生效时浏览器按真实 DNS 解析。
- **产物多包了一层目录。** `root` 指到 build 的外层目录，请求 `/` 落不到 `index.html`，整站 404，检查发布目录层级永远是第一步。

## 面试可能被问到的问题

1. 面试官追问：「前后端分离的项目，前端发布为什么只发静态文件？」
   答：构建工具把源码编译、打包、压缩成浏览器可直接消费的静态资源，运行期不再需要编译环境。Nginx 托管静态文件足以承载高并发，Node 只在开发期承担本地服务与代理，生产环境由 Nginx 反向代理替代它的职责。
2. 面试官追问：「工程里为什么要留一个 Node 接口服务？」
   答：开发期一部分后端接口还没实现，Node 服务按约定路径返回 mock 数据，保证前端可以独立开发联调；它也常兼任开发代理，把跨域请求转发到真实后端。上线后这些路径要么由真实接口接管，要么把这个服务部署到服务器继续承接。
3. 面试官追问：「构建产物文件名里带 hash 有什么用？」
   答：内容变则 hash 变，文件名天然做版本隔离。静态资源可以设置很长的缓存有效期而不怕用户拿到旧版本，更新时入口 `index.html` 不缓存、其余文件长缓存，是静态站缓存策略的标准做法。
4. 面试官追问：「多个域名解析到同一台 Nginx，怎么区分不同站点？」
   答：靠 server_name 的虚拟主机机制。Nginx 收到请求后按请求头里的 Host 字段匹配 server 块，`www.haoke.com`、`manage.haoke.com`、`im.haoke.com` 各自的配置互不干扰，一台机器一个 80 端口就能承载多个站点。
5. 面试官追问：「上线后页面能打开但数据全拿不到，你怎么排查？」
   答：先看浏览器控制台 Network 面板确认失败请求的域名与路径，常见原因是地址替换遗漏或代理前缀问题；再查 Nginx 的 access 与 error 日志确认请求有没有到达、转发给了谁；最后核对 hosts 与 DNS 解析是否指向了正确的接入机器。层层往里定位，不要一上来就重启服务。

## 配套资料

- 本教学日无源码包：`materials/code/03/day18-项目发布以及各种服务集群搭建/` 下仅有解压清单 `_extracted.json` 与房源抓取测试数据 `data.json`（位于 `day18-项目发布以及各种服务集群搭建 - 副本/资料/data.json`）。
- `config.js`、组件请求地址、发布目录结构与产物清单抄录自本课画面线；Node 接口服务的启动脚本细节与 `mv` 整理命令为按本课写法补全的示例。
- 关联篇目：后台前端构建见 `0298-通过umi构建-haoke-manage-web系统.md`，manage-web 的 server 配置见 `0300-部署后台系统的前端系统(nginx配置).md`，`api.manage.haoke.com` 域名见 `0301-配置api.manage.haoke.com进行访问.md`，WebSocket 反代见 `0302-nginx反向代理websocket.md`。
