from django.db import models
from .functions import cutting_paper_before_printing_offset_fun, cutting_paper_before_printing_digit_fun, \
    time_breaking_fun, number_paper_sheets_fun, sheets_fun, \
    printing_performance_fun, time_print_digit_fun, time_print_offset_fun, plates_number_cover_fun, \
    plates_number_other_fun, conversion_to_time

PAPER = [('A3', 'A3 (297 x 420)'), ('A4', 'A4 (210 x 297)'), ('A5', 'A5 (148 x 210)'), ('A6', 'A6 (105 x 148)'),
         ('5', '100 x 200'), ('6', '110 x 190'), ('7', '115 x 200'), ('8', '156 x 232'), ('9', '164 x 238')]
PAPER_TYPE = [(1, 'offset 80'), (2, 'kreda 90'), (3, 'kreda 115'), (4, 'kreda 135'),
              (5, 'kreda 170'), (6, 'kreda 200'), (7, 'kreda 250'), (8, 'kreda 300'),
              (9, 'karton 240'), (10, 'karton 300')]
BINDING_TYPE = [(1, 'brak'), (2, 'klejenie'), (3, 'szycie drutem oczkowym'),
                (4, 'szycie drutem zeszyt'), (5, 'szycie nićmi'), (6, 'spiralowanie')]
COLLECTING_TYPE = [(1, 'ręczne'), (2, 'maszynowe-krokodyl'), (3, 'pojedyńcze kartki')]

PACKING_TYPE = [(1, 'brak'), (2, 'pojedyńcze w folię'), (3, 'pojedyńcze w folię z wrzutką'),
                (4, 'folia do 20 sztuk'), (5, 'folia do 50 sztuk'), (6, 'folia do 100 sztuk'),
                (7, 'papier do 5 sztuk'), (8, 'papier do 10 sztuk'), (9, 'papier do 20 sztuk'),
                (10, 'papier do 50 sztuk'), (11, 'papier do 100 sztuk')]


def utility_converter_for_peper_size_offset_fun(paper_size):
    utility_converter_for_peper_size_offset = UtilityConverterOffset.objects.get(paper_size=paper_size).cover_pages
    return utility_converter_for_peper_size_offset


def utility_converter_for_peper_size_inside_offset_fun(paper_size):
    utility_converter_for_peper_size_inside_offset = UtilityConverterOffset.objects.get(
        paper_size=paper_size).inside_pages
    return utility_converter_for_peper_size_inside_offset


def utility_converter_for_peper_size_digit_fun(paper_size):
    utility_converter_for_peper_size_digit = UtilityConverterDigit.objects.get(paper_size=paper_size).pages
    return utility_converter_for_peper_size_digit


def performance_standard_fun(page, paper):
    if page == 1:
        performance_standard_digit = PerformanceStandardDigit.objects.get(paper=paper).color_1
    else:
        performance_standard_digit = PerformanceStandardDigit.objects.get(paper=paper).other_color
    return performance_standard_digit


class UtilityConverterOffset(models.Model):
    paper_size = models.CharField(max_length=20, choices=PAPER)
    cover_pages = models.IntegerField()
    inside_pages = models.IntegerField()


class UtilityConverterDigit(models.Model):
    paper_size = models.CharField(max_length=20, choices=PAPER)
    pages = models.IntegerField()


class Cut(models.Model):
    grammage = models.IntegerField(choices=PAPER_TYPE)
    sheets_number = models.IntegerField()


class Breaking(models.Model):
    paper_size = models.CharField(max_length=20, choices=PAPER)
    breaks_number = models.IntegerField()
    offset_80_chalk_90_200_cardboard_240 = models.IntegerField()
    cardboard_300_chalk_250_300 = models.IntegerField()


class Collecting(models.Model):
    name = models.IntegerField(choices=COLLECTING_TYPE)
    norm = models.IntegerField()


class AligningNorm(models.Model):
    ALIGNING_NAME = [(1, 'Obrównywanie okładek na netto'), (2, 'Obrównywanie składek na netto')]

    name = models.IntegerField(choices=ALIGNING_NAME)
    norm = models.IntegerField()


class JoiningNorm(models.Model):
    JOINING_NORM = [(3, 'szycie drutem oczkowym'), (4, 'szycie drutem zeszyt')]

    name = models.IntegerField(choices=JOINING_NORM)
    norm = models.IntegerField()


class GluingNorm(models.Model):
    pages_sum = models.IntegerField()
    norm = models.IntegerField()


class TrimmingNorm(models.Model):
    binding = models.IntegerField(choices=BINDING_TYPE)
    max_limit_pages_20 = models.IntegerField()
    max_limit_pages_30 = models.IntegerField()
    max_limit_pages_60 = models.IntegerField()
    max_limit_pages_100 = models.IntegerField()
    max_limit_pages_300 = models.IntegerField()
    max_limit_pages_700 = models.IntegerField()
    max_limit_pages_1100 = models.IntegerField()


class PackingNorm(models.Model):
    name = models.IntegerField(choices=PACKING_TYPE)
    norm = models.IntegerField()


class PerformanceStandardDigit(models.Model):
    paper = models.IntegerField(choices=PAPER_TYPE)
    color_1 = models.IntegerField()
    other_color = models.IntegerField()


class TechnicalData(models.Model):
    TRIMMING_TYPE = [(1, 'brak'), (2, 'trójnóż'), (3, 'gilotyna')]
    FOIL_TYPE = [(1, 'brak'), (2, 'mat'), (3, 'błysk'), (4, 'satyna'), (5, 'mat-2 str'), (6, 'błysk-2 str')]

    project_number = models.CharField(max_length=20)
    project_name = models.CharField(max_length=80)
    date_to_be_printed = models.DateTimeField()
    date_to_customer = models.DateField()
    printing_type = models.IntegerField(choices=[(1, 'cyfra'), (2, 'offset')])
    circulation = models.IntegerField()
    paper_size = models.CharField(max_length=20, choices=PAPER, default='A4')
    binding = models.IntegerField(choices=BINDING_TYPE, default=2)
    collecting = models.IntegerField(choices=COLLECTING_TYPE, default=1)
    trimming = models.IntegerField(choices=TRIMMING_TYPE, default=2)
    packing = models.IntegerField(choices=PACKING_TYPE, default=9)
    foil = models.IntegerField(choices=FOIL_TYPE, default=3)
    manual_work = models.IntegerField(default='1')
    cover = models.IntegerField(choices=[(1, 'okładka 1 stronna'), (2, 'okładka 2 stronna')])
    cover_color = models.IntegerField(default=4)
    inside_color = models.IntegerField(default=0)
    insole_color = models.IntegerField(default=0)
    cover_page = models.IntegerField(default=4)
    inside_page = models.IntegerField(default=0)
    insole_page = models.IntegerField(default=0)
    cover_paper = models.IntegerField(choices=PAPER_TYPE, default=7)
    inside_paper = models.IntegerField(choices=PAPER_TYPE, default=3, blank=True, null=True)
    insole_paper = models.IntegerField(choices=PAPER_TYPE, blank=True, null=True)

    @property
    # time_cutting_paper_before_printing
    def time_cutting_paper_before_printing(self):
        utility_converter_for_peper_size_offset = utility_converter_for_peper_size_offset_fun(self.paper_size)
        utility_converter_for_peper_size_inside_offset = utility_converter_for_peper_size_inside_offset_fun(
            self.paper_size)
        utility_converter_for_peper_size_digit = utility_converter_for_peper_size_digit_fun(self.paper_size)

        if self.printing_type == 2 and self.cover_paper is not None:
            cutting_norm_for_given_grammage_cover = Cut.objects.get(grammage=self.cover_paper).sheets_number
            time_cutting_paper_before_printing_cover = cutting_paper_before_printing_offset_fun(self.cover_page,
                                                                                                utility_converter_for_peper_size_offset,
                                                                                                self.circulation,
                                                                                                cutting_norm_for_given_grammage_cover)

        elif self.printing_type == 1 and self.cover_paper is not None:
            cutting_norm_for_given_grammage_cover = Cut.objects.get(grammage=self.cover_paper).sheets_number
            time_cutting_paper_before_printing_cover = cutting_paper_before_printing_digit_fun(self.cover_page,
                                                                                               utility_converter_for_peper_size_digit,
                                                                                               self.circulation,
                                                                                               cutting_norm_for_given_grammage_cover)

        else:
            time_cutting_paper_before_printing_cover = 0

        if self.printing_type == 2 and self.inside_paper is not None:
            cutting_norm_for_given_grammage_inside = Cut.objects.get(grammage=self.inside_paper).sheets_number
            time_cutting_paper_before_printing_inside = cutting_paper_before_printing_offset_fun(self.inside_page,
                                                                                                 utility_converter_for_peper_size_inside_offset,
                                                                                                 self.circulation,
                                                                                                 cutting_norm_for_given_grammage_inside)

        elif self.printing_type == 1 and self.inside_paper is not None:
            cutting_norm_for_given_grammage_inside = Cut.objects.get(grammage=self.inside_paper).sheets_number
            time_cutting_paper_before_printing_inside = cutting_paper_before_printing_digit_fun(self.inside_page,
                                                                                                utility_converter_for_peper_size_digit,
                                                                                                self.circulation,
                                                                                                cutting_norm_for_given_grammage_inside)

        else:
            time_cutting_paper_before_printing_inside = 0

        if self.printing_type == 2 and self.insole_paper is not None:
            cutting_norm_for_given_grammage_insole = Cut.objects.get(grammage=self.insole_paper).sheets_number
            time_cutting_paper_before_printing_insole = cutting_paper_before_printing_offset_fun(self.insole_page,
                                                                                                 utility_converter_for_peper_size_inside_offset,
                                                                                                 self.circulation,
                                                                                                 cutting_norm_for_given_grammage_insole)
        elif self.printing_type == 1 and self.insole_paper is not None:
            cutting_norm_for_given_grammage_insole = Cut.objects.get(grammage=self.insole_paper).sheets_number
            time_cutting_paper_before_printing_insole = cutting_paper_before_printing_digit_fun(self.insole_page,
                                                                                                utility_converter_for_peper_size_digit,
                                                                                                self.circulation,
                                                                                                cutting_norm_for_given_grammage_insole)

        else:
            time_cutting_paper_before_printing_insole = 0

        if self.printing_type == 2:
            time_cutting_paper_before_printing = time_cutting_paper_before_printing_cover + time_cutting_paper_before_printing_inside + time_cutting_paper_before_printing_insole + 0.5
        else:

            time_cutting_paper_before_printing = time_cutting_paper_before_printing_cover + time_cutting_paper_before_printing_inside + time_cutting_paper_before_printing_insole + 0.25

        return conversion_to_time(time_cutting_paper_before_printing)

    @property
    # all_time_breaking
    def time_breaking(self):

        if self.collecting == 3 or self.inside_paper is None:
            time_breaking = 0

        elif self.printing_type == 2 and self.binding == 2:

            paper_size = Breaking.objects.get(paper_size=self.paper_size)

            if self.inside_paper == 7 or self.inside_paper == 8 or self.inside_paper == 10:
                breaking_norm_inside = paper_size.cardboard_300_chalk_250_300

            else:
                breaking_norm_inside = paper_size.offset_80_chalk_90_200_cardboard_240

            if self.insole_paper is None:
                breaking_norm_insole = 1
            elif int(self.insole_paper) == 7 or int(self.insole_paper) == 8 or int(self.insole_paper) == 10:
                breaking_norm_insole = paper_size.cardboard_300_chalk_250_300
            else:
                breaking_norm_insole = paper_size.offset_80_chalk_90_200_cardboard_240

            utility_converter_for_peper_size_inside_offset = utility_converter_for_peper_size_inside_offset_fun(
                self.paper_size)

            if self.inside_page != 0:
                time_breaking_inside = time_breaking_fun(self.inside_page,
                                                         utility_converter_for_peper_size_inside_offset,
                                                         self.circulation, breaking_norm_inside)
            else:
                time_breaking_inside = 0
            if self.insole_page != 0:
                time_breaking_insole = time_breaking_fun(self.insole_page,
                                                         utility_converter_for_peper_size_inside_offset,
                                                         self.circulation, breaking_norm_insole)
            else:
                time_breaking_insole = 0

            time_breaking = time_breaking_inside + time_breaking_insole

        else:
            time_breaking = 0

        return conversion_to_time(time_breaking)

    @property
    # all_time_cover_alignment
    def time_cover_alignment(self):
        aligning_norm_cover = AligningNorm.objects.get(name=1)

        utility_converter_for_peper_size_offset = utility_converter_for_peper_size_offset_fun(self.paper_size)
        utility_converter_for_peper_size_digit = utility_converter_for_peper_size_digit_fun(self.paper_size)

        if self.printing_type == 1:
            time_cover_alignment = self.circulation / utility_converter_for_peper_size_digit * self.cover_page / 2 / aligning_norm_cover.norm + 0.25

        elif (self.binding == 3 or self.binding == 4) and self.printing_type == 2:

            number_paper_sheets_cover = number_paper_sheets_fun(self.printing_type, self.cover_color, self.cover_page,
                                                                self.circulation,
                                                                utility_converter_for_peper_size_offset)
            time_cover_alignment = number_paper_sheets_cover / aligning_norm_cover.norm + 0.5
        else:
            time_cover_alignment = 0

        return conversion_to_time(time_cover_alignment)

    @property
    # all_time_section_quire_alignment
    def time_section_quire_alignment(self):
        utility_converter_for_peper_size_inside_offset = utility_converter_for_peper_size_inside_offset_fun(
            self.paper_size)
        utility_converter_for_peper_size_offset = utility_converter_for_peper_size_offset_fun(self.paper_size)
        utility_converter_for_peper_size_digit = utility_converter_for_peper_size_digit_fun(self.paper_size)

        aligning_norm_cover = AligningNorm.objects.get(name=1)
        aligning_norm_section_quire = AligningNorm.objects.get(name=2)

        if self.printing_type == 1:
            number_paper_sheets_cover = number_paper_sheets_fun(self.printing_type, self.cover_color, self.cover_page,
                                                                self.circulation,
                                                                utility_converter_for_peper_size_digit)
            number_paper_sheets_inside = number_paper_sheets_fun(self.printing_type, self.inside_color,
                                                                 self.inside_page, self.circulation,
                                                                 utility_converter_for_peper_size_digit)
            number_paper_sheets_insole = number_paper_sheets_fun(self.printing_type, self.insole_color,
                                                                 self.insole_page, self.circulation,
                                                                 utility_converter_for_peper_size_digit)

            time_section_quire_alignment = (
                                                   number_paper_sheets_cover + number_paper_sheets_inside + number_paper_sheets_insole) / aligning_norm_section_quire.norm + 0.25


        elif self.binding == 2 and self.printing_type == 2:
            time_section_quire_alignment = self.cover_page / utility_converter_for_peper_size_offset * self.circulation / aligning_norm_cover.norm + 0.5

        elif (self.binding == 3 or self.binding == 4) and self.printing_type == 2:

            time_section_quire_alignment = (
                                                   self.inside_page + self.insole_page) / utility_converter_for_peper_size_inside_offset * self.circulation / aligning_norm_cover.norm + self.cover_page / utility_converter_for_peper_size_offset * self.circulation / aligning_norm_section_quire.norm + 0.5
        else:
            time_section_quire_alignment = 0

        return conversion_to_time(time_section_quire_alignment)

    @property
    # all_collection_time
    def collection_time(self):
        utility_converter_for_peper_size_offset = utility_converter_for_peper_size_offset_fun(self.paper_size)
        if self.inside_color == 0 or self.printing_type == 1:
            collection_time = 0
        else:
            collecting_norm = Collecting.objects.get(name=self.collecting)
            collection_time = ((
                                       self.inside_page + self.insole_page) / utility_converter_for_peper_size_offset * self.circulation) / collecting_norm.norm

        return conversion_to_time(collection_time)

    @property
    # all_stapling_time
    def stapling_time(self):

        if self.binding == 3 or self.binding == 4:
            joining_norm = JoiningNorm.objects.get(name=self.binding)

            stapling_time = self.circulation / joining_norm.norm + 0.5
            stapling_time = round(stapling_time, 2)
        else:
            stapling_time = 0

        return conversion_to_time(stapling_time)

    @property
    # all_gluing_time
    def gluing_time(self):
        pages_number = self.cover_page + self.inside_page + self.insole_page
        if self.binding != 2:
            gluing_time = 0
        else:
            if pages_number <= 200:
                gluing_time = self.circulation / GluingNorm.objects.get(pages_sum=200).norm + 0.5
            elif pages_number <= 250:
                gluing_time = self.circulation / GluingNorm.objects.get(pages_sum=250).norm + 0.5
            elif pages_number <= 300:
                gluing_time = self.circulation / GluingNorm.objects.get(pages_sum=300).norm + 0.5
            else:
                gluing_time = self.circulation / GluingNorm.objects.get(pages_sum=301).norm + 0.5

        return conversion_to_time(gluing_time)

    @property
    # all_trimming_time
    def trimming_time(self):
        if self.binding == 2:
            trimming_norm = TrimmingNorm.objects.get(binding=self.binding)
            pages_number = self.cover_page + self.inside_page + self.insole_page
            if pages_number <= 20:
                trimming_time = self.circulation / trimming_norm.max_limit_pages_20 + 0.5
            elif pages_number <= 30:
                trimming_time = self.circulation / trimming_norm.max_limit_pages_30 + 0.5
            elif pages_number <= 60:
                trimming_time = self.circulation / trimming_norm.max_limit_pages_60 + 0.5
            elif pages_number <= 100:
                trimming_time = self.circulation / trimming_norm.max_limit_pages_100 + 0.5
            elif pages_number <= 300:
                trimming_time = self.circulation / trimming_norm.max_limit_pages_300 + 0.5
            elif pages_number <= 700:
                trimming_time = self.circulation / trimming_norm.max_limit_pages_700 + 0.5
            else:
                trimming_time = self.circulation / trimming_norm.max_limit_pages_1100 + 0.5
        else:
            trimming_time = 0

        return conversion_to_time(trimming_time)

    @property
    # all_time_packing
    def time_packing(self):
        if self.packing == 1:
            time_packing = 0
        else:
            paking_norm = PackingNorm.objects.get(name=self.packing)
            time_packing = self.circulation / paking_norm.norm

        return conversion_to_time(time_packing)

    @property
    # all_time_foil
    def time_foil(self):
        utility_converter_for_peper_size_offset = utility_converter_for_peper_size_offset_fun(self.paper_size)
        utility_converter_for_peper_size_digit = utility_converter_for_peper_size_digit_fun(self.paper_size)

        if self.printing_type == 1:
            number_paper_sheets_cover = number_paper_sheets_fun(self.printing_type, self.cover_color, self.cover_page,
                                                                self.circulation,
                                                                utility_converter_for_peper_size_digit)
        else:
            number_paper_sheets_cover = number_paper_sheets_fun(self.printing_type, self.cover_color, self.cover_page,
                                                                self.circulation,
                                                                utility_converter_for_peper_size_offset)
        if self.foil == 1:
            time_foil = 0
        else:
            time_foil = number_paper_sheets_cover / 950 + 0.5

        return conversion_to_time(time_foil)

    @property
    # all_time_print_digit
    def time_print_digit(self):

        utility_converter_for_peper_size_digit = utility_converter_for_peper_size_digit_fun(self.paper_size)

        number_paper_sheets_cover = number_paper_sheets_fun(self.printing_type, self.cover_color, self.cover_page,
                                                            self.circulation, utility_converter_for_peper_size_digit)
        number_paper_sheets_inside = number_paper_sheets_fun(self.printing_type, self.inside_color, self.inside_page,
                                                             self.circulation, utility_converter_for_peper_size_digit)
        number_paper_sheets_insole = number_paper_sheets_fun(self.printing_type, self.insole_color, self.insole_page,
                                                             self.circulation, utility_converter_for_peper_size_digit)

        performance_standard_digit_cover = performance_standard_fun(self.cover, self.cover_paper)  # działa

        if self.inside_paper is None:
            performance_standard_digit_inside = 0
        else:
            performance_standard_digit_inside = performance_standard_fun(2, self.inside_paper)

        if self.insole_paper is None:
            performance_standard_digit_insole = 0
        else:
            performance_standard_digit_insole = performance_standard_fun(2, self.insole_paper)

        if self.printing_type == 1:

            if self.cover == 1:
                time_digit_cover = time_print_digit_fun(number_paper_sheets_cover, performance_standard_digit_cover)
            else:
                time_digit_cover = 2 * time_print_digit_fun(number_paper_sheets_cover, performance_standard_digit_cover)
            try:
                time_digit_inside = 2 * time_print_digit_fun(number_paper_sheets_inside,
                                                             performance_standard_digit_inside)
            except ZeroDivisionError:
                time_digit_inside = 0

            try:
                time_digit_insole = 2 * time_print_digit_fun(number_paper_sheets_insole,
                                                             performance_standard_digit_insole)
            except ZeroDivisionError:
                time_digit_insole = 0

            time_print_digit = time_digit_cover + time_digit_inside + time_digit_insole + 0.2  # działa
        else:
            time_print_digit = 0

        return conversion_to_time(time_print_digit)

    @property
    # all_time_print_offset
    def time_print_offset(self):
        utility_converter_for_peper_size_offset = utility_converter_for_peper_size_offset_fun(self.paper_size)
        utility_converter_for_peper_size_inside_offset = utility_converter_for_peper_size_inside_offset_fun(
            self.paper_size)

        sheets_number_cover = self.cover_page / utility_converter_for_peper_size_offset
        sheets_number_inside = self.inside_page / utility_converter_for_peper_size_inside_offset
        sheets_number_insole = self.insole_page / utility_converter_for_peper_size_inside_offset

        sheets_cover = sheets_fun(sheets_number_cover, self.circulation)
        sheets_inside = sheets_fun(sheets_number_inside, self.circulation)
        sheets_insole = sheets_fun(sheets_number_insole, self.circulation)

        printing_performance_cover = printing_performance_fun(self.cover_color, sheets_cover)
        printing_performance_inside = printing_performance_fun(self.inside_color, sheets_inside)
        printing_performance_insole = printing_performance_fun(self.insole_color, sheets_insole)

        plates_number_cover = plates_number_cover_fun(self.cover, self.cover_page,
                                                      utility_converter_for_peper_size_offset, self.cover_color)
        plates_number_inside = plates_number_other_fun(self.inside_page, utility_converter_for_peper_size_inside_offset,
                                                       self.inside_color)
        plates_number_insole = plates_number_other_fun(self.insole_page, utility_converter_for_peper_size_inside_offset,
                                                       self.insole_color)

        if self.printing_type == 2:

            try:
                time_print_offset_cover = time_print_offset_fun(self.cover, self.circulation, sheets_number_cover,
                                                                printing_performance_cover, plates_number_cover)
            except ZeroDivisionError:
                time_print_offset_cover = 0
            try:
                time_print_offset_inside = time_print_offset_fun(2, self.circulation, sheets_number_inside,
                                                                 printing_performance_inside, plates_number_inside)
            except ZeroDivisionError:
                time_print_offset_inside = 0
            try:
                time_print_offset_insole = time_print_offset_fun(2, self.circulation, sheets_number_insole,
                                                                 printing_performance_insole, plates_number_insole)
            except ZeroDivisionError:
                time_print_offset_insole = 0

            time_print_offset = time_print_offset_cover + time_print_offset_inside + time_print_offset_insole

        else:
            time_print_offset = 0

        return conversion_to_time(time_print_offset)

    @property
    def time_exposure(self):
        if self.printing_type == 2:
            utility_converter_for_peper_size_offset = utility_converter_for_peper_size_offset_fun(self.paper_size)
            utility_converter_for_peper_size_inside_offset = utility_converter_for_peper_size_inside_offset_fun(
                self.paper_size)

            plates_number_cover = plates_number_cover_fun(self.cover, self.cover_page,
                                                          utility_converter_for_peper_size_offset,
                                                          self.cover_color)
            plates_number_inside = plates_number_other_fun(self.inside_page,
                                                           utility_converter_for_peper_size_inside_offset,
                                                           self.inside_color)
            plates_number_insole = plates_number_other_fun(self.insole_page,
                                                           utility_converter_for_peper_size_inside_offset,
                                                           self.insole_color)

            time_exposure = (plates_number_cover + plates_number_inside + plates_number_insole) * 0.06
        else:
            time_exposure = 0

        return conversion_to_time(time_exposure)

    @property
    def pages_number(self):
        pages_number = self.cover_page + self.inside_page + self.insole_page
        return pages_number

