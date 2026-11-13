-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案7：螺旋矩阵分派表 place）
local function place(row, col, direction, n, m) -- local function place(row, col, direction, 元素个数, 映射表)
	local handlers = { -- 把 { 写入 local handlers
		D = function() -- 把 function() 存入 D
			if row + 1 <= n and m[row + 1][col] == 0 then
				return row + 1, col, nil
			end
			return row, col + 1, "R" -- 返回 row, col 加 1, 「R」
		end,
		R = function() -- 把 function() 存入 R
			if col + 1 <= n and m[row][col + 1] == 0 then
				return row, col + 1, nil
			end
			return row - 1, col, "U" -- 返回 row 减 1, col, 「U」
		end,
		U = function() -- 把 function() 存入 U
			if row - 1 >= 1 and m[row - 1][col] == 0 then
				return row - 1, col, nil
			end
			return row, col - 1, "L" -- 返回 row, col 减 1, 「L」
		end,
		L = function() -- 把 function() 存入 L
			if col - 1 >= 1 and m[row][col - 1] == 0 then
				return row, col - 1, nil
			end
			return row + 1, col, "D" -- 返回 row 加 1, col, 「D」
		end,
	}
	return handlers[direction]() -- 返回 handlers[direction]()
end -- 终点

local function fill_spiral(n) -- local function fill_spiral(元素个数)
	local m = {} -- 把 {} 写入 local m
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		m[i] = {} -- 把 {} 写入 m[i]
		for j = 1, n do
			m[i][j] = 0
		end -- 让 下标 j 从 1 走到 元素个数（Lua 1 基）
	end -- 终点
	local row, col = 1, 1 -- 把 1, 1 写入 local row, col
	local direction = "D" -- 把 「D」 写入 local direction
	local num = 1 -- 把 1 写入 local num
	while num <= n * n do -- 把 元素个数 乘 元素个数 do 写入 while num <
		m[row][col] = num -- 把 num 写入 m[row][col]
		num = num + 1 -- 把 num 加 1 存入 num
		local r, c, d = place(row, col, direction, n, m) -- 把 place(row, col, direction, 元素个数, 映射表) 写入 local r, c, d
		row, col = r, c -- 把 右指针, 字符 写入 row, col
		if d then
			direction = d
		end -- 若 d then direction 赋值为 d 终点
	end -- 终点
	return m -- 返回 映射表
end -- 终点

local function check(got, want, n, tag) -- local function check(got, want, 元素个数, tag)
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		for j = 1, n do -- 让 下标 j 从 1 走到 元素个数（Lua 1 基）
			assert(got[i][j] == want[i][j], tag) -- 断言校验
		end -- 终点
	end -- 终点
end -- 终点

check(fill_spiral(3), { { 1, 8, 7 }, { 2, 9, 6 }, { 3, 4, 5 } }, 3, "spiral3")
check(fill_spiral(4), { { 1, 12, 11, 10 }, { 2, 13, 16, 9 }, { 3, 14, 15, 8 }, { 4, 5, 6, 7 } }, 4, "spiral4")
print("PASS") -- 全部用例通过，输出 PASS
