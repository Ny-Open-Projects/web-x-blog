import type { UploadType } from "@lowcode/share";
import request from "~/utils/request";

// 上传接口
export async function uploadFile(formData: FormData) {
  return request("/resources/upload", {
    data: formData,
    method: "POST",
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
}

// 资源获取接口
export async function getResources(type: UploadType) {
  return request("/resources", {
    params: { type },
    method: "GET",
  });
}

// 资源删除的接口
export async function deleteResource(id: number) {
  return request("/resources", {
    params: { id },
    method: "DELETE",
  });
}
