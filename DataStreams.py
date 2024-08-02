import heapq
import time
class DataStreamScheduler:
def __init__(self):
self.queue = [] # Priority queue to store requests
def schedule_request(self, request, priority): """Schedule a new request""" heapq.heappush(self.queue, (priority, time.time(), request)) # Priority, timestamp, request
def process_requests(self): """Process requests in priority order""" while self.queue:
priority, _, request = heapq.heappop(self.queue) # Get the request with highest priorityprint(f"Processing request: {request}")
# Example usage
if __name__ == "__main__":
scheduler = DataStreamScheduler()
# Schedule some requests
scheduler.schedule_request("Data stream request 1", priority=3)
scheduler.schedule_request("Data stream request 2", priority=1)
scheduler.schedule_request("Data stream request 3", priority=2)
# Process requests
scheduler.process_requests()

Output
Processing request: Data Stream Request 2
Processing request: Data Stream Request 3
Processing request: Data Stream Request 1