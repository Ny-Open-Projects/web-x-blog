-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案5：Matrix 封装 set/call）
local Matrix = {} -- 把 {} 写入 local Matrix
Matrix.__index = Matrix -- 把 Matrix 写入 Matrix.__index
function Matrix.new(r, c) -- function Matrix.new(右指针, 字符)
	local m = setmetatable({ row = r, col = c, buf = {} }, Matrix)
	for i = 1, r do -- 让 下标 i 从 1 走到 右指针（Lua 1 基）
		m.buf[i] = {} -- 把 {} 写入 m.buf[i]
		for j = 1, c do
			m.buf[i][j] = 0
		end -- 让 下标 j 从 1 走到 字符（Lua 1 基）
	end -- 终点
	return m -- 返回 映射表
end -- 终点
function Matrix:set(r, c, v)
	self.buf[r + 1][c + 1] = v
end
function Matrix:call(r, c)
	return self.buf[r + 1][c + 1]
end

local m = Matrix.new(4, 5) -- 把 Matrix.new(4, 5) 写入 local m
for i = 0, 3 do -- 让 下标 i 从 0 走到 3（Lua 1 基）
	for j = 0, 4 do
		m:set(i, j, i * j)
	end -- 让 下标 j 从 0 走到 4（Lua 1 基）
end -- 终点
assert(m:call(2, 3) == 6, "matrix call") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
