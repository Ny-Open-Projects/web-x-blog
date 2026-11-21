---
disableNunjucks: true
title: 14-35 使用 Github Actions Build 和 Push 镜像到 ACR
date: 2026-11-17 15:47:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课完成了第一步：构建并上传镜像；第二步用一个单独的 docker-compose 文件启动应用，这样不需要任何其他依赖，通过一个简单的文件就能启动整个应用。现在要用 GitHub Actions 模拟这个流程。整体可以分为两步：第一步在 runner（GitHub 的服务器）上 build image 并 push；第二步使用 docker-compose-online 配置文件在服务器上运行应用。一个在 GitHub 服务器，一个在我们自己的服务器。

## 步骤分析

这节课完成第一步。细化后的步骤：

1. checkout 代码，把代码拉下来（在 GitHub 服务器上）。
2. 特别注意、容易被忽略：服务器上没有本地的那些文件，需要创建 .env 文件。这两个环境变量是 upload to OSS 需要的信息，其他不需要。看代码里上传生成的文件到 OSS 的部分就能确认，所以这里要添加对应的 secret。
3. 使用阿里云 ACR 完成 docker login，然后用阿里云的 tag 进行 docker build。这里有一个特殊问题：每次 push 都要生成一个和 commit 相关的特殊 tag。这节课先不解决，标记为后续要解决的问题。
4. 调用 docker push。

所以需要四个环境变量：两个是 OSS 的 secret（access key 和 secret key），另外因为是 docker login，还需要 ACR username 和 ACR password，请大家自己去创建这四个 secrets。

写 workflow 需要耐心：尤其对初学者，经常有意想不到的 bug，很可能多次提交代码。建议调试期间建一个新 branch（比如基于 week17 创建 week17-test），在这里多次提交测试 action 的行为；调通后再把对应的 commit cherry-pick 到 week17，避免冗余的 commit 污染代码库。

## 编写 push-image.yml

在 .github/workflows 下创建 push-image.yml：

```yaml
steps:
  # checkout 对应的代码
  - uses: actions/checkout@v2

  # 创建 .env 文件
  - name: Create env file
    run: |
      touch .env
      echo "ALIYUN_ACCESS_KEY=${{ secrets.ACCESS_KEY }}" >> .env
      echo "ALIYUN_SECRET_KEY=${{ secrets.SECRET_KEY }}" >> .env

  # 登录到阿里云 ACR
  - name: Log into Aliyun ACR
    uses: aliyun/acr-login@v1
    with:
      login-server: https://registry.cn-hangzhou.aliyuncs.com
      region-id: cn-hangzhou
      username: ${{ secrets.ACR_USERNAME }}
      password: ${{ secrets.ACR_PASSWORD }}

  # build image for Docker
  - name: Build image for Docker
    run: docker build --tag <registry地址>/<命名空间>/<仓库>:0.0.2 .

  # push to ACR
  - name: Push image to ACR
    run: docker push <registry地址>/<命名空间>/<仓库>:0.0.2
```

要点：

- 创建 .env 时用 touch 先建文件，再用 echo 把字符串追加进去。追加用 `>>`：一个 `>` 是 overwrite，直接重写文件（再写一次会把原始内容覆盖掉）；两个 `>>` 是 append，一直往里添加。我们要一直用 `>>` 把环境变量一一添加进去。
- 登录 ACR 阿里云提供了现成的 action，叫 Alibaba Cloud Container Registry (ACR) login，参数有 login-server（从文档直接复制地址，比如 cn-hangzhou）、region-id（同样是 cn-hangzhou）、username 和 password（都从 secrets 取）。
- build 的命令就是上节课写过的 `docker build --tag ...`，比较长，注意别写错。版本号这节课先写死：之前测试过 0.0.1，现在用 0.0.2（选一个没用过的版本就行）。commit 相关的自动 tag 后面再解决。
- push 命令与上节课一致，特别注意网址别写错，版本号要与上面对应。

另外修改一下 Dockerfile：原来 npm install 加了淘宝镜像源参数，那是本地构建用的；现在构建发生在 GitHub 服务器上，直接 npm install 即可，GitHub 服务器上没有访问限制，其实会更快。

## 运行验证

检查完步骤后 push（在 week17-test 分支 commit "test aliyun ACR push image"）。push 成功后到 Actions 页面，点开这个 job 看运行流程。发现运行到 build image for Docker 时时间最长，因为要执行 npm install，耐心等待。job 运行完毕是绿色，说明成功了。点开每一步看结果：build 的 log 最长（步骤多），最后上传成功；push image to ACR 里也有推送成功的输出。最后到 ACR 页面检查：0.0.2 版本已经 push 成功并出现在列表中，时间正是刚刚推送的。

自动化部署的第一步（构建并 push 镜像）就完成了。其实流程就是把本地的操作整理出来，用脚本一个个完成。第一步任务到此结束。
