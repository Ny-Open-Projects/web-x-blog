import { useMemo } from "react";
import { Form, Input } from "antd";

import type { IListComponentProps } from "@lowcode/share";
import {
  fillComponentPropsByConfig,
  listComponentDefaultConfig,
  listItem,
} from "@lowcode/share";

import { FormContainerWithList, UploadEditOrChooiseInput } from "..";

export default function ListComponentProps(_props: IListComponentProps) {
  const props = useMemo(() => {
    return fillComponentPropsByConfig(_props, listComponentDefaultConfig);
  }, [_props]);

  if (props.items.isHidden) return <>暂无可选配置</>;

  return (
    <FormContainerWithList
      id={props.id.value}
      items={props.items.value}
      newItemDefaultValue={listItem}
    >
      <Form.Item label="标题：" name="title">
        <Input />
      </Form.Item>
      <Form.Item label="标题点击后链接：" name="titleLink">
        <Input />
      </Form.Item>
      <Form.Item label="头像：" name="avatar">
        <UploadEditOrChooiseInput
          propName="avatar"
          type="image"
          listOptions={{
            defaultValues: listItem,
          }}
        />
      </Form.Item>
      <Form.Item label="描述：" name="description">
        <Input />
      </Form.Item>
    </FormContainerWithList>
  );
}
