# 14-31-学习 Github Actions 的进阶知识

上节课了解了 GitHub Actions 最初步的知识，这节课深入它最重要的概念：Actions。有了这个自定义的 Action，做很多操作时都非常简单。新创建一个 workflow 文件 actions-demo.yaml，把基本结构写好，job 叫 build。

## 版本：@ 后面的信息

第一步还是用上节课的 checkout：

```yaml
steps:
  - uses: actions/checkout@v2
```

@ 后面可以加版本，v2 表示使用 2 版本上面的最新版本。到 checkout action 的页面，有一个下拉菜单能看到它历史的一系列版本，这些就是对应的 tag，选好后写在 @ 后面即可（比如 v2 对应最新的 v2.4.0）。除了 tag 名称，还可以用 branch 作为变量：到 checkout 的代码库下，点 main 能看到所有 branches 和 tags，直接把 branch 名称写在后面也可以使用。

## 参数：with

一个 action 就像一个函数，可以接受不同的参数，参数可变，从而定义不同的行为。看 checkout 的文档：uses 后面有一个特殊的 `with`，后面加对应的参数。比如：

- `repository`：可以 check out 一个除了当前推送的代码库之外的 public repository；
- `ref`：定义 branch 名称，可以 check out 另外的 branch；
- 还有一系列其他参数，甚至可以 check out 不是 GitHub 的代码库。

测试一下 repository 参数：

```yaml
      - uses: actions/checkout@v2
        with:
          repository: <你的public组件库repo>
      - name: List files in the repo
        run: ls ${{ github.workspace }}
```

check out 之后再运行一遍 ls 验证。

## setup-node：预装 Node 环境

第二个非常常见的 action 是 setup-node，它可以在 runner 上预装 Node.js 环境。是不是很熟悉？没错，它内部都是用 Docker 实现的。用法和之前一样用 uses：

```yaml
      - uses: actions/setup-node@v2
        with:
          node-version: 16
```

它提供一个参数 node-version，这里设成 16。环境设置完毕后，就可以在 GitHub 服务器上跑一系列功能了：npm install、跑测试、跑代码覆盖率，成功后再进行后续操作，这就是之前说的 CI/CD 基本流程。大多数服务都有对应的 actions，比如 Mongo 和 Redis，都可以用 actions 快速在 runner 中完成部署，内部同样是 Docker 实现的。

再写几个自定义的 run 验证环境：

```yaml
      - run: node -v
      - run: npm install typescript -g
      - run: tsc -v
```

运行测试：commit（more actions tested）后 push。到 Actions 页面能看到两个 workflow 在运行（之前的 GitHub Action Demo 和新的 More Actions Demo，因为有两个 workflow 文件）。点进 Build 看步骤：checkout 成功；list files 列出的已经不是本 repo 的内容，而是 Jest、Test 等，说明确实是我们指定的那个组件库 repo 的信息；setup-node 后 `node -v` 返回 16.13.1，没问题；安装 TypeScript 后 `tsc -v` 返回 4.5.4，全局 tsc 也安装成功。

这节课学习了 Actions 的两个进阶用法：@ 后面提供对应的版本信息；使用 with 传入可变的参数，改变 Action 的运行结果。
