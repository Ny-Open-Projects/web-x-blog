# 画面线理解：04-前端权限控制：实现思路分析-待修改

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\04-前端权限控制：实现思路分析-待修改_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:42, 01:12, 01:37, 02:13, 02:44, 03:26, 03:52, 04:15, 04:26, 05:14, 05:34, 05:56, 06:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:10:32

1) 这一组画面整体在讲如何在 Vue 项目中通过路由守卫（router.beforeEach）和 Vuex 状态管理实现用户登录态的判断与路由权限控制。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 permission.js 文件中用于动态添加路由的 actions 函数，其中包含过滤异步路由和提交状态的逻辑。
画面 2: 展示了 index.js 文件中定义的常量路由数组 constantRouterMap，包含登录、注册、重定向等路由配置。
画面 3: 展示了 index.js 文件中创建 Vue Router 实例并配置 beforeEach 守卫的代码。
画面 4: 在画图软件中开始绘制流程图，先画出一个“登录界面”椭圆。
画面 5: 在画图软件中，从“登录界面”椭圆引出一条线指向一个“构造页面”的矩形框，并标注“vue路由管理”。
画面 6: 在画图软件中，从“vue路由管理”矩形框引出两条线，分别指向“1.公共路由”和“2.钩子函数 router.beforeEach”。
画面 7: 展示了 index.js 文件中 router.beforeEach 守卫的具体实现，包含判断是否为登录页、检查角色权限并动态添加路由的逻辑。
画面 8: 展示了 index.js 文件中 router.beforeEach 守卫的代码，其中注释说明了如何处理登录态和动态路由。
画面 9: 展示了 users.js 文件中 getUserInfo 函数的实现，用于获取用户信息并提交到 Vuex。
画面 10: 在画图软件中，从“vue路由管理”矩形框引出一条线指向“store.dispatch('getUserInfo')”，再从该节点引出一条线指向“获取用户信息”的代码块。
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
画面 5: 标题为“登录界面”，从“登录界面”指向“构造页面”，并标注“vue路由管理”。
画面 6: 标题为“vue路由管理”，从“vue路由管理”指向“1.公共路由”和“2.钩子函数 router.beforeEach”。
画面 10: 标题为“vue路由管理”，从“vue路由管理”指向“store.dispatch('getUserInfo')”，再从“store.dispatch('getUserInfo')”指向“获取用户信息”。
画面 12: 标题为“获取用户信息”，在“获取用户信息”下方添加了“判断当前的所有md”文字。
画面 13: 标题为“获取用户信息”，在“获取用户信息”下方添加了“1 英”等文字。

5) 无。
