# hours pay
# work hours
# extra hours


class Paycheck:
    rate = int(input("What's your rate in hour?  "))
    print(rate)
    work_hours = int(input("How many hours you did last week? "))
    print(work_hours)
    extra_hours = int(input("Did you work extra hours last week? "))
    total_hours = work_hours + extra_hours
    print(total_hours)

    paycheck = int(rate) * total_hours
    print(paycheck)