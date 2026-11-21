import React, { useMemo } from "react";
import { getDefaultValueByConfig } from "..";
import { type IImageComponentProps, imageComponentDefaultConfig } from ".";

export default function ImageComponent(_props: IImageComponentProps) {
  // 当配置属性发生变化，重置属性并且重新渲染
  const props = useMemo(() => {
    return {
      ...getDefaultValueByConfig(imageComponentDefaultConfig),
      ..._props,
    };
  }, [_props]);

  const img = (
    <img
      src={props.url}
      alt={props.name}
      className="w-full"
      style={{ height: `${props.height}px`, objectFit: props.fit }}
    />
  );

  // 如果图片可跳转，则覆盖上a标签
  if (props.handleClicked === "open-url")
    return (
      <a href={props.link} target="_blank" rel="noreferrer">
        {img}
      </a>
    );
  else return img;
}
