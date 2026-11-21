import { useMemo } from "react";
import {
  type IEmptyComponentProps,
  emptyComponentDefaultConfig,
  fillComponentPropsByConfig,
} from "@lowcode/share";
import { Input, Select } from "antd";
import { FormContainer, FormPropLabel } from "..";
import { fitOptions } from "../LowCodeImage/ImageComponentProps";

export default function EmptyComponentProps(_props: IEmptyComponentProps) {
  const props = useMemo(() => {
    return fillComponentPropsByConfig(_props, emptyComponentDefaultConfig);
  }, [_props]);

  return (
    <FormContainer layout="vertical" config={props}>
      <FormPropLabel name="image" label="图片" prop={props.image}>
        <Input />
        {/* <UploadEditOrChooiseInput propName="image" type="image" /> */}
      </FormPropLabel>
      <FormPropLabel name="description" label="描述" prop={props.description}>
        <Input />
      </FormPropLabel>
      <FormPropLabel name="imageWidth" label="图片宽度" prop={props.imageWidth}>
        <Input type="number" />
      </FormPropLabel>
      <FormPropLabel
        name="imageHeight"
        label="图片高度"
        prop={props.imageHeight}
      >
        <Input type="number" />
      </FormPropLabel>
      <FormPropLabel
        name="imageObjectFit"
        prop={props.imageObjectFit}
        label="图片填充方式："
      >
        <Select options={fitOptions} />
      </FormPropLabel>
    </FormContainer>
  );
}
