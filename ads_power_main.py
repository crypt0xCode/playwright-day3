import json
from pathlib import Path
import asyncio
import time

from playwright.async_api import async_playwright

from ads_power.client import Client
import config
from ads_power.data.models import Proxy


def create_profile(
        client: Client | None = None,
        proxy: Proxy | None = None,
        group_name: str | None = None):
    """
    Create worker profile.
    :param client: ADS Client.
    :param proxy: Proxy.
    :param group_name: Group name.
    :return: user_id.
    """
    profile = client.profiles.new_profile(proxy=proxy, group_name=group_name)
    time.sleep(1)
    group_id = str(client.groups.get_group_id_by_group_name(group_name=group_name))
    time.sleep(1)
    user_id = client.profiles.query_profile(group_id=group_id)['data']['list'][-1]['user_id']

    return user_id


async def main():
    # Setting up proxy.
    proxy = Proxy(proxy_line='http://ip:port@login:password')
    # New client,
    ads_power_client = Client(api_key=config.ADS_API_KEY, api_uri=config.ADS_API_URI)

    user_id = create_profile(client=ads_power_client, proxy=proxy, group_name='ADS PW TEST4')
    profile_data = ads_power_client.browser.open_browser(user_id=user_id)
    print(profile_data)

    '''
    {
        "code": 0,
        "msg": "success",
        "data": {
            "ws": {
                "puppeteer": "ws://127.0.0.1:58299/devtools/browser/922320e5-1e5e-4c4d-b44e-b45d46dbbfbf",
                "selenium": "127.0.0.1:58299"
            },
            "debug_port": "58299",
            "webdriver": "/Users/riocrash/Library/Application Support/adspower_global/cwd_global/chrome_127/chromedriver.app/Contents/MacOS/chromedriver"
        }
    }
    '''
    for i in range(2):
        if not Path('./cookies.json').exists():
            async with async_playwright() as p:
                browser = await p.chromium.connect_over_cdp(profile_data['data']['ws']['puppeteer'])
                print(browser.contexts)
                context = browser.contexts[0]

                page = await context.new_page()
                await page.goto('https://stackoverflow.com/questions')

                link = page.locator('//*[@id="nav-users"]')
                await asyncio.sleep(3)

                await link.click()
                cookies = await context.cookies()
                print(cookies)
                await asyncio.sleep(3)

                Path('./cookies.json').write_text(json.dumps(cookies))
                await context.close()
        else:
            # Create second profile.
            second_user_id = create_profile(client=ads_power_client, proxy=proxy, group_name='ADS PW TEST4')
            second_profile_data = ads_power_client.browser.open_browser(user_id=second_user_id)
            print(second_profile_data)
            async with async_playwright() as p:
                browser = await p.chromium.connect_over_cdp(second_profile_data['data']['ws']['puppeteer'])
                context = await browser.new_context()
                await context.add_cookies(json.loads(Path('./cookies.json').read_text()))
                page = await context.new_page()
                await page.goto('https://stackoverflow.com/questions')
                await context.close()


if __name__ == '__main__':
    asyncio.run(main())
