from aiopath import AsyncPath
from aiofile import AIOFile
import asyncio
from datetime import datetime
from exchange_rate import main as main_exchange
from logger import get_logger


import aiohttp
import names
from prettytable import PrettyTable
import websockets
from websockets import WebSocketServerProtocol
from websockets.exceptions import ConnectionClosedOK

# logging.basicConfig(level=logging.INFO)
logger = get_logger(__name__)


async def request(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    return result
                else:
                    print(f"Error status: {resp.status} for {url}")
        except aiohttp.ClientConnectorError as err:
            print(f'Connection error: {url}', str(err))


async def get_exchange(dig, valuta):

    try:
        s = await main_exchange(dig, valuta)
        list_rate = []
        for i in s:
            for date, value in i.items():
                list_rate.append(f'<date> {date} ')
                for key, val in value.items():
                    list_rate.append(f"{key} Sale: {val['sale']}  Buy: {val['purchase']}" + ', ')

        return list_rate
    except AttributeError:
        logger.error(f"AttributeError: Entered {dig}")
        return f'AttributeError: Entered {dig}, Enter digit max 10 days'
    except TypeError as err:
        logger.error(f"TypeError {err}  valuta {valuta}")
        return f'TypeError {err}  valuta {valuta}'


class Server:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        ws.name = names.get_full_name()
        self.clients.add(ws)
        logger.debug(f'{ws.remote_address} connects - {ws.name}')

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logger.debug(f'{ws.remote_address} disconnects - {ws.name}')

    async def send_to_clients(self, message: str):
        if self.clients:
            [await client.send(message) for client in self.clients]

    async def ws_handler(self, ws: WebSocketServerProtocol):
        await self.register(ws)
        try:
            await self.distribute(ws)
        except ConnectionClosedOK:
            pass
        finally:
            await self.unregister(ws)

    async def distribute(self, ws: WebSocketServerProtocol):
        async for message in ws:
            if 'exchange' in message.lower():
                message = message.upper().split(' ')
                time_now = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                digit = "1"
                valuta = ["USD", "EUR"]
                if 'EXCHANGE' in message:
                    if len(message) == 2:
                        digit = message[1]
                    elif len(message) >= 3:
                        digit = message[1]
                        valuta = message[2:]
                logger.info(f"log{message}, {ws.name}")
                exc = await get_exchange(digit, valuta)
                await save_logg_mess(f"[{time_now}] {' '.join(message)}, {ws.name}\n")
                await self.send_to_clients(exc)
            elif message == 'Hello':
                await self.send_to_clients(f"{ws.name}: {message}")
                await self.send_to_clients('Привіт мої любі!')
            else:
                await self.send_to_clients(f"{ws.name}: {message}")


async def save_logg_mess(message):
    try:
        file = AsyncPath("logg.txt")
        async with AIOFile(file, "a", encoding="utf-8") as afd:
            await afd.write(message)
    except AttributeError as err:
        return f'AttributeError {err} save_logg_mess'


async def main():
    server = Server()
    async with websockets.serve(server.ws_handler, 'localhost', 8080):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())
