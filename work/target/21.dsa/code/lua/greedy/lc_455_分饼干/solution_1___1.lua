-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135096603
-- LeetCode 455. 分发饼干 — Lua 版（方案1）
local function find_content_children(g, s) -- local function find_content_children(g, 字符串)
	table.sort(g) -- 排序
	table.sort(s) -- 排序
	local child, cookie = 1, 1 -- 把 1, 1 写入 local child, cookie
	while child <= #g and cookie <= #s do -- 把 #g and cookie 不超过 #字符串 do 写入 while child <
		if s[cookie] >= g[child] then
			child = child + 1
		end -- 若 字符串[cookie] 不低于 g[子节点] then 子节点 赋值为 子节点 加 1 终点
		cookie = cookie + 1 -- 把 cookie 加 1 存入 cookie
	end -- 终点
	return child - 1 -- 返回 子节点 减 1
end -- 终点
assert(find_content_children({ 1, 2, 3 }, { 1, 1 }) == 1) -- 断言校验
assert(find_content_children({ 1, 2 }, { 1, 2, 3 }) == 2) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
