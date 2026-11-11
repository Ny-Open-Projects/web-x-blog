-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
-- LeetCode 116567013. PM — Lua 版（方案1：Brute-Force 主串指针回退）
local function match_v1(p, t) -- local function match_v1(节点, 另一字符串)
	local n, m = #t, #p -- 把 #另一字符串, #节点 写入 local n, m
	local i, j = 1, 1 -- 1 基
	while j <= m and i <= n do -- 把 映射表 and 下标 i 不超过 元素个数 do 写入 while j <
		if t:sub(i, i) == p:sub(j, j) then -- 若 另一字符串:sub(下标 i, 下标 i) 等于 节点:sub(下标 j, 下标 j) then
			i, j = i + 1, j + 1 -- 把 下标 i 加 1, 下标 j 加 1 写入 i, j
		else -- 否则
			i = i - j + 2 -- 主串回退到本次对齐的下一位置（1 基）
			j = 1 -- 把 1 存入 下标 j
		end -- 终点
	end -- 终点
	if j > m then
		return i - j
	end -- 若 下标 j 超过 映射表 then return 下标 i 减 下标 j 终点
	return -1 -- 返回 减 1
end -- 终点

local T = "now is the time for all good people to come" -- 把 「now is the time for all good people to come」 写入 local T
local cases = { -- 把 { 写入 local cases
	{ "people", T, 29 },
	{ "good", T, 24 },
	{ "xyz", T, -1 },
	{ "a", "", -1 }, -- 边界：空文本
	{ "is", T, 4 },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	local got = match_v1(c[1], c[2]) -- 把 match_v1(字符[1], 字符[2]) 写入 local got
	assert(got == c[3], string.format("case %d failed: match_v1(%s)=%d want %d", idx, c[1], got, c[3])) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
