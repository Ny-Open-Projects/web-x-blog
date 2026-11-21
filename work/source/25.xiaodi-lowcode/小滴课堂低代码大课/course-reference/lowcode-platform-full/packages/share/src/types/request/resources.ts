import type { IResources } from "..";

// 上传资源的类型
export type UploadType = "image" | "video";

// 上传资源的参数
export type ResourcesRequest = Pick<IResources, "type">;

// 删除资源的参数
export type DeleteResourcesRequest = Pick<IResources, "id">;
