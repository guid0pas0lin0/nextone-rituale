import { writeFileSync } from "fs";
import { ethers } from "ethers";

const RPC = process.env.POLYGON_RPC; // anche pubblico
const provider = new ethers.JsonRpcProvider(RPC);
const abi = JSON.parse(process.env.CONTRACT_ABI);
const c = new ethers.Contract(process.env.CONTRACT_ADDR, abi, provider);

const total = Number(await c.totalCount());
const fund  = Number(await c.fundPool()); // USDC 6 dec
const bonus = 100 * 1e6;

const state = { total_confessions: total, fund_pool: fund, is_paused: fund < bonus };
writeFileSync("data/state.json", JSON.stringify(state, null, 2));
