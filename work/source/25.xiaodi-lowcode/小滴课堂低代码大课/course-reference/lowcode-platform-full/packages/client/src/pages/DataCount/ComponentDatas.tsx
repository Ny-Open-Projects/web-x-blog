import type { ColumnsType } from "antd/es/table";
import { Button, Space, Table, message } from "antd";
import { useRequest } from "ahooks";
import type { IComponent } from "@lowcode/share";
import { useMemo, useState } from "react";
import { getQuestionData } from "~/api/low-code";
import { useStorePage } from "~/hooks";
import { excelToZip, jsonToExcel } from "~/utils/excel";

export default function ComponentDatas(props: {
  components: IComponent[];
  handleDisable: () => void;
}) {
  const [dataSource, setDataSource] = useState<any[]>([]);

  // 处理成 table 组件需要的数据格式
  const columns: ColumnsType<any> = useMemo(() => {
    return props.components.map((item) => {
      return {
        key: item.id,
        dataIndex: item.id,
        title: item.options.title ?? "默认展示的标题",
      };
    });
  }, [props.components]);

  // 请求问卷组件问卷数据处理成 table 需要的格式
  const { loading } = useRequest(getQuestionData, {
    onSuccess: ({ data }) => {
      if (data.length === 0) {
        props.handleDisable();
        message.warning("还未有用户提交数据哦");
        return;
      }

      const result = data.map((res: any) => {
        return res
          .map((item: any) => {
            let value: any = item.result?.value;
            // 如果是radio或checkbox类型
            if (["radio", "checkbox"].includes(item.type)) {
              // 如果value为空，则使用第一个选项的value
              if (!value) {
                value = !item.options?.length
                  ? "选项1"
                  : item.options![0].value;
              } else {
                // 如果value是数组，则将其转换为逗号分隔的字符串
                if (Array.isArray(value))
                  value = value
                    .map(
                      (v) =>
                        item.options!.find((option: any) => option.id === v)
                          ?.value
                    )
                    .join(",");
                // 如果value是数字，则将其转换为对应选项的value
                else
                  value = item.options!.find(
                    (option: any) => option.id === value
                  )?.value;
              }
            }

            return {
              value,
              key: item.result.id,
            };
          })
          .reduce((pre: any, cur: any) => {
            return {
              key: cur.key,
              [cur.key]: cur.value,
              ...pre,
            };
          }, {});
      });
      setDataSource(result);
    },
  });

  const { store } = useStorePage();

  // 生成 excel 文件下载
  async function handleExportExcel(isWriteFile?: boolean) {
    return jsonToExcel({
      columns,
      dataSource,
      title: store.title,
      isWriteFile: isWriteFile ?? true,
    });
  }

  // 生成 excel 压缩包文件下载
  async function handleExportZip() {
    const excel = await jsonToExcel({
      columns,
      dataSource,
      title: store.title,
      isWriteFile: false,
    });

    excelToZip(excel);
  }

  return (
    <div className="relative">
      <Table
        columns={columns}
        dataSource={dataSource}
        loading={loading}
      ></Table>
      <div className="absolute z-10 right-2 bottom-[-40px]">
        {/* 导出压缩包+导出Excel  */}
        <Space>
          <Button onClick={handleExportZip}>导出压缩包</Button>
          <Button type="primary" onClick={() => handleExportExcel()}>
            导出Excel
          </Button>
        </Space>
      </div>
    </div>
  );
}
