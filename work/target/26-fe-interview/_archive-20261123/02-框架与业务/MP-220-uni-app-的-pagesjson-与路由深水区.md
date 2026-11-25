---
title: [MP-220] uni-app 的 pages.json 路由深水区（守卫/动态路由/参数）？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-220：uni-app 路由深水区？
**答**：
- pages.json 静态声明页面/分包/tabBar/窗口表现——编译期展开为各端路由配置。
- 路由守卫缺失：小程序无 beforeEach——工程上用「路由表封装」（navigateTo 前 checkAuth）或拦截 open-type 按钮。
- 动态参数：navigateTo url query 传递；对象参数 encodeURIComponent + 长度限制（URL 长度）→ 复杂对象走全局 store/eventChannel。
- 页面栈管理：getCurrentPages 操作层级（10 层限制）、redirectTo 清栈语义。
- H5 端路由：vue-router 接管，支持动态路由（/:id）与 history 模式——跨端路由差异集中在适配层。
