-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133982215
-- LeetCode 417. 太平洋大西洋水流问题 — Lua 版

-- 方案1（DFS 反向流动，从海洋边界出发）
local function pacific_atlantic(matrix) -- local function pacific_atlantic(矩阵)
	if not matrix or #matrix == 0 or #matrix[1] == 0 then
		return {}
	end -- 若 not 矩阵 or #矩阵 等于 0 or #矩阵[1] 等于 0 then return {} 终点
	local m, n = #matrix, #matrix[1] -- 把 #矩阵, #矩阵[1] 写入 local m, n
	local pacific, atlantic = {}, {} -- 把 {}, {} 写入 local pacific, atlantic
	for r = 1, m do -- 让 右指针 从 1 走到 映射表（Lua 1 基）
		pacific[r] = {} -- 把 {} 写入 pacific[r]
		atlantic[r] = {} -- 把 {} 写入 atlantic[r]
		for c = 1, n do -- 让 字符 从 1 走到 元素个数（Lua 1 基）
			pacific[r][c] = false -- 把 false 写入 pacific[r][c]
			atlantic[r][c] = false -- 把 false 写入 atlantic[r][c]
		end -- 终点
	end -- 终点

	local dirs = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } }
	local function dfs(r, c, flow) -- local function dfs(右指针, 字符, flow)
		flow[r][c] = true -- 把 true 写入 flow[r][c]
		for _, d in ipairs(dirs) do -- 遍历取 d
			local nr, nc = r + d[1], c + d[2] -- 把 右指针 加 d[1], 字符 加 d[2] 写入 local nr, nc
			if
				nr >= 1
				and nr <= m
				and nc >= 1
				and nc <= n -- 若 nr 不低于 1 and nr 不超过 映射表 and nc 不低于 1 and nc 不超过 元素个数
				and not flow[nr][nc] -- and not flow[nr][nc]
				and matrix[nr][nc] >= matrix[r][c]
			then -- 把 矩阵[右指针][字符] then 写入 and matrix[nr][nc] >
				dfs(nr, nc, flow) -- dfs(nr, nc, flow)
			end -- 终点
		end -- 终点
	end -- 终点

	for r = 1, m do -- 让 右指针 从 1 走到 映射表（Lua 1 基）
		dfs(r, 1, pacific) -- dfs(右指针, 1, pacific)
		dfs(r, n, atlantic) -- dfs(右指针, 元素个数, atlantic)
	end -- 终点
	for c = 1, n do -- 让 字符 从 1 走到 元素个数（Lua 1 基）
		dfs(1, c, pacific) -- dfs(1, 字符, pacific)
		dfs(m, c, atlantic) -- dfs(映射表, 字符, atlantic)
	end -- 终点

	local res = {} -- 把 {} 写入 local res
	for r = 1, m do -- 让 右指针 从 1 走到 映射表（Lua 1 基）
		for c = 1, n do -- 让 字符 从 1 走到 元素个数（Lua 1 基）
			if pacific[r][c] and atlantic[r][c] then -- 若 pacific[右指针][字符] and atlantic[右指针][字符] then
				res[#res + 1] = { r - 1, c - 1 } -- 转回 0 基坐标
			end -- 终点
		end -- 终点
	end -- 终点
	return res -- 返回 结果
end -- 终点

-- 空输入：null 矩阵应返回 []
local got = pacific_atlantic(nil) -- 把 pacific_atlantic(nil) 写入 local got
assert(#got == 0, "null matrix should yield []") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
