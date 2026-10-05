# Go PaaS 平台开发: Go Module 代理与私有仓库配置

## 纲要

- 为何需要单独配置 Go Module：私有仓库与代理并存
- 设置 `GOPROXY` 加速公共包拉取
- 设置 `GOPRIVATE` 让私有仓库绕过代理、走直接连接
- 配置 `git` 的 `insteadOf` 解决慕课网 SSH 端口（80）问题
- 生成并配置 SSH 密钥完成私有仓库鉴权
- 通过 `go get` 验证配置是否生效

## 为什么需要单独配置

本 PaaS 平台采用多服务（微服务）架构，各服务之间以 Go Module 方式互相引用。课程代码托管在慕课网的私有仓库（如 `git.imooc.com/coding-535/...`），这与公共的 GitHub 包存在本质区别：

- 公共包需要通过代理加速；
- 私有包不能走代理（代理不会做私有权限校验），必须直连且带鉴权。

如果配置不当，会导致私有仓库地址无法拉取、或公共包拉取缓慢。因此开写代码前必须先把模块与代理环境打通。

## 设置 GOPROXY

设置代理后，从 GitHub 拉取依赖会明显加快：

```bash
go env -w GOPROXY=https://goproxy.cn,direct
```

`goproxy.cn` 为国内常用公共代理，`direct` 表示代理不可达时直连源站。

## 设置 GOPRIVATE

将课程私有仓库域名加入 `GOPRIVATE`，使其**跳过代理**并保留鉴权：

```bash
go env -w GOPRIVATE=git.imooc.com
```

一旦设置，任何以 `git.imooc.com` 为域名的模块都会直连，不再经过 `GOPROXY`，从而避免私有仓库权限校验失败。

## 配置 Git 的 insteadOf（SSH 端口转换）

慕课网私有仓库使用 SSH 方式，但其 SSH 端口是 **80** 而非默认的 22。通过 `git config` 的 `insteadOf` 把默认 SSH 地址统一改写为带 80 端口的地址：

```bash
git config --global url."ssh://git@git.imooc.com:80".insteadOf "https://git.imooc.com"
```

这样无论后续以 HTTPS 还是 SSH 形式书写仓库地址，都会被替换为正确的 `ssh://...:80` 形式，无需记忆特殊端口。

## 生成并添加 SSH 密钥

在开发机或需要拉取代码的服务器上生成密钥，并添加到慕课网账户（右上角"用户设置 → 密钥 → 添加密钥"）：

```bash
ssh-keygen -t rsa -C "your_email@example.com"
# 将 ~/.ssh/id_rsa.pub 的内容复制到慕课网的密钥添加框
```

## 验证配置

在本机拉取一次课程代码，或在 `go mod` 初始化后执行 `go get` 验证：

```bash
go get git.imooc.com/coding-535/pod
```

若能成功拉取且不报鉴权错误，说明代理与私有仓库配置已打通。后续各服务在 API 层调用其它服务时，可直接以远程模块方式引入。

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/go-paas-html/pages-404.html`
- `code/课件/go-paas-html/pages-forgot-password.html`
- `code/课件/go-paas-html/pages-login.html`
- `code/课件/go-paas-html/pages-login2.html`
- `code/课件/go-paas-html/pages-sign-up.html`
- `code/课件/go-paas-html/layouts-nosidebars.html`
- `code/课件/go-paas-front/volume-create.html`
- `code/课件/go-paas-front/route-create.html`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：否。
