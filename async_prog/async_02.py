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
    get = await get_http_request()
    post = await post_http_request("Johnny Boy")
    print(f"GET result: {get}, Post result: {post}")


if __name__ == "__main__":
    asyncio.run(main())
