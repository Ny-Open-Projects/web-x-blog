-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113764246
-- 图搜索之DFS详解 — Lua 版（方案2）
local function dfs_order(graph, start) -- local function dfs_order(graph, 起点)
	local visited = {} -- 把 {} 写入 local visited
	local order = {} -- 把 {} 写入 local order
	local function go(c) -- local function go(字符)
		visited[c + 1] = true -- 把 true 写入 visited[c + 1]
		order[#order + 1] = c -- 把 字符 写入 order[#order + 1]
		for _, nx in ipairs(graph[c + 1] or {}) do -- 遍历取 nx
			if not visited[nx + 1] then
				go(nx)
			end -- 若 not 已访问集合[nx 加 1] then go(nx) 终点
		end -- 终点
	end -- 终点
	go(start) -- go(起点)
	return order -- 返回 order
end -- 终点
local g = { { 1, 2 }, { 3, 4 }, { 5 }, {}, {}, {} } -- 把 {{1,2},{3,4},{5},{},{},{}} 写入 local g
assert(table.concat(dfs_order(g, 0), ",") == "0,1,3,4,2,5") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
