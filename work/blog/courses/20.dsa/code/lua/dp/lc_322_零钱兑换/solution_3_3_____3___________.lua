-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130683917
-- LeetCode 322. 零钱兑换 — Lua 版（方案3）
local function coin_change(coins, amount) -- local function coin_change(硬币面额, 目标金额)
	local dp = {} -- 把 {} 写入 local dp
	for i = 0, amount do
		dp[i] = math.huge
	end -- 让 下标 i 从 0 走到 目标金额（Lua 1 基）
	dp[0] = 0 -- 把 0 写入 dp[0]
	for a = 1, amount do -- 让 数组 从 1 走到 目标金额（Lua 1 基）
		for _, c in ipairs(coins) do -- 遍历取 字符
			if c <= a and dp[a - c] ~= math.huge then -- 若 字符 不超过 数组 and DP 表[数组 减 字符] ~ 赋值为 math.huge then
				if dp[a - c] + 1 < dp[a] then
					dp[a] = dp[a - c] + 1
				end
			end -- 终点
		end -- 终点
	end -- 终点
	if dp[amount] == math.huge then
		return -1
	end -- 若 DP 表[目标金额] 等于 math.huge then return 减 1 终点
	return dp[amount] -- 返回 DP 表[目标金额]
end -- 终点
assert(coin_change({ 1, 2, 5 }, 11) == 3) -- 断言校验
assert(coin_change({ 2 }, 3) == -1) -- 断言校验
assert(coin_change({ 1 }, 0) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
