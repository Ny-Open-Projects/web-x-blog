import { Button } from "antd";
import { LineChartOutlined } from "@ant-design/icons";
import { useNavigate } from "react-router-dom";

export default function Right() {
  const navigate = useNavigate();
  const toStatistics = () => {
    navigate("/dataCount");
  };

  return (
    <div className="flex items-center">
      <Button onClick={toStatistics} className="flex items-center mr-5">
        后台数据统计
        <LineChartOutlined />
      </Button>
      <img
        src="https://sdfsdf.dev/40x40.png"
        className="rounded-full border cursor-pointer"
      />
    </div>
  );
}
