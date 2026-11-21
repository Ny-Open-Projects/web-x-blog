import type {
  PostReleaseRequest,
  getQuestionDataByIdRequest,
} from "@lowcode/share";
import request from "~/utils/request";

// 页面发布接口
export async function postRelease(data: PostReleaseRequest) {
  return request("/low_code/release", {
    data,
    method: "POST",
  });
}

// 获取页面组件接口
export async function getLowCodePage() {
  return request("/low_code/release_with_user");
}

// 获取问卷组件借口
export async function getQuestionComponents() {
  return request("/low_code/question_components");
}

// 获取问卷组件内容接口
export async function getQuestionData() {
  return request("/low_code/question_data");
}

// 动态获取问卷组件内容接口
export async function getQuestionDataByTypeRequest(
  data: getQuestionDataByIdRequest
) {
  return request("/low_code/get_question_data_by_id", { data, method: "POST" });
}
