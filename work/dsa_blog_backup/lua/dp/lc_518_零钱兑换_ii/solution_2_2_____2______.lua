-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734179
-- LeetCode 518. 零钱兑换II — Lua 版（方案2）
local function change(amount, coins) -- local function change(目标金额, 硬币面额)
	local dp = {} -- 把 {} 写入 local dp
	for i = 0, amount do
		dp[i] = 0
	end -- 让 下标 i 从 0 走到 目标金额（Lua 1 基）
	dp[0] = 1 -- 把 1 写入 dp[0]
	for _, c in ipairs(coins) do -- 遍历取 字符
		for a = c, amount do -- 把 字符, 目标金额 do 写入 for a
			dp[a] = dp[a] + dp[a - c] -- 把 DP 表[数组] 加 DP 表[数组 减 字符] 写入 dp[a]
		end -- 终点
	end -- 终点
	return dp[amount] -- 返回 DP 表[目标金额]
end -- 终点
assert(change(5, { 1, 2, 5 }) == 4) -- 断言校验
assert(change(3, { 2 }) == 0) -- 断言校验
assert(change(10, { 1, 2, 5 }) == 10) -- 断言校验
assert(change(0, { 1, 2 }) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
