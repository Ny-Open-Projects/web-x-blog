-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130515763
-- LeetCode 121. 买卖股票的最佳时机 — Lua 版（方案3）
local function max_profit(prices) -- local function max_profit(价格序列)
	local min_p, best = math.huge, 0 -- 把 math.huge, 0 写入 local min_p, best
	for _, p in ipairs(prices) do -- 遍历取 节点
		if p < min_p then
			min_p = p
		end -- 若 节点 小于 min_p then min_p 赋值为 节点 终点
		if p - min_p > best then
			best = p - min_p
		end -- 若 节点 减 min_p 超过 当前最优 then 当前最优 赋值为 节点 减 min_p 终点
	end -- 终点
	return best -- 返回 当前最优
end -- 终点
assert(max_profit({ 7, 1, 5, 3, 6, 4 }) == 5) -- 断言校验
assert(max_profit({ 7, 6, 4, 3, 1 }) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
