import heapq

class Twitter:

    def __init__(self):
        self.connections = {} # userID : (set of followers)
        self.tweets = {} # userId : [(most recent post count , tweetId)]
        self.count = 0 # for keeping track of most-recent/least-recent post count 

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((-self.count, tweetId))
        self.count += 1
        
        if userId not in self.connections:
            self.connections[userId] = set()
            self.connections[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for el in self.connections.get(userId, {userId}):
            for tup in self.tweets.get(el, []):
                heapq.heappush(heap, tup)
            
        res = []
        while heap and len(res) < 10:
            res.append(heapq.heappop(heap)[1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.connections:
            self.connections[followerId] = set()
            self.connections[followerId].add(followerId)

        if followeeId not in self.connections:
            self.connections[followeeId] = set()
            self.connections[followeeId].add(followeeId)

        self.connections[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.connections:
            self.connections[followerId].discard(followeeId)
