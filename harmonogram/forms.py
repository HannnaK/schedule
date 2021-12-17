from django.forms import ModelForm
from .models import TechnicalData


class TechnicalDataForm(ModelForm):
    class Meta:
        model = TechnicalData
        fields = ['project_number', 'project_name', 'date_to_be_printed', 'date_to_customer', 'printing_type',
                  'circulation', 'paper_size', 'binding', 'collecting', 'trimming', 'packing', 'foil', 'manual_work',
                  'cover', 'cover_color', 'inside_color', 'insole_color', 'cover_page', 'inside_page', 'insole_page',
                  'cover_paper', 'inside_paper', 'insole_paper']
