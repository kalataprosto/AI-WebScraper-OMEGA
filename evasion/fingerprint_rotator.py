import random
from playwright.async_api import async_playwright

class StealthBrowser:
    async def launch_undetected(self):
        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context(
            user_agent=random.choice(self._get_user_agents()),
            viewport={"width": random.randint(1200,1400), "height": random.randint(800,1000)}
        )
        await self._apply_stealth(context)
        return browser, context

    def _get_user_agents(self):
        return [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)..."
        ]

    async def _apply_stealth(self, context):
        await context.add_init_script("""
        delete navigator.__proto__.webdriver;
        window.navigator.chrome = { runtime: {}, app: { isInstalled: false }};
        """)
