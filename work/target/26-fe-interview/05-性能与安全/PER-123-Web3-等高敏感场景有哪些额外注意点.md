---
title: [PER-123] Web3 等高敏感场景有哪些额外注意点？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-123：Web3 等高敏感场景有哪些额外注意点？

**答**：
- 私钥铁律：**私钥/助记词永不触网、永不上报、永不进日志**——前端只做签名请求转发，签名由钱包扩展/硬件完成。
- 签名防钓鱼：展示**人话版签名内容**（交易解码后呈现）、警惕 `personal_sign` 空白签名、域名与合约地址白名单。
- 前端特有风险：恶意 RPC 注入（window.ethereum 被伪造）、剪贴板劫持（地址替换木马）、克隆站钓鱼（验证域名与证书固定）。
- 合规注意：KYC/AML 场景数据本地化存储、链上数据不可删的合规影响（个保法删除权）。

```javascript
// Web3 前端防护：签名前解码校验 + 域名与合约白名单
const TRUSTED_CONTRACTS = new Set([
  '0xAAAA...aaa1'.toLowerCase(), // 官方合约地址，小写归一化
]);

async function safeMint(signer) {
  const contractAddress = MINT_CONTRACT.toLowerCase();
  if (!TRUSTED_CONTRACTS.has(contractAddress)) {
    throw new Error('合约地址不在白名单，拒绝交互');   // 防克隆站换合约
  }
  // 构造交易：由钱包扩展签名，私钥全程不出扩展
  const tx = await signer.sendTransaction({
    to: contractAddress,
    data: mintInterface.encodeFunctionData('mint', [1]),
    value: ethers.parseEther('0.01'),
  });
  // 签名请求发起前：向用户呈现解码后的操作摘要（人话版），防空白签名钓鱼
  showConfirmDialog({
    action: '铸造 1 个 NFT',
    contract: contractAddress,
    cost: '0.01 ETH',
  });
  return tx.wait();
}

// 剪贴板防护：转账前校验地址一致性，防剪贴板劫持替换
function verifyAddress(pasted, expectedChecksum) {
  return ethers.getAddress(pasted) === ethers.getAddress(expectedChecksum); // EIP-55 校验和验证
}
```
