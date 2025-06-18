import asyncio
# from decorators import runtime_benchmark


async def get_http_request():
    print("Starting GET HTTP request")
    await asyncio.sleep(1)
    print("Finished GET HTTP request")
    return "GET HTTP request result"


async def post_http_request(data):
    print("Starting POST HTTP request")
    await asyncio.sleep(2)
    print("Finished POST HTTP request")
    return data


async def main():
    get = asyncio.create_task(get_http_request())
    post = asyncio.create_task(post_http_request("Johnny"))
    result = await asyncio.gather(get, post)
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
