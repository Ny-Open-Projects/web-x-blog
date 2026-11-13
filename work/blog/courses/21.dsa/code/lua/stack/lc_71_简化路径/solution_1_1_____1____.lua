-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134368624
-- LeetCode 71. 简化路径 — Lua 版（方案1）
local function simplify_path(path) -- local function simplify_path(当前路径)
	local st = {} -- 把 {} 写入 local st
	for part in path:gmatch("[^/]+") do -- for part in 当前路径:gmatch(「[ 按位异或 除以 ] 加 」) do
		if part == ".." then -- 若 part 等于 「..」 then
			if #st > 0 then
				st[#st] = nil
			end -- 若 #st 超过 0 then st[#st] 赋值为 nil 终点
		elseif part ~= "." then -- 把 「.」 then 写入 elseif part ~
			st[#st + 1] = part -- 把 part 写入 st[#st + 1]
		end -- 终点
	end -- 终点
	if #st == 0 then
		return "/"
	end -- 若 #st 等于 0 then return 「 除以 」 终点
	return "/" .. table.concat(st, "/") -- 返回 「 除以 」 .. table.concat(st, 「 除以 」)
end -- 终点
assert(simplify_path("/home/") == "/home") -- 断言校验
assert(simplify_path("/../") == "/") -- 断言校验
assert(simplify_path("/home//foo/") == "/home/foo") -- 断言校验
assert(simplify_path("/a/./b/../../c/") == "/c") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
