#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重建 mksz824 knowledge_graph v2。

原图（47 节点/120 边）随外接盘目录灭失（废纸篓被清空），依据 _SCANS/PASS3.md 的
实测证据重建：22 章节点 + 25 个补录技术点 + 7 个代码模块 + 引用的既有概念；
删除 PASS3 判定的 4 条幽灵/弱边，补齐 6 类缺边。每条边带 evidence。

产出：work/target/mksz824/_SCANS/knowledge_graph_v2.json
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "work" / "target" / "mksz824" / "_SCANS" / "knowledge_graph_v2.json"

CHAPTERS = {
    1: "课程简介", 2: "需求分析与架构设计", 3: "B端项目需求分析与架构设计",
    4: "前端基础技术回顾（TS/Vue3）", 5: "项目整体搭建（Vue CLI/Vite/Vuex/Router）",
    6: "编辑器基本布局与业务组件库", 7: "单元测试与 TDD（Jest）",
    8: "通用上传组件开发", 9: "组件库打包发布（Rollup）与 CI",
    10: "后端技术选型（Koa2/Egg/MongoDB）", 11: "MongoDB 与 egg-mongoose",
    12: "用户系统（Cookie/Session）", 13: "文件上传/流处理/SSR/权限",
    14: "Docker 部署与 GitHub Actions CI/CD", 15: "低代码核心：裁剪/画布/组合式函数",
    16: "编辑器画布交互", 17: "前后端整合（Mock/axios/鉴权）",
    18: "B 端功能（html2canvas/二维码/下载）", 19: "编译部署与性能优化（Webpack/Nginx）",
    20: "Nuxt3 管理系统基础", 21: "Nuxt3 进阶实战", 22: "Nuxt3 收尾与部署（PM2/Bun）",
}

# PASS3 少漏 25 点：id, 名称, covers 章节, 关联模块
NEW_POINTS = [
    ("C_vue_router", "Vue Router（嵌套路由/守卫/权限验证）", [5, 17], []),
    ("C_vuex", "Vuex 状态管理（module/action/mutations 测试）", [5, 6, 16, 17], ["mod_opsflow-web"]),
    ("C_vite", "Vite（创建项目/与 Vue CLI 对比）", [4, 5], []),
    ("C_webpack", "Webpack 工程化深入（手写 loader/plugin/分包/懒加载）", [19], []),
    ("C_rollup", "Rollup 与组件库打包（UMD/ESM/Vue 插件/npm link）", [9], ["mod_opsflow-ui"]),
    ("C_fe_eng", "前端工程化规范（ESLint/Prettier/Git Flow）", [4, 5], []),
    ("C_tdd", "TDD 与 Jest mock 体系（timers/第三方/异步）", [7, 8], []),
    ("C_http_perf", "Web 性能优化（Nginx/HTTP 缓存/gzip/Brotli/HTTP2）", [19], []),
    ("C_envs", "多环境与环境变量（mode/.env）", [14, 19, 20], []),
    ("C_node_proc", "Node 进程模型（Cluster/Egg 多进程/压测）", [14], ["mod_opsflow-server"]),
    ("C_docker_sub", "Docker 细分（Dockerfile/compose/镜像优化/YAML）", [14], []),
    ("C_gha_sub", "GitHub Actions 细分（Secrets/ACR/自动部署+回滚/release-it）", [14], []),
    ("C_server_ops", "云服务器运维（SSH key 免密/Linux 装机）", [14], []),
    ("C_stream_img", "流与图片处理（Sharp/Stream/busboy/egg-multipart）", [13], ["mod_opsflow-server"]),
    ("C_cropperjs", "CropperJS 图片裁剪", [15], []),
    ("C_publish_lib", "B 端发布工具库（html2canvas/qrcode/Clipboard/FileSaver）", [18], []),
    ("C_composable", "Vue3 组合式函数复用（usePublishWork/useLoadMore 等）", [15, 17, 18], []),
    ("C_mock", "Mock 联调（JSON Server + JWT mock）", [17], []),
    ("C_form_validate", "表单验证体系（egg-validate/错误码/AForm 源码）", [12, 17], []),
    ("C_session", "Session 体系（Cookie/egg-session/koa-session/bcrypt）", [12], []),
    ("C_mongo_adv", "MongoDB 进阶（索引/$lookup/egg-mongoose 源码/插件抽象）", [11], []),
    ("C_nuxt_sub", "Nuxt3 细分（渲染模式/Nitro/存储层/SEO）", [20], []),
    ("C_nuxt_eco", "Nuxt 生态（Zod/VeeValidate/NuxtUI/Tailwind）", [21], []),
    ("C_admin_deploy", "管理系统部署（Nuxt 构建/PM2/Bun）", [22], []),
    ("C_publish_flow", "业务闭环：作品发布/展示渠道/H5 渲染链路/自动保存", [13, 17, 18], []),
]

MODULES = ["mod_opsflow-web", "mod_opsflow-ui", "mod_opsflow-server",
           "mod_opsflow-admin", "mod_mongo-lab", "mod_ts-lab", "mod_vue-starter"]

# 既有概念（原图既有 ID，v2 保留并按 PASS3 修正连接）
EXISTING_CONCEPTS = ["C_vue2", "C_nuxt", "C_cicd", "C_docker", "C_test",
                     "C_auth", "C_mongo", "C_ssr", "C_upload", "C_oss", "C_editor"]

# 4 条幽灵/弱边（PASS3 建议删除，v2 不收录，留档 removed_edges）
REMOVED_EDGES = [
    {"edge": "ch18 -> C_nuxt", "reason": "第18章 30 篇 grep nuxt = 0 命中"},
    {"edge": "ch19 -> C_cicd", "reason": "第19章 grep 'github actions' = 0 命中"},
    {"edge": "ch19 -> C_docker", "reason": "仅 5-1 顺带回顾，非教学内容"},
    {"edge": "ch04 -> C_vue2 / ch05 -> C_vue2", "reason": "素材仅 2 处对比提及，降级为 mentions"},
]

# 6 类缺边补齐
EXTRA_EDGES = [
    ("C_ssr", "mod_opsflow-server", "generates", "第13章/13-23~13-27：SSR 产物由 server 生成并上传 OSS"),
    ("mod_opsflow-admin", "C_upload", "uses", "第22章/22-4~22-7：admin 上传组件传阿里云"),
    ("mod_opsflow-admin", "C_oss", "uses", "第22章/22-4~22-7"),
    ("mod_opsflow-admin", "C_admin_deploy", "deployed_by", "第22章/22-13~22-16：PM2/Bun，与 web 部署方式不同"),
    ("mod_opsflow-admin", "mod_opsflow-server", "depends_on", "第20~21章：admin 注册/登录/表格均打同一后端"),
    ("mod_opsflow-web", "mod_opsflow-server", "depends_on", "原图已有，v2 保留"),
]


def main() -> int:
    nodes, edges = [], []

    for no, name in CHAPTERS.items():
        nodes.append({"id": f"ch{no:02d}", "type": "chapter", "label": f"第{no}章 {name}"})

    for cid, label, chs, mods in NEW_POINTS:
        nodes.append({"id": cid, "type": "concept", "label": label, "origin": "pass3-gap"})
        for ch in chs:
            edges.append({"from": f"ch{ch:02d}", "to": cid, "rel": "covers",
                          "evidence": f"PASS3 表条目 {label}"})
        for m in mods:
            edges.append({"from": m, "to": cid, "rel": "uses", "evidence": f"PASS3 表条目 {label}"})

    for cid in EXISTING_CONCEPTS:
        nodes.append({"id": cid, "type": "concept", "label": cid, "origin": "original-graph"})

    for m in MODULES:
        nodes.append({"id": m, "type": "module", "label": m.replace("mod_", "opsflow-").replace("opsflow-mongo-lab", "mongo-lab").replace("opsflow-ts-lab", "ts-lab").replace("opsflow-vue-starter", "vue-starter"), "origin": "original-graph"})

    # mentions 弱边：Vue2 仅对比提及
    edges.append({"from": "ch01", "to": "C_vue2", "rel": "mentions", "evidence": "1-1 L229 仅对比提及"})
    edges.append({"from": "ch08", "to": "C_vue2", "rel": "mentions", "evidence": "8-15 L11 仅对比提及"})
    # Nuxt 主线边（原图 ch18→C_nuxt 删除，改为 ch20/21）
    edges.append({"from": "ch20", "to": "C_nuxt", "rel": "covers", "evidence": "第20章 Nuxt3 基础"})
    edges.append({"from": "ch21", "to": "C_nuxt", "rel": "covers", "evidence": "第21章 Nuxt3 进阶"})
    edges.append({"from": "ch22", "to": "C_nuxt", "rel": "covers", "evidence": "第22章 Nuxt3 收尾"})
    edges.append({"from": "ch14", "to": "C_cicd", "rel": "covers", "evidence": "第14章 14-30~14-40 GitHub Actions"})
    edges.append({"from": "ch14", "to": "C_docker", "rel": "covers", "evidence": "第14章 14-17~14-29 Docker"})
    edges.append({"from": "ch07", "to": "C_test", "rel": "covers", "evidence": "第7章 Jest 全章"})
    edges.append({"from": "ch12", "to": "C_auth", "rel": "covers", "evidence": "第12章 Cookie/Session"})
    edges.append({"from": "ch11", "to": "C_mongo", "rel": "covers", "evidence": "第11章 MongoDB"})
    edges.append({"from": "ch13", "to": "C_ssr", "rel": "covers", "evidence": "第13章 SSR 实现 H5"})
    edges.append({"from": "ch15", "to": "C_editor", "rel": "covers", "evidence": "第15章 编辑器核心"})
    edges.append({"from": "ch16", "to": "C_editor", "rel": "covers", "evidence": "第16章 画布交互"})
    edges.append({"from": "ch17", "to": "C_editor", "rel": "covers", "evidence": "第17章 整合后端"})
    edges.append({"from": "ch13", "to": "C_upload", "rel": "covers", "evidence": "第13章 上传"})
    edges.append({"from": "ch13", "to": "C_oss", "rel": "covers", "evidence": "第13章 阿里云 OSS"})
    edges.append({"from": "C_publish_flow", "to": "C_ssr", "rel": "chains_to", "evidence": "发布→渲染链路"})
    edges.append({"from": "C_publish_flow", "to": "C_oss", "rel": "chains_to", "evidence": "发布产物上 OSS"})
    edges.append({"from": "C_publish_flow", "to": "C_editor", "rel": "chains_to", "evidence": "编辑→发布闭环"})
    edges.extend([{"from": a, "to": b, "rel": r, "evidence": v} for a, b, r, v in EXTRA_EDGES])

    # 去重边
    seen, uniq = set(), []
    for e in edges:
        key = (e["from"], e["to"], e["rel"])
        if key not in seen:
            seen.add(key)
            uniq.append(e)

    graph = {
        "version": "v2-rebuilt-from-pass3",
        "rebuilt_at": "2026-11-21",
        "note": "原 47 节点/120 边图随外接盘目录灭失，依据 PASS3 实测证据重建；ghost 边已删除",
        "removed_edges": REMOVED_EDGES,
        "nodes": nodes,
        "edges": uniq,
    }
    OUT.write_text(json.dumps(graph, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"nodes={len(nodes)} edges={len(uniq)} -> {OUT}")


if __name__ == "__main__":
    raise SystemExit(main())
