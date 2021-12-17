from django.contrib import admin
from .models import TechnicalData, UtilityConverterOffset, UtilityConverterDigit, Cut, Breaking, Collecting, \
    AligningNorm, \
    JoiningNorm, GluingNorm, TrimmingNorm, PackingNorm, PerformanceStandardDigit


@admin.register(TechnicalData)
class TechnicalDataAdmin(admin.ModelAdmin):
    list_display = ['project_number', 'project_name', 'date_to_be_printed', 'date_to_customer', 'printing_type',
                    'circulation', 'paper_size', 'binding', 'collecting', 'trimming', 'packing', 'foil', 'manual_work',
                    'cover', 'cover_color', 'inside_color', 'insole_color', 'cover_page', 'inside_page', 'insole_page',
                    'cover_paper', 'inside_paper']


@admin.register(UtilityConverterOffset)
class UtilityConverterOffsetAdmin(admin.ModelAdmin):
    list_display = ['paper_size', 'cover_pages', 'inside_pages']


@admin.register(UtilityConverterDigit)
class UtilityConverterDigitAdmin(admin.ModelAdmin):
    list_display = ['paper_size', 'pages']


@admin.register(Cut)
class CutAdmin(admin.ModelAdmin):
    list_display = ['grammage', 'sheets_number']


@admin.register(Breaking)
class BreakingAdmin(admin.ModelAdmin):
    list_display = ['paper_size', 'breaks_number', 'offset_80_chalk_90_200_cardboard_240',
                    'cardboard_300_chalk_250_300']


@admin.register(Collecting)
class CollectingAdmin(admin.ModelAdmin):
    list_display = ['name', 'norm']


@admin.register(AligningNorm)
class AligningNormAdmin(admin.ModelAdmin):
    list_display = ['name', 'norm']


@admin.register(JoiningNorm)
class JoiningNormAdmin(admin.ModelAdmin):
    list_display = ['name', 'norm']


@admin.register(GluingNorm)
class GluingNormAdmin(admin.ModelAdmin):
    list_display = ['pages_sum', 'norm']


@admin.register(TrimmingNorm)
class TrimmingNormAdmin(admin.ModelAdmin):
    list_display = ['binding', 'max_limit_pages_20', 'max_limit_pages_30', 'max_limit_pages_60',
                    'max_limit_pages_100', 'max_limit_pages_300', 'max_limit_pages_700', 'max_limit_pages_1100']


@admin.register(PackingNorm)
class PackingNormAdmin(admin.ModelAdmin):
    list_display = ['name', 'norm']


@admin.register(PerformanceStandardDigit)
class PerformanceStandardDigit(admin.ModelAdmin):
    list_display = ['paper', 'color_1', 'other_color']

