import { Carousel } from "antd";
import React, { useMemo } from "react";
import { ImageComponent, getDefaultValueByConfig } from "..";
import { swiperComponentDefaultConfig } from ".";
import type { ISwiperComponentProps } from ".";

export default function SwiperComponent(_props: ISwiperComponentProps) {
  // 当配置属性发生变化，重置属性并且重新渲染
  const props = useMemo(() => {
    return {
      ...getDefaultValueByConfig(swiperComponentDefaultConfig),
      ..._props,
    };
  }, [_props]);

  return (
    <Carousel
      autoplaySpeed={props.interval}
      autoplay={props.autoPlay}
      dots={props.showIndicators}
      dotPosition={props.dotPosition}
    >
      {props.images.map((image, index) => (
        <ImageComponent {...image} key={index} />
      ))}
    </Carousel>
  );
}
