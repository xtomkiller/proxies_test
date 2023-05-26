import aiohttp
import asyncio
from termcolor import colored

async def check_proxy(proxy, session):
    try:
        async with session.get('https://www.google.com', proxy=proxy, timeout=5) as response:
            if response.status == 200:
                return True
    except aiohttp.ClientError:
        pass
    return False

async def test_proxies():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=5000') as response:
                proxies = await response.text()

        proxies = proxies.splitlines()
        total_proxies = len(proxies)
        checked_proxies = 0
        verified_proxies = []
        not_working_proxies = []

        print(colored(f'Total proxies to check: {total_proxies}', 'yellow'))

        async with aiohttp.ClientSession() as session:
            tasks = []
            for idx, proxy in enumerate(proxies, start=1):
                checked_proxies += 1
                task = asyncio.create_task(check_proxy(proxy, session))
                tasks.append(task)

            results = await asyncio.gather(*tasks)

            for idx, result in enumerate(results, start=1):
                proxy = proxies[idx - 1]
                if result:
                    verified_proxies.append(proxy)
                    print(colored(f'{idx}. Proxy {proxy.ljust(20)} is working', 'green'))
                else:
                    not_working_proxies.append(proxy)
                    print(colored(f'{idx}. Proxy {proxy.ljust(20)} is not working', 'red'))

        print(colored(f'Total proxies checked: {checked_proxies}', 'yellow'))
        print(colored(f'Verified proxies: {len(verified_proxies)}', 'green'))
        print(colored(f'Not working proxies: {len(not_working_proxies)}', 'red'))

        if verified_proxies:
            with open('proxies_verify.txt', 'w') as file:
                for proxy in verified_proxies:
                    file.write(proxy + '\n')
            print('Verified proxies saved to proxies_verify.txt')

    except KeyboardInterrupt:
        print('Script interrupted.')

    finally:
        print('Exiting...')
        print(colored(f'Total proxies to check: {total_proxies}', 'yellow'))
        print(colored(f'Total proxies checked: {checked_proxies}', 'yellow'))
        print(colored(f'Verified proxies: {len(verified_proxies)}', 'green'))
        print(colored(f'Not working proxies: {len(not_working_proxies)}', 'red'))
        exit()

asyncio.run(test_proxies())
