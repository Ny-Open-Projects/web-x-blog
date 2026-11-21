# 画面线理解：01.课程介绍

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\01.课程介绍【海量资源尽在 ubkz.com】.mp4
- 抽帧：8 帧 @ 02:38, 03:32, 03:35, 03:39, 03:40, 03:41, 03:55, 04:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 19:57:37

1) 这一组画面整体在讲什么（一句话）：
本课程介绍部分，主要讲解ES6新特性与ReactJS入门，内容涵盖ECMAScript的发展历程、前端开发演变阶段及ES6基础语法示例。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 当前页面标题为“课程介绍”，左侧导航栏显示“1. ES6 新特性”下的“1.1. 了解ES6”。
- 主体内容介绍ES6是ECMAScript 6的简称，是JavaScript的下一代标准，于2015年6月正式发布。
- 子标题“1.1.1 什么是ECMAScript?”下，列出“web1.0时代”和“web2.0时代”的发展历程。

画面2：
- 左侧导航栏高亮“2. ReactJS入门”下的“2.1. 前端开发的演变”。
- 主体内容展示前端开发的四个阶段：静态页面阶段、ajax阶段、前端MVC阶段、SPA阶段。
- “静态页面阶段”部分说明使用MVC模式，其中Model指向Controller，Controller指向View。
- “ajax阶段”部分说明MVC模式演变为MVC，其中Model指向Controller，Controller指向View。
- “前端MVC阶段”部分说明MVC模式演变为MVVM，其中Model指向View Model，View Model指向Controller，Controller指向View。
- “SPA阶段”部分说明前端应用从页面跳转变为单页应用，用户交互不再需要页面跳转。

画面3：
- 左侧导航栏高亮“1. ES6 新特性”下的“1.1. 了解ES6”。
- 主体内容与画面1相同，展示ECMAScript的发展历程。

画面4：
- 左侧导航栏高亮“1. ES6 新特性”下的“1.1. 了解ES6”。
- 主体内容与画面1相同，展示ECMAScript的发展历程。

画面5：
- 左侧导航栏高亮“1. ES6 新特性”下的“1.1. 了解ES6”。
- 主体内容与画面1相同，展示ECMAScript的发展历程。
- 画面中展示了一段JavaScript代码，内容如下：
```javascript
class User{
    constructor(name, age = 20) { // 构造方法
        this.name = name;
        this.age = age;
    }
    sayHello(){
        return "hello";
    }
}
static isAdult(age){
    if(age >= 18){
        return "成年人";
    }
    return "未成年人";
}
class zhangSan extends User{
    constructor(name, age, address) {
        super(name, age);
        this.address = address;
    }
}
```

画面6：
- 左侧导航栏高亮“1. ES6 新特性”下的“1.1. 了解ES6”。
- 主体内容与画面1相同，展示ECMAScript的发展历程。

画面7：
- 左侧导航栏高亮“1. ES6 新特性”下的“1.1. 了解ES6”。
- 主体内容与画面1相同，展示ECMAScript的发展历程。
- 页面顶部显示“课程介绍项目课程介绍-v1.0”，并带有“博学谷”的水印。

画面8：
- 左侧导航栏高亮“1. ES6 新特性”下的“1.1. 了解ES6”。
- 主体内容与画面1相同，展示ECMAScript的发展历程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5中的代码：
```javascript
class User{
    constructor(name, age = 20) { // 构造方法
        this.name = name;
        this.age = age;
    }
    sayHello(){
        return "hello";
    }
}
static isAdult(age){
    if(age >= 18){
        return "成年人";
    }
    return "未成年人";
}
class zhangSan extends User{
    constructor(name, age, address) {
        super(name, age);
        this.address = address;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2中的架构图/流程图：
- 静态页面阶段：
  - Model（模型层）指向Controller（控制器层）
  - Controller（控制器层）指向View（视图层）
- ajax阶段：
  - Model（模型层）指向Controller（控制器层）
  - Controller（控制器层）指向View（视图层）
- 前端MVC阶段：
  - Model（模型层）指向View Model（视图模型层）
  - View Model（视图模型层）指向Controller（控制器层）
  - Controller（控制器层）指向View（视图层）
- SPA阶段：
  - 无明确的架构图，仅说明前端应用从页面跳转变为单页应用。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
