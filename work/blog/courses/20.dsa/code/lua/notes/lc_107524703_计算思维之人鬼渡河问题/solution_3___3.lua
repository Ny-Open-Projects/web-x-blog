-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
-- LeetCode 107524703. 人鬼渡河问题 — Lua 版（方案3：DFS+奇偶步求解）
local D = { { 2, 0 }, { 1, 0 }, { 1, 1 }, { 0, 1 }, { 0, 2 } } -- 把 {{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}} 写入 local D

local function safe(r, g) -- local function safe(右指针, g)
	return 0 <= r and r <= 3 and 0 <= g and g <= 3 and (r == 0 or r == 3 or r == g)
end -- 终点

local function solve() -- local function solve()
	local path = {} -- 把 {} 写入 local path
	local visited = {} -- 把 {} 写入 local visited

	local dfs -- local dfs
	dfs = function(r, g, step) -- 把 function(右指针, g, 步数) 存入 dfs
		if r == 0 and g == 0 then
			return true
		end -- 若 右指针 等于 0 and g 等于 0 then return true 终点
		local key = r .. "," .. g .. "," .. (step % 2) -- 把 右指针 .. 「,」 .. g .. 「,」 .. (步数 对…取模 2) 写入 local key
		if visited[key] then
			return false
		end -- 若 已访问集合[key] then return false 终点
		visited[key] = true -- 把 true 写入 visited[key]
		local odd = (step % 2 == 1) -- 把 (步数 对…取模 2 等于 1) 写入 local odd
		for _, d in ipairs(D) do -- 遍历取 d
			local dr, dg = d[1], d[2] -- 把 d[1], d[2] 写入 local dr, dg
			local nr, ng -- local nr, ng
			if odd then -- 若 odd then
				if r < dr or g < dg then -- 若 右指针 小于 dr or g 小于 dg then
					-- 跳过
					goto continue_move -- goto continue_move
				end -- 终点
				nr = r - dr -- 把 右指针 减 dr 存入 nr
				ng = g - dg -- 把 g 减 dg 存入 ng
			else -- 否则
				if (3 - r) < dr or (3 - g) < dg then -- 若 3 减 右指针) 小于 dr or (3 减 g) 小于 dg then
					goto continue_move -- goto continue_move
				end -- 终点
				nr = r + dr -- 把 右指针 加 dr 存入 nr
				ng = g + dg -- 把 g 加 dg 存入 ng
			end -- 终点
			if safe(nr, ng) and dfs(nr, ng, step + 1) then -- 若 safe(nr, ng) and dfs(nr, ng, 步数 加 1) then
				path[#path + 1] = { dr, dg } -- 把 {dr, dg} 写入 path[#path + 1]
				return true -- 返回 true
			end -- 终点
			::continue_move:: -- ::continue_move::
		end -- 终点
		return false -- 返回 false
	end -- 终点

	dfs(3, 3, 1) -- dfs(3, 3, 1)
	-- 反转
	local n = #path -- 把 #当前路径 写入 local n
	for i = 1, math.floor(n / 2) do -- 让 下标 i 从 1 走到 math（Lua 1 基）
		path[i], path[n - i + 1] = path[n - i + 1], path[i]
	end -- 终点
	return path -- 返回 当前路径
end -- 终点

local want = { -- 把 { 写入 local want
	{ 1, 1 },
	{ 1, 0 },
	{ 0, 2 },
	{ 0, 1 },
	{ 2, 0 },
	{ 1, 1 },
	{ 2, 0 },
	{ 0, 1 },
	{ 0, 2 },
	{ 1, 0 },
	{ 1, 1 },
}
local got = solve() -- 把 solve() 写入 local got
assert(#got == #want, "solve length mismatch") -- 断言校验
for i = 1, #want do -- 把 1, #want do 写入 for i
	assert(got[i][1] == want[i][1] and got[i][2] == want[i][2], "solve at " .. i .. " mismatch") -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
