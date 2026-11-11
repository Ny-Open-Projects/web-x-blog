-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134204437
-- LeetCode 79. 单词搜索 — Lua 版（方案1）
local function exist(board, word) -- local function exist(棋盘, 单词)
	local rows, cols = #board, #board[1] -- 把 #棋盘, #棋盘[1] 写入 local rows, cols
	local w = {} -- 把 {} 写入 local w
	word:gsub(".", function(c)
		w[#w + 1] = c
	end) -- 把 字符 终点) 写入 word:gsub(".", function(c) w[#w + 1]
	local function dfs(i, j, k) -- local function dfs(下标 i, 下标 j, 下标 k)
		if k > #w then
			return true
		end -- 若 下标 k 超过 #权重 then return true 终点
		if i < 1 or i > rows or j < 1 or j > cols then
			return false
		end
		if board[i][j] ~= w[k] then
			return false
		end -- 若 棋盘[下标 i][下标 j] ~ 赋值为 权重[下标 k] then return false 终点
		local saved = board[i][j] -- 把 棋盘[下标 i][下标 j] 写入 local saved
		board[i][j] = "#" -- 把 「#」 写入 board[i][j]
		local found = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
		board[i][j] = saved -- 把 saved 写入 board[i][j]
		return found -- 返回 found
	end -- 终点
	for i = 1, rows do -- 让 下标 i 从 1 走到 行数（Lua 1 基）
		for j = 1, cols do -- 让 下标 j 从 1 走到 列数（Lua 1 基）
			if dfs(i, j, 1) then
				return true
			end -- 若 dfs(下标 i, 下标 j, 1) then return true 终点
		end -- 终点
	end -- 终点
	return false -- 返回 false
end -- 终点
local b = { { "A", "B", "C", "E" }, { "S", "F", "C", "S" }, { "A", "D", "E", "E" } }
assert(exist(b, "ABCCED") == true) -- 断言校验
assert(exist(b, "SEE") == true) -- 断言校验
assert(exist(b, "ABCB") == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
