class MediaServer:
def __init__(self):
self.popularity = {}
def track_request(self, content_id):
if content_id in self.popularity:
self.popularity[content_id] += 1
else:
self.popularity[content_id] = 1
def get_popularity(self, content_id):
return self.popularity.get(content_id, 0)
def get_top_content(self, n=10):
sorted_popularity = sorted(self.popularity.items(), key=lambda x: x[1], reverse=True)
return sorted_popularity[:n]
# Example usage:
if __name__ == "__main__":
server = MediaServer()
# Simulate requests
requests = [1, 2, 3, 1, 2, 4, 1, 3, 2, 1, 4, 5, 1, 2, 3]
# Track requests
for request in requests:
server.track_request(request)
# Get popularity of specific content
print("Popularity of content 1:", server.get_popularity(1))
print("Popularity of content 2:", server.get_popularity(2))
# Get top N popular content
top_content = server.get_top_content(3)
print("\nTop 3 popular content:")
for content_id, popularity in top_content:
print(f"Content {content_id}: {popularity} requests")
