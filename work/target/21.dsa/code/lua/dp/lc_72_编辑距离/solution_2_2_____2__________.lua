-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130540333
-- LeetCode 72. 编辑距离 — Lua 版（方案2）
local function min_distance(w1, w2) -- local function min_distance(w1, w2)
	local m, n = #w1, #w2 -- 把 #w1, #w2 写入 local m, n
	local dp = {} -- 把 {} 写入 local dp
	for j = 0, n do
		dp[j] = j
	end -- 让 下标 j 从 0 走到 元素个数（Lua 1 基）
	for i = 1, m do -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
		local prev_diag = dp[0] -- 把 DP 表[0] 写入 local prev_diag
		dp[0] = i -- 把 下标 i 写入 dp[0]
		for j = 1, n do -- 让 下标 j 从 1 走到 元素个数（Lua 1 基）
			local tmp = dp[j] -- 把 DP 表[下标 j] 写入 local tmp
			if w1:sub(i, i) == w2:sub(j, j) then
				dp[j] = prev_diag
			else
				dp[j] = 1 + math.min(prev_diag, dp[j], dp[j - 1])
			end -- 否则
			prev_diag = tmp -- 把 临时变量 存入 prev_diag
		end -- 终点
	end -- 终点
	return dp[n] -- 返回 DP 表[元素个数]
end -- 终点
assert(min_distance("horse", "ros") == 3) -- 断言校验
assert(min_distance("intention", "execution") == 5) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
