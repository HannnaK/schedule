from datetime import timedelta


def working_hours_on_a_schedule(start_data, working_hours, hours):
    number_of_days = (working_hours.days * 24 + working_hours.seconds / 3600) // hours
    number_of_houts = (working_hours.days * 24 + working_hours.seconds / 3600) % hours
    end_data = start_data + timedelta(days=number_of_days, hours=number_of_houts)
    if end_data.hour >= 21 and end_data.hour < 22:
        end_data = end_data + timedelta(hours=9)
    elif (int(start_data.hour) + number_of_houts) >= 21:
        end_data = end_data + timedelta(hours=9)
    return end_data


def select_employee(employee_bookbinder_1_work_hours, employee_bookbinder_1, employee_bookbinder_2_work_hours,
                    employee_bookbinder_2):
    if len(employee_bookbinder_1_work_hours) == 0:
        employee_bookbinder_1_work_hours.append(employee_bookbinder_1)
        return employee_bookbinder_1
    elif len(employee_bookbinder_2_work_hours) == 0:
        employee_bookbinder_2_work_hours.append(employee_bookbinder_2)
        return employee_bookbinder_2
    elif employee_bookbinder_1[1] <= employee_bookbinder_2[1]:
        employee_bookbinder_1_work_hours.append(employee_bookbinder_1)
        return employee_bookbinder_1
    else:
        employee_bookbinder_2_work_hours.append(employee_bookbinder_2)
        return employee_bookbinder_2


def next_data_fun(index, employee_work_hours_list):
    if index < (len(employee_work_hours_list) - 1):
        next_data = employee_work_hours_list[index + 1]
        return next_data


def when_employee_is_free(employee_work_hours, employee_work_hours_list, work_hours):
    if len(employee_work_hours_list) > 0:
        if employee_work_hours_list[-1][1] < employee_work_hours[1] and employee_work_hours_list[-1][1] > \
                employee_work_hours[0]:
            employee_work_hours[0] = employee_work_hours_list[-1][1]
            employee_work_hours[1] = working_hours_on_a_schedule(employee_work_hours[0], work_hours, 15)
            return employee_work_hours

        for index, data in enumerate(employee_work_hours_list):
            next_data = next_data_fun(index, employee_work_hours_list)
            previous_data = employee_work_hours_list[index - 1]

            if employee_work_hours[0] >= data[1] and next_data != None and employee_work_hours[1] <= next_data[0]:
                return employee_work_hours
            elif employee_work_hours[0] <= data[0] and (
                    working_hours_on_a_schedule(previous_data[1], work_hours, 15)) <= data[0]:

                employee_work_hours[0] = previous_data[1]
                employee_work_hours[1] = employee_work_hours[0] + work_hours
                return employee_work_hours
    return employee_work_hours


def selected_process_employee(employee_bookbinder_1_work_hours, employee_bookbinder_2_work_hours, selected_employee,
                              employee_work_hours):
    for data in employee_bookbinder_1_work_hours:
        if data == selected_employee:
            employee_bookbinder_1_work_hours.append(employee_work_hours)
            break
    for data in employee_bookbinder_2_work_hours:
        if data == selected_employee:
            employee_bookbinder_2_work_hours.append(employee_work_hours)
