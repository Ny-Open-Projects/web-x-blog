-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130741193
-- LeetCode 714. 买卖股票的最佳时机含手续费 — Lua 版（方案1）
local function max_profit_fee(prices, fee) -- local function max_profit_fee(价格序列, fee)
	local hold, sold = -prices[1], 0 -- 把 减 价格序列[1], 0 写入 local hold, sold
	for i = 2, #prices do -- 把 2, #价格序列 do 写入 for i
		local p = prices[i] -- 把 价格序列[下标 i] 写入 local p
		local nh = math.max(hold, sold - p) -- 把 math.取较大值 hold, sold 减 节点) 写入 local nh
		local ns = math.max(sold, hold + p - fee) -- 把 math.取较大值 sold, hold 加 节点 减 fee) 写入 local ns
		hold, sold = nh, ns -- 把 nh, ns 写入 hold, sold
	end -- 终点
	return sold -- 返回 sold
end -- 终点
assert(max_profit_fee({ 1, 3, 2, 8, 4, 9 }, 2) == 8) -- 断言校验
assert(max_profit_fee({ 1 }, 1) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
