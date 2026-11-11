-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107579658
-- LeetCode 107579658. 转换视角，提炼共性 — Lua 版（抽象思维之转换视角：统一分书问题与八皇后的回溯框架）
-- queen=false: 分书问题（5人，like 偏好矩阵）; queen=true: 八皇后
local function solve_unified(queen) -- local function solve_unified(queen)
	local SIZE = queen and 8 or 5 -- 把 queen and 8 or 5 写入 local SIZE
	local like = { -- 把 { 写入 local like
		{ 0, 0, 1, 1, 0 },
		{ 1, 1, 0, 0, 1 },
		{ 0, 1, 1, 0, 1 },
		{ 0, 0, 0, 1, 0 },
		{ 0, 1, 0, 0, 1 },
	}
	local Q = {} -- 把 {} 写入 local Q
	for i = 1, SIZE do
		Q[i] = -1
	end -- 让 下标 i 从 1 走到 SIZE（Lua 1 基）
	local rows = {} -- 把 {} 写入 local rows
	for i = 1, SIZE do
		rows[i] = true
	end -- 让 下标 i 从 1 走到 SIZE（Lua 1 基）
	local diag1, diag2 = {}, {} -- 把 {}, {} 写入 local diag1, diag2
	for i = 1, 2 * SIZE - 1 do -- 让 下标 i 从 1 走到 2（Lua 1 基）
		diag1[i] = true -- 把 true 写入 diag1[i]
		diag2[i] = true -- 把 true 写入 diag2[i]
	end -- 终点
	local results = {} -- 把 {} 写入 local results

	local function is_valid(row, col) -- local function is_valid(row, col)
		if queen then
			return true
		end -- 若 queen then return true 终点
		return like[row][col] == 1 -- 返回 like[row][col] 等于 1
	end -- 终点

	local function is_safe(row, col) -- local function is_safe(row, col)
		if queen then -- 若 queen then
			return rows[row] and diag1[col - row + SIZE - 1] and diag2[col + row - 1]
		end -- 终点
		return rows[row] -- 返回 行数[row]
	end -- 终点

	local function place(col) -- local function place(col)
		if col > SIZE then -- 若 col 超过 SIZE then
			local snap = {} -- 把 {} 写入 local snap
			for i = 1, SIZE do
				snap[i] = Q[i]
			end -- 让 下标 i 从 1 走到 SIZE（Lua 1 基）
			results[#results + 1] = snap -- 把 snap 写入 results[#results + 1]
			return -- return
		end -- 终点
		for row = 1, SIZE do -- 让 row 从 1 走到 SIZE（Lua 1 基）
			if is_valid(row, col) and is_safe(row, col) then -- 若 is_valid(row, col) and is_safe(row, col) then
				Q[col] = row - 1 -- 0 基行号
				rows[row] = false -- 把 false 写入 rows[row]
				local d1, d2 = col - (row - 1) + SIZE - 1, (col - 1) + (row - 1) + 1
				if queen then -- 若 queen then
					diag1[d1] = false -- 把 false 写入 diag1[d1]
					diag2[d2] = false -- 把 false 写入 diag2[d2]
				end -- 终点
				place(col + 1) -- place(col 加 1)
				rows[row] = true -- 把 true 写入 rows[row]
				if queen then -- 若 queen then
					diag1[d1] = true -- 把 true 写入 diag1[d1]
					diag2[d2] = true -- 把 true 写入 diag2[d2]
				end -- 终点
			end -- 终点
		end -- 终点
	end -- 终点

	place(1) -- place(1)
	return results -- 返回 results
end -- 终点

local want = { { 1, 2, 0, 3, 4 }, { 1, 4, 0, 3, 2 } } -- 把 {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}} 写入 local want
local got = solve_unified(false) -- 把 solve_unified(false) 写入 local got
assert(#got == #want, "results length mismatch") -- 断言校验
for i = 1, #want do -- 把 1, #want do 写入 for i
	for j = 1, 5 do -- 让 下标 j 从 1 走到 5（Lua 1 基）
		assert(got[i][j] == want[i][j], string.format("results[%d][%d] mismatch", i, j)) -- 断言校验
	end -- 终点
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
