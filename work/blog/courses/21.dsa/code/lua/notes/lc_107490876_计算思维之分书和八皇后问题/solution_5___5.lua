-- 来源：https://blog.csdn.net/tyro_java/article/details/107490876
-- LeetCode 107490876. 分书和八皇后问题 — Lua 版（方案5：八皇后布尔数组标记，行号 0..n-1）
local function n_queens_bool(n) -- local function n_queens_bool(元素个数)
	local SIZE = n -- 把 元素个数 写入 local SIZE
	local col_row = {} -- 把 {} 写入 local col_row
	local rows, diag1, diag2 = {}, {}, {} -- 把 {}, {}, {} 写入 local rows, diag1, diag2
	local OFFSET = SIZE - 1 -- 把 SIZE 减 1 写入 local OFFSET
	for i = 0, SIZE - 1 do
		col_row[i] = 0
	end -- 让 下标 i 从 0 走到 SIZE（Lua 1 基）
	for i = 0, SIZE - 1 do
		rows[i] = true
	end -- 让 下标 i 从 0 走到 SIZE（Lua 1 基）
	for i = 0, 2 * SIZE - 2 do -- 让 下标 i 从 0 走到 2（Lua 1 基）
		diag1[i] = true -- 把 true 写入 diag1[i]
		diag2[i] = true -- 把 true 写入 diag2[i]
	end -- 终点
	local results = {} -- 把 {} 写入 local results

	local function place(col) -- local function place(col)
		if col == SIZE then -- 若 col 等于 SIZE then
			local snap = {} -- 把 {} 写入 local snap
			for i = 0, SIZE - 1 do
				snap[i + 1] = col_row[i]
			end -- 让 下标 i 从 0 走到 SIZE（Lua 1 基）
			results[#results + 1] = snap -- 把 snap 写入 results[#results + 1]
			return -- return
		end -- 终点
		for row = 0, SIZE - 1 do -- 让 row 从 0 走到 SIZE（Lua 1 基）
			local d1 = col - row + OFFSET -- 把 col 减 row 加 OFFSET 写入 local d1
			local d2 = col + row -- 把 col 加 row 写入 local d2
			if rows[row] and diag1[d1] and diag2[d2] then -- 若 行数[row] and diag1[d1] and diag2[d2] then
				col_row[col] = row -- 把 row 写入 col_row[col]
				rows[row] = false -- 把 false 写入 rows[row]
				diag1[d1] = false -- 把 false 写入 diag1[d1]
				diag2[d2] = false -- 把 false 写入 diag2[d2]
				place(col + 1) -- place(col 加 1)
				rows[row] = true -- 把 true 写入 rows[row]
				diag1[d1] = true -- 把 true 写入 diag1[d1]
				diag2[d2] = true -- 把 true 写入 diag2[d2]
			end -- 终点
		end -- 终点
	end -- 终点

	place(0) -- place(0)
	return results -- 返回 results
end -- 终点

local cases = { -- 把 { 写入 local cases
	{ 8, 92, { 0, 4, 7, 5, 2, 6, 1, 3 } },
	{ 1, 1, { 0 } },
	{ 2, 0, nil },
	{ 4, 2, { 1, 3, 0, 2 } },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	local sols = n_queens_bool(c[1]) -- 把 n_queens_bool(字符[1]) 写入 local sols
	assert(#sols == c[2], "case " .. idx .. " count mismatch: " .. #sols) -- 断言校验
	if c[3] then -- 若 字符[3] then
		for j = 1, #c[3] do -- 把 1, #字符[3] do 写入 for j
			assert(sols[1][j] == c[3][j], "case " .. idx .. " first mismatch") -- 断言校验
		end -- 终点
	end -- 终点
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
