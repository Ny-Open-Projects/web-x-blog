import { Tabs } from "antd";
import { AppstoreOutlined } from "@ant-design/icons";
import ComponentList from "./LeftPanel/ComponentList";

export default function EdiotLeftPanel() {
  const items = [
    {
      key: "component-list",
      label: (
        <>
          <AppstoreOutlined /> <span>组件列表</span>
        </>
      ),
      /**
       * 不同组件列表
       */
      children: <ComponentList />,
    },
  ];

  return <Tabs defaultActiveKey="component-list" items={items} />;
}
