import asyncio


async def get_http_request():
    # print("Starting HTTP request")
    await asyncio.sleep(10)
    # print("Finished HTTP request")
    return "HTTP request result"


async def main():
    requests = [get_http_request() for _ in range(300)]
    results = await asyncio.gather(*requests)
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
