-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135154838
-- LeetCode 242. 有效的字母异位词 — Lua 版（方案1）
local function is_anagram(s, t) -- local function is_anagram(字符串, 另一字符串)
	if #s ~= #t then
		return false
	end -- 若 #字符串 ~ 赋值为 #另一字符串 then return false 终点
	local a, b = {}, {} -- 把 {}, {} 写入 local a, b
	s:gsub(".", function(c)
		a[#a + 1] = c
	end) -- 把 字符 终点) 写入 s:gsub(".", function(c) a[#a + 1]
	t:gsub(".", function(c)
		b[#b + 1] = c
	end) -- 把 字符 终点) 写入 t:gsub(".", function(c) b[#b + 1]
	table.sort(a) -- 排序
	table.sort(b) -- 排序
	for i = 1, #a do -- 把 1, #数组 do 写入 for i
		if a[i] ~= b[i] then
			return false
		end -- 若 数组[下标 i] ~ 赋值为 b[下标 i] then return false 终点
	end -- 终点
	return true -- 返回 true
end -- 终点
assert(is_anagram("anagram", "nagaram") == true) -- 断言校验
assert(is_anagram("rat", "car") == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
