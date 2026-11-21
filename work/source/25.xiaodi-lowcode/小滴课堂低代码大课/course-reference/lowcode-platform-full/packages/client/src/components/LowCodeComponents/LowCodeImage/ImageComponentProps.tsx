import { Input, Segmented, Select } from "antd";
import type { SegmentedLabeledOption } from "antd/es/segmented";
import { useMemo } from "react";
import type { IImageComponentProps } from "@lowcode/share";
import {
  fillComponentPropsByConfig,
  imageComponentDefaultConfig,
} from "@lowcode/share";
import { FormContainer, FormPropLabel, UploadEditOrChooiseInput } from "..";

export const fitOptions = [
  {
    value: "contain",
    label: "包含",
  },
  {
    value: "cover",
    label: "覆盖",
  },
  {
    value: "fill",
    label: "填充",
  },
  {
    value: "none",
    label: "无",
  },
  {
    value: "scale-down",
    label: "缩小",
  },
  {
    value: "initial",
    label: "默认",
  },
  {
    value: "revert",
    label: "恢复",
  },
  {
    value: "unset",
    label: "重置",
  },
];

export default function ImageComponentProps(_props: IImageComponentProps) {
  const props = useMemo(() => {
    return fillComponentPropsByConfig(_props, imageComponentDefaultConfig);
  }, [_props]);

  const options: SegmentedLabeledOption[] = [
    {
      value: "open-url",
      label: "跳转链接",
    },
    {
      value: "none",
      label: "无",
    },
  ];

  return (
    <FormContainer layout="vertical" config={props}>
      <FormPropLabel name="name" prop={props.name} label="图片名称：">
        <Input />
      </FormPropLabel>

      <FormPropLabel name="height" prop={props.height} label="图片大小：">
        <Input type="number" />
      </FormPropLabel>
      <FormPropLabel name="fit" prop={props.fit} label="图片填充方式：">
        <Select options={fitOptions} />
      </FormPropLabel>
      <FormPropLabel
        name="handleClicked"
        prop={props.handleClicked}
        label="图片点击后方式："
      >
        <Segmented options={options} />
      </FormPropLabel>
      <FormPropLabel name="link" prop={props.link} label="图片跳转地址：">
        <Input />
      </FormPropLabel>

      <FormPropLabel name="url" prop={props.url} label="图片地址：">
        <UploadEditOrChooiseInput type="image" propName="url" />
      </FormPropLabel>
    </FormContainer>
  );
}
