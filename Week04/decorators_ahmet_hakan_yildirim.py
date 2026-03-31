import time,tracemalloc
 

def performance(fn):
    """Decorator that tracks execution time and memory consumption of a function."""
    # Initialize tracking attributes if not already present
    if not hasattr(performance, "call_count"):
        performance.call_count = 0
        performance.time_elapsed = 0
        performance.memory_used = 0
    
    def inner(*args, **kwargs):
        # Update function invocation count
        performance.call_count += 1
        
        # Begin memory and execution time monitoring
        tracemalloc.start()
        start = time.time()
        
        # Run the original function
        ret_value = fn(*args, **kwargs)
        
        # End monitoring and capture metrics
        end = time.time()
        current_usage, max_usage = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Accumulate memory and execution time
        performance.memory_used += max_usage
        performance.time_elapsed += (end - start)
        
        return ret_value
    
    return inner
