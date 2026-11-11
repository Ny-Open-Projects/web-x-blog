-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案4：螺旋矩阵方向模拟 placeFill）
local function place_fill(n) -- local function place_fill(元素个数)
	local m = {} -- 把 {} 写入 local m
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		m[i] = {} -- 把 {} 写入 m[i]
		for j = 1, n do
			m[i][j] = 0
		end -- 让 下标 j 从 1 走到 元素个数（Lua 1 基）
	end -- 终点
	-- 内部 1 基，输出 0 基
	local row, col = 1, 1 -- 把 1, 1 写入 local row, col
	local direction = "D" -- 把 「D」 写入 local direction
	local num = 1 -- 把 1 写入 local num
	local total = n * n -- 把 元素个数 乘 元素个数 写入 local total
	while num <= total do -- 把 总和 do 写入 while num <
		m[row][col] = num -- 把 num 写入 m[row][col]
		num = num + 1 -- 把 num 加 1 存入 num
		if direction == "D" then -- 若 direction 等于 「D」 then
			if row + 1 <= n and m[row + 1][col] == 0 then
				row = row + 1
			else
				direction = "R"
				col = col + 1
			end -- 否则
		elseif direction == "R" then -- 把 赋值为 「R」 then 写入 elseif direction
			if col + 1 <= n and m[row][col + 1] == 0 then
				col = col + 1
			else
				direction = "U"
				row = row - 1
			end -- 否则
		elseif direction == "U" then -- 把 赋值为 「U」 then 写入 elseif direction
			if row - 1 >= 1 and m[row - 1][col] == 0 then
				row = row - 1
			else
				direction = "L"
				col = col - 1
			end -- 否则
		else -- 否则
			if col - 1 >= 1 and m[row][col - 1] == 0 then
				col = col - 1
			else
				direction = "D"
				row = row + 1
			end -- 否则
		end -- 终点
	end -- 终点
	-- 转 0 基输出
	local out = {} -- 把 {} 写入 local out
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		out[i] = {} -- 把 {} 写入 out[i]
		for j = 1, n do
			out[i][j] = m[i][j]
		end -- 让 下标 j 从 1 走到 元素个数（Lua 1 基）
	end -- 终点
	return out -- 返回 out
end -- 终点

local got3 = place_fill(3) -- 把 place_fill(3) 写入 local got3
local want3 = { { 1, 8, 7 }, { 2, 9, 6 }, { 3, 4, 5 } } -- 把 {{1, 8, 7}, {2, 9, 6}, {3, 4, 5}} 写入 local want3
for i = 1, 3 do
	for j = 1, 3 do
		assert(got3[i][j] == want3[i][j], "place3")
	end
end -- 让 下标 i 从 1 走到 3（Lua 1 基）
local got4 = place_fill(4) -- 把 place_fill(4) 写入 local got4
local want4 = { { 1, 12, 11, 10 }, { 2, 13, 16, 9 }, { 3, 14, 15, 8 }, { 4, 5, 6, 7 } }
for i = 1, 4 do
	for j = 1, 4 do
		assert(got4[i][j] == want4[i][j], "place4")
	end
end -- 让 下标 i 从 1 走到 4（Lua 1 基）
print("PASS") -- 全部用例通过，输出 PASS
