-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113951689
-- LeetCode 113951689. 动态规划之 LCS — Lua 版（最长公共子序列：DP 填表 + 回溯构造）

local function sub(s, i) -- local function sub(字符串, 下标 i)
	return s:sub(i, i) -- 返回 字符串:sub(下标 i, 下标 i)
end -- 终点

local function lcs_table(a, b) -- local function lcs_table(数组, b)
	local m, n = #a, #b -- 把 #数组, #b 写入 local m, n
	local dp = {} -- 把 {} 写入 local dp
	for i = 0, m do -- 让 下标 i 从 0 走到 映射表（Lua 1 基）
		dp[i] = {} -- 把 {} 写入 dp[i]
		for j = 0, n do
			dp[i][j] = 0
		end -- 让 下标 j 从 0 走到 元素个数（Lua 1 基）
	end -- 终点
	for i = 1, m do -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
		for j = 1, n do -- 让 下标 j 从 1 走到 元素个数（Lua 1 基）
			if sub(a, i) == sub(b, j) then -- 若 sub(数组, 下标 i) 等于 sub(b, 下标 j) then
				dp[i][j] = dp[i - 1][j - 1] + 1 -- 把 DP 表[下标 i 减 1][下标 j 减 1] 加 1 写入 dp[i][j]
			else -- 否则
				dp[i][j] = math.max(dp[i - 1][j], dp[i][j - 1])
			end -- 终点
		end -- 终点
	end -- 终点
	return dp -- 返回 DP 表
end -- 终点

local function lcs_length(a, b) -- local function lcs_length(数组, b)
	local dp = lcs_table(a, b) -- 把 lcs_table(数组, b) 写入 local dp
	return dp[#a][#b] -- 返回 DP 表[#数组][#b]
end -- 终点

local function lcs_string(a, b) -- local function lcs_string(数组, b)
	local dp = lcs_table(a, b) -- 把 lcs_table(数组, b) 写入 local dp
	local i, j = #a, #b -- 把 #数组, #b 写入 local i, j
	local out = {} -- 把 {} 写入 local out
	while i > 0 and j > 0 do -- while 下标 i 超过 0 and 下标 j 超过 0 do
		if sub(a, i) == sub(b, j) then -- 若 sub(数组, 下标 i) 等于 sub(b, 下标 j) then
			out[#out + 1] = sub(a, i) -- 把 sub(数组, 下标 i) 写入 out[#out + 1]
			i = i - 1 -- 把 下标 i 减 1 存入 下标 i
			j = j - 1 -- 把 下标 j 减 1 存入 下标 j
		elseif dp[i - 1][j] >= dp[i][j - 1] then -- 把 DP 表[下标 i][下标 j 减 1] then 写入 elseif dp[i - 1][j] >
			i = i - 1 -- 把 下标 i 减 1 存入 下标 i
		else -- 否则
			j = j - 1 -- 把 下标 j 减 1 存入 下标 j
		end -- 终点
	end -- 终点
	-- 反转拼接
	local s = {} -- 把 {} 写入 local s
	for k = #out, 1, -1 do
		s[#s + 1] = out[k]
	end -- 把 #out, 1, 减 1 do 字符串[#字符串 加 1] 赋值为 out[下标 k] 终点 写入 for k
	return table.concat(s) -- 返回 table.concat(字符串)
end -- 终点

local function is_common_sub(a, b, s) -- local function is_common_sub(数组, b, 字符串)
	local ia, ib = 1, 1 -- 把 1, 1 写入 local ia, ib
	for k = 1, #s do -- 把 1, #字符串 do 写入 for k
		local ch = sub(s, k) -- 把 sub(字符串, 下标 k) 写入 local ch
		while ia <= #a and sub(a, ia) ~= ch do
			ia = ia + 1
		end
		while ib <= #b and sub(b, ib) ~= ch do
			ib = ib + 1
		end
		if ia > #a or ib > #b then
			return false
		end -- 若 ia 超过 #数组 or ib 超过 #b then return false 终点
		ia = ia + 1 -- 把 ia 加 1 存入 ia
		ib = ib + 1 -- 把 ib 加 1 存入 ib
	end -- 终点
	return true -- 返回 true
end -- 终点

local cases = { -- 把 { 写入 local cases
	{ "ABCBDAB", "BDCABA", 4 },
	{ "AGGTAB", "GXTXAYB", 4 },
	{ "abc", "abc", 3 },
	{ "", "abc", 0 },
	{ "abc", "xyz", 0 },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	local got = lcs_length(c[1], c[2]) -- 把 lcs_length(字符[1], 字符[2]) 写入 local got
	assert(got == c[3], string.format("case %d failed: got %d want %d", idx, got, c[3])) -- 断言校验
end -- 终点
for _, p in ipairs({ { "ABCBDAB", "BDCABA" }, { "AGGTAB", "GXTXAYB" } }) do -- 遍历取 节点
	local s = lcs_string(p[1], p[2]) -- 把 lcs_string(节点[1], 节点[2]) 写入 local s
	assert(#s == lcs_length(p[1], p[2]), "lcs_string length mismatch: " .. s) -- 断言校验
	assert(is_common_sub(p[1], p[2], s), "not a common subsequence: " .. s) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
