-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136847926
-- LeetCode 502. IPO — Lua 版（方案1）
local function find_maximized_capital(k, w, profits, capital)
	local n = #profits -- 把 #profits 写入 local n
	local used = {} -- 把 {} 写入 local used
	for _ = 1, k do -- 让 _ 从 1 走到 下标 k（Lua 1 基）
		local best, best_j = -1, -1 -- 把 减 1, 减 1 写入 local best, best_j
		for j = 1, n do -- 让 下标 j 从 1 走到 元素个数（Lua 1 基）
			if not used[j] and capital[j] <= w and profits[j] > best then
				best = profits[j] -- 把 profits[下标 j] 存入 当前最优
				best_j = j -- 把 下标 j 存入 best_j
			end -- 终点
		end -- 终点
		if best_j < 0 then
			break
		end -- 若 best_j 小于 0 then break 终点
		w = w + best -- 把 权重 加 当前最优 存入 权重
		used[best_j] = true -- 把 true 写入 used[best_j]
	end -- 终点
	return w -- 返回 权重
end -- 终点
assert(find_maximized_capital(2, 0, { 1, 2, 3 }, { 0, 1, 1 }) == 4) -- 断言校验
assert(find_maximized_capital(3, 0, { 1, 2, 3 }, { 0, 1, 2 }) == 6) -- 断言校验
assert(find_maximized_capital(1, 0, { 1, 2 }, { 1, 2 }) == 0) -- 断言校验
assert(find_maximized_capital(2, 1, { 1, 2, 3 }, { 1, 1, 2 }) == 6) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
