# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *

from django.contrib import admin

class OrganisationAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
    ordering = ['-name']
    search_fields = ['name']
admin.site.register(Organisation, OrganisationAdmin)

class ResearcherAdmin(admin.ModelAdmin):
    fields = ('fio', 'organisation', 'lab', 'contacts', 'user')
    list_display = ('fio', 'organisation', 'lab', 'contacts')
    ordering = ('-organisation',)
    search_fields = ['fio', 'organisation', 'lab', 'contacts']
    list_filter = ['organisation']
admin.site.register(Researcher, ResearcherAdmin)

class PublicationAdmin(admin.ModelAdmin):
    fields = ('title', 'authors','publisher','year','pages','file')
    list_display = ('title','publisher','year','pages')
    ordering = ['title', 'publisher', "year"]
    search_fields = ['title','publisher','year','pages']
    list_filter = ['publisher']
admin.site.register(Publication, PublicationAdmin)

class WaterObjectAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(WaterObject, WaterObjectAdmin)

class WaterZoneAdmin(admin.ModelAdmin):
    fields = ('name', 'water_obj')
    list_display = ('name', 'water_obj')
    ordering = ['name']
    search_fields = ['name']
    list_filter = ['water_obj']
admin.site.register(WaterZone, WaterZoneAdmin)

class StationAdmin(admin.ModelAdmin):
    fields = ('name', 'abbreviation', 'depth','wo', 'wz', 'gps')
    list_display = ('name', 'abbreviation', 'depth','wo', 'wz', 'gps')
    ordering = ('name', 'depth',)
    search_fields = ['name', 'wo', 'abbreviation', 'wz']
    list_filter = ['wo', 'wz']
admin.site.register(Station, StationAdmin)

class TypeResearchAdmin(admin.ModelAdmin):
    fields = ('type',)
    list_display = ('type',)
    ordering = ('-type',)
admin.site.register(TypeResearch,TypeResearchAdmin)

class TypeSampleAdmin(admin.ModelAdmin):
    fields = ('type', 'descr', 'value')
    list_display = ('type', 'descr', 'value')
    ordering = ('-type',)
admin.site.register(TypeSample, TypeSampleAdmin)

class TypeEquipmentAdmin(admin.ModelAdmin):
    fields = ('type','depends')
    list_display = ('type','depends')
    list_filter = ['depends']
    ordering = ('-type',)
admin.site.register(TypeEquipment, TypeEquipmentAdmin)

class AnalysisParameterAdmin(admin.ModelAdmin):
    fields = ('name', 'type', 'unit', 'descr', 'have')
    list_display = ('name', 'type', 'unit', 'descr', 'have')
    ordering = ('name', 'type', 'unit', 'have')
    search_fields = ['name', 'type', 'unit', 'descr']
    list_filter = ['type']
admin.site.register(AnalysisParameter, AnalysisParameterAdmin)

class EquipmentAdmin(admin.ModelAdmin):
    fields = ('name', 'type', 'error', 'desc')
    list_display = ('name', 'type', 'error', 'desc')
    ordering = ('name', 'type')
    search_fields = ['name', 'type', 'desc']
    list_filter = ['type']
admin.site.register(Equipment)

class SampleAdmin(admin.ModelAdmin):
    fields = ('code', 'station', 'type_sample', 'date_time', 'depth', 'depth2', 'volume', 'takenb', 'takene', 'descr')
    list_display = ('code', 'station', 'type_sample', 'date_time', 'depth', 'depth2', 'volume', 'descr')
    ordering = ('code', 'station', 'type_sample', 'date_time')
    search_fields = ['code', 'station', 'type_sample', 'volume', 'date_time', 'takenb', 'takene', 'descr']
    list_filter = ['station', 'type_sample', 'takene']
admin.site.register(Sample,SampleAdmin)

class MethodAdmin(admin.ModelAdmin):
    fields = ('name', 'ref', 'used', 'descr')
    list_display = ('name', 'descr')
    ordering = ('name','used')
    search_fields = ['name', 'ref', 'used', 'descr']
    list_filter = ['used']
admin.site.register(Method, MethodAdmin)

class SampleAnalysisAdmin(admin.ModelAdmin):
    fields = ('sample', 'parameter', 'researcher', 'method', 'equipment', 'result', 'file', 'dta')
    list_display = ('sample', 'parameter', 'method', 'equipment', 'result','dta')
    ordering = ('sample', 'parameter', 'method', 'equipment', 'dta')
    search_fields = ['sample', 'parameter', 'researcher', 'method', 'equipment', 'result']
    list_filter = ['sample', 'parameter', 'method', 'equipment',]
admin.site.register(SampleAnalysis, SampleAnalysisAdmin)

class GeneAdmin(admin.ModelAdmin):
    fields = ['gene']
    list_display = ['gene']
    ordering = ['-gene']
admin.site.register(Gene, GeneAdmin)

class ProgramPipeAdmin(admin.ModelAdmin):
    fields = ('name', 'version', 'os')
    list_display = ('name', 'version', 'os')
    ordering = ('name', 'version', 'os')
    search_fields = ['name', 'version', 'os']
admin.site.register(ProgramPipe, ProgramPipeAdmin)

class PipelineAdmin(admin.ModelAdmin):
    fields = ('name', 'program')
    list_display = ('name', 'program')
    ordering = ('name', 'program')
    search_fields = ['name', 'program']
    list_filter = ['program']
admin.site.register(Pipeline, PipelineAdmin)

class AmpliconAdmin(admin.ModelAdmin):
    fields = ('descr', 'gene', 'sample', 'method', 'date', 'research', 'region', 'chao', 'shannon',
              'sraid', 'lenbp', 'pipe', 'identa')
    list_display = ('descr', 'gene', 'sample', 'method', 'date', 'region', 'chao', 'shannon',
                    'sraid', 'lenbp', 'pipe', 'identa')
    ordering = ('gene', 'sample', 'method', 'date', 'pipe')
    search_fields = ['descr', 'gene', 'sample', 'method', 'date', 'research', 'region', 'chao', 'shannon',
                    'sraid', 'lenbp', 'pipe', 'identa']
    list_filter = ['gene', 'sample', 'method', 'date', 'pipe']
admin.site.register(Amplicon, AmpliconAdmin)

class TaxBaseAdmin(admin.ModelAdmin):
    fields = ('name', 'basen', 'basev', 'base_url', 'base_user', 'base_pass', 'base_port')
    list_display = ('name', 'basen', 'basev', 'base_url')
    ordering = ('name', 'basen', 'basev')
    search_fields = ['name', 'basen', 'basev', 'base_url']
admin.site.register(TaxBase, TaxBaseAdmin)

class TaxIDsAdmin(admin.ModelAdmin):
    fields = ('base', 'taxID')
    list_display = ('base', 'taxID')
    ordering = ('base',)
    search_fields = ['base', 'taxID']
admin.site.register(TaxIDs, TaxIDsAdmin)

class OTUAdmin(admin.ModelAdmin):
    fields = ('pipe', 'taxID', 'ref_seq', 'read')
    list_display = ('pipe', 'taxID', 'read')
    ordering = ('pipe', 'taxID', 'read')
    search_fields = ['pipe', 'taxID', 'read']
    list_filter = ['pipe', 'taxID']
admin.site.register(OTU,OTUAdmin)

class ReadsAdmin(admin.ModelAdmin):
    fields = ('ampl', 'otiu', 'rri')
    list_display = ('ampl', 'otiu', 'rri')
    ordering = ('ampl', 'otiu')
    search_fields = ['ampl', 'otiu']
    list_filter = ['ampl', 'otiu']
admin.site.register(Reads, ReadsAdmin)


class Seq_runAdmin(admin.ModelAdmin):
    fields = ('data', 'org', 'research', 'descr')
    list_display = ('data', 'org', 'research', 'descr')
    ordering = ('data', 'org', 'research')
    search_fields = ['data', 'org', 'research', 'descr']
    list_filter = ['data', 'org', 'research']
admin.site.register(Seq_run, Seq_runAdmin)

class Seq_resultAdmin(admin.ModelAdmin):
    fields = ('ampl', 'file', 'plathorm', 'run')
    list_display = ('ampl', 'plathorm', 'run')
    ordering = ('ampl', 'plathorm', 'run')
    search_fields = ['ampl', 'plathorm']
    list_filter = ['ampl', 'plathorm']
admin.site.register(Seq_result, Seq_resultAdmin)

# class Admin(admin.ModelAdmin):
#     fields = ('')
#     list_display = ('')
#     ordering = ('')
#     search_fields = ['']
#     list_filter = []

# Register your models here.
