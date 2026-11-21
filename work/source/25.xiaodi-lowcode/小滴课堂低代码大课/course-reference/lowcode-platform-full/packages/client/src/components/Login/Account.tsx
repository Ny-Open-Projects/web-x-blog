import { Button, Form, Input } from "antd";
import { useRequest } from "ahooks";
import { getLoginWithPassword } from "../../api/user";
import { useStoreAuth } from "../../hooks/useStoreAuth";

export default function Account() {
  const { login } = useStoreAuth();
  //  账号密码登录请求
  const { run, loading } = useRequest(
    async (values) => await getLoginWithPassword(values),
    {
      manual: true,
      onSuccess: ({ data }) => {
        login(data);
      },
    }
  );

  return (
    <div className="space-y-4">
      <div className="space-y-2">
        <Form onFinish={run}>
          <Form.Item
            label="账号"
            name="phone"
            rules={[
              { required: true, message: "请输入手机号!" },
              { pattern: /^1\d{10}$/, message: "请输入正确的手机号!" },
            ]}
          >
            <Input placeholder="请输入手机号" />
          </Form.Item>

          <Form.Item
            label="密码"
            name="password"
            rules={[{ required: true, message: "请输入密码!" }]}
          >
            <Input.Password placeholder="请输入密码" />
          </Form.Item>

          <Form.Item>
            <Button
              type="primary"
              htmlType="submit"
              className="w-full"
              loading={loading}
            >
              登录
            </Button>
          </Form.Item>
        </Form>
      </div>
    </div>
  );
}
