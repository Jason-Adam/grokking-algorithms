Hours_Needed = 24
Over_Time_Threshold = 8

Guard_Roster = {
    "Guard_1": 0,
    "Guard_2": 0,
    "Guard_3": 0,
    "Guard_4": 0,
    "Guard_5": 0,
    "Guard_6": 0,
}


def Schedule_Guards(graph, Hours_Needed):
    overtime_guards = []
    while (
        Hours_Needed > 0
    ):  # Here we check the completion condition. If we still have hours to schedule then
        for key, value in graph.items():  # For our guards in our roster
            while (
                value < Over_Time_Threshold and Hours_Needed > 0
            ):  # If they have regular hours left to work and if we need to schedule more hours
                value = value + 1  # Update our value to track our hours
                new_dict_value = {
                    key: value
                }  # variable to hold our updated dictionary value
                graph.update(new_dict_value)  # Update the hours worked by the guard
                Hours_Needed = Hours_Needed - 1  # Update our remaining scheduled ours
            else:
                if value >= 8:
                    overtime_guards.append(
                        key
                    )  # Add guard to our lis tof guards who have hit overtime
    else:  # If we have met the condition we return our schedule
        return graph


print(Schedule_Guards(Guard_Roster, Hours_Needed))


