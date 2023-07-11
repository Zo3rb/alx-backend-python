#!/usr/bin/env python3
'''2. Run time for four parallel comprehensions'''

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
	'''will execute async_comprehension four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
Notice that the total runtime is roughly 10 seconds, explain it to yourself.

 	Returns:
		float: time exceeded.
 	'''
	start_time = asyncio.get_event_loop().time()
	await asyncio.gather(async_comprehension(), async_comprehension(),async_comprehension(),
											 async_comprehension())
	end_time = asyncio.get_event_loop().time()
	total_runtime = end_time - start_time
	return total_runtime
