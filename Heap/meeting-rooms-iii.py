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

# The code uses two min-heaps: one (unused) to track available rooms by room number, and another (used) to track busy rooms by their meeting end times. For each meeting (sorted by start time), the code first frees up any rooms whose meetings have ended, then either assigns the meeting to the lowest-numbered available room or delays it until the soonest room becomes free—keeping the original meeting duration. Each time a room is assigned a meeting, its count is incremented. Finally, the room with the most meetings (preferring the smallest number in case of a tie) is returned.
