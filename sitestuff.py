import requests, os, time, asyncio
from pyppeteer import launch
from rgbprint import gradient_print, gradient_change, gradient_scroll, rgbprint, Color

name = "SiteStuff"

os.system(f"title {name}")

def inputcolor(text, color):
    txt = f"\033[38;2;{((color >> 16) & 255)};{((color >> 8) & 255)};{(color & 255)}m{text}\033[0m"
    return txt

def init():
    rgbprint("Hello", color=0xa45acc)

async def screenshot(url, output_file='testical.png'):
    try:
        browser = await launch()
        context = await browser.createIncognitoBrowserContext()
        page = await context.newPage()

        await page.goto(url)

        await page.waitForSelector('body')

        size = await page.evaluate('''() => {
            return {
                width: document.documentElement.clientWidth,
                height: Math.max(document.documentElement.clientHeight, window.innerHeight)
            };
        }''')

        await page.setViewport(size)

        rslt = inputcolor(f"Enter the output file name (default is 'testical'): ", color=0xa45acc)
        result = input(rslt).strip()
        if result == "":
            result = "testical"

        await page.screenshot({'path': f"{result}.png", 'fullPage': True})
        rgbprint(f"Full-page screenshot saved to {result}.png", color=0xa45acc)

    except Exception as e:
        rgbprint(f"An error occurred: {str(e)}", color=0xa45acc)

    finally:
        if browser:
            await browser.close()
    
    rgbprint("You must restart to use commands again", color=0xa45acc)
        
def options(prompt):
    print("\n")
    inputcolor1 = inputcolor(f"{prompt}: ", color=0xa45acc)
    inp = input(inputcolor1).lower()
    if inp == "info":
        os.system("cls")
        rgbprint(f"""Info
---
  
I created this for fun because I wanted a multitool that can do basic stuff for me like take a screenshot of a website, without needing to go on a siteshot website 
Its called {name} because I honestly didnt know what to call it""", color=0xa45acc)
        options(prompt)
    elif inp == "cmds":
        os.system("cls")
        rgbprint(f"""Commands
--------

<query> - Required
[query] - Optional

info - Returns info about the program
cmds - Displays the command list
screenshot <website> - Takes a full page screenshot of a website from url""", color=0xa45acc)
        options(prompt)
    elif inp.startswith("screenshot ") and len(inp.split()) > 1:
        url = inp.split()[1]
        asyncio.run(screenshot(url))

# webs = input("Enter the website URL: ")
# result = input(f"Enter the output file name (default is '{webs} Screenshot.png'): ") or f'{webs} Screenshot.png'

init()
options("Enter a command")

while True:
    pass