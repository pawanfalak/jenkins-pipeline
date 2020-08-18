"""
Objective:
Find the minimum number of meeting rooms required in the office so that no meeting is delayed.
Input: two arrays which represent start and finish time of meetings,
Output: minimum number of conference rooms to be booked.
"""

def get_meeting_timeline(meeting_count):
    """
    Get start and finish time of all meetings provided number of meets
    """
    start_meet, end_meet = [], []
    for i in range(1, meeting_count+1):
        while True:
            start_time = int(input(f'Enter the start time of meeting {i}: '))
            end_time = int(input(f'Enter the end time of meeting {i}: '))
            if start_time >= end_time or start_time < 0 or start_time > 2359 or end_time < 0 or end_time > 2359:
                print('Please enter the valid start and end time for the meeting...')
            else:
                break
        start_meet.append(start_time)
        end_meet.append(end_time)
    return start_meet, end_meet

def find_meeting_timeline(begin_meet, end_meet, meeting_count):
    """
    find minimum meeting rooms required for all meetings
    """
    begin_meet.sort()
    end_meet.sort()
    room_needed = 1
    result = 1
    i = 1
    j = 0
    while (i < meeting_count and j < meeting_count):
        if begin_meet[i] <= end_meet[j]:
            room_needed += 1
            i += 1
        elif begin_meet[i] > end_meet[j]:
            room_needed -= 1
            j += 1
        if room_needed > result:
            result = room_needed
    return result

if __name__ == '__main__':
    total_meeting = int(input('Enter the number of meetings: '))
    get_begin_meet, get_end_meet = get_meeting_timeline(total_meeting)
    ROOMS = find_meeting_timeline(get_begin_meet, get_end_meet, total_meeting)
    print("Minimum Number of meeting rooms required: ", ROOMS)
