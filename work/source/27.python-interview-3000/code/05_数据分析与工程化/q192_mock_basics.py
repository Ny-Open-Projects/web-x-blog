from unittest.mock import MagicMock

class EmailClient:
    def send(self, to, subject):
        raise RuntimeError("真实实现不会在测试中被调用")

def notify(client: EmailClient, user):
    return client.send(to=user["email"], subject="welcome")

def test_notify_called_once():
    client = MagicMock(spec=EmailClient)  # spec 限制只能 mock 真实存在的方法
    notify(client, {"email": "a@b.com"})
    client.send.assert_called_once_with(to="a@b.com", subject="welcome")

def test_return_value():
    client = MagicMock()
    client.send.return_value = True
    assert notify(client, {"email": "x@y.com"}) is True
