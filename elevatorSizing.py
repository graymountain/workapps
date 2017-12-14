# This script performs traffic analysis for elevators

# Variables
n = 22  # Integer. Number of floors above terminal
cap = 8  # Integer. Lift capacity in terms of persons
ratedSpeed = 1.75  # Meters per second
avgFloorHeight = 3  # Meters
lifts = 3  # Number of lifts in a single group

# Assumptions
"""Average period of time required for a single passenger to enter
or leave the lift car in seconds.
"""
tp = 5

"""Time period measured from the instant that car
doors start to close until the doors are locked in seconds.
"""
tc = 5

"""Time period measured from the instant that car
doors start to open until they are open 800 mm in seconds."""
to = 5

"""Time period measured from the instant that car doors
are locked until the lift is level at the next adjacent floor in seconds"""
tf = 3

# Calculated Items
"""Where 5 is the number of occupants in a dwelling unit
including floating staff."""
occupants = 7
pop = (21 * 4 * occupants)

"""Average passengers carried"""
p = 0.8 * cap

"""Period of time required to transit two adjacent floors
at rated speed in seconds"""
tv = avgFloorHeight / ratedSpeed

"""Time period measured from the instant that car doors start
to close to the instant that the
car doors are open 800 mm at the
next adjacent floor in seconds"""
t = (tc + to) + tf


def elevatorSizing(n, cap, ratedSpeed,
                   avgFloorHeight, p, tv, t, tp, l, pop, className):
    """
    This function calculates;
    round trip time,
    waiting interval,
    and
    handling capacity
    """
    print("***********Variables & Assumptions***********")
    print("Number of floor above terminal are = {}".format(n))
    print("Elevator capacity in terms of persons is = {}".format(cap))
    print("Average elevator capacity " +
          " in terms of persons carried is = {}".format(p))
    print("Rated speed of elevator is = {} m/s".format(ratedSpeed))
    print("Average floor height is = {} meters".format(avgFloorHeight))
    print("Number of elevators in a single group are = {}".format(l))
    print("Average period of time required for a single passenger" +
          "to enter or leave the lift car is = {} seconds".format(tp))
    print("Population per towers is = {} persons".format(pop))
    print("Time period measured from the instant that" +
          "car doors start to close" +
          "until the doors are locked is = {} seconds".format(tc))
    print("Time period measured from the instant " +
          "that car doors start to open until " +
          " they are open 800 mm is = {} seconds".format(to))
    print("Time period measured from the instant that car doors " +
          "are locked until the lift is level at " +
          "the next adjacent floor is = {} seconds".format(tf))
    print("Time period required to transit " +
          "two adjacent floors " +
          "at rated speed is = {} seconds".format(round(tv, 2)))
    print("Time period measured from the" +
          "instant that car doors start to close" +
          "to the instant that the car" +
          "doors are open 800 mm at" +
          "the next adjacent floor is = {} seconds".format(t))

    print(" " * 2)
    print("***********Calculation Results***********")
    # Calculating average highest reversal floor
    total = 0
    for i in range(1, n):
        add = (i / n)**p
        total += add
    h = n - total  # Highest reversal floor
    print("Highest reversal floor is = {}".format(round(h, 2)))

    # Calculating average number of stop
    s = n * (1 - (1 - 1 / n)**p)
    print("Average number of stops is = {}".format(round(s, 2)))

    # Calculating RTT
    rtt = 2 * h * tv + (s + 1) * (t - tv) + 2 * p * tp
    print("The round trip time is = {} seconds".format(round(rtt, 2)))

    # Calculating INT
    interval = rtt / l
    print("The period between successive " +
          "car arrivals is = {} seconds".format(round(interval, 2)))

    # Calculating Handling capacity
    hc = (300 * p * l * (100 / pop)) / rtt
    print("Handling capacity for " +
          "this selection is = {} %".format(round(hc, 2)))


elevatorSizing(n, cap, ratedSpeed, avgFloorHeight,
               p, tv, t, tp, lifts, pop, "mid-end")
