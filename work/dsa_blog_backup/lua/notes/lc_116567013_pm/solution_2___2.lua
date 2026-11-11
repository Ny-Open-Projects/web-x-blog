-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
-- LeetCode 116567013. PM — Lua 版（方案2：Brute-Force 双循环对齐）
local function match_v2(p, t) -- local function match_v2(节点, 另一字符串)
	local n, m = #t, #p -- 把 #另一字符串, #节点 写入 local n, m
	for i = 1, n - m + 1 do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		local j = 1 -- 把 1 写入 local j
		while j <= m and t:sub(i + j - 1, i + j - 1) == p:sub(j, j) do
			j = j + 1 -- 把 下标 j 加 1 存入 下标 j
		end -- 终点
		if j > m then
			return i - 1
		end -- 若 下标 j 超过 映射表 then return 下标 i 减 1 终点
	end -- 终点
	return -1 -- 返回 减 1
end -- 终点

local T = "now is the time for all good people to come" -- 把 「now is the time for all good people to come」 写入 local T
local cases = { -- 把 { 写入 local cases
	{ "people", T, 29 },
	{ "time", T, 11 },
	{ "all", T, 20 },
	{ "xyz", T, -1 },
	{ "a", "", -1 },
	{ "is", T, 4 },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	local got = match_v2(c[1], c[2]) -- 把 match_v2(字符[1], 字符[2]) 写入 local got
	assert(got == c[3], string.format("case %d failed: match_v2(%s)=%d want %d", idx, c[1], got, c[3])) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
