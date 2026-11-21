# 14-32-学习使用 Github Secrets

上节课学习了 actions 的具体用法，这节课学习一个新概念：secrets。代码中会出现很多敏感信息，常用做法是用 .env 文件保存并在代码库中忽略掉。同样，GitHub Actions 的 workflow 文件里也可能出现不想被外界感知的秘密信息，GitHub Secrets 就是为此准备的。

通过一个实例来演示：用 Secrets 登录到服务器，在服务器中做具体操作，把一个私密的信息写入服务器的文件，这为以后每次代码更新 push 后自动完成服务器应用更新打下基础。

## 创建 Secret

文档里写得很清楚：creating encrypted secrets for a repository，按步骤操作即可。到 learn-mongo 仓库点 Settings，左侧最下面找到 Secrets，点进去就能创建。点 New repository secret，格式是 Name 和 Value。

我这里已经添加好了四个值：三个和 SSH 登录相关（host、user、pwd），还有一个 mySecret，是要写入服务器文件的秘密。注意：任何 secret 写入后就再也看不到原始值了，只能 update 或 remove。我写入了一行特殊的英文字符串，一会儿就能看到。

## SSH Remote Commands action

有了 secret 之后要登录服务器。不需要自己写，选一个现成的 action：SSH Remote Commands，目前最流行的实现 SSH 功能的 action，使用非常简便。它支持的参数有 host、port、username、password，正是登录服务器需要的一系列参数，和我们在 secrets 里添加的值一一对应。

新建 workflow 文件 test-secrets.yaml：

```yaml
name: Test Secrets
on: push
jobs:
  secrets-ssh-actions:
    runs-on: ubuntu-latest
    steps:
      - uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USER }}
          password: ${{ secrets.PWD }}
          script_stop: true
          script: |
            pwd
            ls -l
            touch secret.txt
            echo ${{ secrets.MY_SECRET }} >> secret.txt
```

steps 第一步就是 uses 这个 action，名称是 appleboy/ssh-actions，它这里用的是 branch 名称（master）而不是版本号。参数用 with 提供：访问已创建的 secret 时，和之前一样用美元符号加两个花括号，里面有一个自动注入的变量叫 secrets，后面接 secret 的名称。这个写法要特别注意，不要写错。

再加一个参数 script_stop：意思是一旦发生错误就停止执行后面的命令。注意如果服务器禁止了用户名密码登录，它也支持 ssh key 的登录形式，具体参考它的文档即可，这里用用户名密码方式。

script 参数支持在服务器上直接运行脚本，多行的话用竖线（literal block），文档最下面也有对应的例子，可以支持多个命令。我们的脚本：`pwd` 看看文件夹在哪、是否在服务器上；`ls -l` 看看有什么文件；然后 `touch secret.txt` 创建文件，`echo` 把 secret 写进去，script 里同样能访问 secrets 变量。

## 运行验证

workflow 写完，要点回顾：一是 secrets 的使用，`secrets.名称` 就能访问对应的秘密；二是 SSH action 的使用，这个 action 很好用，后面会多次用到；script 里可以运行多行脚本。

commit（test ssh and secret）后 push，到仓库的 Actions 页面查看：运行已经完成（21 秒前），点进去看具体步骤。重点是 Run 部分：第一个输出 pwd 显示一个文件夹路径（部分信息被隐藏）；ls -l 的输出里能看到 opsflow-backend 和 logs 这两个文件，说明已经成功登录到服务器并能执行命令。

再看秘密是否写入了服务器文件：登录服务器查看，文件创建成功，内容就是我们写的 "you found me"，说明 secret 可以被成功写入服务器文件。

这节课了解了 secrets 的用法，它为在 workflow 中保存私密信息提供了可能。
