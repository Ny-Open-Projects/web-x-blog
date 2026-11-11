-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145295630
-- LeetCode 1047. 删除字符串中的所有相邻重复项 — Lua 版（方案1）
local function remove_duplicates(s) -- local function remove_duplicates(字符串)
	local st = {} -- 把 {} 写入 local st
	for i = 1, #s do -- 把 1, #字符串 do 写入 for i
		local c = s:sub(i, i) -- 把 字符串:sub(下标 i, 下标 i) 写入 local c
		if #st > 0 and st[#st] == c then -- 若 #st 超过 0 and st[#st] 等于 字符 then
			st[#st] = nil -- 把 nil 写入 st[#st]
		else -- 否则
			st[#st + 1] = c -- 把 字符 写入 st[#st + 1]
		end -- 终点
	end -- 终点
	return table.concat(st) -- 返回 table.concat(st)
end -- 终点
assert(remove_duplicates("abbaca") == "ca") -- 断言校验
assert(remove_duplicates("azxxzy") == "ay") -- 断言校验
assert(remove_duplicates("") == "") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
