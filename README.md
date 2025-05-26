# Pharos Testnet Automated Transaction 🤖

![Pharos Testnet Multi Bot](https://img.shields.io/badge/Pharos%20Testnet%20Multi%20Bot-v1.0.0-blue.svg)
[![Releases](https://img.shields.io/badge/Releases-latest-orange.svg)](https://github.com/kazmight/Pharos-Auto-TX.git/releases)

Welcome to the **Pharos Testnet Multi Bot** repository! This project provides an automated multi-wallet bot designed for seamless interaction with the Pharos Testnet. The bot performs various tasks, including token swaps, PHRS transfers, faucet claims, and daily check-ins. It aims to help users stay active and potentially qualify for airdrops.


## Features

- **Automated Token Swaps**: Swap tokens effortlessly on the Pharos Testnet.
- **PHRS Transfers**: Send and receive PHRS tokens with ease.
- **Faucet Claims**: Claim tokens from faucets automatically.
- **Check-Ins**: Stay active with scheduled check-ins.
- **Add Liquidation**: Automated Add Liquidation PAIR PHRS, WPHRS, USDC, USDT.
- **Multi-Wallet Support**: Manage multiple wallets in one place.
- **Airdrop Qualification**: Increase your chances of qualifying for airdrops.

## Installation

```bash
https://github.com/kazmight/Pharos-Auto-TX.git
cd Pharos-Auto-TX
```

**Install Dependencies**:
```bash
npm install
```

To run the bot, use the following command in your terminal:

```bash
node index.js
```


## ⚙️ Configuration

1. **in the project root directory with your private keys `.env`**
   ```
   # For a single wallet
   PRIVATE_KEY=your_private_key_here

   # OR for multiple wallets
   PRIVATE_KEY_1=your_first_private_key
   PRIVATE_KEY_2=your_second_private_key
   PRIVATE_KEY_3=your_third_private_key
   ```
