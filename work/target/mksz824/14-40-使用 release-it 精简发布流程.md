# 14-40-使用 release-it 精简发布流程

上节课完成了本周大一统的任务，用 GitHub Actions 实现了自动部署。流程没问题，但操作上还有些繁琐：要进入代码手动修改 package.json 的版本，还要用 git tag 命令手动打标签，费时间且容易出错，比如 tag 和 package.json 里的值打得不一致就会出问题。

这时候求助一款工具：release-it，专门用来走软件 release 流程。它的 GitHub 主页上有 4.8k star，用的人很多，功能也很丰富，可以接入很多不同的平台，有些功能甚至和 CI/CD 的范畴有所重合，比如 publish to npm、create release at GitHub or GitLab。这里只用它最简单的功能，也就是第一条：Git commit, tag and push。运行它之后，它会根据当前代码的情况自动打 tag、修改 package.json 中的版本并 commit。

## 安装与配置

```bash
npm install release-it --save-dev
```

然后在 package.json 里添加一个脚本：

```json
"scripts": {
  "release": "release-it"
}
```

注意它有两种模式：弹出模式（交互式）和 CI 模式（用 `--ci` 参数控制）。文档里写了 Interactive vs CI mode 的区别：CI 模式是全自动的，不弹出任何输入，所有需要用户输入的地方都通过参数或配置文件自动填写，对应的是 CI/CD 流程中在服务器上运行自动化脚本的模式。我们这里是手动过程，希望弹出对话框，所以不用 CI 模式。

release-it 其实模拟了整个发布过程：先预检查，然后 add、commit、打 tag，最后 push。

## 预检查排错

运行 `npm run release` 试试。第一次弹出了错误：working dir must be clean，它有一系列前置条件检查，不满足就提示要先完成。这次报错是因为我们安装依赖并添加了脚本，package.json 发生了变化，需要先 add、commit（add release script）再运行。

第二次运行又报错：oh no, upstream config for current branch，违反了 upstream 相关的检查。这里补一点 Git 基础知识：`git branch -vv` 可以查看本地和远程 branch 的对应情况，输出里会显示 upstream。我们的本地只有 main 有对应关系，其他 branch 都没有，所以报这个错。想让本地分支建立对应关系，可以在 push 时加 `-u` 参数，接 remote name 和 branch name。但我本地这些 branch 虽然没设 upstream 也 push 成功了，为什么？

因为 git push 有不同的选项。用 `git config --list` 可以拿到所有 git 配置，grep 一下 push：我们的取值是 current。看 git 文档，push 有五个不同选项：simple 和 upstream 需要设定 upstream；current 则直接用本地 branch 名称对应远程 branch 名称，直接运行 git push 即可。

说了这么多，目的是：我本地的设置允许没有 upstream，所以需要一个配置文件改一下 release-it 的默认选项，让它忽略这个检查。到文档中可以看到它所有的配置项：Git 的选项、npm 的选项，还有 GitHub、GitLab 的选项。在根目录创建 .release-it.json：

```json
{
  "git": {
    "requireUpstream": false
  },
  "npm": {
    "publish": false
  }
}
```

git 下把 requireUpstream 设为 false；另外我们不需要 npm publish，而它的默认值是 true，也设为 false。所有信息都可以定制，比如 commit message 默认是 release 加版本号，可以自己改。这里只改这两项。

改完配置 working directory 又不 clean 了，需要再 commit。可以用合并进上一条的命令：`git commit --amend --no-edit`，不新增一条而是把两条合并，现在这一条 commit 里就包含了两个修改的信息。

## 发布

再次运行 `npm run release`，限制条件都通过了，可以发布版本了。特别注意：运行这个命令前它会先完成对应的 pull 操作。如果发现它时间较长、没弹出界面，可能是你的代码库存在 GitHub 上、速度受影响，多运行几次或耐心等待即可。

之后会弹出选项：它根据当前版本（1.0.8）自动列出可发的版本：Patch（最后一位）、Minor（第二位）、Major（2.0.0），还有一些 pre-patch、pre-minor 等。这里选 patch，发个小版本 1.0.9，回车。接着依次确认：commit（显示的就是配置里自定义的信息，点击 yes）、tag 打到 1.0.9（yes）、push（yes）。稍等片刻，done，commit、打 tag、push 就完成了。

现在静静等待 GitHub Actions 完成 build 等一系列过程：因为推送了新 tag，workflow 被触发，又到了 build image 的时候，要等个两三分钟。等待之后 job 运行完毕，整个流程结束。验证一下版本：刷新应用的 ping 接口，app version 变成了 1.0.9，新版本上线完毕。

这节课完成了 release-it 的使用，现在用一个命令就能轻松完成应用的 release。
