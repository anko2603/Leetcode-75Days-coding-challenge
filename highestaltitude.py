# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
# Example 1:

# Input: gain = [-5,1,5,0,-7]
# Output: 1
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0  # Start with an initial altitude of 0
        current_altitude = 0

        for g in gain:
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude
        