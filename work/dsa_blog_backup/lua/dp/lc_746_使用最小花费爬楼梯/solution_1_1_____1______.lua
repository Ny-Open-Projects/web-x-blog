-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130521152
-- LeetCode 746. 使用最小花费爬楼梯 — Lua 版（方案1）
local function min_cost_climbing_stairs(cost) -- local function min_cost_climbing_stairs(cost)
	local a, b = 0, 0 -- 把 0, 0 写入 local a, b
	for i = 3, #cost + 1 do -- 把 3, #cost 加 1 do 写入 for i
		local t = math.min(a + cost[i - 2], b + cost[i - 1])
		a, b = b, t -- 把 b, 另一字符串 写入 a, b
	end -- 终点
	return b -- 返回 b
end -- 终点
assert(min_cost_climbing_stairs({ 10, 15, 20 }) == 15) -- 断言校验
assert(min_cost_climbing_stairs({ 1, 100, 1, 1, 1, 100, 1, 1, 100, 1 }) == 6) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
