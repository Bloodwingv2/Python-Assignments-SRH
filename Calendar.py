# Exercise 1 – Calendar
# Data Structure: LIST

# Initial Thoughts:
# - Initially considered using sets and intersection logic to find common free gaps,
#   but this approach did not work effectively in practice. 

# Approach:
# - Merged both calendars to identify all gaps between existing meetings.
# - Subtracted these gaps to determine available meeting slots of the required duration.

# Additional Considerations:
# - Working hours for both users were not included at first; these were added later, when i realized my mistake.
#   The current solution provides all valid solutions for any input.

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

# ============ TIME COMPLEXITY ANALYSIS PER FUNCTION ============
# to_minutes():
# - Performs a constant number of string operations and arithmetic conversions.
# - No loops, no recursion, no additional data structures.
# Time Complexity: O(1)
# Space Complexity: O(1)

# to_hours():
# - Loops through the list of 'n' time-interval pairs.
# - Each iteration does constant-time arithmetic (division/modulo) and formatting.
# - Builds a new list of size 'n', so extra memory grows linearly with input.
# Time Complexity: O(n)
# Space Complexity: O(n)

# concatenate_calendars():
# - Creates a single combined list of all meetings (let total = n).
# - Loop runs once per meeting and converts each start/end using to_minutes(), which is O(1).
# - Memory also grows linearly because we store all converted intervals.
# Time Complexity: O(n)
# Space Complexity: O(n)

# sort():
# - Sorting the merged calendar is the heaviest operation in the entire pipeline.
# - Python’s Timsort runs in O(n log n) in the average and worst case.
# - Required to ensure merge_time() works correctly since it relies on sorted intervals.
# Time Complexity: O(n log n)
# Space Complexity: O(n) 

# merge_time():
# - Iterates once through the sorted list of meetings.
# - Each comparison and merge decision is constant time.
# - Produces a new list of merged intervals with a worst-case size of n.
# Time Complexity: O(n)
# Space Complexity: O(n)

# meeting_scheduler():
# - Runs a single pass through the merged calendar.
# - Checks gaps between adjacent meetings (n – 1 gaps total).
# - Appends valid slots into a result list, growing at most to O(n).
# Time Complexity: O(n)
# Space Complexity: O(n)


#============ OVERALL COMPLEXITY ANALYSIS ============
# The dominant term across all steps is the sorting operation.

# Therefore:
# Overall Time Complexity: O(n log n)
# - Everything else is linear, but as we are concatenating and BECAUSE of our algorithm design assuming the list is sorted
#   we must sort the merged calendar first.

# Overall Space Complexity: O(n)
# - We store multiple lists (merged, converted, merged-again, final gaps), all proportional to n.
# - No extra memory beyond linear usage.

#============ THOUGHT PROCESS ============
# Algorithm rundown:
# Basically we merge both calendars into one, sort them, merge overlapping meetings, and then find gaps that fit the meeting duration within overlapping working hours.
# to perform this we retain one element in another variable for comparison which is why concatenating the list proves very useful here and a condensed list helps us even more.

# Final Thoughts (not part of code):
# Regarding Python's slicing operation i have heard the operation itself creates a copy of the list could it impact a space of a list?
# The question itself is very interesting as i have solved questions regarding gaps before but i have never encountered a question where multiple stages are combined
# My first few minutes were spent scratching my head as the input was in a string format and i couldn't perform any conversions until i realised i had to convert them into minutes
