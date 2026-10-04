# web-x-blog

> **个人创作者工作空间** —— 技术内容生产流水线。
> 仓库里只分两块：**`work/` 管干活，`ai/` 管 agent。**

## 目录约定

| 路径 | 角色 | 说明 |
| --- | --- | --- |
| `work/` | **工作目录** | 所有实际操作与产出都在这里，不往仓库根放业务文件 |
| `work/source/` | **机器翻译的结果**（输入） | 机翻稿，**只读取，不改不删** |
| `work/target/` | **agent 转换后的目录 = 主工作目录** | 拆题 / 纠错 / 质检全在这里落盘 |
| `work/blog/` | **hexo 站点** | 把 target 内容**分类**后生成静态站，本地起服务预览 |
| `ai/` | **agent 层** | 交接文档、prompt、模板、记忆、技能，**全部集中在这里** |

## 生产链路

```
work/source（机翻结果） → work/target（agent 转换） → work/blog（hexo 站点）
      只读取               agent 主工作目录              分类后发布
```

- `source` 只进不出，机翻结果锁死
- `target` 是 agent 的主战场，所有转换结果归位到这里
- `blog` 是出口，靠 `categories / tags` 把 target 的东西分类成站

## 接手 / 执行

任何 agent 接手本仓库，**先读 `ai/AGENTS.md`**（事实源在 `ai/`，根目录这份只做指针）。
