import requests
from web3 import Web3
import time
import json
import random
from eth_account.messages import encode_defunct
from colorama import init, Fore
from rich.console import Console
from rich.panel import Panel
import datetime

console = Console()

# ASCII Art Banner
print("""
██████╗░██╗░░██╗░█████╗░██████╗░░█████╗░░██████╗  ░█████╗░██╗░░░██╗████████╗░█████╗░  ████████╗██╗░░██╗
██╔══██╗██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗  ╚══██╔══╝╚██╗██╔╝
██████╔╝███████║███████║██████╔╝██║░░██║╚█████╗░  ███████║██║░░░██║░░░██║░░░██║░░██║  ░░░██║░░░░╚███╔╝░
██╔═══╝░██╔══██║██╔══██║██╔══██╗██║░░██║░╚═══██╗  ██╔══██║██║░░░██║░░░██║░░░██║░░██║  ░░░██║░░░░██╔██╗░
██║░░░░░██║░░██║██║░░██║██║░░██║╚█████╔╝██████╔╝  ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝  ░░░██║░░░██╔╝╚██╗
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═════╝░  ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝

by Kazmight
""")


# Configuration from the provided config.py content
w3 = Web3(Web3.HTTPProvider("https://testnet.dplabs-internal.com"))

CHAIN_ID = 688688
RPC_URL = "https://testnet.dplabs-internal.com"
EXPLORER = "https://testnet.pharosscan.xyz/tx/"

WPHRS_ADDRESS = w3.to_checksum_address("0x76aaada469d23216be5f7c596fa25f282ff9b364")
USDC_ADDRESS = w3.to_checksum_address("0xad902cf99c2de2f1ba5ec4d642fd7e49cae9ee37")
USDT_ADDRESS = w3.to_checksum_address("0xed59de2d7ad9c043442e381231ee3646fc3c2939")
POSITION_MANAGER_ADDRESS = w3.to_checksum_address("0xF8a1D4FF0f9b9Af7CE58E1fc1833688F3BFd6115")
FACTORY = w3.to_checksum_address("0x7CE5b44F2d05babd29caE68557F52ab051265F01")
QUOTER = w3.to_checksum_address("0x00f2f47d1ed593Cf0AF0074173E9DF95afb0206C")
SWAP_ROUTER_ADDRESS = w3.to_checksum_address("0x1a4de519154ae51200b0ad7c90f7fac75547888a")
USDC_POOL_ADDRESS = w3.to_checksum_address("0x0373a059321219745aee4fad8a942cf088be3d0e")
USDT_POOL_ADDRESS = w3.to_checksum_address("0x70118b6eec45329e0534d849bc3e588bb6752527")

ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "spender", "type": "address"},
            {"name": "amount", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [
            {"name": "owner", "type": "address"},
            {"name": "spender", "type": "address"}
        ],
        "name": "allowance",
        "outputs": [{"name": "", "type": "uint256"}],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "to", "type": "address"},
            {"name": "amount", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function",
    }
]

SWAP_ROUTER_ABI = [
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "address", "name": "tokenIn", "type": "address"},
                    {"internalType": "address", "name": "tokenOut", "type": "address"},
                    {"internalType": "uint24", "name": "fee", "type": "uint24"},
                    {"internalType": "address", "name": "recipient", "type": "address"},
                    {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                    {"internalType": "uint256", "name": "amountOutMinimum", "type": "uint256"},
                    {"internalType": "uint160", "name": "sqrtPriceLimitX96", "type": "uint160"},
                ],
                "internalType": "struct IV3SwapRouter.ExactInputSingleParams",
                "name": "params",
                "type": "tuple",
            },
        ],
        "name": "exactInputSingle",
        "outputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"}],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "bytes", "name": "path", "type": "bytes"},
                    {"internalType": "address", "name": "recipient", "type": "address"},
                    {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                    {"internalType": "uint256", "name": "amountOutMinimum", "type": "uint256"},
                ],
                "internalType": "struct IV3SwapRouter.ExactInputParams",
                "name": "params",
                "type": "tuple",
            },
        ],
        "name": "exactInput",
        "outputs": [{"internalType": "uint256", "name": "amountOut", "type": "uint256"}],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "bytes[]", "name": "data", "type": "bytes[]"}],
        "name": "multicall",
        "outputs": [{"internalType": "bytes[]", "name": "results", "type": "bytes[]"}],
        "stateMutability": "payable",
        "type": "function",
    },
]

LP_ROUTER_ABI = [
    {
        "inputs": [
            {
                "internalType": "tuple",
                "components": [
                    {"internalType": "address", "name": "token0", "type": "address"},
                    {"internalType": "address", "name": "token1", "type": "address"},
                    {"internalType": "uint24", "name": "fee", "type": "uint24"},
                    {"internalType": "int24", "name": "tickLower", "type": "int24"},
                    {"internalType": "int24", "name": "tickUpper", "type": "int24"},
                    {"internalType": "uint256", "name": "amount0Desired", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount1Desired", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount0Min", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount1Min", "type": "uint256"},
                    {"internalType": "address", "name": "recipient", "type": "address"},
                    {"internalType": "uint256", "name": "deadline", "type": "uint256"}
                ],
                "name": "params",
                "type": "tuple"
            }
        ],
        "name": "mint",
        "outputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}],
        "stateMutability": "payable",
        "type": "function"
    }
]

POOL_ABI = [
    {
        "inputs": [],
        "name": "token0",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "token1",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "fee",
        "outputs": [{"internalType": "uint24", "name": "", "type": "uint24"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "slot0",
        "outputs": [
            {"internalType": "uint160", "name": "sqrtPriceX96", "type": "uint160"},
            {"internalType": "int24", "name": "tick", "type": "int24"},
            {"internalType": "uint16", "name": "observationIndex", "type": "uint16"},
            {"internalType": "uint16", "name": "observationCardinality", "type": "uint16"},
            {"internalType": "uint16", "name": "observationCardinalityNext", "type": "uint16"},
            {"internalType": "uint8", "name": "feeProtocol", "type": "uint8"},
            {"internalType": "bool", "name": "unlocked", "type": "bool"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

POSITION_MANAGER_ABI = [
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "address", "name": "token0", "type": "address"},
                    {"internalType": "address", "name": "token1", "type": "address"},
                    {"internalType": "uint24", "name": "fee", "type": "uint24"},
                    {"internalType": "int24", "name": "tickLower", "type": "int24"},
                    {"internalType": "int24", "name": "tickUpper", "type": "int24"},
                    {"internalType": "uint256", "name": "amount0Desired", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount1Desired", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount0Min", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount1Min", "type": "uint256"},
                    {"internalType": "address", "name": "recipient", "type": "address"},
                    {"internalType": "uint256", "name": "deadline", "type": "uint256"}
                ],
                "internalType": "struct INonfungiblePositionManager.MintParams",
                "name": "params",
                "type": "tuple"
            }
        ],
        "name": "mint",
        "outputs": [
            {"internalType": "uint256", "name": "tokenId", "type": "uint256"},
            {"internalType": "uint128", "name": "liquidity", "type": "uint128"},
            {"internalType": "uint256", "name": "amount0", "type": "uint256"},
            {"internalType": "uint256", "name": "amount1", "type": "uint256"}
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "uint256", "name": "tokenId", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount0Desired", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount1Desired", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount0Min", "type": "uint256"},
                    {"internalType": "uint256", "name": "amount1Min", "type": "uint256"},
                    {"internalType": "uint256", "name": "deadline", "type": "uint256"}
                ],
                "internalType": "struct INonfungiblePositionManager.IncreaseLiquidityParams",
                "name": "params",
                "type": "tuple"
            }
        ],
        "name": "increaseLiquidity",
        "outputs": [
            {"internalType": "uint128", "name": "liquidity", "type": "uint128"},
            {"internalType": "uint256", "name": "amount0", "type": "uint256"},
            {"internalType": "uint256", "name": "amount1", "type": "uint256"}
        ],
        "stateMutability": "payable",
        "type": "function"
    }
]

DELAY_BETWEEN_TX = 10 # Default value, can be overridden if needed from an external config file

API_URL = "https://api.pharosnetwork.xyz"
BASE_URL = API_URL


def generate_random_address():
    return w3.eth.account.create().address

def acak_angka(min_val, max_val):
    return round(random.uniform(min_val, max_val), 6)

def sign_message(private_key, message="pharos"):
    acct = w3.eth.account.from_key(private_key)
    msg = encode_defunct(text=message)
    signed = acct.sign_message(msg)
    return signed.signature.hex()

def login_with_private_key(private_key):
    address = w3.eth.account.from_key(private_key).address
    signature = sign_message(private_key)
    url = f"{API_URL}/user/login?address={address}&signature={signature}"
    headers = {"Origin": "https://testnet.pharosnetwork.xyz", "Referer": "https://testnet.pharosnetwork.xyz"}
    try:
        response = requests.post(url, headers=headers)
        data = response.json()
        return data.get("data", {}).get("jwt")
    except Exception as e:
        print(f"❌ Gagal login: {e}")
        return None

def get_profile_info(address, bearer_token):
    url = f"{API_URL}/user/profile?address={address}"
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Origin': 'https://testnet.pharosnetwork.xyz',
        'Referer': 'https://testnet.pharosnetwork.xyz'
    }
    try:
        res = requests.get(url, headers=headers)
        if res.ok:
            data = res.json()
            poin = data.get("data", {}).get("user_info", {}).get("TotalPoints", 0)
            print(f"📋 Poin: {poin}")
            return data
        else:
            print("❌ Gagal ambil profil")
            return {}
    except Exception as e:
        print(f"❌ Gagal ambil profil: {e}")
        return {}

def get_today_index():
    day_of_week = datetime.datetime.today().weekday()
    return day_of_week


def is_checkin_available(status_str):
    index = get_today_index()
    if len(status_str) != 7:
        return False, "⚠️ Status tidak valid."
    
    char_today = status_str[index]
    if char_today == "2":
        return True, "🕓 Belum check-in, akan mencoba check-in."
    elif char_today == "0":
        return False, "ℹ️ Sudah check-in hari ini."
    elif char_today == "1":
        return False, "⏭️ Hari ini dilewati."
    else:
        return False, "❌ Status tidak dikenal."

def checkin(address, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Referer': 'https://testnet.pharosnetwork.xyz/',
        'Origin': 'https://testnet.pharosnetwork.xyz',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': 'application/json, text/plain, */*',
    }

    url_status = f"{API_URL}/sign/status?address={address}"
    try:
        res = requests.get(url_status, headers=headers)
        if res.ok:
            status_str = res.json().get("data", {}).get("status", "2222222")
            available, info = is_checkin_available(status_str)
            print(info)
            if available:
                url_checkin = f"{API_URL}/sign/in?address={address}"
                res_checkin = requests.post(url_checkin, headers=headers)
                if res_checkin.ok:
                    print("✅ Check-in berhasil!")
                else:
                    print(f"❌ Gagal check-in: {res_checkin.text}")
            else:
                print("ℹ️ Tidak melakukan check-in.")
        else:
            print(f"⚠️ Gagal mendapatkan status check-in: {res.text}")
    except Exception as e:
        print(f"❌ Error saat check-in: {e}")

def send_transaction(private_key, to_address, value=0.001):
    account = w3.eth.account.from_key(private_key)
    address = account.address
    value_wei = w3.to_wei(value, 'ether')
    nonce = w3.eth.get_transaction_count(address)

    tx = {
        'chainId': CHAIN_ID,
        'to': to_address,
        'value': value_wei,
        'gas': 21000,
        'gasPrice': w3.to_wei(1.2, 'gwei'),
        'nonce': nonce,
    }

    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(tx_hash)

    return tx_hash.hex(), address

def verify_transaction(address, tx_hash, bearer_token):
    url = f"{API_URL}/task/verify?address={address}&task_id=103&tx_hash={tx_hash}"
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Origin': 'https://testnet.pharosnetwork.xyz',
        'Referer': 'https://testnet.pharosnetwork.xyz'
    }
    try:
        return requests.post(url, headers=headers).json()
    except Exception as e:
        return {"error": str(e)}

def swap_token(private_key):
    jumlah = acak_angka(0.001, 0.002)
    amount_in_wei = w3.to_wei(jumlah, 'ether')
    account = w3.eth.account.from_key(private_key)
    address = account.address
    nonce = w3.eth.get_transaction_count(address)
    token = w3.eth.contract(address=WPHRS_ADDRESS, abi=ERC20_ABI)
    router = w3.eth.contract(address=SWAP_ROUTER_ADDRESS, abi=SWAP_ROUTER_ABI)

    approve_tx = token.functions.approve(SWAP_ROUTER_ADDRESS, amount_in_wei).build_transaction({
        'from': address,
        'nonce': nonce,
        'gas': 60000,
        'gasPrice': w3.eth.gas_price,
        'chainId': CHAIN_ID
    })
    signed_approve = w3.eth.account.sign_transaction(approve_tx, private_key)
    w3.eth.send_raw_transaction(signed_approve.rawTransaction)
    time.sleep(5)

    params = {
        "tokenIn": WPHRS_ADDRESS,
        "tokenOut": USDC_ADDRESS,
        "fee": 500,
        "recipient": address,
        "amountIn": amount_in_wei,
        "amountOutMinimum": 0,
        "sqrtPriceLimitX96": 0
    }

    tx = router.functions.exactInputSingle(params).build_transaction({
        'from': address,
        'nonce': nonce + 1,
        'gas': 300000,
        'gasPrice': w3.eth.gas_price,
        'chainId': CHAIN_ID
    })
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"✅ Swap sukses: {EXPLORER}{tx_hash.hex()}")

def get_pool_contract(token0, token1, fee):
    return None

def add_liquidity(w3, private_key, token0_address, token1_address, amount0, amount1, position_manager, position_manager_abi, fee):
    wallet = w3.eth.account.from_key(private_key)
    address = wallet.address

    token0 = w3.eth.contract(address=token0_address, abi=ERC20_ABI)
    token1 = w3.eth.contract(address=token1_address, abi=ERC20_ABI)
    position_manager_contract = w3.eth.contract(address=position_manager, abi=position_manager_abi)

    nonce = w3.eth.get_transaction_count(address)

    tx1 = token0.functions.approve(position_manager, amount0).build_transaction({
        'from': address,
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': w3.eth.gas_price
    })
    signed_tx1 = w3.eth.account.sign_transaction(tx1, private_key)
    w3.eth.send_raw_transaction(signed_tx1.rawTransaction)
    time.sleep(3)

    tx2 = token1.functions.approve(position_manager, amount1).build_transaction({
        'from': address,
        'nonce': nonce + 1,
        'gas': 200000,
        'gasPrice': w3.eth.gas_price
    })
    signed_tx2 = w3.eth.account.sign_transaction(tx2, private_key)
    w3.eth.send_raw_transaction(signed_tx2.rawTransaction)
    time.sleep(3)

    deadline = int(time.time()) + 600
    tick_lower = -60000
    tick_upper = 60000

    mint_params = {
        "token0": token0_address,
        "token1": token1_address,
        "fee": fee,
        "tickLower": tick_lower,
        "tickUpper": tick_upper,
        "amount0Desired": amount0,
        "amount1Desired": amount1,
        "amount0Min": 0,
        "amount1Min": 0,
        "recipient": address,
        "deadline": deadline
    }

    tx3 = position_manager_contract.functions.mint(mint_params).build_transaction({
        'from': address,
        'nonce': nonce + 2,
        'value': 0,
        'gas': 800000,
        'gasPrice': w3.eth.gas_price
    })
    signed_tx3 = w3.eth.account.sign_transaction(tx3, private_key)
    tx_hash3 = w3.eth.send_raw_transaction(signed_tx3.rawTransaction)
    print("💧 LP Mint dikirim...")
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash3)
    return tx_hash3.hex()

def main():
    try:
        jumlah_tx = int(input("Jumlah transaksi per wallet: "))
        jumlah_swap = int(input("Jumlah swap per wallet: "))
        jumlah_lp = int(input("Jumlah add LP per wallet: "))
    except ValueError:
        print("Masukkan angka yang valid.")
        return

    try:
        with open("privateKeys.txt", "r") as f:
            private_keys = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("File privateKeys.txt tidak ditemukan.")
        return

    for i, pk in enumerate(private_keys):
        print("=" * 50)
        print(f"▶️ Wallet #{i+1}")

        if not pk.startswith("0x"):
            pk = "0x" + pk

        try:
            account = w3.eth.account.from_key(pk)
            address = account.address
            print(f"Wallet Address: {address}")
        except Exception as e:
            print(f"❌ Private key tidak valid atau koneksi RPC gagal: {e}")
            continue

        token = login_with_private_key(pk)
        if not token:
            print("❌ Login gagal.")
            continue
        print("✅ Login berhasil!")

        try:
            get_profile_info(address, token)
            checkin(address, token)
        except Exception as e:
            print(f"❗ Gagal ambil profil atau checkin: {e}")

        for txi in range(1, jumlah_tx + 1):
            print(f"\n🔄 Transaksi native #{txi}")
            tujuan = generate_random_address()
            print(f"Alamat tujuan: {tujuan}")

            try:
                tx_hash, sender = send_transaction(pk, tujuan)
                print(f"✅ TX berhasil: {tx_hash}")

                verif = verify_transaction(sender, tx_hash, token)
                if verif.get("code") == 0 and verif.get("data", {}).get("verified"):
                    print("🔒 Verifikasi sukses!")
                else:
                    print("❌ Verifikasi gagal.")

                profil = get_profile_info(sender, token)
                poin = profil.get("data", {}).get("user_info", {}).get("TaskPoints", 0)
                print(f"🎯 Total Poin: {poin}")

                if txi < jumlah_tx:
                    print(f"⏳ Menunggu {DELAY_BETWEEN_TX} detik...")
                    time.sleep(DELAY_BETWEEN_TX)

            except Exception as e:
                print(f"❗ Kesalahan: {str(e)}")
                time.sleep(5)

        for sxi in range(1, jumlah_swap + 1):
            print(f"\n🔁 Swap token #{sxi}")
            try:
                swap_token(pk)
                time.sleep(5)
            except Exception as e:
                print(f"❗ Gagal swap: {e}")

        for lpi in range(1, jumlah_lp + 1):
            print(f"\n💧 Add LP #{lpi}")
            try:
                amount0 = w3.to_wei(0.01, "ether")
                amount1 = w3.to_wei(0.01, "ether")

                tx_hash = add_liquidity(
                    w3,
                    pk,
                    WPHRS_ADDRESS,
                    USDC_ADDRESS,
                    amount0,
                    amount1,
                    POSITION_MANAGER_ADDRESS,
                    POSITION_MANAGER_ABI,
                    3000
                )
                print(f"✅ Add LP selesai: {EXPLORER}{tx_hash}")
                time.sleep(DELAY_BETWEEN_TX)
            except Exception as e:
                print(f"❌ Gagal LP: {str(e)}")
                time.sleep(5)

        print("=" * 50)

if __name__ == "__main__":
    main()
