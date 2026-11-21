# 14-27-Docker Build 提高构建速度

上节课减小了镜像的大小，这节课优化构建速度。构建镜像的过程中最费时的步骤是 npm install 安装依赖。但两次代码修改之间，添加或删除依赖并不是常见操作，即使没有修改依赖，只是改了一部分源代码，每次也会重新安装一遍 npm 包，费时费力。我们希望把这部分时间优化掉。

## 层与缓存机制

要解决问题，先了解镜像的组成。和传统的 ISO 镜像文件不一样，Docker 采用了独特的分层技术：构建时一层层地构建，前一层是后一层的基础，每一层构建完就不会再发生改变，后一层的任何改变只发生在自己这一层。

自定义 image 由 Dockerfile 构建而来，其中每一条指令就构成 image 的一层。比如 FROM node 的基础镜像，它自己也有 Dockerfile，里面也是一系列指令、多个层；它的层加上我们的层，就构成了整个 Docker Image 的分层结构。

实际 build 一次就能看到这些步骤：输出里的 `1/6`、`2/6` 说明它一层层执行，有些层前面显示 cached，很快就完成了。也就是说 Docker Engine 会在本地文件系统缓存一系列层的信息。用 `docker system df` 可以看到系统中有多少缓存，其中 build cache 就是这些层的信息。我们的电脑上已经有 21GB 的缓存了，所以要时常清理，不然会吃掉大量容量。再次 build 时，如果操作没有任何修改，就会直接使用缓存中的结果。

验证一下：先把 build 好的 image 删掉再 build，因为有缓存，构建很快完成。但假如对代码做一点点修改（比如在 home.ts 里加一个变量），删掉 image 再 build：前面三层还是 cached，到了第四步 COPY 这里，第五步就开始重新安装依赖了。

原因是层的 cache 机制：COPY 时发现文件变化，这一层的缓存失效，从它往下的一系列缓存全部失效，后面的层都要重新运行，自然也包括 npm install。所以问题变成：一般文件的修改我们不希望触发 npm install 重新执行，只有 package.json 有修改时才执行。

## 单独拷贝依赖文件，将安装提前

解决办法：先单独拷贝依赖文件并安装，再把整个项目拷进去。这样只有 package.json 变化才会让安装层失效。调整 Dockerfile 的指令顺序：

```dockerfile
COPY package.json package-lock.json ./
RUN npm install --registry=https://registry.npm.taobao.org
COPY . .
RUN npm run tsc
CMD [...]
```

只 COPY 两个与版本相关的文件（package.json 和 package-lock.json），先安装依赖，然后再 COPY 整个项目，最后 npm run tsc 并启动。

做一个简单测试：先做一次全新构建（新镜像必然完整构建，要稍等一会儿）。构建完成后，把之前的代码修改加上去，预期是 npm install 不会重新执行。再 build 一次，可以看到 `npm install` 直接被 cache 掉了，没有变化；到 COPY 之后才有变化，所以只有 npm run tsc 被执行，整个安装过程被跳过。

现在的时间比之前快得多。这节课学习了 Docker 构建优化，理解了层（layer）的概念，并根据层的缓存机制完成了优化，构建速度比原来快得多。
