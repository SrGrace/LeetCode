class SeatManager:

    def __init__(self, n: int):
        self.available_seats = [i for i in range(1, n+1)]
        # heapq.heapify(self.available_seats)

    def reserve(self) -> int:
        seat_number = heapq.heappop(self.available_seats)
        return seat_number
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available_seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
