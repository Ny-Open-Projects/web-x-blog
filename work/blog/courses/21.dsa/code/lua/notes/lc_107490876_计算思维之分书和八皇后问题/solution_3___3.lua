-- 来源：https://blog.csdn.net/tyro_java/article/details/107490876
-- LeetCode 107490876. 分书和八皇后问题 — Lua 版（方案3：八皇后递归 isSafe，行号 1..n）
local function n_queens_safe(n) -- local function n_queens_safe(元素个数)
	local results = {} -- 把 {} 写入 local results
	local board = {} -- 把 {} 写入 local board
	for i = 1, n do
		board[i] = 0
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）

	local function is_safe(col, row) -- local function is_safe(col, row)
		for c = 1, col - 1 do -- 让 字符 从 1 走到 col（Lua 1 基）
			if board[c] == row or math.abs(board[c] - row) == math.abs(c - col) then
				return false -- 返回 false
			end -- 终点
		end -- 终点
		return true -- 返回 true
	end -- 终点

	local function place(col) -- local function place(col)
		if col > n then -- 若 col 超过 元素个数 then
			local snap = {} -- 把 {} 写入 local snap
			for i = 1, n do
				snap[i] = board[i]
			end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
			results[#results + 1] = snap -- 把 snap 写入 results[#results + 1]
			return -- return
		end -- 终点
		for row = 1, n do -- 让 row 从 1 走到 元素个数（Lua 1 基）
			if is_safe(col, row) then -- 若 is_safe(col, row) then
				board[col] = row -- 把 row 写入 board[col]
				place(col + 1) -- place(col 加 1)
			end -- 终点
		end -- 终点
	end -- 终点

	place(1) -- place(1)
	return results -- 返回 results
end -- 终点

local cases = { -- 把 { 写入 local cases
	{ 8, 92, { 1, 5, 8, 6, 3, 7, 2, 4 } },
	{ 1, 1, { 1 } },
	{ 2, 0, nil },
	{ 4, 2, { 2, 4, 1, 3 } },
}
for idx, c in ipairs(cases) do -- 遍历取 字符
	local sols = n_queens_safe(c[1]) -- 把 n_queens_safe(字符[1]) 写入 local sols
	assert(#sols == c[2], "case " .. idx .. " count mismatch: " .. #sols) -- 断言校验
	if c[3] then -- 若 字符[3] then
		for j = 1, #c[3] do -- 把 1, #字符[3] do 写入 for j
			assert(sols[1][j] == c[3][j], "case " .. idx .. " first mismatch") -- 断言校验
		end -- 终点
	end -- 终点
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
