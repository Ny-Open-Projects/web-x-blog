---
disableNunjucks: true
title: 16-4-2 快捷键编码第一部分：创建 useHotKeys
date: 2026-11-17 14:36:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课我们把快捷键功能分析清楚并选好了第三方库，这节课开始编码。先安装依赖：

```bash
npm install hotkeys-js --save
```

它自带 types 文件，不需要额外安装类型声明。

查文档可知它的用法：把 `hotkeys` 引进来直接作为函数调用，第一个参数是要绑定的键值组合，第二个参数是回调，回调里有两个参数 `event` 和 `handler`。针对这个功能，我们可以创建一个独立的 hook 函数，它应该和之前的 `useKeyPress` 非常类似，只是内部实现换成 hotkeys-js 这个库。

先处理生命周期：绑定和解绑的时机和之前一样，是 Vue 的 `onMounted` 和 `onUnmounted`。hook 命名为 `useHotKey`，第一个参数 `keys` 是要绑定的按键组合，第二个参数 `callback` 是触发后的回调。

这里有一个怎么确定回调类型的问题。我的建议是直接进到 hotkeys-js 的类型文件里一探究竟。可以看到它导出了 `hotkeys` 变量，类型是 `Hotkeys`，这是个 interface，里面重载了三种调用方式：我们用的是最简单的一种，第一个参数 key、第二个参数 method（回调）；另外还有第二参数为 scope 或 options 的两种复杂形式。

继续往下找，需要的类型叫 `KeyHandler`，它就是一个 function，接收两个参数：第一个是我们熟悉的原生 `KeyboardEvent`，第二个是 hotkeys 自己定义的 `HotkeysEvent`，里面有它的一系列属性。

这一步其实体现了 TypeScript 的一大好处：读类型文件里的类型代码，你能获得比文档或 demo 更详细的关于这个库的使用信息，包括参数和返回类型。找到了 `KeyHandler`，`callback` 自然就是它的类型。把函数写完整：

```ts
export default function useHotKeys(keys: string, callback: KeyHandler) {
  onMounted(() => {
    hotkeys(keys, callback)
  })
  onUnmounted(() => {
    hotkeys.unbind(keys, callback)
  })
}
```

内部很简单：`onMounted` 时调用 `hotkeys(keys, callback)` 绑定，类型完全匹配；`onUnmounted` 时用库提供的 `unbind` 方法解绑，参数和绑定完全一致，同样传 keys 和 callback。最后导出这个函数即可。

有了这个 hook，就可以创建很多快捷键了。既然快捷键有一大堆，这里引入一个新的概念：plugins，插件。快捷键操作独立于整个应用，是为了更好的交互而单独添加的、看起来相对独立的功能，所以把它归为我们整个项目的插件。在 `src/plugins` 下创建 `hotkeys.ts`，关于快捷键的处理都放在这个文件里：

```ts
import useHotKeys from '@/hooks/useHotKeys'

export default function initHotKeys() {
  useHotKeys('ctrl.c, command.c', () => { alert('复制') })
  useHotKeys('ctrl.v, command.v', () => { alert('粘贴') })
}
```

默认导出一个函数来初始化所有键盘响应，命名为 `initHotKeys`，内部把各个快捷键逐个注册进来。测试时先加两个组合键：`ctrl.c` 加 `command.c`，兼顾 Windows 和 Mac 两种系统；再加一组 `ctrl.v` 加 `command.v`。回调里先用 alert 验证响应。

最后在 Editor 中启用：导入 `initHotKeys`，在 `setup` 的最前面调用一次，整个流程就完成了。

界面上验证：按下 command+c 出现对应的响应，command+v 也一样。这节课我们初步搭好了快捷键功能的文件结构并做了简单测试。代码骨架已经有了，下节课把具体的逻辑添加到不同快捷键中，让它们完成对元素的一系列操作。
