import ComponentRender from "../../components/ComponentRender";
import type { GetReleaseDataResponse } from "@lowcode/share";

async function getData(id: string) {
  // 请求后端接口获取发布页面组件
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_BASE_URL}/low_code/release?id=${id}`,
    {
      cache: "no-cache",
    }
  );

  if (!response.ok) throw new Error("未找到");

  const toJson = (await response.json()) as {
    code: number;
    data?: GetReleaseDataResponse;
  };

  if (!toJson.data) throw new Error("404");

  return toJson.data!;
}

interface PageType {
  params: { id: string };
}
export default async function Page({ params }: PageType) {
  const data = await getData(params.id);

  return (
    <div className="App">
      <ComponentRender data={data} id={params.id} />
    </div>
  );
}
