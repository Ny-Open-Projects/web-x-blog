-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134045157
-- LeetCode 37. 解数独 — Lua 版（方案2）
local function solve_sudoku(board) -- local function solve_sudoku(棋盘)
	local function valid(r, c, ch) -- local function valid(右指针, 字符, 字符)
		for i = 1, 9 do -- 让 下标 i 从 1 走到 9（Lua 1 基）
			if board[r][i] == ch or board[i][c] == ch then
				return false
			end
		end -- 终点
		local br, bc = math.floor((r - 1) / 3) * 3 + 1, math.floor((c - 1) / 3) * 3 + 1
		for i = br, br + 2 do -- 把 br, br 加 2 do 写入 for i
			for j = bc, bc + 2 do -- 把 bc, bc 加 2 do 写入 for j
				if board[i][j] == ch then
					return false
				end -- 若 棋盘[下标 i][下标 j] 等于 字符 then return false 终点
			end -- 终点
		end -- 终点
		return true -- 返回 true
	end -- 终点
	local function dfs() -- local function dfs()
		for r = 1, 9 do -- 让 右指针 从 1 走到 9（Lua 1 基）
			for c = 1, 9 do -- 让 字符 从 1 走到 9（Lua 1 基）
				if board[r][c] == "." then -- 若 棋盘[右指针][字符] 等于 「.」 then
					for n = 1, 9 do -- 让 元素个数 从 1 走到 9（Lua 1 基）
						local ch = tostring(n) -- 把 tostring(元素个数) 写入 local ch
						if valid(r, c, ch) then -- 若 valid(右指针, 字符, 字符) then
							board[r][c] = ch -- 把 字符 写入 board[r][c]
							if dfs() then
								return true
							end -- 若 dfs() then return true 终点
							board[r][c] = "." -- 把 「.」 写入 board[r][c]
						end -- 终点
					end -- 终点
					return false -- 返回 false
				end -- 终点
			end -- 终点
		end -- 终点
		return true -- 返回 true
	end -- 终点
	dfs() -- dfs()
end -- 终点
local board = { -- 把 { 写入 local board
	{ "5", "3", ".", ".", "7", ".", ".", ".", "." },
	{ "6", ".", ".", "1", "9", "5", ".", ".", "." },
	{ ".", "9", "8", ".", ".", ".", ".", "6", "." },
	{ "8", ".", ".", ".", "6", ".", ".", ".", "3" },
	{ "4", ".", ".", "8", ".", "3", ".", ".", "1" },
	{ "7", ".", ".", ".", "2", ".", ".", ".", "6" },
	{ ".", "6", ".", ".", ".", ".", "2", "8", "." },
	{ ".", ".", ".", "4", "1", "9", ".", ".", "5" },
	{ ".", ".", ".", ".", "8", ".", ".", "7", "9" },
}
solve_sudoku(board) -- solve_sudoku(棋盘)
local solved = { -- 把 { 写入 local solved
	"534678912",
	"672195348",
	"198342567",
	"859761423",
	"426853791",
	"713924856",
	"961537284",
	"287419635",
	"345286179",
}
for r = 1, 9 do -- 让 右指针 从 1 走到 9（Lua 1 基）
	assert(table.concat(board[r]) == solved[r], "row " .. r) -- 打印输出
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
