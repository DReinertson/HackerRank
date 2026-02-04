#
# Complete the 'maximizeNonOverlappingMeetings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY meetings as parameter.
#
# So essentially sorting is part of the question, so I can use that. Will need to use sorted() by index 1 of each nested array
# then loop through the meetings array, compare the end time of the previous meeting (index 1) to the current meeting's start_time. This is where I got mixed up, in the examples, it was showing that it only counted when those two values were equal to each other, but in reality, it's if the start time of the current meeting is greater than or equal to the previous meeting's end_time

def maximizeNonOverlappingMeetings(meetings):
    # Write your code here
    # print('meetings: ', meetings)
    sorted_meetings = sorted(meetings, key=lambda x: x[1])
    # print('sorted_meetings: ', sorted_meetings)
    maximum_meetings = 0
    
    for index, meeting in enumerate(sorted_meetings):
        if index == 0:
            maximum_meetings += 1
            end = meeting[1]
        
        elif meeting[0] >= end:
            maximum_meetings +=1
            end = meeting[1]
    
    return maximum_meetings
