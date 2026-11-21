# 04-前端权限控制：实现思路分析-待修改

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\04-前端权限控制：实现思路分析-待修改_【海量资源尽在 ubkz.com】.mp4
- 时长 6分32秒（音频 392s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了我们现在只是展示了一下它这个前端控制的这个效果那接下来我们关注的就是说它这个前端究竟是怎么做到的那这个前端做到的就不得不提VUE它的两大核心功能一个是它的一个叫做路由一个是叫做它的状态管理那这边的这个代码由于比较复杂我简单跟各位说一下逻辑其实就可以了我们先去找到我们的代码当中的router目录下
[00:30] SRC Router目录下有一个叫做index.js这个index.js是我们整个VUE工程它的最主要的路由配置那在这个路由配置当中上边constant router map是我们的一些公共路由里面有登录注册等等相关的内容那底下呢还这边定义了一个叫做async router map这个是我们的业务路由或者模块路由
[00:57] 那业务路由或者模块路由它就是动态加载不同的模块那针对这些不同的模块我一个一个的往里添加不同的不同的我们根据前全线添加不同的菜单那这个是怎么做的借助的是我们VOE路由当中的勾字函数这个勾字函数叫做before each那借助这个before each方法里面可以动态构造
[01:23] 那我这边呢可以以一张图形的形式和各位简单的分析一下它是怎么做的首先呢左边是我们的登录界面登录界面那登录界面输入了用户名输入了密码之后接来它去渲染或者构造我们的整个页面当然了只有在登录成功之后才会去构造那构造页面的时候就会经历我们的VUE路由好了VUE
[02:08] 路由管理在VOE路由管理当中它就开始去加载动态创建那加载的内容其中第一个是公共路由公共的这些内容比如说404手机是什么等等那除了公共的路由之外接下来它还借助我们的勾字函数当然这是一个前置勾字函数before each就是这个before each方法那这个before each方法它究竟在做什么各位跟我一起简单的来看一下
[02:47] 而这个before each方法往里走他判断了一下get token这个get token啥意思呢就是说我判断一下你当前是否已经登录了因为前端他要存储我们登录的token信息如果已经登录如果已经登录那并且呢这玩意的to pass还是等于等于login也就是说啥意思你当前要跳转到一个页面那这个页面呢你已经登录过了并且你还要再去访问login那这个时候我就不让你再去访问了我让你跳远了首页
[03:18] 就这个意思当然了这句话你可有可无你想写就写不写也无所谓好了接下来我们关注的是里面有token信息那有token信息的话它发送了一个叫做getUserInfo的这么一个状态的一个方法触发了这么一个状态方法那这个getUserInfo在做什么我们这边全局的去搜索一下好了找到getUserInfo好了这边呢我也给它记录下来截一个图勾子函数里面去执行
[03:57] 那getUserInfo它在做什么呢我们一起来看一下那getUserInfo它执行的是一个profile方法那这profile我们还记着它是我们之前的API其中的一个那这个profile是不是就去获取用户信息所以接下来它做的事情就是去获取用户信息获取用户信息那获取用户信息的时候那各位来看这边呢它有自己的一个处理其中的处理的时候commit就是setRose
[04:38] 等等这个内容那这个set rows究竟在处理的是什么注意人家处理的是data.rows就是我们登录的我们的rows里面的两个按钮和我们的这个权限点的相关内容也就是说我会把这两个玩意儿给它保存下来那保存下来触发的就是set rows这么一个方法我们一起来找一下这个set rows的方法好了这个set rows的方法其实就是共享或者存储到我们的前端页面上那也就意味着
[05:07] 那就意味着我前端页面其实已经知道了你有什么样的权限你有什么样的内容好那我们全部都存储好了这些内容那接下来呢这边他又去触发一些自己的一些方法又去抱歉抱歉刚才的方法去哪在这边那这回呢他又去触发自己的一些方法这些方法就不是我们关注了那这样一来这样一来
[05:33] 那当我页面进行构造的过程当中或者登录之后页面构造的过程当中借助钩子函数获取我们的信息获取信息获取我们的菜单权限获取我们的按钮权限保存下来那保存下来之后接下来他要做的事情就比较简单了就开始进行判断判断当前的所有模块路由是否具有访问权限
[06:00] 因为别忘了其实我们的所有模块路由呢已经配置好了它有很多比如说呢有我们的SaaS比如说呢有我们的Company等等等等这些都已经配置好那它做的事情就是判断一下你这里面的这个菜单是否具备这些内容如果具备这个模块给我显示出来如果具备这个模块给我加载出来就是这个意思它就是这样做的当然这个代码呢有一点点复杂各位感兴趣的话呢其实去自己去
[06:29] 看一下其实就可以了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Vue 项目中通过路由守卫（router.beforeEach）和 Vuex 状态管理实现用户登录态的判断与路由权限控制。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 permission.js 文件中用于动态添加路由的 actions 函数，其中包含过滤异步路由和提交状态的逻辑。
画面 2: 展示了 index.js 文件中定义的常量路由数组 constantRouterMap，包含登录、注册、重定向等路由配置。
画面 3: 展示了 index.js 文件中创建 Vue Router 实例并配置 beforeEach 守卫的代码。
画面 4: 在画图软件中开始绘制流程图，先画出一个“登录界面”椭圆。
画面 5: 在画图软件中，从“登录界面”椭圆引出一条线指向一个“构造页面”的矩形框，并标注“Vue路由管理”。
画面 6: 在画图软件中，从“Vue路由管理”矩形框引出两条线，分别指向“1.公共路由”和“2.钩子函数 router.beforeEach”。
画面 7: 展示了 index.js 文件中 router.beforeEach 守卫的具体实现，包含判断是否为登录页、检查角色权限并动态添加路由的逻辑。
画面 8: 展示了 index.js 文件中 router.beforeEach 守卫的代码，其中注释说明了如何处理登录态和动态路由。
画面 9: 展示了 users.js 文件中 getUserInfo 函数的实现，用于获取用户信息并提交到 Vuex。
画面 10: 在画图软件中，从“Vue路由管理”矩形框引出一条线指向“store.dispatch('getUserInfo')”，再从该节点引出一条线指向“获取用户信息”的代码块。
画面 11: 展示了 users.js 文件中 getUserInfo 函数的实现，其中包含获取用户信息并提交到 Vuex 的逻辑。
画面 12: 在画图软件中，对“获取用户信息”的代码块进行编辑，突出显示了 commit('SET_ROLES', data.roles) 这一行。
画面 13: 在画图软件中，对“获取用户信息”的代码块进行编辑，添加了“判断当前的所有md”文字，并在下方添加了“1 英”等文字。
画面 14: 展示了 index.js 文件中 router.beforeEach 守卫的代码，其中包含处理用户未登录时跳转到登录页的逻辑。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 1:
```javascript
state.addRouters = routers
state.routers = constantRouterMap.concat(routers)

actions: {
  GenerateRoutes({ commit }, data) {
    return new Promise(resolve => {
      const roles = data
      // 过滤异步路由
      let accessedRouters = filterAsyncRouter(asyncRouterMap, roles)
      commit('SET_ROUTERS', accessedRouters) // 重置路由
      resolve()
    })
  }
}
```

画面 2:
```javascript
export const constantRouterMap = [
  {
    path: '/login',
    component: import('dashboard/pages/login'),
    hidden: true
  },
  {
    path: '/reg',
    component: import('dashboard/pages/reg'),
    hidden: true
  },
  {
    path: '/authredirect',
    component: import('dashboard/pages/authredirect'),
    hidden: true
  },
  {
    path: '/404',
    component: import('dashboard/pages/404'),
    hidden: true
  },
  {
    path: '/401',
    component: import('dashboard/pages/401'),
    hidden: true
  },
  {
    path: '',
    component: Layout,
    redirect: 'dashboard',
    children: [
```

画面 3:
```javascript
let router = new Router({
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})

router.beforeEach((to, from, next) => {
  NProgress.start() // start progress bar
  if (getToken()) {
    if (to.path === '/login') {
      next({ path: '/' })
    } else {
      if (store.getters.roles.length === 0) {
        store.dispatch('GetUserInfo').then(() => {
          const roles = res.data.data.roles // note: roles must be a array! such as: ['editor','develop']
          store.dispatch('GenerateRoutes', { roles }).then(() => {
            router.addRoutes(store.getters.addRouters) // 动态添加可访问路由
            next({ ...to, replace: true }) // hack方法 确保路由不会留下历史记录
          })
        })
      } else {
        next()
      }
    }
  } else {
    next('/login')
  }
})
```

画面 7:
```javascript
if (to.path === '/login') {
  next(path: '/')
  NProgress.done() // if current page is dashboard will not trigger afterEach hook, so manually handle it
} else if (store.getters.roles.length === 0) {
  store
    .dispatch('GetUserInfo')
    .then(res => {
      const roles = res.data.data.roles // note: roles must be a array! such as: ['editor','develop']
      store.dispatch('GenerateRoutes', { roles }).then(() => {
        router.addRoutes(store.getters.addRouters) // 动态添加可访问路由
        next({ ...to, replace: true }) // hack方法 确保路由不会留下历史记录
      })
    })
  } else {
    next()
  }
}
```

画面 9:
```javascript
export function getUserInfo({ commit, state }) {
  return new Promise((resolve, reject) => {
    api.profile().then(response => {
      const profile = response.data
      commit('SET_ROLES', data.roles.data.roles: (menus: []))
      commit('SET_NAME', data.username)
      commit('SET_AVATAR', data.avatar)
      commit('SET_INTRODUCTION', data.company)
      commit('SET_APPROVALS', data.approvals)
      resolve(response)
    }).catch(error => {
      reject(error)
    })
  })
}
```

画面 11:
```javascript
export function getUserInfo({ commit, state }) {
  return new Promise((resolve, reject) => {
    api.profile().then(response => {
      const profile = response.data
      commit('SET_ROLES', data.roles.data.roles: (menus: []))
      commit('SET_NAME', data.username)
      commit('SET_AVATAR', data.avatar)
      commit('SET_INTRODUCTION', data.company)
      commit('SET_APPROVALS', data.approvals)
      resolve(response)
    }).catch(error => {
      reject(error)
    })
  })
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 4: 无标题，无架构图。
画面 5: 标题为“登录界面”，从“登录界面”指向“构造页面”，并标注“Vue路由管理”。
画面 6: 标题为“Vue路由管理”，从“Vue路由管理”指向“1.公共路由”和“2.钩子函数 router.beforeEach”。
画面 10: 标题为“Vue路由管理”，从“Vue路由管理”指向“store.dispatch('getUserInfo')”，再从“store.dispatch('getUserInfo')”指向“获取用户信息”。
画面 12: 标题为“获取用户信息”，在“获取用户信息”下方添加了“判断当前的所有md”文字。
画面 13: 标题为“获取用户信息”，在“获取用户信息”下方添加了“1 英”等文字。

5) 无。

