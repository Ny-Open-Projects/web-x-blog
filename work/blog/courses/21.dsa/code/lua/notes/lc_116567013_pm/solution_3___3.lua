-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
-- LeetCode 116567013. PM — Lua 版（方案3：KMP，next 表失配大步跳跃）
local function build_next(p) -- local function build_next(节点)
	local m = #p -- 把 #节点 写入 local m
	local N = {} -- 把 {} 写入 local N
	for i = 1, m do
		N[i] = -1
	end -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
	local J, T = 0, -1 -- 0 基逻辑游标（存储仍按 1 基下标）
	while J < m - 1 do -- while J 小于 映射表 减 1 do
		if T < 0 or p:sub(J + 1, J + 1) == p:sub(T + 1, T + 1) then
			J = J + 1 -- 把 J 加 1 存入 J
			T = T + 1 -- 把 T 加 1 存入 T
			N[J + 1] = T -- 把 T 写入 N[J + 1]
		else -- 否则
			T = N[T + 1] -- 把 N[T 加 1] 存入 T
		end -- 终点
	end -- 终点
	return N -- 返回 N
end -- 终点

local function kmp_match(p, t) -- local function kmp_match(节点, 另一字符串)
	local N = build_next(p) -- 把 build_next(节点) 写入 local N
	local n, m = #t, #p -- 把 #另一字符串, #节点 写入 local n, m
	local i, j = 1, 1 -- 把 1, 1 写入 local i, j
	local at = function(s, k)
		return s:sub(k, k)
	end
	while j <= m and i <= n do -- 把 映射表 and 下标 i 不超过 元素个数 do 写入 while j <
		if j < 1 or at(t, i) == at(p, j) then -- 若 下标 j 小于 1 or at(另一字符串, 下标 i) 等于 at(节点, 下标 j) then
			i = i + 1 -- 把 下标 i 加 1 存入 下标 i
			j = j + 1 -- 把 下标 j 加 1 存入 下标 j
		else -- 否则
			j = N[j] + 1 -- N 存 0 基，转 1 基
		end -- 终点
	end -- 终点
	if j > m then
		return i - j
	end -- 若 下标 j 超过 映射表 then return 下标 i 减 下标 j 终点
	return -1 -- 返回 减 1
end -- 终点

local function eq_arr(a, b) -- local function eq_arr(数组, b)
	if #a ~= #b then
		return false
	end -- 若 #数组 ~ 赋值为 #b then return false 终点
	for i = 1, #a do
		if a[i] ~= b[i] then
			return false
		end
	end
	return true -- 返回 true
end -- 终点

local T = "now is the time for all good people to come" -- 把 「now is the time for all good people to come」 写入 local T
local cases = { -- 把 { 写入 local cases
	{ "people", T, 29 },
	{ "all", T, 20 },
	{ "no", T, 0 },
	{ "xyz", T, -1 },
	{ "a", "", -1 },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	local got = kmp_match(c[1], c[2]) -- 把 kmp_match(字符[1], 字符[2]) 写入 local got
	assert(got == c[3], "case " .. idx .. " failed") -- 断言校验
end -- 终点
-- 特殊边界
assert(kmp_match("aaaa", "aaaaa") == 0, "overlap failed") -- 断言校验
assert(kmp_match("aaab", "aaabaaa") == 0, "reuse failed") -- 断言校验
-- next 表
assert(eq_arr(build_next("ababaca"), { -1, 0, 0, 1, 2, 3, 0 }), "next ababaca failed") -- 断言校验
assert(eq_arr(build_next("aaaa"), { -1, 0, 1, 2 }), "next aaaa failed") -- 断言校验
assert(eq_arr(build_next("abcd"), { -1, 0, 0, 0 }), "next abcd failed") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
