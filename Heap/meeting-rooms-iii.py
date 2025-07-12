class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused, used = list(range(n)), []
        heapify(unused)
        meeting_count = [0] * n

        for start, end in sorted(meetings):
            while used and used[0][0] <= start:
                _, room = heappop(used)
                heappush(unused, room)
            if unused:
                room = heappop(unused)
                heappush(used, [end, room])
            else:
                room_availability_time, room = heappop(used)
                heappush(
                    used,
                    [room_availability_time + end - start, room]
                ) 
            meeting_count[room] += 1
        
        return meeting_count.index(max(meeting_count))

# 2402. Meeting Rooms III
