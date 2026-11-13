-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130641517
-- LeetCode 62. 不同路径 — Lua 版（方案1）
local function unique_paths(m, n) -- local function unique_paths(映射表, 元素个数)
	local dp = {} -- 把 {} 写入 local dp
	for j = 1, n do
		dp[j] = 1
	end -- 让 下标 j 从 1 走到 元素个数（Lua 1 基）
	for _ = 2, m do -- 让 _ 从 2 走到 映射表（Lua 1 基）
		for j = 2, n do
			dp[j] = dp[j] + dp[j - 1]
		end -- 让 下标 j 从 2 走到 元素个数（Lua 1 基）
	end -- 终点
	return dp[n] -- 返回 DP 表[元素个数]
end -- 终点
assert(unique_paths(3, 7) == 28) -- 断言校验
assert(unique_paths(3, 2) == 3) -- 断言校验
assert(unique_paths(1, 1) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
