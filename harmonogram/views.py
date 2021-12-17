from django.shortcuts import render, get_object_or_404
from .models import TechnicalData
from .forms import TechnicalDataForm
from datetime import timedelta
from django.db.models import Min
from .function_views import working_hours_on_a_schedule, select_employee, when_employee_is_free, \
    selected_process_employee


def one_project(request, id):
    project = get_object_or_404(TechnicalData, pk=id)
    form_project = TechnicalDataForm(request.POST or None, request.FILES or None, instance=project)
    return render(request, 'project_form.html', {'form_project': form_project})


def technical_data(request):
    all_technical_data = TechnicalData.objects.all()
    return render(request, 'technical_data.html', {'technical_data': all_technical_data})


def time_for_project(request):
    all_technical_data = TechnicalData.objects.all()
    all_project_number = [data.project_number for data in all_technical_data]
    all_project_name = [data.project_name for data in all_technical_data]
    all_time_cutting_paper_before_printing = [data.time_cutting_paper_before_printing for data in all_technical_data]
    all_time_breaking = [data.time_breaking for data in all_technical_data]
    all_time_cover_alignment = [data.time_cover_alignment for data in all_technical_data]
    all_time_section_quire_alignment = [data.time_section_quire_alignment for data in all_technical_data]
    all_collection_time = [data.collection_time for data in all_technical_data]
    all_stapling_time = [data.stapling_time for data in all_technical_data]
    all_gluing_time = [data.gluing_time for data in all_technical_data]
    all_trimming_time = [data.trimming_time for data in all_technical_data]
    all_time_packing = [data.time_packing for data in all_technical_data]
    all_time_foil = [data.time_foil for data in all_technical_data]
    all_time_print_digit = [data.time_print_digit for data in all_technical_data]
    all_time_print_offset = [data.time_print_offset for data in all_technical_data]
    all_time_exposure = [data.time_exposure for data in all_technical_data]

    all_time_for_project = [(
            data.time_exposure + data.time_cutting_paper_before_printing + data.time_print_offset + data.time_print_digit + data.time_foil + data.time_breaking + data.collection_time + data.time_cover_alignment + data.time_section_quire_alignment + data.gluing_time + data.trimming_time + data.stapling_time + data.time_packing)
        for data in all_technical_data]

    context = {'project_number': all_project_number,
               'project_name': all_project_name,
               'all_time_cutting_paper_before_printing': all_time_cutting_paper_before_printing,
               'all_time_breaking': all_time_breaking,
               'all_time_cover_alignment': all_time_cover_alignment,
               'all_time_section_quire_alignment': all_time_section_quire_alignment,
               'all_collection_time': all_collection_time,
               'all_stapling_time': all_stapling_time,
               'all_gluing_time': all_gluing_time,
               'all_trimming_time': all_trimming_time,
               'all_time_packing': all_time_packing,
               'all_time_foil': all_time_foil,
               'all_time_print_digit': all_time_print_digit,
               'all_time_print_offset': all_time_print_offset,
               'all_time_exposure': all_time_exposure,
               'all_time_for_project': all_time_for_project
               }

    return render(request, 'time_for_project.html', context)


def schedule(request):
    all_technical_data = TechnicalData.objects.order_by('date_to_be_printed')
    all_project_number = [data.project_number for data in all_technical_data]
    all_project_name = [data.project_name for data in all_technical_data]
    all_project_circulation = [data.circulation for data in all_technical_data]
    all_pages_number = [data.pages_number for data in all_technical_data]
    all_project_paper_size = [data.paper_size for data in all_technical_data]
    all_project_binding = [data.get_binding_display() for data in all_technical_data]
    all_project_printing_type = [data.get_printing_type_display() for data in all_technical_data]
    all_time_exposure = [data.time_exposure for data in all_technical_data]
    all_time_print_digit = [data.time_print_digit for data in all_technical_data]
    all_time_print_offset = [data.time_print_offset for data in all_technical_data]
    all_time_bindery = []
    all_time_start = [data.date_to_be_printed for data in all_technical_data]
    all_time_end_proces = []

    for data in all_technical_data:
        time_bindery = data.time_cutting_paper_before_printing + data.time_foil + data.time_breaking + data.collection_time + data.time_cover_alignment + data.time_section_quire_alignment + data.gluing_time + data.trimming_time + data.stapling_time + data.time_packing
        all_time_bindery.append(time_bindery)

    all_time_for_project = [(
            data.time_exposure + data.time_cutting_paper_before_printing + data.time_print_offset + data.time_print_digit + data.time_foil + data.time_breaking + data.collection_time + data.time_cover_alignment + data.time_section_quire_alignment + data.gluing_time + data.trimming_time + data.stapling_time + data.time_packing)
        for data in all_technical_data]

    date_start_digit = TechnicalData.objects.aggregate(Min('date_to_be_printed'))['date_to_be_printed__min']
    date_start_offset = TechnicalData.objects.aggregate(Min('date_to_be_printed'))['date_to_be_printed__min']
    date_start_platesetter = TechnicalData.objects.aggregate(Min('date_to_be_printed'))['date_to_be_printed__min']
    date_start_employee_printer = TechnicalData.objects.aggregate(Min('date_to_be_printed'))['date_to_be_printed__min']
    date_start_cutting_paper = TechnicalData.objects.aggregate(Min('date_to_be_printed'))['date_to_be_printed__min']
    date_start_foil = TechnicalData.objects.aggregate(Min('date_to_be_printed'))['date_to_be_printed__min']
    date_start_breaking = TechnicalData.objects.aggregate(Min('date_to_be_printed'))['date_to_be_printed__min']
    date_start_collection = TechnicalData.objects.aggregate(Min('date_to_be_printed'))['date_to_be_printed__min']
    date_start_cover_alignment = TechnicalData.objects.aggregate(Min('date_to_be_printed'))['date_to_be_printed__min']
    date_start_section_quire_alignment = TechnicalData.objects.aggregate(Min('date_to_be_printed'))[
        'date_to_be_printed__min']
    date_start_gluing = TechnicalData.objects.aggregate(Min('date_to_be_printed'))['date_to_be_printed__min']
    date_start_trimming = TechnicalData.objects.aggregate(Min('date_to_be_printed'))['date_to_be_printed__min']
    date_start_stapling = TechnicalData.objects.aggregate(Min('date_to_be_printed'))['date_to_be_printed__min']
    date_start_packing = TechnicalData.objects.aggregate(Min('date_to_be_printed'))['date_to_be_printed__min']
    date_end_digit = 0
    date_end_offset = 0
    employee_bookbinder_1_work_hours = []
    employee_bookbinder_2_work_hours = []

    for data in all_technical_data:

        if data.date_to_be_printed > date_start_cutting_paper:
            date_start_cutting_paper = data.date_to_be_printed

        employee_work_hours_before_printing_1 = []
        employee_work_hours_before_printing_2 = []
        employee_work_hours_before_printing_1.append(date_start_cutting_paper)
        employee_work_hours_before_printing_2.append(date_start_cutting_paper)

        date_start_cutting_paper = working_hours_on_a_schedule(date_start_cutting_paper,
                                                               data.time_cutting_paper_before_printing,
                                                               15)
        employee_work_hours_before_printing_1.append(date_start_cutting_paper)
        employee_work_hours_before_printing_2.append(date_start_cutting_paper)
        work_hours = timedelta(seconds=data.time_cutting_paper_before_printing.total_seconds())

        employee_bookbinder_1 = when_employee_is_free(employee_work_hours_before_printing_1,
                                                      employee_bookbinder_1_work_hours, work_hours)
        employee_bookbinder_2 = when_employee_is_free(employee_work_hours_before_printing_2,
                                                      employee_bookbinder_2_work_hours, work_hours)

        employee_bookbinder_1_work_hours = sorted(employee_bookbinder_1_work_hours)
        employee_bookbinder_2_work_hours = sorted(employee_bookbinder_2_work_hours)

        selected_employee = select_employee(employee_bookbinder_1_work_hours, employee_bookbinder_1,
                                            employee_bookbinder_2_work_hours,
                                            employee_bookbinder_2)

        date_start_real = selected_employee[1]

        if data.printing_type == 1:
            if date_start_real < date_start_digit:
                date_start_real = date_start_digit
            if date_start_real < date_start_employee_printer:
                date_start_real = date_start_employee_printer

            date_start_employee_printer = working_hours_on_a_schedule(date_start_real,
                                                                      timedelta(minutes=30), 15)

            date_start_digit = working_hours_on_a_schedule(date_start_real, data.time_print_digit, 15)

            date_end_digit = date_start_digit

        else:

            if date_start_real < date_start_platesetter:
                date_start_real = date_start_platesetter

            if date_start_real < date_start_employee_printer:
                date_start_real = date_start_employee_printer

            date_start_employee_printer = working_hours_on_a_schedule(date_start_real, timedelta(minutes=30), 15)
            date_start_platesetter = working_hours_on_a_schedule(date_start_real, data.time_exposure, 15)
            date_start_real = date_start_platesetter

            if date_start_real < date_start_offset:
                date_start_real = date_start_offset

            if date_start_real < date_start_employee_printer:
                date_start_real = date_start_employee_printer

            if data.circulation < 1000:
                date_start_employee_printer = working_hours_on_a_schedule(date_start_real, data.time_print_offset, 15)
            else:
                date_start_employee_printer = working_hours_on_a_schedule(date_start_real, timedelta(minutes=60), 15)

            date_start_offset = working_hours_on_a_schedule(date_start_real, data.time_print_offset, 15)

            date_start_real = date_start_employee_printer

            date_end_offset = date_start_offset

        if data.printing_type == 1:
            date_start_real = date_end_digit
        else:
            date_start_real = date_end_offset

        # date_start_foil
        if date_start_real < date_start_foil:
            date_start_real = date_start_foil

        employee_work_hours_foil_1 = []
        employee_work_hours_foil_2 = []
        employee_work_hours_foil_1.append(date_start_real)
        employee_work_hours_foil_2.append(date_start_real)

        date_start_foil = working_hours_on_a_schedule(date_start_real, data.time_foil, 15)
        date_start_real = working_hours_on_a_schedule(date_start_real, data.time_foil, 15)

        employee_work_hours_foil_1.append(date_start_real)
        employee_work_hours_foil_2.append(date_start_real)

        work_hours = timedelta(seconds=data.time_foil.total_seconds())

        employee_bookbinder_1 = when_employee_is_free(employee_work_hours_foil_1,
                                                      employee_bookbinder_1_work_hours,
                                                      work_hours)

        employee_bookbinder_2 = when_employee_is_free(employee_work_hours_foil_2,
                                                      employee_bookbinder_2_work_hours,
                                                      work_hours)

        employee_bookbinder_1_work_hours = sorted(employee_bookbinder_1_work_hours)
        employee_bookbinder_2_work_hours = sorted(employee_bookbinder_2_work_hours)

        selected_employee = select_employee(employee_bookbinder_1_work_hours, employee_bookbinder_1,
                                            employee_bookbinder_2_work_hours,
                                            employee_bookbinder_2)

        date_start_real = selected_employee[1]

        # date_start_breaking
        if data.printing_type == 2 and data.binding == 2:

            if data.date_to_be_printed < date_start_breaking:
                date_start_real = date_start_breaking

            employee_work_hours_breaking = []
            employee_work_hours_breaking.append(date_start_real)

            date_start_breaking = working_hours_on_a_schedule(date_start_real, data.time_breaking, 15)
            date_start_real = working_hours_on_a_schedule(date_start_real, data.time_breaking, 15)

            employee_work_hours_breaking.append(date_start_real)

            employee_bookbinder_1_work_hours = sorted(employee_bookbinder_1_work_hours)
            employee_bookbinder_2_work_hours = sorted(employee_bookbinder_2_work_hours)

            selected_process_employee(employee_bookbinder_1_work_hours, employee_bookbinder_2_work_hours,
                                      selected_employee, employee_work_hours_breaking)

        # date_start_collection
        if data.printing_type == 2:
            if date_start_real < date_start_collection:
                date_start_real = date_start_collection

            employee_work_hours_collection = []
            employee_work_hours_collection.append(date_start_real)

            date_start_collection = working_hours_on_a_schedule(date_start_real, data.collection_time, 15)
            date_start_real = working_hours_on_a_schedule(date_start_real, data.collection_time, 15)

            employee_work_hours_collection.append(date_start_real)

            employee_bookbinder_1_work_hours = sorted(employee_bookbinder_1_work_hours)
            employee_bookbinder_2_work_hours = sorted(employee_bookbinder_2_work_hours)

            selected_process_employee(employee_bookbinder_1_work_hours, employee_bookbinder_2_work_hours,
                                      selected_employee, employee_work_hours_collection)

        # date_start_cover_alignment
        if data.printing_type == 1 or (
                data.printing_type == 2 and (data.binding == 3 or data.binding == 4 or data.binding == 5)):

            if date_start_real < date_start_cover_alignment:
                date_start_real = date_start_cover_alignment

            employee_work_hours_cover_alignment = []
            employee_work_hours_cover_alignment.append(date_start_real)

            date_start_cover_alignment = working_hours_on_a_schedule(date_start_real, data.time_cover_alignment, 15)
            date_start_real = working_hours_on_a_schedule(date_start_real, data.time_cover_alignment, 15)

            employee_work_hours_cover_alignment.append(date_start_real)

            employee_bookbinder_1_work_hours = sorted(employee_bookbinder_1_work_hours)
            employee_bookbinder_2_work_hours = sorted(employee_bookbinder_2_work_hours)

            selected_process_employee(employee_bookbinder_1_work_hours, employee_bookbinder_2_work_hours,
                                      selected_employee, employee_work_hours_cover_alignment)

        # date_start_section_quire_alignment
        if date_start_real < date_start_section_quire_alignment:
            date_start_real = date_start_section_quire_alignment

        employee_work_hours_section_quire_alignment = []
        employee_work_hours_section_quire_alignment.append(date_start_real)

        date_start_section_quire_alignment = working_hours_on_a_schedule(date_start_real,
                                                                         data.time_section_quire_alignment, 15)
        date_start_real = working_hours_on_a_schedule(date_start_real, data.time_section_quire_alignment, 15)

        employee_work_hours_section_quire_alignment.append(date_start_real)

        employee_bookbinder_1_work_hours = sorted(employee_bookbinder_1_work_hours)
        employee_bookbinder_2_work_hours = sorted(employee_bookbinder_2_work_hours)

        selected_process_employee(employee_bookbinder_1_work_hours, employee_bookbinder_2_work_hours, selected_employee,
                                  employee_work_hours_section_quire_alignment)

        if data.binding == 2:

            # date_start_gluing
            if date_start_real < date_start_gluing:
                date_start_real = date_start_gluing

            employee_work_hours_gluing = []
            employee_work_hours_gluing.append(date_start_real)

            date_start_gluing = working_hours_on_a_schedule(date_start_real, data.gluing_time, 15)
            date_start_real = working_hours_on_a_schedule(date_start_real, data.gluing_time, 15)

            employee_work_hours_gluing.append(date_start_real)

            employee_bookbinder_1_work_hours = sorted(employee_bookbinder_1_work_hours)
            employee_bookbinder_2_work_hours = sorted(employee_bookbinder_2_work_hours)

            selected_process_employee(employee_bookbinder_1_work_hours, employee_bookbinder_2_work_hours,
                                      selected_employee, employee_work_hours_gluing)

            # date_start_trimming
            if date_start_real < date_start_trimming:
                date_start_real = date_start_trimming

            employee_work_hours_trimming = []
            employee_work_hours_trimming.append(date_start_real)

            date_start_trimming = working_hours_on_a_schedule(date_start_real, data.trimming_time, 15)
            date_start_real = working_hours_on_a_schedule(date_start_real, data.trimming_time, 15)

            employee_work_hours_trimming.append(date_start_real)

            employee_bookbinder_1_work_hours = sorted(employee_bookbinder_1_work_hours)
            employee_bookbinder_2_work_hours = sorted(employee_bookbinder_2_work_hours)

            selected_process_employee(employee_bookbinder_1_work_hours, employee_bookbinder_2_work_hours,
                                      selected_employee, employee_work_hours_trimming)


        elif data.binding == 3 or data.binding == 4 or data.binding == 5:

            # date_start_stapling
            if date_start_real < date_start_stapling:
                date_start_real = date_start_stapling

            employee_work_hours_stapling = []
            employee_work_hours_stapling.append(date_start_real)

            date_start_stapling = working_hours_on_a_schedule(date_start_real, data.stapling_time, 15)
            date_start_real = working_hours_on_a_schedule(date_start_real, data.stapling_time, 15)

            employee_work_hours_stapling.append(date_start_real)

            employee_bookbinder_1_work_hours = sorted(employee_bookbinder_1_work_hours)
            employee_bookbinder_2_work_hours = sorted(employee_bookbinder_2_work_hours)

            selected_process_employee(employee_bookbinder_1_work_hours, employee_bookbinder_2_work_hours,
                                      selected_employee, employee_work_hours_stapling)

        # date_start_packing
        if date_start_real < date_start_packing:
            date_start_real = date_start_packing

        employee_work_hours_packing = []
        employee_work_hours_packing.append(date_start_real)

        date_start_packing = working_hours_on_a_schedule(date_start_real, data.time_packing, 15)
        date_start_real = working_hours_on_a_schedule(date_start_real, data.time_packing, 15)

        employee_work_hours_packing.append(date_start_real)

        employee_bookbinder_1_work_hours = sorted(employee_bookbinder_1_work_hours)
        employee_bookbinder_2_work_hours = sorted(employee_bookbinder_2_work_hours)

        selected_process_employee(employee_bookbinder_1_work_hours, employee_bookbinder_2_work_hours, selected_employee,
                                  employee_work_hours_packing)

        time_end_process = date_start_real
        all_time_end_proces.append(time_end_process)

    context = {'all_project_number': all_project_number,
               'all_project_name': all_project_name,
               'all_project_circulation': all_project_circulation,
               'all_pages_number': all_pages_number,
               'all_project_paper_size': all_project_paper_size,
               'all_project_binding': all_project_binding,
               'all_project_printing_type': all_project_printing_type,
               'all_time_exposure': all_time_exposure,
               'all_time_print_offset': all_time_print_offset,
               'all_time_print_digit': all_time_print_digit,
               'all_time_bindery': all_time_bindery,
               'all_time_start': all_time_start,
               'all_time_for_project': all_time_for_project,
               'all_time_end_proces': all_time_end_proces
               }
    return render(request, 'schedule.html', context)