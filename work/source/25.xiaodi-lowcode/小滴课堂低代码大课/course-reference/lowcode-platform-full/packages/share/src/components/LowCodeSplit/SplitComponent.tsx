import React, { useMemo } from "react";
import { Divider } from "antd";

import { getDefaultValueByConfig } from "..";
import { objectOmit } from "../..";
import { splitComponentDefaultConfig } from ".";
import type { ISplitComponentProps } from ".";

export default function SplitComponent(_props: ISplitComponentProps) {
  const props = useMemo(() => {
    return {
      ...getDefaultValueByConfig(splitComponentDefaultConfig),
      ..._props,
    };
  }, [_props]);

  // 如果没有文本直接显示分割线
  if (!props.text) {
    return <Divider {...objectOmit(props, ["text"])} />;
  } else {
    return (
      <Divider {...objectOmit(props, ["text"])}>
        <span className="text-gray-500/80">{props?.text}</span>
      </Divider>
    );
  }
}
