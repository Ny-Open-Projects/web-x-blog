# 批6（05 第五期 26 篇）审核修正落地记录（2026-11-19）

来源：review-b6-p5.md（P1×24 / P2×71）。
- 簇一 `/local` 旧路由 15 处全清（19-4/19-5/20-3/20-4/20-7/20-8 → api/low-code + snake_case 路径）。
- P1 全落地：17-1 域名正则改为可命中示例的写法、17-2 await+account_id+resources 路由簇、17-4 IDOR 口径注+Delete()、17-5 getResources、18-1/18-2/18-3 命名簇（UploadEditOrChooiseInput/LoadResource/handleChooise/itemsExpandIndex/useStoreComponents）、18-5 useComponentKeyPress+粘贴存完整结构、18-6 标题回归引用名、19-2 localStorageInStore、19-3 storeInLocalStorage 三处张冠李戴、19-4/19-5 api/low-code、20-1 component_data 四列口径（组件 ID 在 props[i].id）、20-3/20-4 LowCodeController+snake_case、20-7/20-8 NEXT_PUBLIC_API_BASE_URL+A5 同源残留清除。
- 簇二命名 ~28 处对齐 SRC（compConfigs 族、store_time/release_time、textarea→textArea、Resources* 实体族、getUserMess、EditorHeader、FloatButton、isPosted、refrash 等）。
- 簇三标题：26 篇 title/h1 全量对齐文件名。簇五 deps/build、簇六 trust proxy 口径注（20-1/20-3）、簇七 textArea/titleText、簇八 19-5 现状注均已落。
- 20-x 提示文案对齐源码（「您已提交过问卷，感谢您的参与」「请填写完整问卷信息」）。
- 同步：target 05 → blog `diff -rq` 校验一致。
