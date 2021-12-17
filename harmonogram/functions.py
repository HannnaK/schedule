from math import ceil
from datetime import timedelta


def cutting_paper_before_printing_offset_fun(page, utility_converter, circulation, cutting_norm):
    cutting_paper_before_printing = page / utility_converter * circulation / cutting_norm
    return cutting_paper_before_printing


def cutting_paper_before_printing_digit_fun(page, utility_converter, circulation, cutting_norm):
    cutting_paper_before_printing = ceil(circulation / utility_converter * page / 2) / 2 / cutting_norm
    return cutting_paper_before_printing


def time_breaking_fun(page, utility_converter, circulation, breaking_norm):
    time_breaking = page / utility_converter * circulation / breaking_norm + 1
    return time_breaking


def number_paper_sheets_fun(printing_type, color, page, circulation, utility):
    if color == 0:
        number_paper_sheets = 0
    else:
        if printing_type == 1:
            number_paper_sheets = circulation / utility * page / 2
        else:
            number_paper_sheets = ceil(page / utility * circulation + 200 * page / utility)
    return number_paper_sheets


def sheets_fun(sheets_number, circulation):
    if sheets_number < 1:
        sheets = sheets_number * circulation
    else:
        sheets = circulation
    return sheets


def printing_performance_fun(color, sheets):
    if color == 0:
        printing_performance = 0
    elif color < 3:
        printing_performance = sheets / ((10 + (sheets / 7000) * 10 + (sheets / 13000) * 60) / 60)
    elif color < 5:
        printing_performance = sheets / ((25 + (sheets / 5000) * 10 + (sheets / 10000) * 60) / 60)
    else:
        printing_performance = sheets / ((25 + (sheets / 5000) * 10 + (sheets / 10000) * 60) / 60) / 2
    return printing_performance


def time_print_digit_fun(sheets_number, performance_standard_digit):
    partial_time_digit = sheets_number / performance_standard_digit
    return partial_time_digit


def time_print_offset_fun(page, circulation, sheets, performance, plates):
    time_print_offset = page * circulation * sheets / performance + 0.125 * plates
    return time_print_offset


def plates_number_cover_fun(cover, page, utility, color):
    if cover == 1:
        plates_number_cover = ceil(page / utility) * color
    else:
        plates_number_cover = ceil(page / utility) * color * 2
    return plates_number_cover


def plates_number_other_fun(page, utility, color):
    try:
        plates_number_other = ceil(page / utility) * color * 2
    except TypeError:
        plates_number_other = 0
    return plates_number_other


def conversion_to_time(number):
    number = round(number, 2)
    hours = (number * 60 // 60)
    minutes = 5 * round(ceil(((number - (number * 60 // 60)) * 60) / 5))
    delta = timedelta(minutes=minutes, hours=hours)
    return delta

