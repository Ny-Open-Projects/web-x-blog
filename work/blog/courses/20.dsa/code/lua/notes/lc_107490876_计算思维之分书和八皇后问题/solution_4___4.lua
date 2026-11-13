-- 来源：https://blog.csdn.net/tyro_java/article/details/107490876
-- LeetCode 107490876. 分书和八皇后问题 — Lua 版（方案4：八皇后显式栈迭代）
local function valid(x, a) -- local function valid(x, 数组)
	local y = #a + 1 -- 把 #数组 加 1 写入 local y
	for i = 1, #a do -- 把 1, #数组 do 写入 for i
		if x == a[i] or math.abs(y - i) == math.abs(x - a[i]) then
			return false -- 返回 false
		end -- 终点
	end -- 终点
	return true -- 返回 true
end -- 终点

local function n_queens_stack(n) -- local function n_queens_stack(元素个数)
	local solutions = {} -- 把 {} 写入 local solutions
	local stack = { {} } -- 把 {{}} 写入 local stack
	while #stack > 0 do -- while #栈 超过 0 do
		local a = table.remove(stack) -- 弹栈（LIFO）
		if #a == n then -- 若 #数组 等于 元素个数 then
			solutions[#solutions + 1] = a -- 把 数组 写入 solutions[#solutions + 1]
		else -- 否则
			for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
				if valid(i, a) then -- 若 valid(下标 i, 数组) then
					local b = {} -- 把 {} 写入 local b
					for k = 1, #a do
						b[k] = a[k]
					end -- 把 1, #数组 do b[下标 k] 赋值为 数组[下标 k] 终点 写入 for k
					b[#b + 1] = i -- 把 下标 i 写入 b[#b + 1]
					stack[#stack + 1] = b -- 把 b 写入 stack[#stack + 1]
				end -- 终点
			end -- 终点
		end -- 终点
	end -- 终点
	return solutions -- 返回 solutions
end -- 终点

local cases = { -- 把 { 写入 local cases
	{ 8, 92, { 8, 4, 1, 3, 6, 2, 7, 5 } },
	{ 1, 1, { 1 } },
	{ 2, 0, nil },
	{ 4, 2, { 3, 1, 4, 2 } },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	local sols = n_queens_stack(c[1]) -- 把 n_queens_stack(字符[1]) 写入 local sols
	assert(#sols == c[2], "case " .. idx .. " count mismatch: " .. #sols) -- 断言校验
	if c[3] then -- 若 字符[3] then
		for j = 1, #c[3] do -- 把 1, #字符[3] do 写入 for j
			assert(sols[1][j] == c[3][j], "case " .. idx .. " first mismatch") -- 断言校验
		end -- 终点
	end -- 终点
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
