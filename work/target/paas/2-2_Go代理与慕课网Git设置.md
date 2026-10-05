# Go PaaS 平台开发: Go 代理与私有仓库 Git 设置

## 纲要

- 为什么要设置 Go 代理：加速从公网（如 GitHub）拉取模块，避免链路慢、超时
- `GOPROXY`：配置公共模块代理（如 `goproxy.cn`），`go get` / `go mod` 默认走代理
- `GOPRIVATE`：声明私有模块前缀，使其跳过代理与校验数据库（sumdb）
- 私有仓库拉取：通过 `git config` 的 `url.<base>.insteadOf` 把 HTTPS 重写为 SSH，并携带非标准端口
- 校验方式：`go env` 查看环境变量、`go mod tidy` 触发实际下载验证

## 为什么需要 Go 代理

日常开发中大量依赖从公网代码托管平台拉取。若不配置代理，模块下载链路长、速度慢、容易超时。设置 Go Module 代理后：

- `go get` 与 `go mod download` 默认经由代理下载，速度大幅提升
- 代理仅面向**公共仓库**生效；私有仓库需要单独绕开代理

## 设置公共模块代理

通过 `go env -w` 写入全局环境变量：

```bash
# 配置公共代理，direct 作为兜底（允许直连）
go env -w GOPROXY=https://goproxy.cn,direct

# 关闭校验数据库（对公共代理的可选优化，按网络环境决定）
go env -w GOSUMDB=off
```

设置后，`go mod tidy`、`go get` 都会优先走该代理。可用 `go env` 查看当前生效值：

```bash
go env GOPROXY
go env GOSUMDB
```

## 私有仓库绕开代理

私有仓库需要鉴权，代理无法代为传递凭证，因此必须显式排除。关键环境变量是 `GOPRIVATE`，它同时会让匹配前缀的模块跳过 `GOPROXY` 与 `GOSUMDB`：

```bash
# 多个私有域名用逗号分隔
go env -w GOPRIVATE=git.example.com,github.com/your-org
```

这样既能加速公共模块下载，又不影响私有仓库的正常使用。

## 私有仓库的 Git 协议改写

部分私有代码平台（如课程所用的慕课网）使用 SSH 协议且端口并非标准 22，而是 80。此时 `go get` 内部基于 HTTPS 克隆会失败，需要通过 `git config` 把 HTTPS 地址重写为 SSH 地址：

```bash
# 将平台 HTTPS 地址统一改写为 SSH（端口 80 必须显式写出，不可省略）
git config --global url."ssh://git@git.imooc.com:80".insteadOf "https://git.imooc.com/"
```

要点：

- 端口 `:80` 必须带上，与平时可省略的 `:22` 不同
- 该命令只需在本机执行一次，作用域为全局 Git 配置

此外，还需把本机 SSH 公钥添加到平台账号的后台「用户设置 → SSH 密钥」中，否则无法以 SSH 方式拉取私有仓库。

## 验证配置

```bash
# 查看 Go 环境变量，确认 GOPROXY / GOPRIVATE 已生效
go env

# 进入工程目录，触发依赖下载以验证代理与私有仓库均可用
go mod tidy
```

若 `go mod tidy` 能够顺利下载公共依赖、并成功拉取私有模块，说明代理与私有仓库配置均已正确完成。

## API 速览

| 环境变量 | 作用 | 示例 |
| --- | --- | --- |
| `GOPROXY` | 模块下载代理地址，`direct` 表示直连 | `https://goproxy.cn,direct` |
| `GOSUMDB` | 校验数据库，可设为 `off` 关闭 | `off` |
| `GOPRIVATE` | 私有模块前缀，跳过代理与 sumdb | `git.example.com` |

| Git 命令 | 作用 |
| --- | --- |
| `git config --global url."<ssh>".insteadOf "<https>"` | 把 HTTPS 克隆地址改写为 SSH |

## Demo 示例

运行说明：在已安装 Go 与 Git 的终端执行，将示例域名替换为你的实际私有平台域名。

代码说明：下面给出一组可直接套用的配置命令，完成「公共走代理、私有走 SSH」的完整设置。

```bash
# 1. 公共模块走代理
go env -w GOPROXY=https://goproxy.cn,direct
go env -w GOSUMDB=off

# 2. 私有模块绕开代理
go env -w GOPRIVATE=git.imooc.com

# 3. 私有平台使用 SSH（端口 80）而非默认 HTTPS
git config --global url."ssh://git@git.imooc.com:80".insteadOf "https://git.imooc.com/"

# 4. 验证
go env
go mod tidy
```

技术点总结：

- `GOPROXY` 解决公共依赖下载慢的问题，`GOPRIVATE` 解决私有依赖鉴权问题，二者配合互不冲突
- 私有平台若使用非标准 SSH 端口，必须借助 `git config` 的 `insteadOf` 完成协议改写
- 配置完成后用 `go mod tidy` 做一次真实下载，是验证环境是否就绪的最直接手段

## 总结

相关度：100%。是否需要继续：是。代码是否可运行：是。
