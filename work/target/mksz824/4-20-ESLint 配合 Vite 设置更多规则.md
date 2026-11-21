# 4-20-ESLint 配合 Vite 设置更多规则

现在我们可以让 ESLint 运行起来，也了解了它配置文件几个字段的内容。但还没把 Vite 和 ESLint 结合起来，下面的任务是安装一个插件，让 Vite 脚手架运行的时候自动监测 ESLint 的错误。

对于 ESLint 我讲得比较细，不像其他课程那样直接给一个现成模板使用。因为我发现，很多同学虽然启用了 ESLint，但不知道 ESLint 配置以及怎样修改规则。通过这样的过程，希望大家更好地了解 ESLint 的工作原理和配置方式，在其他项目中可以举一反三。

## 安装 vite-plugin-eslint

插件官网是 vite-plugin-eslint。ESLint 前面已经安装过了，这里只安装插件：

```bash
npm install vite-plugin-eslint --save-dev
```

安装完毕后简单修改 Vite 的配置文件 vite.config.ts。第一步把插件引过来，from 'vite-plugin-eslint'，然后直接放到 plugins 数组下面作为新的一项。特别注意它是一个函数，要以调用的形式写：

```ts
import vue from '@vitejs/plugin-vue'
import eslintPlugin from 'vite-plugin-eslint'

export default defineConfig({
  plugins: [vue(), eslintPlugin()]
})
```

配置文件添加完毕。先别着急运行，要修改一下 ESLint 自身的配置文件 .eslintrc.cjs。

首先修正一个错误：这里 module 报错 module is not defined。module 是 node.js 环境下的全局变量，但上节课设置时没有勾选 node，只有 browser，自然报错了。把 node 加上并设为 true 就可以了。保存后注意，只有有输入的时候它才会重新验证，随便输入一下，这个错误就消失了。

然后删除一些字段。第一个是 parser，这是上节课选择 TypeScript 时添加的自定义 parser。后面要添加 Vue 对应的插件，不需要使用它，删掉。同样，plugins 也删掉。最后挪动一下字段的位置：把 extends 提前。位置是随意的，但一般的做法是 extends 在前面，具体的 rules 在下面。

## 运行验证

配置修改完了，运行 npm run dev，看看两者能否良好运作。5173 端口，看会不会出现错误。我们发现 unexpected debugger 出现了，和编辑器中报的是同样的错误，说明没问题。把 debugger 删掉，错误应该消失。但是否会有新的错误呢？出现了：App.vue 当中有错误，第一行遇到 unexpected token。

因为目前 ESLint 只能验证标准的 JavaScript 文件，没法验证 Vue 文件的语法。Vue 文件中有好几块内容，会遇到 script 等各种标签，ESLint 在一个标准文件中遇到标签就会报错。

特别注意：假如你在这里没有出现对应的验证，说明没有像上节课那样把配置添加进去。VS Code 里有个 settings.json，要把想验证的文件类型添加到对应的数组中，这样才会获得验证能力。我们这里添加了 vue，所以会对 vue 进行验证，报出这个错误。

## 安装 eslint-plugin-vue

下一步安装 Vue 官方的 ESLint 插件，来分析和验证 Vue 这种结构的文件。官网是 eslint.vuejs.org，安装很简单：

```bash
npm install eslint-plugin-vue --save-dev
```

它里面包含一系列和 Vue 相关的规则，规则列表分三个层级，按规则越来越多排序：vue3-essential 规则最少，vue3-strongly-recommended 居中，vue3-recommended 最多。按自己的需求配置：想少一点限制就选规则少的，想强烈限制就选最多的。

这些规则一般都是针对 Vue 单文件格式的特殊规则，有针对 HTML 节点的，也有其中 JS 部分的规则。举个例子：no-multiple-template-root 之类的规则里有一条是关于 v-html / v-text 的（no-child-content），意思是 template 中如果使用 v-html 或 v-text，对应的 children 应该为空，如果有内容就会报错。

试一下这个规则。先把规则组放进配置文件，复制添加进去，原来 ESLint 自带的 eslint:recommended 就不需要了，先去掉。保存后复制一个刚才的节点放在 template 里，可以看到爆出红线，内容和刚才看到的一样：Child content is disallowed because it will be overwritten by the v-text directive。想看详情的话和上节课一样，直接点击链接跳到规则页。

Vue 文件的验证完成了，把它去掉，看看还有没有别的问题、有没有新的规则组可用。

## 针对 TypeScript 的规则组

把应用运行起来，会发现一个小问题：HelloWorld 第四行出现问题。看是什么问题：这里是一个 TS 专有的语法（泛型），但 ESLint 不认识泛型语法，所以报错。文档也说了详情：没法验证 TypeScript 语法，一些符号会报错，比如泛型的括号等。

所以要针对 TypeScript 添加一个规则组。规则组地址是 @vue/eslint-config-typescript，它其实是一个插件，最终使用的是很出名的规则组 typescript-eslint，里面是 ESLint 针对 TS 的特殊规则，规则也非常多。这个插件把这个规则组拿了过来，并对 Vue 文件做了对应的配置，所以直接安装它：

```bash
npm install @vue/eslint-config-typescript --save-dev
```

安装完毕后，只需要把新的规则组添加到 extends 数组中：

```js
extends: [
  'plugin:vue/vue3-essential',
  '@vue/typescript/recommended'
]
```

保存后验证：HelloWorld 当中随便输入一个泛型语法，错误不存在了，说明没问题。再把应用运行起来，稍等片刻发现没有任何问题，直接显示出应用，说明 TS 的验证已经生效。

最后再验证一下错误的语法是否会被检查：输入 `const a = 1`，这里爆出一个 warning 并写了详情：a is assigned a value but never used。使用的是哪条规则呢？就是刚添加的规则组里的 @typescript-eslint/no-unused-vars。规则已经成功生效。

## 回顾

这节课我们做了几件事：添加插件让 Vite 和 ESLint 完美运行起来；添加了两个规则组，一个针对 Vue 文件，一个针对 TypeScript。通过这两个规则组，可以比较完美地验证代码。

通过这两节课，希望大家掌握几个基本的 ESLint 配置知识点：

1. **怎样创建 ESLint 的配置文件**：有一个对应的命令自动生成。
2. **怎样运行 ESLint**：可以在三个环境运行。第一个是命令行，用 npx eslint 对单个文件验证；第二个是编辑器中运行，安装 ESLint 插件后，如果想验证更多类型的文件，记得在 .vscode 文件夹下的配置文件里把想验证的文件类型都写进去，输入时就会验证；第三个是配合 Vite，运行本地服务器时自动检查。
3. **看懂报错并按自己的要求修改单条规则**：把那条规则拿过来放到 rules 当中，设置为 0、1 或 2，很方便。
4. **安装 extends 并使用**：找到你喜欢的规则组，安装后放到 extends 数组中，就完成了任务。
