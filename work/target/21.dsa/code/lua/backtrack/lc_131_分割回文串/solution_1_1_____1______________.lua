-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133772625
-- LeetCode 131. 分割回文串 — Lua 版（方案1）
local function is_pal(s) -- local function is_pal(字符串)
	local i, j = 1, #s -- 把 1, #字符串 写入 local i, j
	while i < j do -- while 下标 i 小于 下标 j do
		if s:sub(i, i) ~= s:sub(j, j) then
			return false
		end
		i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		j = j - 1 -- 把 下标 j 减 1 存入 下标 j
	end -- 终点
	return true -- 返回 true
end -- 终点
local function partition(s) -- local function partition(字符串)
	local res = {} -- 把 {} 写入 local res
	local path = {} -- 把 {} 写入 local path
	local n = #s -- 把 #字符串 写入 local n
	local function dfs(start) -- local function dfs(起点)
		if start > n then -- 若 起点 超过 元素个数 then
			local cp = { table.unpack(path) } -- 把 {table.unpack(当前路径)} 写入 local cp
			res[#res + 1] = cp -- 把 cp 写入 res[#res + 1]
			return -- return
		end -- 终点
		for e = start, n do -- 把 起点, 元素个数 do 写入 for e
			local sub = s:sub(start, e) -- 把 字符串:sub(起点, e) 写入 local sub
			if is_pal(sub) then -- 若 is_pal(sub) then
				path[#path + 1] = sub -- 把 sub 写入 path[#path + 1]
				dfs(e + 1) -- dfs(e 加 1)
				path[#path] = nil -- 把 nil 写入 path[#path]
			end -- 终点
		end -- 终点
	end -- 终点
	dfs(1) -- dfs(1)
	return res -- 返回 结果
end -- 终点
local got = partition("aab") -- 把 partition(「aab」) 写入 local got
assert(#got == 2) -- 断言校验
assert(got[1][1] == "a" and got[1][2] == "a" and got[1][3] == "b") -- 断言校验
assert(got[2][1] == "aa" and got[2][2] == "b") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
