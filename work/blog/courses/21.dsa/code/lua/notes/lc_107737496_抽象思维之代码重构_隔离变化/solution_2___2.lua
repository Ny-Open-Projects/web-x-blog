-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案2：螺旋矩阵递归填充）
local Matrix = {} -- 把 {} 写入 local Matrix
Matrix.__index = Matrix -- 把 Matrix 写入 Matrix.__index
function Matrix.new(size) -- function Matrix.new(大小)
	local m = setmetatable({ N = size, M = {} }, Matrix) -- 把 setmetatable({ N 赋值为 大小, M 赋值为 {} }, Matrix) 写入 local m
	for i = 1, size do -- 让 下标 i 从 1 走到 大小（Lua 1 基）
		m.M[i] = {} -- 把 {} 写入 m.M[i]
		for j = 1, size do
			m.M[i][j] = 0
		end -- 让 下标 j 从 1 走到 大小（Lua 1 基）
	end -- 终点
	return m -- 返回 映射表
end -- 终点
function Matrix:fill(num, begin_, size) -- function Matrix:fill(num, begin_, 大小)
	if size == 0 then
		return
	end -- 若 大小 等于 0 then return 终点
	if size == 1 then -- 若 大小 等于 1 then
		self.M[begin_ + 1][begin_ + 1] = num -- 把 num 写入 self.M[begin_ + 1][begin_ + 1]
		return -- return
	end -- 终点
	for j = 0, size - 2 do -- 让 下标 j 从 0 走到 大小（Lua 1 基）
		self.M[begin_ + j + 1][begin_ + 1] = num -- 把 num 写入 self.M[begin_ + j + 1][begin_ + 1]
		num = num + 1 -- 把 num 加 1 存入 num
	end -- 终点
	for j = 0, size - 2 do -- 让 下标 j 从 0 走到 大小（Lua 1 基）
		self.M[begin_ + size][begin_ + j + 1] = num -- 把 num 写入 self.M[begin_ + size][begin_ + j + 1]
		num = num + 1 -- 把 num 加 1 存入 num
	end -- 终点
	for j = size - 1, 1, -1 do -- 把 大小 减 1, 1, 减 1 do 写入 for j
		self.M[begin_ + j + 1][begin_ + size] = num -- 把 num 写入 self.M[begin_ + j + 1][begin_ + size]
		num = num + 1 -- 把 num 加 1 存入 num
	end -- 终点
	for j = size - 1, 1, -1 do -- 把 大小 减 1, 1, 减 1 do 写入 for j
		self.M[begin_ + 1][begin_ + j + 1] = num -- 把 num 写入 self.M[begin_ + 1][begin_ + j + 1]
		num = num + 1 -- 把 num 加 1 存入 num
	end -- 终点
	self:fill(num, begin_ + 1, size - 2) -- self:fill(num, begin_ 加 1, 大小 减 2)
end -- 终点

local function fmt_row(row) -- local function fmt_row(row)
	local parts = {} -- 把 {} 写入 local parts
	for i, x in ipairs(row) do -- 遍历取 x
		parts[i] = string.format("%2d", x) -- 把 string.format(「 对…取模 2d」, x) 写入 parts[i]
	end -- 终点
	return table.concat(parts, " ") -- 返回 table.concat(parts, 「 」)
end -- 终点

local m = Matrix.new(6) -- 把 Matrix.new(6) 写入 local m
m:fill(1, 0, 6) -- 映射表:fill(1, 0, 6)
local rows = {} -- 把 {} 写入 local rows
for i = 1, 6 do
	rows[i] = fmt_row(m.M[i])
end -- 让 下标 i 从 1 走到 6（Lua 1 基）
local want = { -- 把 { 写入 local want
	" 1 20 19 18 17 16",
	" 2 21 32 31 30 15",
	" 3 22 33 36 29 14",
	" 4 23 34 35 28 13",
	" 5 24 25 26 27 12",
	" 6  7  8  9 10 11",
}
for i = 1, 6 do -- 让 下标 i 从 1 走到 6（Lua 1 基）
	assert(rows[i] == want[i], "spiral6 row " .. i) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
