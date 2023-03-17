import asyncio
import platform
import sys
from pars_date import main as dates
from timing import async_timed

import aiohttp

URL = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='
VALUTA = ("USD", "EUR", "PLN")


async def request(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    result = await response.json()
                    return result
                else:
                    print(f'Error status: {response.status} for {url}')
        except aiohttp.ClientError as err:
            print(f'Connection error: {url}', str(err))


def parser(info_bank, valuta):
    currencies = info_bank['exchangeRate']
    value = dict()
    s = {info_bank['date']: value}
    for val in valuta:
        exc = list(filter(lambda el: el["currency"] == val, currencies))
        if exc:
            value.update({exc[0]['currency']: {"sale": exc[0]['saleRateNB'], "purchase": exc[0]['purchaseRateNB']}})
        else:
            value.update({val: "Not found"})
    return s


@async_timed()
async def main():
    try:
        digit = sys.argv[1]
        list_date = dates(digit)
        ex_rate = []
        for date in list_date:
            urls = URL + date
            result = await request(urls)
            if result:
                ex_rate.append(parser(result, VALUTA))
            else:
                return f'Not found'
        return ex_rate
    except IndexError as err:
        return f'IndexError {err}'
    except KeyboardInterrupt as err:
        return f'KeyboardInterrupt {err}'
    except TypeError as err:
        return f'TypeError {err}'


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)
