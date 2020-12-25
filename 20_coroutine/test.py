# 协程运行底层
import asyncio
import time

if __name__ == "__main__":

    async def worker_1():
        print("work1开始")
        await asyncio.sleep(1)
        print("work1结束")

    async def worker_2():
        print("work2开始")
        await asyncio.sleep(2)
        print("work2结束")

    async def main6():
        task1 = asyncio.create_task(worker_1())
        task2 = asyncio.create_task(worker_2())
        print("await之前")
        await task1
        print("await worker_1之后")
        await task2
        print("await worker_2之后")


    start = time.perf_counter()
    asyncio.run(main6())
    end = time.perf_counter()
    print("6运行耗时{}秒".format(end - start))