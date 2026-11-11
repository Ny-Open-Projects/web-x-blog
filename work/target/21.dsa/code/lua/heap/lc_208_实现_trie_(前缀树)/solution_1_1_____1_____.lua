-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135533027
-- LeetCode 208. 实现 Trie (前缀树) — Lua 版（方案1）
local TrieNode = {} -- 把 {} 写入 local TrieNode
TrieNode.__index = TrieNode -- 把 TrieNode 写入 TrieNode.__index
function TrieNode.new()
	return setmetatable({ children = {}, is_end = false }, TrieNode)
end
local Trie = {} -- 把 {} 写入 local Trie
Trie.__index = Trie -- 把 Trie 写入 Trie.__index
function Trie.new()
	return setmetatable({ root = TrieNode.new() }, Trie)
end
function Trie:insert(word) -- function Trie:insert(单词)
	local node = self.root -- 把 self.根节点 写入 local node
	for i = 1, #word do -- 把 1, #单词 do 写入 for i
		local ch = word:sub(i, i) -- 把 单词:sub(下标 i, 下标 i) 写入 local ch
		if not node.children[ch] then
			node.children[ch] = TrieNode.new()
		end
		node = node.children[ch] -- 把 节点.children[字符] 存入 节点
	end -- 终点
	node.is_end = true -- 把 true 写入 node.is_end
end -- 终点
function Trie:search(word) -- function Trie:search(单词)
	local node = self.root -- 把 self.根节点 写入 local node
	for i = 1, #word do -- 把 1, #单词 do 写入 for i
		local ch = word:sub(i, i) -- 把 单词:sub(下标 i, 下标 i) 写入 local ch
		if not node.children[ch] then
			return false
		end -- 若 not 节点.children[字符] then return false 终点
		node = node.children[ch] -- 把 节点.children[字符] 存入 节点
	end -- 终点
	return node.is_end -- 返回 节点.is_end
end -- 终点
function Trie:startsWith(prefix) -- function Trie:startsWith(prefix)
	local node = self.root -- 把 self.根节点 写入 local node
	for i = 1, #prefix do -- 把 1, #prefix do 写入 for i
		local ch = prefix:sub(i, i) -- 把 prefix:sub(下标 i, 下标 i) 写入 local ch
		if not node.children[ch] then
			return false
		end -- 若 not 节点.children[字符] then return false 终点
		node = node.children[ch] -- 把 节点.children[字符] 存入 节点
	end -- 终点
	return true -- 返回 true
end -- 终点
local t = Trie.new() -- 把 Trie.new() 写入 local t
t:insert("apple") -- 另一字符串:insert(「apple」)
assert(t:search("apple") == true) -- 断言校验
assert(t:search("app") == false) -- 断言校验
assert(t:startsWith("app") == true) -- 断言校验
assert(t:search("appl") == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
