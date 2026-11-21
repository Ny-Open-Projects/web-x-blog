import type { IComponent } from "@lowcode/share";
import { useRequest } from "ahooks";
import { useEffect, useMemo, useState } from "react";
import ReactECharts from "echarts-for-react";
import { getQuestionDataByTypeRequest } from "~/api/low-code";
import { useStorePage } from "../../hooks/useStorePage";
interface DataSourceProps {
  currentSelected?: IComponent;
}

export default function DataSource({ currentSelected }: DataSourceProps) {
  const [currentData, setCurrentData] = useState<string[][]>([]);
  const [currentOptions, setCurrentOptions] = useState<
    { id: string; value: string }[]
  >([]);

  const { store } = useStorePage();

  // 用于判断点击的组件是否为输入类型组件
  const isMore = useMemo(
    () => ["radio", "checkbox"].includes(currentSelected?.type ?? ""),
    [currentSelected]
  );

  // 请求点击的某个组件信息
  const { run: execGetQuestionData } = useRequest(
    () =>
      getQuestionDataByTypeRequest({
        id: currentSelected!.id,
      }),
    {
      manual: true,
      onSuccess: ({ data }) => {
        setCurrentData(data.map((item: any) => item.value));
        isMore &&
          setCurrentOptions(
            data[0].options.map((item: any) => ({
              id: item.id,
              value: item.value,
            }))
          );
      },
    }
  );

  // 当查看不同问卷组件展示不同组件信息
  useEffect(() => {
    currentSelected && execGetQuestionData();
  }, [currentSelected]);

  // 生成用户输入类型问卷组件信息
  function generatorTexts() {
    return (
      <div className="p-10">
        <span>《{store.title}》问卷填写数据：</span>
        <br />
        <br />
        {currentData.flat().map((item, index) => {
          return (
            <span key={index}>
              {"填写: "}
              {item} <br />
            </span>
          );
        })}
      </div>
    );
  }

  // 不同非输入类型组件展示的标题
  const itemTitle = useMemo(
    () => currentSelected?.options.title ?? "默认展示的标题",
    [currentSelected]
  );

  // 将currentData数组中的每个元素的每个属性作为key，统计出现次数
  const result = useMemo(() => {
    const a = currentData.reduce((acc, prev) => {
      prev.forEach((id) => {
        acc[id ?? ""] = (acc?.[id] ?? 0) + 1;
      });
      return acc;
    }, {} as any);
    return a;
  }, [currentData]);

  // 处理成图表需要的数据格式
  const data = useMemo(() => {
    // 根据currentOptions生成一个新的数组，每个元素包含name和value属性
    return currentOptions.map((item) => {
      return {
        name: item.value,
        value: result[item.id] ?? 0,
      };
    });
  }, [currentOptions]);

  console.log("result:", result);
  console.log("currentData:", currentData);
  console.log("data:", data);

  // 饼状图配置
  function getPieOptions() {
    return {
      // 标题
      title: {
        text: itemTitle,
        left: "center",
      },
      // 设置提示框
      tooltip: {
        trigger: "item",
      },
      // 设置图例的显示方向
      legend: {
        orient: "vertical",
        left: "20%",
      },
      // 设置饼状图的详细配置
      series: [
        {
          name: "分类个数",
          type: "pie",
          radius: "50%",
          data,
          // 设置鼠标悬停时的样式
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: "rgba(0, 0, 0, 0.5)",
            },
          },
        },
      ],
    };
  }

  // 横向柱状图配置
  function getTopOptions() {
    return {
      // 设置图表宽度为 500 像素
      width: "500px",
      backgroundColor: "#fff",
      grid: {
        left: "25%",
        containLabel: true, // 确保网格内的标签不会被剪裁
      },
      tooltip: {
        trigger: "item",
        // 定义坐标轴指示器的配置对象
        axisPointer: {
          type: "none",
        },
      },
      xAxis: {
        show: false,
        type: "value",
      },
      yAxis: [
        {
          type: "category",
          inverse: true,
          axisLabel: {
            show: true,
            align: "right",
            textStyle: {
              fontSize: 14,
              color: "#333",
              rich: {
                name: {
                  width: 7 * 14,
                  align: "left",
                  textAlign: "left",
                },
              },
            },
          },
          splitLine: {
            show: false,
          },
          axisTick: {
            show: false,
          },
          axisLine: {
            show: false,
          },
          data: data.map((item) => item.name),
        },
        {
          type: "category",
          inverse: true,
          axisTick: "none",
          axisLine: "none",
          show: true,
          axisLabel: {
            textStyle: {
              color: "#3196fa",
              fontSize: "12",
            },
            formatter: "{value}%",
          },
          data: data.map((item) => item.value),
        },
      ],
      series: [
        {
          name: "值",
          type: "bar",
          zlevel: 1,
          itemStyle: {
            normal: {
              barBorderRadius: 30,
              color: "#3196fa",
            },
          },
          barWidth: 20,
          data,
        },
        {
          name: "背景",
          type: "bar",
          barWidth: 20,
          barGap: "-100%",
          data: Array.from({ length: data.length }).fill(100),
          itemStyle: {
            normal: {
              color: "#ededed",
              barBorderRadius: 30,
            },
          },
        },
      ],
    };
  }
  return (
    <>
      {isMore ? (
        <div>
          <ReactECharts option={getPieOptions()} />
          <ReactECharts option={getTopOptions()} />
        </div>
      ) : (
        generatorTexts()
      )}
    </>
  );
}
