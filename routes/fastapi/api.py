import aiohttp
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/api/demons/{demon_list}", tags = ["API"])
async def demons(demon_list):
    pointercrate_base = "/api/v2/demons/listed/"

    async with aiohttp.ClientSession() as session:
        if demon_list == "pointercrate":
            async with session.get(f"https://pointercrate.com{pointercrate_base}") as p:
                return await p.json()
        elif demon_list == "challenge":
            async with session.get(f"https://challengelist.gd{pointercrate_base}") as ch:
                return await ch.json()
        else:
            raise HTTPException(status_code = 404, detail = "Demon list not found. The only accepted values are pointercrate and challenge.")