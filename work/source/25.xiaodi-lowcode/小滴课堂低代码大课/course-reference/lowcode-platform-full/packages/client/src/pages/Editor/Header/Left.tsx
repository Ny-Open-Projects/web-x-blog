import { CheckOutlined, EditOutlined } from "@ant-design/icons";
import { Input, Space } from "antd";
import { useState } from "react";
import type { ChangeEvent } from "react";

import { useStorePage } from "~/hooks";

export default function Left(props: { title: string }) {
  const { setPageTitle } = useStorePage();
  const [isEditState, setIsEditState] = useState(false);

  // 确认按钮方法
  function handleEdit(event: ChangeEvent<HTMLInputElement>) {
    setPageTitle(event.target.value);
  }

  // 标题的样式和按钮点击方法
  const publicProps = {
    className: "cursor-pointer ml-1 hover:bg-gray-100 p-2 rounded-full",
    onClick: () => setIsEditState(!isEditState),
  };

  // 判断是否展示编辑还是显示状态
  if (isEditState) {
    return (
      <Space>
        <Input value={props.title} onChange={handleEdit} />
        <CheckOutlined {...publicProps} />
      </Space>
    );
  } else {
    return (
      <Space>
        <h1 className="text-lg">{props.title}</h1>
        <EditOutlined {...publicProps} />
      </Space>
    );
  }
}
