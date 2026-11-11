-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130687299
-- LeetCode 1027. 最长等差数列 — Lua 版（方案1）
local function longest_arith_seq_length(nums) -- local function longest_arith_seq_length(数组)
	local n = #nums -- 把 #数组 写入 local n
	local dp = {} -- 把 {} 写入 local dp
	for i = 1, n do
		dp[i] = {}
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
	local best = 1 -- 把 1 写入 local best
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		for j = 1, i - 1 do -- 让 下标 j 从 1 走到 下标 i（Lua 1 基）
			local d = nums[i] - nums[j] -- 把 数组[下标 i] 减 数组[下标 j] 写入 local d
			local cur = (dp[j][d] or 1) + 1 -- 把 (DP 表[下标 j][d] or 1) 加 1 写入 local cur
			dp[i][d] = cur -- 把 当前值 写入 dp[i][d]
			if cur > best then
				best = cur
			end -- 若 当前值 超过 当前最优 then 当前最优 赋值为 当前值 终点
		end -- 终点
	end -- 终点
	return best -- 返回 当前最优
end -- 终点
assert(longest_arith_seq_length({ 9, 4, 7, 2, 10 }) == 3) -- 断言校验
assert(longest_arith_seq_length({ 3, 6, 9, 12 }) == 4) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
