# 19-5-5-使用gzip压缩对应的HTTP请求资源

这节课讲一个重要且非常有效的 HTTP 传输优化方案：采用对 HTTP 请求非常友好的压缩算法 gzip，很多人应该都对它比较熟悉了。

## gzip 命令

先看维基百科的定义：gzip 是一种压缩文件格式，也是一个类 Unix 上面的文件压缩软件，是 Unix 系统上面的一个标准命令。用 man ls 一类的命令可以看到，它是 using LZW77（LZ77）编码算法的压缩和解压缩工具。

来实际使用一下。看 Ant Design Vue 里面添加的一个文件（npm 目录下的 ant-design-vue），它是 451KB。调用 gzip 对它进行压缩：

```bash
gzip ant-design-vue.js
```

回车之后压缩完毕。再看文件大小：原始的文件不存在了，剩下了一个 .gz 后缀名的文件，只有 108KB。从 451KB 压缩到了 108KB，是一个高效率的压缩比。

可以用 `gzip -d` 把它恢复回去，d 就是 decompression，解压。执行之后文件又恢复到 451KB。

## 与 HTTP 请求的挂钩

这个命令是怎样和 HTTP 请求挂钩的？根据 HTTP 官方的定义（维基百科上 HTTP Compression 的专题），有一份 Content-Encoding Tokens 的官方列表，列出服务器和客户端可用的压缩和解压缩算法，其中就包括我们要用的 gzip，它也是使用最多的算法之一。也就是说，HTTP 请求天生支持 gzip 的压缩方式：需要服务器在文件返回的时候进行压缩，浏览器接到文件的时候进行解压缩，就完成了整个流程。

## nginx 的 gzip 模块

首先让服务器支持对应的选项。nginx 有一个内置的 gzip module，有一系列选项来支持 HTTP 启用 gzip：

- gzip on：开启 gzip；
- gzip_min_length：启用 gzip 压缩的最小文件，小于设置值的文件不压缩，比如 1k 表示小于 1KB 的文件不使用 gzip 压缩；
- gzip_comp_level：压缩级别 1 到 9，数字越大压缩得越好，但越占用 CPU 时间；
- gzip_types：选择哪些文件类型进行压缩，类型叫 mime types，比如 application/javascript 就是 js 类型，还有各种图片等类型。

剩下的几个选项文档写得很清楚，不太重要，大家可以自己看。

给配置文件添加对应的选项，让服务器支持 gzip 压缩：

```nginx
gzip on;
gzip_types text/plain text/css application/json application/javascript application/x-javascript text/javascript text/xml application/xml application/rss+xml application/atom+xml image/svg+xml;
```

第一项是 gzip on 开启；第二项是 gzip types，也就是哪些文件需要被压缩，这个必须添加，因为默认只有 HTML 和 XML 是压缩的，需要把不同的文件类型都添加上。保存后重启服务器：`nginx -s reload`。

## 观察效果

重启完毕后到页面上观察。来到 OpsFlow 页面刷新，点击一个文件，也就是我们的 js 文件：会发现 response headers 里多添加了一个 content-encoding: gzip，告诉浏览器它使用了 gzip 进行压缩，看到这个头后浏览器要使用对应的算法进行解压缩。当然现在浏览器都支持 gzip 解压缩，但有一个浏览器大家都知道，神奇又古板的 IE6 不支持 gzip 解压缩，所以会有一个特殊的配置，禁用 IE6 的 gzip。

看一下效率：可以看到几项 compression，能看到它是使用 gzip 进行压缩的。再看 size，它有两个值：上面的值是 transferred over network，第二个是 resource size。第一个就是传输过程中耗费的流量，这里是 139KB；462KB 是真正的 resource size，也就是文件的大小。压缩比就是 462 除以 139，和刚才命令行的演示类似，压缩效果比较可观。

所以我认为采取 HTTP 启用 gzip 压缩是一种非常简单有效的提升速度的方式，大家在做任何项目的时候，服务器配置一定要注意将它打开。

HTTP 请求既然支持这么多的压缩算法，那 gzip 是最优的解决方案吗？下节课我们一起来看看还有没有比 gzip 更有意思的压缩算法。
