import {
  CheckOutlined,
  FundViewOutlined,
  PlusOutlined,
} from "@ant-design/icons";
import type { IComponent, PostReleaseRequest } from "@lowcode/share";
import { useRequest } from "ahooks";
import { Button, Space, message } from "antd";
import { useNavigate } from "react-router-dom";
import { postRelease } from "~/api/low-code";
import { useStoreComponents, useStorePage } from "~/hooks";

export default function Center() {
  const nav = useNavigate();
  const { store } = useStorePage();
  const {
    store: storeComponents,
    getComponentById,
    storeInLocalStorage,
  } = useStoreComponents();

  // 发布接口调用
  const { run, loading } = useRequest(
    async (values: PostReleaseRequest) => postRelease(values),
    {
      manual: true,
      onSuccess: ({ msg, data }) => {
        // 跳转发布之后的页面
        nav(`/release?id=${data}`);
        localStorage.setItem("release_time", String(Date.now()));
        message.success(msg);
      },
    }
  );

  // 预览按钮
  function handleGoPreview() {
    // 将配置的组件储存在 localStorage
    storeInLocalStorage();
    // 跳转预览页面
    nav("/preview");
  }

  // 发布按钮
  function handleGoRelease() {
    // 将前端的组件数据类型结构转成符合后端接口入参的类型结构
    const components = storeComponents.sortableCompConfig
      .map((comp) => getComponentById(comp))
      .map((comp) => ({
        type: comp.type,
        options: comp.props,
      })) as IComponent[];

    run({
      components,
      desc: store.description,
      page_name: store.title,
      tdk: store.tdk,
    });
  }

  return (
    <Space>
      <Button className="flex items-center" onClick={handleGoPreview}>
        预览 <FundViewOutlined />
      </Button>
      <Button className="flex items-center" onClick={storeInLocalStorage}>
        存至草稿 <PlusOutlined />
      </Button>
      <Button
        loading={loading}
        className="flex items-center"
        type="primary"
        onClick={handleGoRelease}
      >
        发布 <CheckOutlined />
      </Button>
    </Space>
  );
}
