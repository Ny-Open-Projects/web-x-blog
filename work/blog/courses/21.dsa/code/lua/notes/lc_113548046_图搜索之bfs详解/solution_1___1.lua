-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113548046
-- 图搜索之BFS详解 — Lua 版（方案1）
local function bfs_order(graph, start) -- local function bfs_order(graph, 起点)
	local n = #graph -- 把 #graph 写入 local n
	local visited = {} -- 把 {} 写入 local visited
	local order = {} -- 把 {} 写入 local order
	local queue = { start } -- 把 {起点} 写入 local queue
	local head = 1 -- 把 1 写入 local head
	visited[start + 1] = true -- 把 true 写入 visited[start + 1]
	while head <= #queue do -- 把 #队列 do 写入 while head <
		local c = queue[head] -- 把 队列[头节点] 写入 local c
		head = head + 1 -- 把 头节点 加 1 存入 头节点
		order[#order + 1] = c -- 把 字符 写入 order[#order + 1]
		for _, nx in ipairs(graph[c + 1] or {}) do -- 遍历取 nx
			if not visited[nx + 1] then -- 若 not 已访问集合[nx 加 1] then
				visited[nx + 1] = true -- 把 true 写入 visited[nx + 1]
				queue[#queue + 1] = nx -- 把 nx 写入 queue[#queue + 1]
			end -- 终点
		end -- 终点
	end -- 终点
	return order -- 返回 order
end -- 终点
local g = { { 1, 2 }, { 3, 4 }, { 5 }, {}, {}, {} } -- 把 {{1,2},{3,4},{5},{},{},{}} 写入 local g
assert(table.concat(bfs_order(g, 0), ",") == "0,1,2,3,4,5") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
