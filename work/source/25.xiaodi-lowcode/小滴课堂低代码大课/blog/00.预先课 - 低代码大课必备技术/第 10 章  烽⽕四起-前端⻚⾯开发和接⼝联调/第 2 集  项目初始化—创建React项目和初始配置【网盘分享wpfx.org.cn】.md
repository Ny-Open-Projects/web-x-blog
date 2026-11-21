# 项目初始化：创建 React 项目和初始配置

> **导语**：前端工程的第一步，往往决定了后面所有页面的组织方式。本文用 Vite 从零创建一个 React + TypeScript 项目，精简模板代码、配置 react-router-dom 路由表（`createHashRouter` + `RouterProvider`）、接入 Tailwind CSS，并加一层基于 localStorage token 的最简路由守卫。做完这些，登录、注册、课程管理三个页面就共享同一套骨架了。

## 前置知识

- 建议先了解《项目需求分析—前端页面需求分析》与《项目需求分析—接口和数据库数据结构分析》，明确要拆出哪些页面、对接哪些接口。
- 需要 React、TypeScript 基础，以及 pnpm 与 Vite 的基本使用经验。

## 正文

### 用 Vite 创建 React + TypeScript 项目

项目通过 Vite 脚手架创建，复制命令到目标目录执行，按提示填入项目名（示例中为 `react-project`），再用键盘上下键选择 React、选择 TypeScript，回车确认。创建完成后 `cd` 进目录安装依赖并启动，浏览器访问终端给出的地址即可看到初始页面。

```bash
pnpm create vite
```

### 精简模板代码

脚手架自带的样式文件先清理掉：删除 `App.css`、`index.css`，并同步剪掉 `main.tsx`、`App.tsx` 里对应的引入，否则会残留报错。清理后确认计数器点击仍然可用，说明入口没被破坏。样式清空后内容会靠左显示，这是符合预期的。

### 配置路由表

先安装路由依赖：

```bash
pnpm install react-router-dom
```

新建 `router/index.ts`。这是**配置文件**、不含 JSX，所以用 `.ts` 即可；而 `pages` 下存放的页面组件含 JSX，必须用 `.tsx`——讲师一开始把页面写成 `.ts` 触发了警告，改成 `.tsx` 后消失，这是最容易忽略的一点。组件命名首字母大写，如 `IndexPage`、`LoginPage`、`RegisterPage`、`CourseManagementPage`。

用 `createHashRouter` 创建路由，传入一个数组，每项描述 `path` 与对应页面：

- 根路径 `/` → `IndexPage`
- `children` 子路由：`login` → `LoginPage`、`register` → `RegisterPage`、`courseManagement` → `CourseManagementPage`

```ts
import { createHashRouter } from 'react-router-dom';
import IndexPage from '../pages/Index';
import LoginPage from '../pages/Login';
import RegisterPage from '../pages/Register';
import CourseManagementPage from '../pages/CourseManagement';

export const router = createHashRouter([
  {
    path: '/',
    element: <IndexPage />,
    children: [
      { path: 'login', element: <LoginPage /> },
      { path: 'register', element: <RegisterPage /> },
      { path: 'courseManagement', element: <CourseManagementPage /> },
    ],
  },
]);
```

> 注意：上面这段一旦写了 JSX，文件就应是 `.tsx`。若坚持用 `.ts` 的纯配置写法，可以改用 `Component` 或懒加载字段承载组件引用，本节演示里正是踩过这个坑后才换成 `.tsx`。

最后在入口 `main.tsx` 里用 `RouterProvider` 包裹并传入 `router`，移除不再使用的 `App.tsx`：路由表至此注册完成，后续在组件内跳转即可。

### 接入 Tailwind CSS

固定安装三个插件：`tailwindcss`、`postcss`、`autoprefixer`。随后配置两个文件：

- `tailwind.config.js`：`content` 里包含 `index.html` 以及 `src` 下 `.ts`/`.tsx`/`.js` 等文件，让 Tailwind 知道去哪里扫描类名。
- `postcss.config.js`：声明 Tailwind 与 autoprefixer 插件。

再新建基础样式文件，写入 Tailwind 的三条基础指令，并在 `main.css` 中 `import` 进来：

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

两个容易卡住的细节：**改了配置文件必须重启项目**，热更新检测不到配置变化；**一定要引入基础样式文件**，否则写了类名也不生效。测试时给 `IndexPage` 加一个深红色文字类，重启后看到红色字体，就说明 Tailwind 生效了。

### 用 token 做最简路由守卫

`IndexPage` 里用 `useEffect` 监听路径变化，结合 localStorage 里的 token 判断去向：

- 登录成功后会把 token 写入缓存，这里用 `localStorage.getItem('token')` 读取。
- **无 token**：只允许停在 `login` / `register`，否则跳转到登录页，不能进课程管理。
- **有 token**：若访问的是根路径、登录或注册，直接送进 `courseManagement`，避免已登录用户回到登录页。
- 子路由的出口用 `Outlet` 渲染，学过 Vue 的同学可以类比成 `Router View`。
- 跳转用 `useNavigate`，当前路径用 `useLocation`，二者都从 `react-router-dom` 引入。

演示时手动塞一个假 token 就能进到有权限的页面——此时还没有做 token 校验，只是先把路由流转逻辑跑通。

### 工程结构与配套代码

本节创建的 React 前端，与课程后端同处一个仓库。配套代码里能看到 NestJS 后端子项目的配置（`代码（已8期）/代码（已8期）/10-2/package.json`、`代码（已8期）/代码（已8期）/10-2/nest-cli.json`、`代码（已8期）/代码（已8期）/10-2/pnpm-lock.yaml`）：

```json
{
  "name": "server",
  "scripts": {
    "build": "nest build",
    "start": "nest start",
    "start:dev": "nest start --watch",
    "start:prod": "node dist/main",
    "test:e2e": "jest --config ./test/jest-e2e.json"
  },
  "dependencies": {
    "@nestjs/common": "^10.0.0",
    "@nestjs/core": "^10.0.0",
    "@nestjs/platform-express": "^10.0.0",
    "@nestjs/typeorm": "^10.0.1",
    "mysql2": "^3.6.3",
    "reflect-metadata": "^0.1.13",
    "rxjs": "^7.8.1",
    "typeorm": "^0.3.17"
  }
}
```

这份依赖说明后端已备好 NestJS + TypeORM + MySQL 驱动，正是本章「前端页面开发和接口联调」后续要对接的对象。`nest-cli.json` 保持默认骨架：

```json
{
  "$schema": "https://json.schemastore.org/nest-cli",
  "collection": "@nestjs/schematics",
  "sourceRoot": "src",
  "compilerOptions": { "deleteOutDir": true }
}
```

## 小结

- Vite 创建 React + TypeScript 项目后，先删掉 `App.css` / `index.css` 并清理入口引入。
- `react-router-dom` 用 `createHashRouter` 建路由表，入口用 `RouterProvider` 包裹；配置文件 `.ts`、含 JSX 的页面 `.tsx`。
- Tailwind CSS 需要 `tailwind.config.js`、`postcss.config.js`、基础样式指令三者齐备，且改配置要重启项目。
- 用 `useEffect` + `useLocation` + `useNavigate` + `Outlet`，配合 localStorage 中的 token，就能实现最简路由守卫。
- 前端 React 与后端 NestJS 同仓协作，为后续接口联调做好准备。

## 下一步

骨架搭好后，就可以逐个实现页面了，建议接着看《页面和数据联调—登录模块开发》与《页面和数据联调—注册模块开发》，把路由守卫里的 token 换成真实登录流程。
