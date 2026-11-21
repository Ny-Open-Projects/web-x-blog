"""用字典模拟一个 MCP Server 的 tools 与 resources 原语,并演示 Host 侧发现与调用。"""


class FakeMCPServer:
    """模拟 MCP Server 暴露的能力清单。"""

    def __init__(self, name: str):
        self.name = name
        self.tools = {}
        self.resources = {}

    def register_tool(self, name: str, description: str, fn):
        self.tools[name] = {"description": description, "fn": fn}

    def register_resource(self, uri: str, fn):
        self.resources[uri] = fn

    def list_tools(self):          # 对应 MCP tools/list
        return [{"name": n, "description": t["description"]} for n, t in self.tools.items()]

    def call_tool(self, name, args):   # 对应 MCP tools/call
        if name not in self.tools:
            return {"isError": True, "content": f"未知工具 {name}"}
        return {"isError": False, "content": str(self.tools[name]["fn"](**args))}

    def read_resource(self, uri):  # 对应 MCP resources/read
        return self.resources[uri]()


# Host 侧:发现并调用,不关心 Server 是本地还是远程
server = FakeMCPServer("fs-server")
server.register_tool("read_file", "读取文件内容",
                     lambda path: f"{path} 的内容(共100行)")
server.register_resource("file:///config.json", lambda: '{"env": "prod"}')

if __name__ == "__main__":
    print("发现工具:", server.list_tools())
    print("调用工具:", server.call_tool("read_file", {"path": "/etc/app.yaml"}))
    print("调用未知:", server.call_tool("write_file", {}))
    print("读取资源:", server.read_resource("file:///config.json"))
