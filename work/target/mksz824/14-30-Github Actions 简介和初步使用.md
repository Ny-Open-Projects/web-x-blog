# 14-30-Github Actions 简介和初步使用

之前已经可以用 Docker 部署应用，但还缺自动化部署流程，每次都可能要手动操作。CI/CD 的概念之前学过，也用 Travis 完成过一些自动化流程，不熟悉可以回之前的课程复习一下。

这里介绍一个新的、非常易用的 CI/CD 自动化平台：GitHub Actions。我认为它比 Travis 还要强大：作为 GitHub 的亲儿子，和 GitHub 几乎可以无缝衔接，还提供了一系列第三方整合的 Actions，可以轻松完成各种操作。有一点要注意：国内访问 GitHub 有时不太通畅，但 Actions 使用起来问题不大，只要代码 push 成功就能触发对应的 action；action 的执行都在 GitHub 的服务器中，速度很快。push 不通畅时一般多重试几次就解决了。

CI/CD 平台很多，除了 GitHub Actions 和 Travis，还有 Circle CI、可自建的 Jenkins 等，课程里不可能讲全，只挑最流行的讲解并拓展视野。深入了解 CI/CD 概念后，大家可以自己选用喜爱的平台并学习它的用法。知乎上有一个讨论 GitHub Actions 相对其他服务优势的帖子，说得比较中肯，有空可以看看。

## 核心概念

GitHub Actions 由一系列概念组成，一张概念图把它们串了起来，下面抽丝剥茧逐个讲。

**workflow**：GitHub Actions 的根本。它是一个可配置的自动化流程，可以包含多个 jobs，通过 repo 中的 YAML 文件定义。一个代码库可以包含多个 workflow。代码库里有一个特殊的目录 `.github/workflows`（特别注意不能写错），在里面可以定义多个 workflow，每个是独立的 `.yaml` 文件，注意它们是并行运行的（parallel）。

**events**：触发 workflow 的特殊事件。比如发起 pull request、push 了代码、有人提出了 issue，也完全可以自定义。文档里有 events that trigger workflows 的完整列表，可以用单一事件，也可以用数组表示多个事件。这里先测试最简单的 push：代码 push 成功后触发 workflow。

**jobs**：workflow 中一系列可执行步骤。每个 job 在同一个 runner 中进行，runner 是 GitHub 提供的一台特殊虚拟机，支持各种操作系统。每个 job 有若干 steps，每个 step 或者是一个可执行的 Shell 脚本，或者是一个可执行的 action；steps 按顺序执行且互相依赖。

**actions**：GitHub Actions 中的自定义应用，可以完成一系列复杂且常用的任务，帮我们减少 workflow 中的重复代码。GitHub 提供了非常多常用的 actions，可以在 marketplace 查阅，上面有一万多个，包括官方的和第三方集成的；我们也可以写自己的 action。这个机制给 GitHub 提供了无限可能，非常强大。

## 写一个 workflow

在 learn-mongo repo 里创建文件：`.github/workflows` 目录下建一个 yaml，名称可自定义，这里叫 github-action-demo.yaml：

```yaml
name: GitHub Action Demo

on:
  - push

jobs:
  check-actions:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repo code
        uses: actions/checkout@v2
      - run: echo "trigger by ${{ github.event_name }}"
      - run: echo "${{ runner.os }} server hosted by GitHub"
      - name: List files in the repo
        run: ls ${{ github.workspace }}
```

逐段看：顶部 `name` 给 workflow 起名；`on` 设定触发时机，是特殊关键字，值可以是数组也可以是单一事件，这里写 push。然后 `jobs`：缩进后的名字是 job 名称（可以随便取），里面有一个特殊字段 `runs-on`，指定 runner 的操作系统。刚才说了每个 job 都有自己的 runner，这里用最新的 Ubuntu；GitHub Actions 支持很多操作系统，包括各种 Linux 发行版和 Windows，非常强大。

接下来 `steps`，多项前面加横杠。第一个可以只用 `run`，写要执行的命令：echo 一段信息，里面用预设的环境变量 `github.event_name`；再来一句 echo，用 `runner.os` 显示操作系统。注意变量都要用两个花括号包裹。除了直接 run，每个 step 还可以加 `name` 给步骤起自定义名称。

然后是第一个 action：用 `uses` 引入 `actions/checkout@v2`，这是官方的 checkout action，它可以把 git 代码 checkout 到 runner 本地，之后就能看到代码内容了。点进 marketplace 的页面就能看到这个 action 的详情。最后再 run 一步 `ls`：用特殊环境变量 `github.workspace` 指定当前的工作目录（注意变量名别写错），列出文件。

## 运行验证

保存后 add、commit（比如 commit test workflow again）、push。push 成功后，到 repo 的 Actions 页面，点击 Test Workflow Again，可以看到 workflow 在运行，变绿说明执行完毕。每一步都可以点进去看结果：我们添加的一系列 steps 的 echo 输出，checkout 使用 action 的过程比较长，是一系列操作；list files in the repo 这步能看到文件都输出了，说明代码确实被 checkout 到了虚拟机中。

这节课的任务就完成了。复习一下配置文件和那两张概念图，就能很清楚地弄明白 GitHub Actions 的整体流程。
