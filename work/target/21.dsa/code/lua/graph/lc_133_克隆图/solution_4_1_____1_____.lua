-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133986698
-- LeetCode 133. 克隆图 — Lua 版

-- 方案4（BFS，visited 以节点对象为键）
local function new_node(val) -- local function new_node(值)
	return { val = val, neighbors = {} } -- 返回 { 值 赋值为 值, neighbors 赋值为 {} }
end -- 终点

local function clone_graph(node) -- local function clone_graph(节点)
	if not node then
		return nil
	end -- 若 not 节点 then return nil 终点
	local visited = {} -- table 自身可作键，等价于 TS 的 Map<Node, Node>
	visited[node] = new_node(node.val) -- 把 new_node(节点.值) 写入 visited[node]
	local q = { node } -- 把 { 节点 } 写入 local q
	local head = 1 -- 把 1 写入 local head
	while head <= #q do -- 把 #节点 do 写入 while head <
		local n = q[head] -- 把 节点[头节点] 写入 local n
		head = head + 1 -- 把 头节点 加 1 存入 头节点
		for _, ne in ipairs(n.neighbors) do -- 遍历取 ne
			if visited[ne] == nil then -- 若 已访问集合[ne] 等于 nil then
				q[#q + 1] = ne -- 把 ne 写入 q[#q + 1]
				visited[ne] = new_node(ne.val) -- 把 new_node(ne.值) 写入 visited[ne]
			end -- 终点
			table.insert(visited[n].neighbors, visited[ne]) -- table 插入 已访问集合[元素个数].neighbors, 已访问集合[ne])
		end -- 终点
	end -- 终点
	return visited[node] -- 返回 已访问集合[节点]
end -- 终点

local function build_graph(adj) -- local function build_graph(邻接表)
	local nodes = {} -- 把 {} 写入 local nodes
	for i = 1, #adj do
		nodes[i] = new_node(i)
	end -- 把 1, #邻接表 do nodes[下标 i] 赋值为 new_node(下标 i) 终点 写入 for i
	for idx, nbrs in ipairs(adj) do -- 遍历取 nbrs
		for _, nb in ipairs(nbrs) do -- 遍历取 nb
			table.insert(nodes[idx].neighbors, nodes[nb]) -- table 插入 nodes[idx].neighbors, nodes[nb])
		end -- 终点
	end -- 终点
	return nodes[1] -- 返回 nodes[1]
end -- 终点

-- 收集签名：每个节点的邻居值列表（排序后），按节点 val 键控
local function signature(node) -- local function signature(节点)
	local vis = {} -- 把 {} 写入 local vis
	local function dfs(n) -- local function dfs(元素个数)
		if vis[n.val] then
			return
		end -- 若 vis[元素个数.值] then return 终点
		local vals = {} -- 把 {} 写入 local vals
		for _, x in ipairs(n.neighbors) do
			vals[#vals + 1] = x.val
		end -- 遍历取 x
		table.sort(vals) -- 排序
		vis[n.val] = vals -- 把 vals 写入 vis[n.val]
		for _, x in ipairs(n.neighbors) do
			dfs(x)
		end -- 遍历取 x
	end -- 终点
	dfs(node) -- dfs(节点)
	return vis -- 返回 vis
end -- 终点

local root = build_graph({ { 2, 4 }, { 1, 3 }, { 2, 4 }, { 1, 3 } })
local cloned = clone_graph(root) -- 把 clone_graph(根节点) 写入 local cloned
assert(cloned ~= nil, "cloneGraph returned null") -- 断言校验
assert(cloned ~= root, "not a deep copy (same object)") -- 断言校验
local sig = signature(cloned) -- 把 signature(cloned) 写入 local sig
local expected = { { 2, 4 }, { 1, 3 }, { 2, 4 }, { 1, 3 } }
for k = 1, 4 do -- 让 下标 k 从 1 走到 4（Lua 1 基）
	local a = sig[k] -- 把 sig[下标 k] 写入 local a
	assert(a ~= nil, "signature mismatch at " .. k) -- 断言校验
	assert(#a == #expected[k], "signature mismatch at " .. k) -- 断言校验
	for i = 1, #expected[k] do -- 把 1, #expected[下标 k] do 写入 for i
		assert(a[i] == expected[k][i], "signature mismatch at " .. k) -- 断言校验
	end -- 终点
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
