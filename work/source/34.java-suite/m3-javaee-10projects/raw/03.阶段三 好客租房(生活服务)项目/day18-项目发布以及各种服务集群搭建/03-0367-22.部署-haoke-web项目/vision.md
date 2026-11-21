# 画面线理解：22.部署-haoke-web项目

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\22.部署itcast-haoke-web项目【海量资源尽在 ubkz.com】.mp4
- 抽帧：13 帧 @ 00:03, 02:15, 03:19, 04:33, 05:12, 06:27, 07:03, 08:41, 09:14, 10:25, 11:22, 12:33, 13:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:01:24

1) 这一组画面整体在讲什么（一句话）：
演示一个前端项目（itcast-haoke-web）的开发、构建与部署流程，包括配置文件修改、代码搜索、构建产物查看及最终在浏览器中运行效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在 IntelliJ IDEA 中，展示 `src/commonjs/config.js` 文件内容，其中定义了多个基础 URL，包括 `imgBaseUrl`、`apiBaseUrl`、`wsBaseUrl`，并注释了公网 IP 和内网 IP 地址。
画面2：在 Xshell 终端中，显示了当前工作目录为 `/haoke/publish/haoke`，并展示了本地文件夹结构，包含 `itcast-haoke` 和 `下` 文件夹。
画面3：在 IntelliJ IDEA 中，高亮显示 `config.js` 文件中 `imgBaseUrl` 和 `apiBaseUrl` 的内网 IP 地址配置。
画面4：在 IntelliJ IDEA 中，展示 `home.js` 文件中 `axios.get` 请求的 URL，其中包含内网 IP `127.0.0.1:18080`。
画面5：在 IntelliJ IDEA 中，使用“查找”功能搜索 `127.0.0.1`，结果显示在 `home.js` 文件中，`axios.get` 请求的 URL 为 `http://127.0.0.1:18080/ad/`。
画面6：在 IntelliJ IDEA 中，展示 `find.js` 文件中 `axios.get` 请求的 URL，其中包含内网 IP `127.0.0.1:18080`。
画面7：在 IntelliJ IDEA 中，展示 `my.js` 文件中 `axios.get` 请求的 URL，其中包含内网 IP `127.0.0.1:18080`。
画面8：在浏览器中，显示一个加载中的页面，页面标题为“首页”，并提示“需要启用 JavaScript”。
画面9：在 Xshell 终端中，显示了 Redis 服务器的连接和操作，包括 `FLUSHALL` 命令和 `keys *` 命令。
画面10：在 Windows 资源管理器中，显示了 `itcast-haoke-web` 项目文件夹结构，包括 `build`、`node_modules`、`public`、`src` 等文件夹。
画面11：在 Xshell 终端中，显示了 `haoke-web` 项目目录下的文件列表，包括 `asset-manifest.json`、`favicon.ico`、`index.html`、`manifest.json`、`service-worker.js` 等文件。
画面12：在 Xshell 终端中，显示了进入 `nginx.conf` 配置文件的命令。
画面13：在浏览器中，显示了项目部署后的首页，包含多个功能按钮和问答内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```javascript
export default {
  // imgBaseUrl: 'http://47.96.21.88:8086/',
  // apiBaseUrl: 'http://47.96.21.88:8086/',
  // wsBaseUrl: 'ws://47.96.21.88:8087';
  imgBaseUrl: 'http://127.0.0.1:8086/',
  apiBaseUrl: 'http://127.0.0.1:8086/',
  wsBaseUrl: 'ws://127.0.0.1:18081/ws'
}
```

画面4：
```javascript
let swipe = new Promise((resolve, reject) => {
  axios.post('/homes/swipe').then((data) => {
    resolve(data.data.list);
  });
});
```

画面5：
```javascript
search = (event, data) => {
  let value = data.value ? data.value : this.state.searchKeyword;
  let page = data.page ? data.page : 1;
  let this = this;
  this.searchHandle(value);
  axios.get('http://api.manage.haoke.com/search?keyWord=' + value + '&page=' + page + '&size=10');
}
```

画面6：
```javascript
url: 'http://api.manage.haoke.com/mock/infos/list?type=1',
```

画面7：
```javascript
axios.get('http://api.manage.haoke.com/mock/my/info', {
  user_id: localStorage.getItem('uid')
}).then((res) => {
  this.setState({
    avatar: res.data.avatar,
    openAvatar: true
  });
});
```

画面9：
```
127.0.0.1:18080> FLUSHALL
127.0.0.1:18080> keys *
```

画面10：
```
itcast-haoke-web
├── build
├── node_modules
├── public
├── src
├── .git
├── package.json
├── package-lock.json
```

画面11：
```
drwxr-xr-x 3 root root 4096 Mar 1 12:07 ./ 
drwxr-xr-x 8 root root 4096 Feb 28 23:48 ../ 
drwxr-xr-x 2 root root 4714226 Mar 1 12:03 build/ 
drwxr-xr-x 2 root root 4096 Feb 28 23:48 build.zip 
drwxr-xr-x 2 root root 4096 Mar 1 00:11 manage-web/ 
drwxr-xr-x 3 root root 4096 Mar 1 12:03 haoke-web/ 
```

画面12：
```
cd /usr/local/nginx/conf/
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
