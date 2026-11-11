-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
-- LeetCode 1143. 最长公共子序列 — Lua 版（方案1）
local function longest_common_subsequence(t1, t2) -- local function longest_common_subsequence(t1, t2)
	local m, n = #t1, #t2 -- 把 #t1, #t2 写入 local m, n
	local dp = {} -- 把 {} 写入 local dp
	for j = 0, n do
		dp[j] = 0
	end -- 让 下标 j 从 0 走到 元素个数（Lua 1 基）
	for i = 1, m do -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
		local prev_diag = 0 -- 把 0 写入 local prev_diag
		for j = 1, n do -- 让 下标 j 从 1 走到 元素个数（Lua 1 基）
			local tmp = dp[j] -- 把 DP 表[下标 j] 写入 local tmp
			if t1:sub(i, i) == t2:sub(j, j) then
				dp[j] = prev_diag + 1
			else
				dp[j] = math.max(dp[j], dp[j - 1])
			end -- 否则
			prev_diag = tmp -- 把 临时变量 存入 prev_diag
		end -- 终点
	end -- 终点
	return dp[n] -- 返回 DP 表[元素个数]
end -- 终点
assert(longest_common_subsequence("abcde", "ace") == 3) -- 断言校验
assert(longest_common_subsequence("abc", "abc") == 3) -- 断言校验
assert(longest_common_subsequence("abc", "def") == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
