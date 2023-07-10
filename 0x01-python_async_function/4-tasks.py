#!/usr/bin/env python3
'''4. Tasks'''

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
	'''Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.

 	Args:
		n (int): Number of delays.
		max_delay (int): The max delay value.

 	Returns:
		List[float]: Sorted values of delays.
 	'''
	delays = []
	async def add_delay():
		task = task_wait_random(max_delay)
		delay = await task
		delays.append(delay)
		tasks = [add_delay() for _ in range(n)]
		await asyncio.gather(*tasks)
		return sorted(delays)
