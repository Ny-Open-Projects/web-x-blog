-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
-- LeetCode 116567013. PM — Lua 版（方案4：buildNext 单测）
local function build_next(p) -- local function build_next(节点)
	local m = #p -- 把 #节点 写入 local m
	local N = {} -- 把 {} 写入 local N
	for i = 1, m do
		N[i] = -1
	end -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
	local J, T = 0, -1 -- 0 基逻辑游标（存储按 1 基下标）
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

assert(eq_arr(build_next("ababaca"), { -1, 0, 0, 1, 2, 3, 0 }), "ababaca failed") -- 断言校验
assert(eq_arr(build_next("aaaa"), { -1, 0, 1, 2 }), "aaaa failed") -- 断言校验
assert(eq_arr(build_next("abcabc"), { -1, 0, 0, 0, 1, 2 }), "abcabc failed") -- 断言校验
assert(eq_arr(build_next("abcd"), { -1, 0, 0, 0 }), "abcd failed") -- 断言校验
assert(eq_arr(build_next("a"), { -1 }), "a failed") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
