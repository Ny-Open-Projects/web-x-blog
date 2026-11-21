# Nestjs环境搭建和项目创建

> **导语**：本文带你完成 NestJS 开发前的环境准备，包括确认 Node.js 版本、安装 pnpm 与 Nest CLI，并用脚手架 `nest new` 创建第一个 NestJS 项目，最后把它启动起来看到经典的 Hello World。

## 前置知识

阅读本文前建议先看《Nestjs框架课程介绍+适合人员+学后水平》，了解 NestJS 是什么、为什么值得学。本文聚焦本地环境的落地。

## 正文

### 第一步：确认本机已安装 Node.js

NestJS 运行依赖 Node.js 环境，动手前先确认本机版本：

```bash
node -v
```

课程演示环境的 Node 版本是 18.x，使用 16、17 版本同样可以。如果命令无输出或报错，说明尚未安装，需要先到 Node.js 官网下载安装包（Mac / Windows 都有对应版本），建议选择左侧「稳定版（LTS）」。

### 第二步：安装 pnpm 包管理工具

传统上大家习惯用 npm，但它在下载依赖时速度偏慢。NestJS 工程推荐使用 **pnpm**，速度更快、磁盘占用更优。

Node.js 18 已经内置了 pnpm，可先检查是否已携带：

```bash
pnpm -v
```

若提示找不到命令，再全局安装即可：

```bash
npm install -g pnpm
```

> 提示：后续所有依赖下载、插件安装、脚本执行都可用 pnpm 完成，用法与 npm 基本一致。

### 第三步：全局安装 Nest CLI 脚手架

用脚手架可以快速初始化标准工程结构。先全局安装 **Nest CLI**：

```bash
pnpm i -g @nestjs/cli
```

（注意包名前的 `@` 符号。）安装完成后，就能用 `nest` 命令创建项目了。

### 第四步：用 nest new 创建项目

建议先切换到明确的工作目录（比如桌面），避免项目不知道生成到哪里：

```bash
cd Desktop
nest new test
```

执行后会让你选择包管理工具（npm / yarn / pnpm），这里选 pnpm 速度更快。选择之后脚手架会一边创建目录结构，一边**同步下载依赖**——所以你会感觉到一段等待时间，这是它在后台帮你 `install` 依赖，省去了后续手动安装的步骤。

创建完成后，用 VS Code 打开项目目录，就能看到 `node_modules` 已经被装好。

### 第五步：理解 package.json 与启动命令

每个 Node 项目根目录都有 `package.json`，里面定义了各类脚本。打开后能看到：

- `build`：打包构建命令；
- 各类 `test`、`lint`（ESLint 校验）等命令；
- 启动相关脚本，如 `start`、`start:dev`。

直接运行：

```bash
npm run start
```

项目即可启动。访问 `http://localhost:3000`，就能看到 `Hello World`。

启动端口从哪里来？打开 `main.ts`，里面有一行：

```ts
app.listen(3000);
```

这与 Express 框架的写法非常相似——同样是监听 3000 端口启动服务。

### 第六步：用 start:dev 开启热重载

如果只是 `start`，修改代码不会自动生效。开发阶段应使用：

```bash
pnpm start:dev
```

它会监听文件变化，当你改动服务层代码（例如把返回值改成 `Hello Nest`）并保存时，项目会自动重启并应用新内容，体验与 `node app.js`、Express 开发时一致。

## 小结

- 开工前先用 `node -v` 确认 Node.js（建议 16+，演示用 18 LTS）。
- 用 pnpm 替代 npm 提升依赖安装速度，Node 18 已内置 pnpm。
- 全局安装 `@nestjs/cli` 后，用 `nest new <项目名>` 一键创建工程并自动装依赖。
- 启动端口在 `main.ts` 的 `app.listen(3000)` 中配置，默认访问 `localhost:3000`。
- 开发用 `pnpm start:dev` 开启热重载，修改保存即自动重启。

## 下一步

项目已经能跑起来并展示 Hello World，下一步建议接着看《什么是装饰器和Nestjs中的应用》，深入讲解 NestJS 中最核心的装饰器机制以及它在框架里的实际应用。
