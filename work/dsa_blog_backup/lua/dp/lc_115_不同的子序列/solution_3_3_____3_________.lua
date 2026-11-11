-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130590161
-- LeetCode 115. 不同的子序列 — Lua 版（方案3）
local function num_distinct(s, t) -- local function num_distinct(字符串, 另一字符串)
	local m, n = #s, #t -- 把 #字符串, #另一字符串 写入 local m, n
	local dp = {} -- 把 {} 写入 local dp
	for j = 0, n do
		dp[j] = 0
	end -- 让 下标 j 从 0 走到 元素个数（Lua 1 基）
	dp[0] = 1 -- 把 1 写入 dp[0]
	for i = 1, m do -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
		for j = n, 1, -1 do -- 把 元素个数, 1, 减 1 do 写入 for j
			if s:sub(i, i) == t:sub(j, j) then
				dp[j] = dp[j] + dp[j - 1]
			end
		end -- 终点
	end -- 终点
	return dp[n] -- 返回 DP 表[元素个数]
end -- 终点
assert(num_distinct("rabbbit", "rabbit") == 3) -- 断言校验
assert(num_distinct("babgbag", "bag") == 5) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
