import asyncio
import time

async def fetch_data(delay, item_id):
    print(f"[{time.time():.2f}] Start fetching data for item {item_id}")
    await asyncio.sleep(delay)  
    print(f"[{time.time():.2f}] Finished fetching data for item {item_id}")
    return f"Data for {item_id} after {delay} seconds"

async def main():
    start_time = time.time()
    tasks = [
        asyncio.create_task(fetch_data(3, "A")),
        asyncio.create_task(fetch_data(1, "B")),
        asyncio.create_task(fetch_data(2, "C"))
    ]
    results = await asyncio.gather(*tasks)
    print("\nAll tasks completed.")
    for res in results:
        print(res)
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
