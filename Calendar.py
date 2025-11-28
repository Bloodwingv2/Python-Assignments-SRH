def to_minutes(time):
    """Converts time in String to minutes as int for comparisons"""
    parts = time.split(':')
    hours = int(parts[0])
    mins = int(parts[1])
    return hours * 60 + mins
    # Time Complexity: O(1) | Space Complexity: O(1)

def to_hours(time):
    """Converts time in minutes back to hours in string format"""
    meetings_in_hours = []
    for gaps in time:
        start, end = gaps[0], gaps[1]
        hours_1, mins_1 = start // 60, start % 60
        hours_2, mins_2 = end // 60, end % 60
        meetings_in_hours.append([f"{hours_1}:{mins_1:02d}", f"{hours_2}:{mins_2:02d}"])
    return meetings_in_hours
    # Time Complexity: O(n) | Space Complexity: O(n)

def concatenate_calendars(your_calendar, coworker_calendar):
    """Concatenate both calendars into one for processing"""
    merged_calendar = your_calendar + coworker_calendar
    converted = []
    for meeting in merged_calendar:
        start, end = meeting[0], meeting[1]
        converted.append([to_minutes(start), to_minutes(end)])
    return converted
    # Time Complexity: O(n) | Space Complexity: O(n)

def merge_time(time):
    """Merge overlapping time slots in the calendar"""
    if not time:
        return []
    compare_variable = [time[0]]
    for start, end in time[1:]:
        compare_END = compare_variable[-1][1]
        if start <= compare_END:
            compare_variable[-1][1] = max(compare_END, end)
        else:
            compare_variable.append([start, end])
    return compare_variable
    # Time Complexity: O(n) | Space Complexity: O(n)

def meeting_scheduler(time, your_hours, coworker_hours, meeting_duration):
    """Find available meeting slots considering both users' working hours"""
    overlap_start = max(to_minutes(your_hours[0]), to_minutes(coworker_hours[0]))
    overlap_end = min(to_minutes(your_hours[1]), to_minutes(coworker_hours[1]))
    
    meetings = []
    
    # Check gap before first meeting
    if time and time[0][0] - overlap_start >= meeting_duration:
        meetings.append([overlap_start, time[0][0]])
    
    # Check gaps between meetings
    for i in range(len(time) - 1):
        gap_start = time[i][1]
        gap_end = time[i + 1][0]
        if gap_end - gap_start >= meeting_duration:
            meetings.append([gap_start, gap_end])
    
    # Check gap after last meeting
    if time and overlap_end - time[-1][1] >= meeting_duration:
        meetings.append([time[-1][1], overlap_end])
    
    return meetings
    # Time Complexity: O(n) | Space Complexity: O(n)

# ============ MAIN EXECUTION ============
if __name__ == "__main__":
    your_calendar = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
    your_working_hours = ['9:00', '20:00']
    coworker_calendar = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
    coworker_working_hours = ['10:00', '18:30']
    meeting_duration = 30
    
    merged = concatenate_calendars(your_calendar, coworker_calendar)
    merged.sort()
    merged = merge_time(merged)
    available = meeting_scheduler(merged, your_working_hours, coworker_working_hours, meeting_duration)
    result = to_hours(available)
    print(result)

# ============ TIME COMPLEXITY ANALYSIS ============
# to_minutes():           O(1) - constant time operations
# to_hours():             O(n) - iterate through n meetings
# concatenate_calendars(): O(n) - iterate through n total meetings
# merge_time():           O(n) - iterate through n meetings
# meeting_scheduler():    O(n) - iterate through n meetings

#============ OVERALL COMPLEXITY ANALYSIS ============
# Overall:                O(n log n) - dominated by sort() operation in main execution but as we need a sorted list to mitgate the concatenation usage, it's necessary 
# Space Complexity:       O(n) - storing merged calendar