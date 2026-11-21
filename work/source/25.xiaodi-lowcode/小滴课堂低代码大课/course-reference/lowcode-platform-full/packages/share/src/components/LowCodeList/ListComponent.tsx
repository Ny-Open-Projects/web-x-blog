import React, { useMemo } from "react";
import { Avatar, List } from "antd";
import { getDefaultValueByConfig } from "..";
import { listComponentDefaultConfig } from ".";
import type { IListComponentProps } from ".";

export default function ListComponent(_props: IListComponentProps) {
  const props = useMemo(() => {
    return {
      ...getDefaultValueByConfig(listComponentDefaultConfig),
      ..._props,
    };
  }, [_props]);

  return (
    <List
      itemLayout="horizontal"
      dataSource={props.items}
      renderItem={(item) => (
        <List.Item>
          <List.Item.Meta
            avatar={<Avatar src={item.avatar} />}
            title={<a href={item.titleLink}>{item.title}</a>}
            description={item.description}
          />
        </List.Item>
      )}
    />
  );
}
