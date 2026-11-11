-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108717090
-- 减治策略之详解Dijkstra算法 — Lua 版（方案1）
local function dijkstra_shortest(graph, start) -- local function dijkstra_shortest(graph, 起点)
	local n = #graph -- 把 #graph 写入 local n
	local dist, visited = {}, {} -- 把 {}, {} 写入 local dist, visited
	for i = 1, n do
		dist[i] = math.huge
		visited[i] = false
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
	dist[start + 1] = 0 -- 把 0 写入 dist[start + 1]
	while true do -- while true do
		local u = nil -- 把 nil 写入 local u
		for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
			if not visited[i] and (u == nil or dist[i] < dist[u]) then
				u = i
			end
		end -- 终点
		if u == nil or dist[u] == math.huge then
			break
		end -- 若 节点 u 等于 nil or dist[节点 u] 等于 math.huge then break 终点
		visited[u] = true -- 把 true 写入 visited[u]
		for _, e in ipairs(graph[u] or {}) do -- 遍历取 e
			local v, w = e[1] + 1, e[2] -- 把 e[1] 加 1, e[2] 写入 local v, w
			if dist[u] + w < dist[v] then
				dist[v] = dist[u] + w
			end
		end -- 终点
	end -- 终点
	local out = {} -- 把 {} 写入 local out
	for i = 1, n do
		out[i] = dist[i]
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
	return out -- 返回 out
end -- 终点
local g = { { { 1, 10 }, { 2, 3 } }, { { 2, 1 }, { 3, 2 } }, { { 1, 4 }, { 3, 8 } }, { { 4, 7 } }, {} }
local d = dijkstra_shortest(g, 0) -- 把 dijkstra_shortest(g, 0) 写入 local d
assert(d[1] == 0 and d[2] == 7 and d[3] == 3 and d[4] == 9 and d[5] == 16) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
