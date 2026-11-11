-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137060905
-- LeetCode 451. 根据字符出现频率排序 — Lua 版（方案5）
local function frequency_sort(s) -- local function frequency_sort(字符串)
	local counts, first = {}, {} -- 把 {}, {} 写入 local counts, first
	for i = 1, #s do -- 把 1, #字符串 do 写入 for i
		local c = s:sub(i, i) -- 把 字符串:sub(下标 i, 下标 i) 写入 local c
		if counts[c] == nil then
			counts[c] = 0
			first[c] = i
		end
		counts[c] = counts[c] + 1 -- 把 counts[字符] 加 1 写入 counts[c]
	end -- 终点
	local order = {} -- 把 {} 写入 local order
	for c in pairs(counts) do
		order[#order + 1] = c
	end -- 把 字符 终点 写入 for c in pairs(counts) do order[#order + 1]
	table.sort(order, function(a, b) -- 排序
		if counts[a] ~= counts[b] then
			return counts[a] > counts[b]
		end
		return first[a] < first[b] -- 返回 first[数组] 小于 first[b]
	end) -- 终点)
	local out = {} -- 把 {} 写入 local out
	for _, c in ipairs(order) do -- 遍历取 字符
		out[#out + 1] = string.rep(c, counts[c]) -- 把 string.rep(字符, counts[字符]) 写入 out[#out + 1]
	end -- 终点
	return table.concat(out) -- 返回 table.concat(out)
end -- 终点
assert(frequency_sort("tree") == "eetr") -- 断言校验
assert(frequency_sort("") == "") -- 断言校验
assert(frequency_sort("cccaaa") == "cccaaa") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
