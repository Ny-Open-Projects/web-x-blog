# 5-14-使用 Vue Router 钩子函数获取路由信息和跳转

上节课用 Vue Router 创建了基本结构，这节课学习怎样在路由中进行跳转。

## RouterLink

使用 useVueRouter 时它还提供了另一个组件：之前接触过 RouterView，现在是 RouterLink。它的用法和 a 链接完全一样，只是跳转目标的属性叫 to。在 TemplateDetail 的"使用模板"处添加：

```html
<router-link to="/editor">使用模板</router-link>
```

点击"使用模板"就成功来到了 editor。再强化一下：给 App.vue 的 logo 也包上 router-link 指向首页，点击 logo 就能回到首页。

## 带参数跳转

接下来希望首页点击任何模板都跳转到 template detail，注意这里有参数：不同的模板跳过去参数不一样。在 TemplateList 的 a-card 外面包 router-link。第一种方法是模板字符串：

```html
<router-link :to="`/template/${item.id}`">
  <a-card>...</a-card>
</router-link>
```

点击第一项到 template/1，第二项到 template/2，以此类推，都没有问题。

另一种形式是不传字符串，传一个 object。object 里第一个是 name，对应路由配置里定义的 name；有参数时用 params 传递：

```html
<router-link :to="{ name: 'template', params: { id: item.id } }">
```

刷新验证，点哪个模板都能正确跳到对应的 template。

## URL 结构

现在能在组件间如愿跳转，但路由的需求还没完成。常见需求是在组件中拿到 URL 的不同参数做下一步处理，比如 TemplateDetail 要拿到 URL 上的 id，再用 id 去取模板数据。

拿 URL 信息之前，先看 URL 的结构。这张经典的图来自 Node.js 文档，建议保存下来好好学习。整串称为 href，它分为几个部分：第一部分 protocol 是协议，可能是 http 或 https；第二部分 auth 是授权，由 username 和 password 组成，中间用冒号连接，平时不常见但也是 HTTP 协议提供的保护资源可访问性的方式；接下来 host 由 hostname 和 port 组成，hostname 就是域名，port 是端口号；然后是 path，可能由多级构成；问号后面的内容一般是 key=value 形式，称为 query，常用来传检索条件，多个条件用 & 连接；最后是 hash 哈希值，以井号出现。

## useRoute 获取信息

在组件代码中访问 URL 参数要使用 Vue Router 提供的钩子函数。特别注意，钩子函数是新版 Vue Router 和之前最大的区别：原来这些功能直接挂在 this 上的全局对象上；钩子函数的做法明显更好，体现了 Vue3 的特点。

在 TemplateDetail 里做一个实验，导入 useRoute：

```typescript
import { useRoute } from 'vue-router';

setup() {
  const route = useRoute();
  return { route };
}
```

调试 object 除了在 JS 中用 console，也可以用 pre 标签包裹变量：`<pre>{{ route }}</pre>`。保存后页面上打出了整个对象：path、name、params（里面的 id）、query、hash，和刚才说的 URL 结构一一对应。在地址栏加上 `?abc=def#123` 后再看：query 里多了 abc，hash 是 123，fullPath 也有显示。现在就可以使用这个对象的属性获取各种数据了。

## useRouter 跳转

另一大功能是程序内跳转。现在只会用 router-link 这个写死的标签，但还需要在代码里跳转，比如登录成功后跳到首页。这是另一个钩子函数 useRouter，注意它和 useRoute 只差一个字母，作用千差万别：route 是获取路由信息，router 是定义路由的一系列行为，让它去做什么。

在 Home.vue 做实验，希望两秒后跳转到 id 为 1 的 template detail：

```typescript
import { useRouter } from 'vue-router';

setup() {
  const router = useRouter();
  setTimeout(() => {
    router.push({ name: 'template', params: { id: 1 } });
  }, 2000);
}
```

useRouter 的返回值上有一系列方法，push 就是跳转，参数和 router-link 的 object 形式完全一样：name 是 template，params 里传 id。保存后来到首页，等待两秒，它跳转到了 Template 一，整个过程完结。

## 小结

这节课介绍了 Vue Router 的一系列用法：用 router-link 和 router.push 在不同 URL 间跳转，用 useRoute 拿到 URL 的各种参数。
