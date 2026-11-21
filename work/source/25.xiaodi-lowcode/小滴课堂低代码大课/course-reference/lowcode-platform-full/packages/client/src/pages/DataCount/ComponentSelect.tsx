import type { IComponent } from "@lowcode/share";
import { Button, Table } from "antd";
import type { ColumnsType } from "antd/es/table";

interface ComponentSelectProps {
  components: IComponent[];
  currentSelected: number;
  setCurrnetSelected: (comp: IComponent) => void;
}

interface DataType {
  key: number;
  title: string;
  type: string;
  component: IComponent;
}

export default function ComponentSelect({
  components,
  currentSelected,
  setCurrnetSelected: setCurrnetSelectedComponent,
}: ComponentSelectProps) {
  // 动态表格表头
  const columns: ColumnsType<DataType> = [
    {
      title: "标题",
      dataIndex: "title",
      key: "title",
    },
    {
      title: "类型",
      dataIndex: "type",
      key: "type",
    },
    {
      title: "操作",
      dataIndex: "action",
      key: "action",
      render: (_: any, record: DataType) => (
        <Button
          disabled={currentSelected === record.key}
          type="primary"
          size="small"
          onClick={() => setCurrnetSelectedComponent(record.component)}
        >
          查看数据
        </Button>
      ),
    },
  ];

  // 整理成 table 需要的数据格式
  const dataSource: DataType[] = components.map((item) => {
    return {
      key: item.id,
      title: item.options.title ?? "默认展示的标题",
      type: item.type,
      component: item,
    };
  });

  return <Table dataSource={dataSource} columns={columns}></Table>;
}
