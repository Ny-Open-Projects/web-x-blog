# Go 企业级抽奖项目: 定义抽奖服务的 Thrift 文件

## 纲要

- Thrift 定义文件（IDL）的作用：统一描述数据结构与服务接口，作为多语言代码生成源头
- 通过 `namespace` 为不同语言声明各自的包名
- 定义两个数据结构：`DataGiftPrize`（中奖奖品信息）与 `DataResult`（抽奖返回值）
- 定义服务 `LuckyService` 及其两个方法：`DoLucky`（抽奖）与 `MyPrizeList`（获取中奖列表）
- 字段必须带序号，复合类型 `list<DataGiftPrize>` 用于返回集合

## Thrift 文件放在哪里

定义文件需要保存到 `thrift` 目录下，文件名为 `lucky.thrift`（注意扩展名是 `.thrift`）。整个抽奖系统的 RPC 接口契约都集中在这一个文件里，后续所有语言的代码都从它生成。

## 声明命名空间

Thrift 通过 `namespace` 为每一种目标语言指定对应的包名。我们课程里用到的有 Go、PHP、Java，它们统一叫 `rpc` 这个包：

```thrift
namespace go rpc
namespace php rpc
namespace java rpc
```

这意味着生成的代码在 Go 里属于 `rpc` 包，在 PHP 里也属于 `rpc` 命名空间。在代码目录里，我们也会用一个 `rpc` 目录来保存生成出来的文件。

## 定义数据结构

抽奖接口涉及两种核心数据。

### 中奖奖品信息 DataGiftPrize

对应数据库里的一条奖品记录，字段类型和 Go 结构体很接近，定义时每个字段都要带一个序号（从 1 开始），并可以给出默认值：

```thrift
# 奖品详情
struct DataGiftPrize{
    1: i64    Id             = 0
    2: string Title          = ""
    3: string Img            = ""
    4: i64    Displayorder   = 0
    5: i64    Gtype          = 0
    6: string Gdata          = ""
}
```

- `Id`：奖品 ID，`i64`（64 位整数）类型。
- `Title`：奖品名称，`string` 类型。
- `Img`：奖品图片地址。
- `Displayorder`：展示排序。
- `Gtype`：奖品类型（如优惠券、实物等）。
- `Gdata`：奖品附属数据，比如优惠券兑换码。

### 抽奖返回值 DataResult

`DataResult` 比 `DataGiftPrize` 略复杂一点，它包含一个 `Code` 状态码、一个 `Msg` 消息，以及一个嵌套的 `DataGiftPrize` 奖品信息：

```thrift
# 返回值
struct DataResult{
    1:i64           Code
    2:string        Msg
    3:DataGiftPrize Gift
}
```

嵌套结构在 Thrift 里是天然支持的——`Gift` 字段的类型直接引用前面定义的 `DataGiftPrize`。

## 定义服务与接口

Thrift 用 `service` 关键字定义服务，服务名我们用 `LuckyService`，内部定义两个方法。方法参数同样需要带上序号。

```thrift
# 服务接口
service LuckyService {
    # 抽奖的方法
    DataResult DoLucky(1:i64 uid, 2:string username, 3:string ip, 4:i64 now, 5:string app, 6:string sign),
    list<DataGiftPrize> MyPrizeList(1:i64 uid, 2:string username, 3:string ip, 4:i64 now, 5:string app, 6:string sign),
}
```

### DoLucky：执行抽奖

参数说明：

| 序号 | 类型 | 名称 | 含义 |
| --- | --- | --- | --- |
| 1 | `i64` | `uid` | 用户 ID |
| 2 | `string` | `username` | 用户名 |
| 3 | `string` | `ip` | 用户操作 IP |
| 4 | `i64` | `now` | 当前时间戳（秒或纳秒） |
| 5 | `string` | `app` | 调用方应用名称 |
| 6 | `string` | `sign` | 签名信息，防止参数被篡改 |

这些参数和我们之前 Web 接口里的登录用户校验信息一致：既要识别“是谁在抽奖”，也要识别“是哪个应用发起的调用”。返回值是 `DataResult`。

### MyPrizeList：获取中奖列表

返回值是 `list<DataGiftPrize>`，即该用户的中奖信息集合。参数与 `DoLucky` 保持一致，同样用于身份识别与调用方识别。

## 完整的 lucky.thrift 文件

把上面的内容合并，完整的 IDL 如下（可直接用于代码生成）：

```thrift
namespace go rpc
namespace php rpc
namespace java rpc

# 奖品详情
struct DataGiftPrize{
    1: i64    Id             = 0
    2: string Title          = ""
    3: string Img            = ""
    4: i64    Displayorder   = 0
    5: i64    Gtype          = 0
    6: string Gdata          = ""
}
# 返回值
struct DataResult{
    1:i64           Code
    2:string        Msg
    3:DataGiftPrize Gift
}

# 服务接口
service LuckyService {
    # 抽奖的方法
    DataResult DoLucky(1:i64 uid, 2:string username, 3:string ip, 4:i64 now, 5:string app, 6:string sign),
    list<DataGiftPrize> MyPrizeList(1:i64 uid, 2:string username, 3:string ip, 4:i64 now, 5:string app, 6:string sign),
}
```

定义文件的书写要点回顾：先定义 `namespace`，再定义涉及的数据结构 `struct`，最后用 `service` 把方法包起来。方法之间保持一行一个、用逗号分隔，整体清晰易读。下一讲我们用这个文件生成 Go 与 PHP 代码。

## 总结

本讲完成了抽奖服务 Thrift 契约的定义：`lucky.thrift` 通过 `namespace` 统一多语言包名，用两个 `struct` 描述中奖信息与返回值，再用 `service LuckyService` 声明 `DoLucky` 与 `MyPrizeList` 两个接口。这份 IDL 是整个 RPC 开发的基础。

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/lottery/thrift/lucky.thrift`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：[是]。代码是否可运行：[是]。
