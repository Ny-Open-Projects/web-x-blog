# 18-4-2-使用 qrcode 将渠道链接生成二维码

这节课来添加二维码的展示。要生成二维码，先要确定把哪个链接渲染为二维码。任何一个渠道展示的 URL 都有固定的规则，这是后端定死的。整个 URL 的格式是这样的：前面是 IP 地址加端口，称为 baseH5URL。它跟后端 RESTful API 的请求地址很类似，只不过端口号是 8082，这个端口专门用来渲染 H5 页面。接下来是 `/p/`，这是定死的；然后是 232，也就是 pageId，从配置上拿到的数据；再后面是配置上的另一个属性 uuid，它是唯一性标识，这个字段之前还没有加。最后是 `?channel=102`，102 就是 channelId，即新创建渠道时返回的 ID。

知道了规则，就可以添加对应的 URL 了。首先在 main.ts 中添加并 export 出 baseH5URL，一个是 8081，一个是 8082。然后在 editor.ts 的 PageData 中多添加一项 uuid，类型是 string，之前没有用到这个值所以没有添加。

接着在 PublishForm 中生成 URL。创建一个函数 generateChannelURL，接收一个 number 类型的 id，直接返回一个模板字符串，把 baseH5URL 导入进来拼进去。函数返回后，在 template 里做替换，把 channelId 传进去。

发布一次验证效果：URL 成功生成了，和约定的格式完全一样。channelId、pageId、pageUUID 都在，两个不同的渠道生成了两个不一样的 URL，只有 channel 部分不同。第一步工作完成，现在可以用生成的 URL 来渲染二维码了。

生成二维码的第三方库有两个备选方案。第一个是 QRCodeJS，它是我之前第一版方案用的库，但问题是维护不积极，很多 bug 没有修复，issues 有一百四十多个，上一次发版本还是六年前，npm 一周下载只有一万五千多次，已经不是好的选择。另一个更好的方案是 node-qrcode，它有 4.8k 的 star，支持多端：server 端（node）和客户端（浏览器）都能用，API 非常丰富，可以生成多种格式的文件，维护也更积极，一周下载达到二十多万次，所以我们选定它。

简单看一下它的用法，直接跳到 API 部分。API 分 browser 和 server 两套，browser 的稍微少一些。想把二维码渲染到一个元素上，使用 toCanvas 这个 API。它有几个参数：第一个是 canvas element，即一个 DOM 节点；第二个是 text，要渲染的链接或字符串；第三个是 options，一系列选项，我们先不管，通过 TS 定义文件可以直接看到；最后还有一个 callback，告诉你成功和失败，这是 NodeJS 风格的设计。后期可以把它转换成 Promise，不过实际上它已经自带 Promise 写法，不需要改写了。

安装 qrcode 时要特别注意：它不自带类型文件，安装完本体之后要单独安装 `@types/qrcode`。

代码上分三步。第一步添加容器，把之前的位置改成一个 canvas 元素，并给它一个独特的 ID，因为每个渠道的 ID 不一样，toCanvas 需要一个 DOM 节点。我这里用模板字符串：`channel-barcode-${channel.id}`。第二步导入库：`import QRCode from 'qrcode'`。第三步决定渲染时机，自然是在 onMounted 的时候。因为有多个二维码，所以要循环 channels.value，forEach 每一项是 channel。

循环里先获取节点，称之为 ele，用 `document.getElementById` 拿到之前定义的 `channel-barcode-${channel.id}`。注意做类型断言 `as HTMLCanvasElement`，因为 toCanvas 的第一个参数要求是 canvas element。然后是关键的渲染部分：`QRCode.toCanvas(ele, generateChannelURL(channel.id), { width: 100 })`。options 里可以配置 margin、scale、width、color 等，我们只设置 width 为 100。它返回 Promise，可以直接调用 then 打印 success。

页面上验证：二维码已经出现了。用手机扫一下会发现，URL 最后显示的就是编辑器中间的那一系列元素。现在我们就可以成功生成二维码了。针对二维码还有一些优化工作，下节课来完成。
