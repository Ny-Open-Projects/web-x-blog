-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690
-- 抽象思维之对比算法 发现共性 — Lua 版（方案2）
local function climb_stairs_refactored(n) -- local function climb_stairs_refactored(元素个数)
	if n == 0 then
		return 1
	end -- 若 元素个数 等于 0 then return 1 终点
	if n < 0 then
		return 0
	end -- 若 元素个数 小于 0 then return 0 终点
	local dp = {} -- 把 {} 写入 local dp
	dp[0] = 1 -- 把 1 写入 dp[0]
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		dp[i] = dp[i - 1] -- 把 DP 表[下标 i 减 1] 写入 dp[i]
		if i >= 2 then
			dp[i] = dp[i] + dp[i - 2]
		end
		if i >= 3 then
			dp[i] = dp[i] + dp[i - 3]
		end
	end -- 终点
	return dp[n] -- 返回 DP 表[元素个数]
end -- 终点
assert(climb_stairs_refactored(10) == 274) -- 断言校验
assert(climb_stairs_refactored(3) == 4) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
