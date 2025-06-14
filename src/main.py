import asyncio
from ai.gpt_integration import AIScraper
from evasion.fingerprint_rotator import StealthBrowser

async def main():
    print("""
    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
    ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    """)
    
    scraper = AIScraper("YOUR_OPENAI_KEY")
    browser = StealthBrowser()
    _, context = await browser.launch_undetected()
    page = await context.new_page()
    await page.goto("https://example.com")
    await page.screenshot(path="/app/data/screenshot.png")
    await context.close()

if __name__ == "__main__":
    asyncio.run(main())
