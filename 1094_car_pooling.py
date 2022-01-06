class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        capacity_remaining = capacity
        pick_ups = {}
        drop_offs = {}
        locations = []
        for passengers, start, end in trips:
            # determine the total number of passengers to be picked up at each location
            if start not in pick_ups:
                pick_ups[start] = passengers
            else:
                pick_ups[start] += passengers

            # determine the total number of passengers to be dropped off at each location
            if end not in drop_offs:
                drop_offs[end] = passengers
            else:
                drop_offs[end] += passengers

            locations.append([start, end])

        locations = sorted(set(sum(locations, [])))

        for location in locations:
            try:
                capacity_remaining -= pick_ups[location]
            except:
                pass
            try:
                capacity_remaining += drop_offs[location]
            except:
                pass
            if capacity_remaining < 0:
                return False
        return True