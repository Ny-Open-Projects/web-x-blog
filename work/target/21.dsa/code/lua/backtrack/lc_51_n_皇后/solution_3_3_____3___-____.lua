-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133970744
-- LeetCode 51. N皇后 — Lua 版（方案3）
local function solve_n_queens(n) -- local function solve_n_queens(元素个数)
	local res = {} -- 把 {} 写入 local res
	local cols = {} -- 把 {} 写入 local cols
	local function ok(row, col) -- local function ok(row, col)
		for r = 1, row - 1 do -- 让 右指针 从 1 走到 row（Lua 1 基）
			if cols[r] == col or math.abs(r - row) == math.abs(cols[r] - col) then
				return false
			end
		end -- 终点
		return true -- 返回 true
	end -- 终点
	local function dfs(row) -- local function dfs(row)
		if row > n then -- 若 row 超过 元素个数 then
			local board = {} -- 把 {} 写入 local board
			for r = 1, n do -- 让 右指针 从 1 走到 元素个数（Lua 1 基）
				local line = {} -- 把 {} 写入 local line
				for c = 1, n do -- 让 字符 从 1 走到 元素个数（Lua 1 基）
					if cols[r] == c then
						line[#line + 1] = "Q"
					else
						line[#line + 1] = "."
					end
				end -- 终点
				board[#board + 1] = table.concat(line) -- 打印输出
			end -- 终点
			res[#res + 1] = board -- 把 棋盘 写入 res[#res + 1]
			return -- return
		end -- 终点
		for col = 1, n do -- 让 col 从 1 走到 元素个数（Lua 1 基）
			if ok(row, col) then -- 若 ok(row, col) then
				cols[row] = col -- 把 col 写入 cols[row]
				dfs(row + 1) -- dfs(row 加 1)
				cols[row] = nil -- 把 nil 写入 cols[row]
			end -- 终点
		end -- 终点
	end -- 终点
	dfs(1) -- dfs(1)
	return res -- 返回 结果
end -- 终点
local got = solve_n_queens(4) -- 把 solve_n_queens(4) 写入 local got
assert(#got == 2) -- 断言校验
assert(got[1][1] == ".Q.." and got[1][4] == "..Q.") -- 断言校验
assert(got[2][1] == "..Q." and got[2][4] == ".Q..") -- 断言校验
assert(#solve_n_queens(1) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
