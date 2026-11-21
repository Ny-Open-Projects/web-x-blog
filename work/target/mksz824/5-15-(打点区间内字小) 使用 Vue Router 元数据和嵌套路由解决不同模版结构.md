# 5-15-(打点区间内字小) 使用 Vue Router 元数据和嵌套路由解决不同模版结构

通过上节课已经了解了 Vue Router 的大体运作规律，就目前应用的需求来说，学到的知识已经够用。但还有一个问题没解决：针对两种不同的布局，一种是有通用头尾的，另一种是不规则、没有头尾的，怎么实现？这里介绍两种做法，对应两个知识点，大家可以自己挑喜欢的方案。

## 方案一：路由元数据 meta

回到需求图，这个需求本质上是根据不同的路由做判断，需要在路由上保存一些个性化的信息，在特定种类的路由上添加独特的信息加以区分。官方文档帮我们解决了：定义路由的时候，可以添加一个 meta 字段，以 object 形式写出需要的额外信息。

来到 router/index.ts，给 home 加上 meta，称之为 withHeader，表示需要头尾的布局，设为 true；template 也是需要的，复制一份：

```typescript
const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: { withHeader: true },
  },
  // ...
];
```

有了这个信息，就可以在 App.vue 中获取它并定义不同的布局。写 setup，用上节课说的钩子函数 useRoute（注意不是 useRouter），并用 computed 包裹：因为 withHeader 本身不是响应式对象，用 computed 转换成响应式对象后，会随路由切换做出对应的改变。

```typescript
import { computed } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const withHeader = computed(() => route.meta.withHeader);
```

返回出去后就能用它做判断了：v-if="withHeader" 时渲染有头尾的结构；v-else 时什么都没有，直接放一个 router-view。看结果：首页有头尾，点击模板详情页也还有，点击使用模板进入 editor 后，头尾消失了，个性化的布局实现。课后请大家给 editor 补充个性的头部，写在 Editor.vue 当中。

## 方案二：嵌套路由

说完第一种方法，另辟蹊径看另一种解法。换个角度：Editor 是这样的布局，Login 是这样的布局，它们都是自己独特的样式；而其他几个页面其实差不多，都是有头尾的。所以可以分成三类：Login 一类，Register 一类，其他都是一类。这些页面像一个新的独特样式，里面嵌套着不同的子 router-view，形成一种多层嵌套关系：router-view 里面又嵌 router-view。

对于这种嵌套关系，Vue Router 提供了 Nested Routes 的解决方案，通过 children 实现多层嵌套。用它来解决我们的问题。

先 reset 回到最原始的状态，然后创建第三种格式，称之为 index.vue，它就是带头尾的通用布局，内容我已写好。App.vue 里头尾都不用写了，只放一个 router-view，改名为 app-container。

在 index.ts 里大做文章。导入 index，先改根目录：根目录时用 index 渲染，component 改成 Index；然后在里面添加嵌套路由 children。children 数组里的项和路由的配置完全一样，直接复制进来：

```typescript
import Index from '../views/Index.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index,
      children: [
        {
          path: '',
          name: 'home',
          component: Home,
        },
      ],
    },
  ],
});
```

特别注意：children 的 path 前面不能加斜杠，否则会变成 root path，而不是连接到父路由。首页没有更深入的子路径，path 传空字符串，就默认渲染这个组件。

从首页开始看效果：首页渲染出了带头尾的内容。逻辑是：先匹配到 Index，它带头尾；再匹配到 children 中 path 为空的项，正好匹配这个路径，渲染出 Home 组件，等于是两层嵌套。

再点使用模板，发现它没有出现头尾。为什么？因为原来的第三项路由没有被删除，路由的匹配规律是第一层最准确的先匹配。把它删掉，保存后自动刷新，头尾就出现了。再点使用模板进入 Editor，它是自己的样式，没有头尾，同样完成了效果。

对于这种解决方案，看着嵌套结构的图理解会更深刻。当然，嵌套路由更适合文档里说的场景：多级 URL、多层 view，切换时外层 view 不变（比如 user 区域固定），里面一小块内容随路由变化。

## 小结

这节课用两个方案解决了布局问题，同时学习了两个知识点：路由元数据 meta 和多层嵌套路由（用 children 在父路由里添加子路由）。
