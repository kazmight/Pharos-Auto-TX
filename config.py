from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://testnet.dplabs-internal.com"))

CHAIN_ID = 688688
RPC_URL = "https://testnet.dplabs-internal.com"
EXPLORER = "https://testnet.pharosscan.xyz/tx/"


WPHRS_ADDRESS = w3.to_checksum_address("0x76aaada469d23216be5f7c596fa25f282ff9b364")
USDC_ADDRESS = w3.to_checksum_address("0xad902cf99c2de2f1ba5ec4d642fd7e49cae9ee37")
USDT_ADDRESS = w3.to_checksum_address("0xed59de2d7ad9c043442e381231ee3646fc3c2939")
POSITIONMANAGER_ADDRESS = w3.to_checksum_address("0xF8a1D4FF0f9b9Af7CE58E1fc1833688F3BFd6115")
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
