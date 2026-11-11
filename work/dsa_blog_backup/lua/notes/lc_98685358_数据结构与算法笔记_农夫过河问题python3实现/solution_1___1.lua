-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/98685358
-- LeetCode 98685358. 农夫过河问题 — Lua 版（农夫过河问题：BFS 求最短过河序列，状态 (农夫,狼,羊,菜)，0=左岸 1=右岸）

local function is_safe(s) -- local function is_safe(字符串)
	if s[2] == s[3] and s[1] ~= s[2] then
		return false
	end
	if s[3] == s[4] and s[1] ~= s[3] then
		return false
	end
	return true -- 返回 true
end -- 终点

local function key(s) -- local function key(字符串)
	return table.concat(s, ",") -- 返回 table.concat(字符串, 「,」)
end -- 终点

local function solve() -- local function solve()
	local start = { 0, 0, 0, 0 } -- 把 {0, 0, 0, 0} 写入 local start
	local goal = { 1, 1, 1, 1 } -- 把 {1, 1, 1, 1} 写入 local goal
	local prev = {} -- key -> 父 key（起点无父，缺省 nil）
	local state_by = {} -- key -> 状态表
	prev[key(start)] = false -- 把 false 写入 prev[key(start)]
	state_by[key(start)] = start -- 把 起点 写入 state_by[key(start)]
	local q = { start } -- 把 {起点} 写入 local q
	local head = 1 -- 把 1 写入 local head
	while head <= #q do -- 把 #节点 do 写入 while head <
		local cur = q[head] -- 把 节点[头节点] 写入 local cur
		head = head + 1 -- 把 头节点 加 1 存入 头节点
		local ck = key(cur) -- 把 key(当前值) 写入 local ck
		if ck == key(goal) then -- 若 ck 等于 key(goal) then
			local path = {} -- 把 {} 写入 local path
			local k = ck -- 把 ck 写入 local k
			while k and k ~= false do -- 把 false do 写入 while k and k ~
				path[#path + 1] = state_by[k] -- 把 state_by[下标 k] 写入 path[#path + 1]
				k = prev[k] -- 把 前一个[下标 k] 存入 下标 k
			end -- 终点
			-- 反转
			local n = #path -- 把 #当前路径 写入 local n
			for i = 1, math.floor(n / 2) do -- 让 下标 i 从 1 走到 math（Lua 1 基）
				path[i], path[n - i + 1] = path[n - i + 1], path[i]
			end -- 终点
			return path -- 返回 当前路径
		end -- 终点
		local farmer = cur[1] -- 把 当前值[1] 写入 local farmer
		for i = 1, 4 do -- 让 下标 i 从 1 走到 4（Lua 1 基）
			if i == 1 or cur[i] == farmer then -- 若 下标 i 等于 1 or 当前值[下标 i] 等于 farmer then
				local nxt = { cur[1], cur[2], cur[3], cur[4] } -- 把 {当前值[1], 当前值[2], 当前值[3], 当前值[4]} 写入 local nxt
				nxt[1] = 1 - farmer -- 把 1 减 farmer 写入 nxt[1]
				if i ~= 1 then
					nxt[i] = 1 - farmer
				end -- 若 下标 i ~ 赋值为 1 then nxt[下标 i] 赋值为 1 减 farmer 终点
				local nk = key(nxt) -- 把 key(nxt) 写入 local nk
				if prev[nk] == nil then -- 若 前一个[nk] 等于 nil then
					if is_safe(nxt) then -- 若 is_safe(nxt) then
						prev[nk] = ck -- 把 ck 写入 prev[nk]
						state_by[nk] = nxt -- 把 nxt 写入 state_by[nk]
						q[#q + 1] = nxt -- 把 nxt 写入 q[#q + 1]
					end -- 终点
				end -- 终点
			end -- 终点
		end -- 终点
	end -- 终点
	return nil -- 返回 nil
end -- 终点

local want = { -- 把 { 写入 local want
	{ 0, 0, 0, 0 },
	{ 1, 0, 1, 0 },
	{ 0, 0, 1, 0 },
	{ 1, 1, 1, 0 },
	{ 0, 1, 0, 0 },
	{ 1, 1, 0, 1 },
	{ 0, 1, 0, 1 },
	{ 1, 1, 1, 1 },
}
local path = solve() -- 把 solve() 写入 local path
assert(path ~= nil, "FAILED: 无解") -- 断言校验
assert(#path == #want, "path length mismatch") -- 断言校验
for i = 1, #want do -- 把 1, #want do 写入 for i
	for j = 1, 4 do -- 让 下标 j 从 1 走到 4（Lua 1 基）
		assert(path[i][j] == want[i][j], "path mismatch at " .. i .. "," .. j) -- 断言校验
	end -- 终点
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
