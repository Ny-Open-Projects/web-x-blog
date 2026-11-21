# 20-6-Pages 概念

这节课继续基础知识的学习，接触的概念是 pages。Nuxt 中有一个很重要的文件夹叫 pages，顾名思义放不同的页面，可以在这里创造主页、登录页、注册页等。用一个熟悉的概念来说，就是路由：在这里路由是通过文件来进行的，只要在文件夹中添加不同的 .vue 文件，Nuxt 3 就能自动生成相应的路由，帮助用户顺利浏览网站。路由基于文件系统，这是很神奇的一点。

来创建两个页面。按照项目需要，肯定有一个登录页面和一个系统管理的首页，所以创建 index.vue 和 login.vue，先在里面加最简单的 template：一个是 HomePage，一个是 the login page。

添加完毕后还要做一个简单的替换。app.vue 是根组件（入口组件），把里面的 HelloWorld 删掉，换成内置的全局组件 NuxtPage。它是干什么的？用来渲染整个应用页面相关的内容：当创建页面并在路由匹配时，NuxtPage 会根据路由匹配动态加载和渲染相应的页面组件。可以把它理解成页面相关的占位符：匹配到对应路由时，页面内容就动态塞进 NuxtPage 中。它的底层逻辑基于我们熟悉的 Vue Router。

现在有了两个路由：index.vue 和 login.vue。index 很特殊，直接在 pages 根目录下，匹配根目录。因为 pages 文件夹是新建的，和之前的问题一样需要重启一下。重启后就能看到路由了：根目录是 index.vue 的内容，访问 /login 就渲染出 the login page。

查看一下网页源代码，验证服务器端渲染的特性：如果是 SSR，the login page 应该出现在网页源代码中。等待片刻后可以看到这个 h1 确实在里面，说明初次渲染是服务器端渲染的，对 SEO 有利。

除了这种完全静态的 URL，我们通常还会遇到动态 URL，比如查看不同的 user：第一个 user 的 ID 是 1234，第二个是另一个 ID 3456。要匹配这样的 URL，还是通过文件完成。先建一个二级文件夹 users，在里面做动态路由：使用方括号指代动态参数，任何参数用方括号包裹就变成了动态路由。方括号既可以加在文件夹名称上，也可以加在文件名称上。要生成 /users/1234 这样的路由，就创建一个 `[id].vue` 文件。参数名可以随便起，选一个更贴切的名称即可。

在 `[id].vue` 里先写死一段 HTML：user detail page。保存后访问 /users/1234，跳到 user detail page，换成 /users/2345 也一样，说明动态路由没问题。如果想直接匹配 /users，在 users 下添加 index.vue（内容写 user index page）即可，直接访问 /users 就跳到了 user index page。

这里还可以打开 DevTools 看一下，里面写得很清楚：pages 部分渲染出当前路由（users 是 activated），并且能展示全部已注册的路由：index、login、users、users/:id 动态路由。DevTools 很强大，除了 pages 还能看 components：hello world 是手动创建并被自动加载的组件，其他还有 built-in component 和 runtime components（可以直接使用的全局组件）。再往下是 imports：能看到上节课说的 composables，有 user composables 里的 useKeyPress，还有一系列内置 composables，一共 77 个。通过 DevTools 可以非常清楚地看到整个项目的结构，之后我们会更多地使用它。

这节课讲述了 pages 的第一部分内容：怎样使用不同的文件生成路由，以及动态路由的生成方式。
