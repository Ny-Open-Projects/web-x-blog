-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133651611
-- LeetCode 133651611. 图及其深度和广度优先遍历实现 — Lua 版（方案1）
local Graph = {} -- 把 {} 写入 local Graph
Graph.__index = Graph -- 把 Graph 写入 Graph.__index

function Graph.new() -- function Graph.new()
	return setmetatable({ adj = {} }, Graph) -- 返回 setmetatable({ 邻接表 赋值为 {} }, Graph)
end -- 终点

function Graph:addEdge(from, to) -- function Graph:addEdge(from, to)
	self.adj[from] = self.adj[from] or {} -- 把 self.邻接表[from] or {} 写入 self.adj[from]
	self.adj[to] = self.adj[to] or {} -- 把 self.邻接表[to] or {} 写入 self.adj[to]
	self.adj[from][#self.adj[from] + 1] = to -- 把 to 写入 self.adj[from][#self.adj[from] + 1]
	self.adj[to][#self.adj[to] + 1] = from -- 把 from 写入 self.adj[to][#self.adj[to] + 1]
end -- 终点

function Graph:dfs(start) -- function Graph:dfs(起点)
	local visited = {} -- 把 {} 写入 local visited
	local result = {} -- 把 {} 写入 local result
	local function helper(node) -- local function helper(节点)
		if visited[node] then
			return
		end -- 若 已访问集合[节点] then return 终点
		visited[node] = true -- 把 true 写入 visited[node]
		result[#result + 1] = node -- 把 节点 写入 result[#result + 1]
		for _, neighbor in ipairs(self.adj[node] or {}) do -- 遍历取 neighbor
			helper(neighbor) -- helper(neighbor)
		end -- 终点
	end -- 终点
	helper(start) -- helper(起点)
	return result -- 返回 结果
end -- 终点

function Graph:bfs(start) -- function Graph:bfs(起点)
	local visited = { [start] = true } -- 把 { [起点] 赋值为 true } 写入 local visited
	local result = {} -- 把 {} 写入 local result
	local queue = { start } -- 把 { 起点 } 写入 local queue
	local head = 1 -- 把 1 写入 local head
	while head <= #queue do -- 把 #队列 do 写入 while head <
		local node = queue[head] -- 把 队列[头节点] 写入 local node
		head = head + 1 -- 把 头节点 加 1 存入 头节点
		result[#result + 1] = node -- 把 节点 写入 result[#result + 1]
		for _, neighbor in ipairs(self.adj[node] or {}) do -- 遍历取 neighbor
			if not visited[neighbor] then -- 若 not 已访问集合[neighbor] then
				visited[neighbor] = true -- 把 true 写入 visited[neighbor]
				queue[#queue + 1] = neighbor -- 把 neighbor 写入 queue[#queue + 1]
			end -- 终点
		end -- 终点
	end -- 终点
	return result -- 返回 结果
end -- 终点

local function eq(a, b) -- local function eq(数组, b)
	if #a ~= #b then
		return false
	end -- 若 #数组 ~ 赋值为 #b then return false 终点
	for i = 1, #a do -- 把 1, #数组 do 写入 for i
		if a[i] ~= b[i] then
			return false
		end -- 若 数组[下标 i] ~ 赋值为 b[下标 i] then return false 终点
	end -- 终点
	return true -- 返回 true
end -- 终点

-- case 1: 方形图 0-1-3-2-0
local g1 = Graph.new() -- 把 Graph.new() 写入 local g1
g1:addEdge(0, 1) -- g1:addEdge(0, 1)
g1:addEdge(0, 2) -- g1:addEdge(0, 2)
g1:addEdge(1, 3) -- g1:addEdge(1, 3)
g1:addEdge(2, 3) -- g1:addEdge(2, 3)
assert(eq(g1:dfs(0), { 0, 1, 3, 2 }), "case1 dfs(0)") -- 断言校验
assert(eq(g1:bfs(0), { 0, 1, 2, 3 }), "case1 bfs(0)") -- 断言校验

-- case 2: 从另一节点出发
assert(eq(g1:dfs(2), { 2, 0, 1, 3 }), "case2 dfs(2)") -- 断言校验
assert(eq(g1:bfs(2), { 2, 0, 3, 1 }), "case2 bfs(2)") -- 断言校验

print("PASS") -- 全部用例通过，输出 PASS
