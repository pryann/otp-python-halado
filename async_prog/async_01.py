import asyncio


async def get_http_request():
    print("Starting HTTP request")
    await asyncio.sleep(1)
    print("Finished HTTP request")
    return "HTTP request result"


async def main():
    print(await get_http_request())


if __name__ == "__main__":
    asyncio.run(main())
