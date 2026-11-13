-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
-- LeetCode 107524703. 人鬼渡河问题 — Lua 版（方案4：方向入状态的 DFS 变体，断言无可行路径）
local D = { { 2, 0 }, { 1, 0 }, { 1, 1 }, { 0, 1 }, { 0, 2 } } -- 把 {{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}} 写入 local D

local function safe(r, g) -- local function safe(右指针, g)
	return 0 <= r and r <= 3 and 0 <= g and g <= 3 and (r == 0 or r == 3 or r == g)
end -- 终点

local function solve() -- local function solve()
	local path = {} -- 把 {} 写入 local path
	local visited = {} -- 把 {} 写入 local visited

	local jump -- local jump
	jump = function(dir, r, g, step) -- 把 function(dir, 右指针, g, 步数) 存入 jump
		if r == 0 and g == 0 and step % 2 == 0 then
			return true
		end -- 若 右指针 等于 0 and g 等于 0 and 步数 对…取模 2 等于 0 then return true 终点
		local key = r .. "," .. g .. "," .. (step % 2) -- 把 右指针 .. 「,」 .. g .. 「,」 .. (步数 对…取模 2) 写入 local key
		if visited[key] then
			return false
		end -- 若 已访问集合[key] then return false 终点
		visited[key] = true -- 把 true 写入 visited[key]
		for _, d in ipairs(D) do -- 遍历取 d
			local dr, dg = d[1], d[2] -- 把 d[1], d[2] 写入 local dr, dg
			local nr = r + dir * dr -- 把 右指针 加 dir 乘 dr 写入 local nr
			local ng = g + dir * dg -- 把 g 加 dir 乘 dg 写入 local ng
			if safe(nr, ng) and jump(-dir, nr, ng, step + 1) then -- 若 safe(nr, ng) and jump( 减 dir, nr, ng, 步数 加 1) then
				path[#path + 1] = { dr, dg } -- 把 {dr, dg} 写入 path[#path + 1]
				return true -- 返回 true
			end -- 终点
		end -- 终点
		return false -- 返回 false
	end -- 终点

	jump(-1, 3, 3, 0) -- jump( 减 1, 3, 3, 0)
	local n = #path -- 把 #当前路径 写入 local n
	for i = 1, math.floor(n / 2) do -- 让 下标 i 从 1 走到 math（Lua 1 基）
		path[i], path[n - i + 1] = path[n - i + 1], path[i]
	end -- 终点
	return path -- 返回 当前路径
end -- 终点

-- 与 TS 原文件一致：该变体断言返回空路径（parity 约束下无解）
local got = solve() -- 把 solve() 写入 local got
assert(#got == 0, "solve 应返回空路径") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
