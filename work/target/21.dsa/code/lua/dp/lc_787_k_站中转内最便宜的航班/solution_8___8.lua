-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133472893
-- LeetCode 787. K站中转内最便宜的航班 — Lua 版（方案8）
local function find_cheapest_price(n, flights, src, dst, k)
	local dist = {} -- 把 {} 写入 local dist
	for i = 0, n - 1 do
		dist[i] = math.huge
	end -- 让 下标 i 从 0 走到 元素个数（Lua 1 基）
	dist[src] = 0 -- 把 0 写入 dist[src]
	for _ = 0, k do -- 让 _ 从 0 走到 下标 k（Lua 1 基）
		local nd = {} -- 把 {} 写入 local nd
		for i = 0, n - 1 do
			nd[i] = dist[i]
		end -- 让 下标 i 从 0 走到 元素个数（Lua 1 基）
		for _, f in ipairs(flights) do -- 遍历取 f
			local u, v, w = f[1], f[2], f[3] -- 把 f[1], f[2], f[3] 写入 local u, v, w
			if dist[u] ~= math.huge and dist[u] + w < nd[v] then
				nd[v] = dist[u] + w -- 把 dist[节点 u] 加 权重 写入 nd[v]
			end -- 终点
		end -- 终点
		dist = nd -- 把 nd 存入 dist
	end -- 终点
	if dist[dst] == math.huge then
		return -1
	end -- 若 dist[dst] 等于 math.huge then return 减 1 终点
	return dist[dst] -- 返回 dist[dst]
end -- 终点
assert(
	find_cheapest_price(4, { { 0, 1, 100 }, { 1, 2, 100 }, { 2, 0, 100 }, { 1, 3, 600 }, { 2, 3, 200 } }, 0, 3, 1)
		== 700
) -- 断言校验
assert(
	find_cheapest_price(4, { { 0, 1, 100 }, { 1, 2, 100 }, { 2, 0, 100 }, { 1, 3, 600 }, { 2, 3, 200 } }, 0, 0, 1) == 0
) -- 断言校验
assert(
	find_cheapest_price(4, { { 0, 1, 100 }, { 1, 2, 100 }, { 2, 0, 100 }, { 1, 3, 600 }, { 2, 3, 200 } }, 0, 3, 2)
		== 400
) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
