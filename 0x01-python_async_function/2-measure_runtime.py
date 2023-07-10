#!/usr/bin/env python3
'''2. Measure the runtime'''

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
	'''Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time.

 	Args:
		n (int): Number of delays.
		max_delay (int): The max delay value.

 	Returns:
		list[float]: Sorted values of delays.
 	'''
	start_time = time.time()
	asyncio.run(wait_n(n, max_delay))
	end_time = time.time()
	
	total_time = end_time - start_time
	
	average_time = total_time / n
	return average_time
