-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/112548608
-- LeetCode 112548608. 计算思维之经典农夫过河问题C++实现（DFS 求任一可行过河序列）

local function invalid(st) -- local function invalid(st)
	local h, w, s, v = st[1], st[2], st[3], st[4] -- 把 st[1], st[2], st[3], st[4] 写入 local h, w, s, v
	if h ~= s and s == w then
		return true
	end -- 若 h ~ 赋值为 字符串 and 字符串 等于 权重 then return true 终点
	if h ~= s and s == v then
		return true
	end -- 若 h ~ 赋值为 字符串 and 字符串 等于 值 then return true 终点
	return false -- 返回 false
end -- 终点

local role_idx = { ["-"] = 0, ["W"] = 1, ["S"] = 2, ["V"] = 3 }

local function solve_farmer() -- local function solve_farmer()
	local path = {} -- 把 {} 写入 local path
	local visited = {} -- 把 {} 写入 local visited

	local go -- local go
	go = function(st) -- 把 function(st) 存入 go
		if st[1] == 1 and st[2] == 1 and st[3] == 1 and st[4] == 1 then
			return true -- 返回 true
		end -- 终点
		local key = table.concat(st, ",") -- 打印输出
		if visited[key] then
			return false
		end -- 若 已访问集合[key] then return false 终点
		visited[key] = true -- 把 true 写入 visited[key]
		for _, role in ipairs({ "-", "W", "S", "V" }) do -- 遍历取 role
			local ns = { st[1], st[2], st[3], st[4] } -- 把 { st[1], st[2], st[3], st[4] } 写入 local ns
			ns[1] = 1 - ns[1] -- 农夫总是过河
			if role ~= "-" then -- 若 role ~ 赋值为 「 减 」 then
				local idx = role_idx[role] + 1 -- 把 role_idx[role] 加 1 写入 local idx
				-- 农夫必须与所带物品在出发前同岸
				if st[1] ~= st[idx] then -- 若 st[1] ~ 赋值为 st[idx] then
					-- continue 语义：不递归
					goto continue_role -- goto continue_role
				end -- 终点
				ns[idx] = 1 - ns[idx] -- 把 1 减 ns[idx] 写入 ns[idx]
			end -- 终点
			if not invalid(ns) then -- 若 not invalid(ns) then
				if go(ns) then -- 若 go(ns) then
					path[#path + 1] = role -- 把 role 写入 path[#path + 1]
					return true -- 返回 true
				end -- 终点
			end -- 终点
			::continue_role:: -- ::continue_role::
		end -- 终点
		return false -- 返回 false
	end -- 终点

	go({ 0, 0, 0, 0 }) -- go({0, 0, 0, 0})
	-- 反转
	local n = #path -- 把 #当前路径 写入 local n
	for i = 1, math.floor(n / 2) do -- 让 下标 i 从 1 走到 math（Lua 1 基）
		path[i], path[n - i + 1] = path[n - i + 1], path[i]
	end -- 终点
	return path -- 返回 当前路径
end -- 终点

-- 模拟走 path，校验每步合法且终点为 (1,1,1,1)
local function simulate(path) -- local function simulate(当前路径)
	local st = { 0, 0, 0, 0 } -- 把 {0, 0, 0, 0} 写入 local st
	for _, role in ipairs(path) do -- 遍历取 role
		local before = { st[1], st[2], st[3], st[4] } -- 把 { st[1], st[2], st[3], st[4] } 写入 local before
		st[1] = 1 - st[1] -- 把 1 减 st[1] 写入 st[1]
		if role ~= "-" then -- 若 role ~ 赋值为 「 减 」 then
			local idx = role_idx[role] + 1 -- 把 role_idx[role] 加 1 写入 local idx
			if before[1] ~= before[idx] then
				return false
			end -- 若 before[1] ~ 赋值为 before[idx] then return false 终点
			st[idx] = 1 - st[idx] -- 把 1 减 st[idx] 写入 st[idx]
		end -- 终点
		if invalid(st) then
			return false
		end -- 若 invalid(st) then return false 终点
	end -- 终点
	return st[1] == 1 and st[2] == 1 and st[3] == 1 and st[4] == 1 -- 返回 st[1] 等于 1 and st[2] 等于 1 and st[3] 等于 1 and st[4] 等于 1
end -- 终点

local wantPath = { "S", "-", "W", "S", "V", "-", "S" } -- 把 {「S」, 「S」, 「S」, 「S」, 「S」, 「S」, 「S」} 写入 local wantPath
local wantReadable = "HS H HW HS HV H HS" -- 把 「HS H HW HS HV H HS」 写入 local wantReadable

local gotPath = solve_farmer() -- 把 solve_farmer() 写入 local gotPath

-- case1: 完整路径一致
assert(#gotPath == #wantPath, "path length mismatch") -- 断言校验
for i = 1, #wantPath do -- 把 1, #wantPath do 写入 for i
	assert(gotPath[i] == wantPath[i], "path[" .. i .. "] mismatch: got " .. tostring(gotPath[i])) -- 断言校验
end -- 终点

-- case2: 可读方案串一致
local parts = {} -- 把 {} 写入 local parts
for i, r in ipairs(gotPath) do -- 遍历取 右指针
	if r ~= "-" then
		parts[i] = "H" .. r
	else
		parts[i] = "H"
	end
end -- 终点
local gotReadable = table.concat(parts, " ") -- 打印输出
assert(gotReadable == wantReadable, "readable mismatch: got " .. gotReadable) -- 断言校验

-- case3: 路径 7 步
assert(#gotPath == 7, "steps mismatch") -- 断言校验

-- case4: 模拟校验
assert(simulate(gotPath), "simulate failed") -- 断言校验

print("PASS") -- 全部用例通过，输出 PASS
