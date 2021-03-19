# hours pay
# work hours
# extra hours

class Paycheck:
    rate = int(input("What's your rate in hour?  "))
    print(rate)
    work_hours = int(input("How many hours you did last week? "))
    print(work_hours)
    extra_hours = int(input("How many extra hours you did last week? "))
    overtime_pay = extra_hours * 1.5
    total_hours = work_hours + overtime_pay
    print(total_hours)

    paycheck = int(rate) * total_hours
    print(paycheck)

    total_pay = paycheck
    print(total_pay)

def tax_calculation(self):
    if self.paycheck >= 600:
        tax = 0.18
    elif self.paycheck >= 1200:
        tax = 0.25
    else:
        tax = 1