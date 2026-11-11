-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133925028
-- LeetCode 122. 买卖股票的最佳时机II — Lua 版（方案2）
local function max_profit(prices) -- local function max_profit(价格序列)
	local profit = 0 -- 把 0 写入 local profit
	for i = 2, #prices do -- 把 2, #价格序列 do 写入 for i
		if prices[i] > prices[i - 1] then -- 若 价格序列[下标 i] 超过 价格序列[下标 i 减 1] then
			profit = profit + prices[i] - prices[i - 1] -- 把 profit 加 价格序列[下标 i] 减 价格序列[下标 i 减 1] 存入 profit
		end -- 终点
	end -- 终点
	return profit -- 返回 profit
end -- 终点
assert(max_profit({ 7, 1, 5, 3, 6, 4 }) == 7) -- 断言校验
assert(max_profit({ 1, 2, 3, 4, 5 }) == 4) -- 断言校验
assert(max_profit({ 7, 6, 4, 3, 1 }) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
