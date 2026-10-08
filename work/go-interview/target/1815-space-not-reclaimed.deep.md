## 思路与架构
```text
排查总思路：df 显示满、du 对不上 → 文件已删但块未释放，按"引用是否还在"分四类：
1. 进程占用：有 fd 持有 → lsof +L1 定位，关进程或 truncate 回收
2. 伪删除：rm 被别名成 mv 到 /tmp → type rm 确认，清 /tmp
3. 硬链接：i_nlink>1 → ls -l 看计数，find -inum 找全，删光
4. 回收站：桌面/图形界面删除 → 清空回收站
架构本质：Linux 释放数据块 = "目录项引用归零 且 进程 fd 引用归零"（i_nlink=0 且 i_count=0）
```

## 方案取舍
```text
回收手段取舍：
- 能停进程：直接重启/kill 占用进程，fd 释放最干净（首选）
- 不能停进程：truncate 清空内容回收，业务无感（次选，留 fd）
- 防误删优先：rm 别名 mv /tmp，代价是"假删除"误导排查（运维权衡）
- 硬链接场景：必须找到并删光所有硬链接，否则空间永久占（易漏）
取舍原则：先 lsof 定位占用（最高频），再依次排除伪删除/硬链接/回收站
```

## 答题技巧
```text
技巧1：先抛"删除≠释放"的核心机制（unlink + fd 引用计数），建立底层认知再分情形
技巧2：用 df/du 不一致作为切入信号，自然引出"已删打开文件"现象
技巧3：四类情形各给一个定位命令（lsof / type rm / ls -l / 回收站），显排查体系
技巧4：收尾强调"i_nlink=0 且 i_count=0 才释放"，一句话封口
```

> 边界：inode 机制本体见 `1814-inode-basics`；各单情形见 `1815-file-deleted-space-held`/`1815-truncate-reclaim`/`1815-pseudo-delete-mv-tmp`/`1815-hardlink-space-held`。
