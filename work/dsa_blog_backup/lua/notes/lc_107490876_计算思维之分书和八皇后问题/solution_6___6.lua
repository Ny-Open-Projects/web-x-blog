-- 来源：https://blog.csdn.net/tyro_java/article/details/107490876
-- LeetCode 107490876. 分书和八皇后问题 — Lua 版（方案6：八皇后不可变状态函数式）
local function n_queens_func(n) -- local function n_queens_func(元素个数)
	local SIZE = n -- 把 元素个数 写入 local SIZE
	local results = {} -- 把 {} 写入 local results

	local function place(col, col_row, rows, diag1, diag2) -- local function place(col, col_row, 行数, diag1, diag2)
		if col == SIZE then -- 若 col 等于 SIZE then
			local snap = {} -- 把 {} 写入 local snap
			for i = 1, #col_row do
				snap[i] = col_row[i]
			end -- 把 1, #col_row do snap[下标 i] 赋值为 col_row[下标 i] 终点 写入 for i
			results[#results + 1] = snap -- 把 snap 写入 results[#results + 1]
			return -- return
		end -- 终点
		for row = 0, SIZE - 1 do -- 让 row 从 0 走到 SIZE（Lua 1 基）
			local d1 = col - row + (SIZE - 1) -- 把 col 减 row 加 (SIZE 减 1) 写入 local d1
			local d2 = col + row -- 把 col 加 row 写入 local d2
			if rows[row] and diag1[d1] and diag2[d2] then -- 若 行数[row] and diag1[d1] and diag2[d2] then
				local nr = {} -- 把 {} 写入 local nr
				for k, v in pairs(rows) do
					nr[k] = v
				end -- 遍历取 值
				nr[row] = false -- 把 false 写入 nr[row]
				local nd1 = {} -- 把 {} 写入 local nd1
				for k, v in pairs(diag1) do
					nd1[k] = v
				end -- 遍历取 值
				nd1[d1] = false -- 把 false 写入 nd1[d1]
				local nd2 = {} -- 把 {} 写入 local nd2
				for k, v in pairs(diag2) do
					nd2[k] = v
				end -- 遍历取 值
				nd2[d2] = false -- 把 false 写入 nd2[d2]
				local ncol = {} -- 把 {} 写入 local ncol
				for i = 1, #col_row do
					ncol[i] = col_row[i]
				end -- 把 1, #col_row do ncol[下标 i] 赋值为 col_row[下标 i] 终点 写入 for i
				ncol[#ncol + 1] = row -- 把 row 写入 ncol[#ncol + 1]
				place(col + 1, ncol, nr, nd1, nd2) -- place(col 加 1, ncol, nr, nd1, nd2)
			end -- 终点
		end -- 终点
	end -- 终点

	local rows0, diag0 = {}, {} -- 把 {}, {} 写入 local rows0, diag0
	for i = 0, SIZE - 1 do
		rows0[i] = true
	end -- 让 下标 i 从 0 走到 SIZE（Lua 1 基）
	for i = 0, 2 * SIZE - 2 do
		diag0[i] = true
	end -- 让 下标 i 从 0 走到 2（Lua 1 基）
	place(0, {}, rows0, diag0, {}) -- place(0, {}, rows0, diag0, {})
	-- diag2 与 diag1 同构，占位用同一初始表
	return results -- 返回 results
end -- 终点

-- 修正：diag2 需独立初始表
local function n_queens_func_fixed(n) -- local function n_queens_func_fixed(元素个数)
	local SIZE = n -- 把 元素个数 写入 local SIZE
	local results = {} -- 把 {} 写入 local results

	local function place(col, col_row, rows, diag1, diag2) -- local function place(col, col_row, 行数, diag1, diag2)
		if col == SIZE then -- 若 col 等于 SIZE then
			local snap = {} -- 把 {} 写入 local snap
			for i = 1, #col_row do
				snap[i] = col_row[i]
			end -- 把 1, #col_row do snap[下标 i] 赋值为 col_row[下标 i] 终点 写入 for i
			results[#results + 1] = snap -- 把 snap 写入 results[#results + 1]
			return -- return
		end -- 终点
		for row = 0, SIZE - 1 do -- 让 row 从 0 走到 SIZE（Lua 1 基）
			local d1 = col - row + (SIZE - 1) -- 把 col 减 row 加 (SIZE 减 1) 写入 local d1
			local d2 = col + row -- 把 col 加 row 写入 local d2
			if rows[row] and diag1[d1] and diag2[d2] then -- 若 行数[row] and diag1[d1] and diag2[d2] then
				local function copy(t) -- local function copy(另一字符串)
					local c = {} -- 把 {} 写入 local c
					for k, v in pairs(t) do
						c[k] = v
					end -- 遍历取 值
					return c -- 返回 字符
				end -- 终点
				local nr = copy(rows)
				nr[row] = false -- 把 copy(行数); nr[row] 赋值为 false 写入 local nr
				local nd1 = copy(diag1)
				nd1[d1] = false -- 把 copy(diag1); nd1[d1] 赋值为 false 写入 local nd1
				local nd2 = copy(diag2)
				nd2[d2] = false -- 把 copy(diag2); nd2[d2] 赋值为 false 写入 local nd2
				local ncol = {} -- 把 {} 写入 local ncol
				for i = 1, #col_row do
					ncol[i] = col_row[i]
				end -- 把 1, #col_row do ncol[下标 i] 赋值为 col_row[下标 i] 终点 写入 for i
				ncol[#ncol + 1] = row -- 把 row 写入 ncol[#ncol + 1]
				place(col + 1, ncol, nr, nd1, nd2) -- place(col 加 1, ncol, nr, nd1, nd2)
			end -- 终点
		end -- 终点
	end -- 终点

	local rows0, diag10, diag20 = {}, {}, {} -- 把 {}, {}, {} 写入 local rows0, diag10, diag20
	for i = 0, SIZE - 1 do
		rows0[i] = true
	end -- 让 下标 i 从 0 走到 SIZE（Lua 1 基）
	for i = 0, 2 * SIZE - 2 do -- 让 下标 i 从 0 走到 2（Lua 1 基）
		diag10[i] = true -- 把 true 写入 diag10[i]
		diag20[i] = true -- 把 true 写入 diag20[i]
	end -- 终点
	place(0, {}, rows0, diag10, diag20) -- place(0, {}, rows0, diag10, diag20)
	return results -- 返回 results
end -- 终点

local cases = { -- 把 { 写入 local cases
	{ 8, 92, { 0, 4, 7, 5, 2, 6, 1, 3 } },
	{ 1, 1, { 0 } },
	{ 2, 0, nil },
	{ 4, 2, { 1, 3, 0, 2 } },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	local sols = n_queens_func_fixed(c[1]) -- 把 n_queens_func_fixed(字符[1]) 写入 local sols
	assert(#sols == c[2], "case " .. idx .. " count mismatch: " .. #sols) -- 断言校验
	if c[3] then -- 若 字符[3] then
		for j = 1, #c[3] do -- 把 1, #字符[3] do 写入 for j
			assert(sols[1][j] == c[3][j], "case " .. idx .. " first mismatch") -- 断言校验
		end -- 终点
	end -- 终点
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
