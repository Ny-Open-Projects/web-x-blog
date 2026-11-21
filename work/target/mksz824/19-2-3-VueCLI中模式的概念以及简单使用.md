# 19-2-3-VueCLI中模式的概念以及简单使用

上节课了解了打包的基本流程，这节课来了解 Vue CLI 运行过程中的模式。最终目的是完成一个重要任务：给生产环境打包时，需要根据是预发布还是正式发布，选取不同的 URL。

## 三种模式

默认情况下，一个 Vue CLI 项目有三个模式：

- development，运行 serve 命令时的模式；
- test，运行 test:unit 时的模式；
- production，运行 build 时的模式。

模式决定了应用在什么样的环境下运行。针对这三种模式，Vue CLI 会创建三种针对不同环境优化过的 Webpack 配置，所以它的根本就是根据模式选择三种不同的 Webpack 配置。test 模式创建的是优化过、用于单元测试的 Webpack 配置，它不会处理图片以及对单元测试非必要的其他资源；development 模式会启用热更新，不对资源进行哈希，也不打出 vendor bundles，目的是开发时能够快速重新构建；production 模式上节课说过，一切为了快，所以有一系列其他的配置。

当运行 vue-cli-service 时，它会根据不同的命令设置对应的模式。而模式说到根本，其实就是一个环境变量：NODE_ENV，这是 Node.js 项目中的一个通用值。

## 打印环境变量验证

做一个最简单的测试，在代码里打印：

```ts
console.log('check', process.env.NODE_ENV);
```

运行时它会把 process.env 对象连同这个变量注入到整个应用中。在开发环境下运行，console.log 打出 check development，说明当前是开发环境。

再测试一下测试环境：随便拿一个测试文件，比如 color-picker.spec.ts，在其中打印同样的代码，然后运行 `npm test:unit --watch` 加上对应的文件地址，输出的是 check test，说明它在测试环境中。

## 用环境变量区分 URL

有了这个环境变量，就可以判断当前是生产环境还是开发环境，根据它添加不同的 URL。修改 main.ts，把两个 URL 设置成可变的 let，然后判断 process.env.NODE_ENV 是否等于 development：等于说明在开发环境下，设置为测试地址的后端 URL；否则设置为生产环境的 URL，正式地址是 HTTPS 的 API 域名，H5 的子域名是 h5。最后把 baseURL 和 baseURL2 导出，外界要使用这两个 URL。

## 强行指定模式

采用什么模式、使用怎样的配置，取决于 NODE_ENV 这个关键的环境变量。那么在一条命令下能否强行修改它的模式？答案很简单：运行命令时修改环境变量即可。

在 Windows 和 Linux 上设置环境变量的命令并不相同，这里推荐一个跨平台设置环境变量的工具 cross-env，它可以完美解决兼容性问题。安装之后，在命令前面加上要设置的环境变量名和值即可。

比如给测试命令加一个 cross-env，希望它运行测试时使用 production 模式：

```bash
cross-env NODE_ENV=production vue-cli-service test:unit
```

重新运行测试命令，打印出来的 log 是 check production，说明环境变量设置成功了。但一个很不幸的消息是测试失败了。这就说明不同模式下 Webpack 的配置大相径庭，为了迎合测试环境，必须使用 test 模式。这个实验说明模式不能乱点鸳鸯谱，强行指定很可能造成错误，之前的测试通过，现在就失败了。

## 小结

这节课讲解了 Vue CLI 中模式的概念，在应用中做了简单使用，区分了两个不同的 URL，还教了大家强行指定模式的方法：用 cross-env 在命令行设置环境变量。

不过我们还没有完成任务：staging 环境希望采取 production 的压缩方式，但采用的还是测试环境的后端 URL。怎样对这个问题继续细分并解决？下节课一起来看。
