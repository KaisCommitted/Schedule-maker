import random

def custom_round(a):
    if int(a) < a < int(a) + 1:
        return int(a) + 1
    else:
        return int(a)

def schedule_remote_days(people, mandatory_day):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    days_of_week.remove(mandatory_day)
    max_people_per_day = custom_round(len(people) * 2 / 4)
    days_assigned = {day: [] for day in days_of_week}
    people_randomized = random.sample(people, len(people))

    for person in people_randomized:
        assigned_days = 0
        for day in days_of_week:
            if len(days_assigned[day]) < max_people_per_day and person not in days_assigned[day]:
                days_assigned[day].append(person)
                assigned_days += 1
                if assigned_days == 2:
                    break
        if assigned_days < 2:
            break

    return days_assigned
