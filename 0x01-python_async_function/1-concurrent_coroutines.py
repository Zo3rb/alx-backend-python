#!/usr/bin/env python3
'''1. Let's execute multiple coroutines at the same time with async'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
	'''takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.
wait_n should return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.

 	Args:
		n (int): Number of delays.
		max_delay (int): The max delay value.

 	Returns:
		list[float]: Sorted values of delays.
 	'''
	delays = []
	async def add_delay():
		delay = await wait_random(max_delay)
		delays.append(delay)
		tasks = [add_delay() for _ in range(n)]
		await asyncio.gather(*tasks)
		return sorted(delays)
