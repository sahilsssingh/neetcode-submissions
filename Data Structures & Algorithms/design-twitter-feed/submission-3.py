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
        followees = self.connections.get(userId, {userId})
        
        for el in followees:
            if el in self.tweets and self.tweets[el]:
                last_idx = len(self.tweets[el]) - 1
                count, tweetId = self.tweets[el][last_idx]
                heapq.heappush(heap, (count, tweetId, el, last_idx))
        
        res = []
        while heap and len(res) < 10:
            count, tweetId, el, idx = heapq.heappop(heap)
            res.append(tweetId)
            
            next_idx = idx - 1 
            if next_idx >= 0:
                next_count, next_tweetId = self.tweets[el][next_idx]
                heapq.heappush(heap, (next_count, next_tweetId, el, next_idx))
        
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
