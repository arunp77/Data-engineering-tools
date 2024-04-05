import requests
import time
from multiprocessing import Pool

def compute_response_time_sync(x):
    t0 = time.time()
    requests.get(url='http://127.0.0.1:8000/sync')
    t1 = time.time()
    return t1 - t0

def compute_response_time_async(x):
    t0 = time.time()
    requests.get(url='http://127.0.0.1:8000/async')
    t1 = time.time()
    return t1 - t0

def overflow_requests(function, number_of_parallel_operations=20):
    with Pool(number_of_parallel_operations) as p:
        values = p.map(function, [i for i in range(
            number_of_parallel_operations)])
        s = 0
        for i in values:
            s += i
        return s/len(values)
if __name__ == '__main__':
    print('making 20 requests on the `/sync` endpoint ...')
    delta_t = overflow_requests(compute_response_time_sync, 20)
    print('took {} seconds'.format(delta_t))
    print('making 20 requests on the `/async` endpoint')
    delta_t = overflow_requests(compute_response_time_async, 20)
    print('took {} seconds'.format(delta_t))