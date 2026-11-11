-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130588647
-- LeetCode 123. 买卖股票的最佳时机III — Lua 版（方案2）
local function max_profit_iii(prices) -- local function max_profit_iii(价格序列)
	local buy1, sell1 = -math.huge, 0 -- 把 减 math.huge, 0 写入 local buy1, sell1
	local buy2, sell2 = -math.huge, 0 -- 把 减 math.huge, 0 写入 local buy2, sell2
	for _, p in ipairs(prices) do -- 遍历取 节点
		if -p > buy1 then
			buy1 = -p
		end -- 若 减 节点 超过 buy1 then buy1 赋值为 减 节点 终点
		if buy1 + p > sell1 then
			sell1 = buy1 + p
		end -- 若 buy1 加 节点 超过 sell1 then sell1 赋值为 buy1 加 节点 终点
		if sell1 - p > buy2 then
			buy2 = sell1 - p
		end -- 若 sell1 减 节点 超过 buy2 then buy2 赋值为 sell1 减 节点 终点
		if buy2 + p > sell2 then
			sell2 = buy2 + p
		end -- 若 buy2 加 节点 超过 sell2 then sell2 赋值为 buy2 加 节点 终点
	end -- 终点
	return sell2 -- 返回 sell2
end -- 终点
assert(max_profit_iii({ 1, 2, 3 }) == 2) -- 断言校验
assert(max_profit_iii({ 1, 2, 3, 4, 5 }) == 4) -- 断言校验
assert(max_profit_iii({ 7, 6, 4, 3, 1 }) == 0) -- 断言校验
assert(max_profit_iii({ 3, 3, 5, 0, 0, 3, 1, 4 }) == 6) -- 断言校验
assert(max_profit_iii({ 1 }) == 0) -- 断言校验
assert(max_profit_iii({ 1, 2 }) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
