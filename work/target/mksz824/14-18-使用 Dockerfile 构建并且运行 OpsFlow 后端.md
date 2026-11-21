# 14-18-使用 Dockerfile 构建并且运行 OpsFlow 后端

上节课学了 Dockerfile 的基础用法，这节课来运行真正的 OpsFlow 后端程序。基于上节课的基础，还要做一些改进。首先需要修改几处代码让它初步跑起来。注意这只是初步实验，不是要完整实现后端的所有功能，先让它跑起来就好。

## 三步预处理

1. 把 TypeScript 版本改为 4 以上。之前用 3 版本跑编译命令会报 TS 错误，这一点之前学过，这里再强调一次。
2. 我们的应用需要连接数据库和 Redis，但跑在 Docker 里的应用无法访问主机的端口和服务，启动时会连不上 host 里的 MongoDB 和 Redis。所以做实验时，把配置里这两块暂时注释掉，后面的课程再学怎样在 Docker 中连通这些服务。
3. 要在 Docker 中安装依赖，可以把项目里不用的大库暂时去掉。比如处理图片的 sharp，有五十多兆，去掉它可以让构建 image 快一点。去掉 sharp 后，把 utility 里和 sharp 相关的代码暂时注释掉。

## 编写 Dockerfile

三步修改完成后，创建 Dockerfile。重温一下步骤：

```dockerfile
FROM node:16

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN npm install --registry=https://registry.npm.taobao.org
RUN npm run tsc

EXPOSE 7001

CMD ["npx", "egg-script", "start", "--title=OpsFlow-backend"]
```

和上节课一样：FROM node:16，创建文件夹 /usr/src/app 并设为工作区。拷贝这次不是拷单个文件，而是把所有文件都拷过去，用 `COPY . /usr/src/app`。

但项目里有很多不希望被拷贝的文件，比如 node_modules、logs 等。这和不希望提交到 Git 的文件处理方式一样：Git 有 .gitignore，Docker 有对应的 `.dockerignore`。新建一个这样的文件（VS Code 会贴心地显示成 Docker 图标），填入一个通用模板，里面是各种应该被忽略的文件。注意有一处要改：模板里默认会把环境变量文件忽略掉，而我们的应用把很多敏感信息保存在环境变量里，没有这些信息启动就会报错，所以要暂时删掉这两条规则。这一步同样服务于"先跑起来"的初步目标，之后会把问题一一解决。

接下来是运行前的启动步骤：安装依赖、运行 `npm run tsc` 生成 JS 文件。出于测试目的，先不添加 webpack 生成和上传 H5 页面的步骤。第一步 `npm install`（已经在工作区内且文件都拷过来了；.dockerignore 把 node_modules 忽略了，所以必须在镜像内安装），加一个淘宝源参数，安装会快一点。第二步 `npm run tsc`。然后 `EXPOSE 7001` 通知暴露的端口。

最后是启动命令。这里不用 CMD 直接跑后台，而是前台运行，保证应用稳定不自动退出。看 package.json，现有的 npm script start 对应的命令带了一个 daemon 参数，去掉它就行，其余写法一致：用 npx 调 egg-script，接 start，再带上 title 参数。

## 构建并运行

```bash
docker build -t opsflow-backend .
docker run -d -p 7001:7001 opsflow-backend
```

因为有 npm install，构建会稍等一会儿。build 完成后启动容器，端口映射 7001 到 7001。在 Dashboard 点进去可以看到 logs，内容与终端输出一致，最后显示应用已在 7001 端口运行。本地访问 7001，有一个 API 会返回 hi egg，输出正确说明启动成功。当然，访问任何跟数据库相关的接口都会报错，因为还没添加数据库。

现在应用可以简单跑起来了，但如前所述还是阉割版，没有数据库和 Redis 等持久化功能。接下来就要学习怎样让几个服务一起运行。
