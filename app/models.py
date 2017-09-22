# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Organisation(models.Model):
    name = models.CharField(_('Organisation name'), unique=True, max_length=100)
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Organisation")
        verbose_name_plural = _("Organisations")

    
    def __unicode__(self):
        return u"%s" % self.name


class Researcher(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), blank=True, null=True,
                             help_text=_("Select the user if there is a"))
    fio = models.CharField(_("FIO"), max_length=100)
    organisation = models.ForeignKey(Organisation, verbose_name=_("Organisation"))
    lab = models.CharField(_("Laboratory"), max_length=250, blank=True, null=True)
    contacts = models.CharField(_("Contact info"), max_length=250, blank=True, null=True)
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Researcher")
        verbose_name_plural = _("Researchers")

    
    def __unicode__(self):
        return u"%s %s" % (self.fio, self.organisation)


class Publication(models.Model):
    title = models.CharField(_("Title"), max_length=512)
    authors = models.ManyToManyField(Researcher, verbose_name=_("Researcher(s)"))
    publisher = models.CharField(_("Publisher"), max_length=200)
    year = models.PositiveSmallIntegerField(_("Year"))
    pages = models.CharField(_("Pages"), max_length=20, help_text=_("Stranicy publikacii"), blank=True, null=True)
    file = models.FileField(_("File with paper"), upload_to="files/publications/%Y/%m/%d/", blank=True, null=True)
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Publication")
        verbose_name_plural = _("Publications")

    
    def __unicode__(self):
        return u"%s" % self.title


class WaterObject(models.Model):
    name = models.CharField(_("Name of water object"), unique=True, max_length=100)
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Water object")
        verbose_name_plural = _("Water objects")

    
    def __unicode__(self):
        return u"%s" % self.name


class WaterZone(models.Model):
    water_obj = models.ForeignKey(WaterObject, verbose_name=_("Water object"))
    name = models.CharField(_("Name zone"), max_length=100)
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Water zone")
        verbose_name_plural = _("Water zone")

    
    def __unicode__(self):
        return u"%s" % self.name


class Station(models.Model):
    name = models.CharField(_("Station name"), max_length=50)
    wo = models.ForeignKey(WaterObject, verbose_name=_("Water object"), help_text=_("pls select water object"))
    wz = models.ForeignKey(WaterZone, verbose_name=_("Water zone"), blank=True, null=True,
                           help_text=_("pls select water zone, if need"))
    gps = models.CharField(_("Geographical coordinates"), max_length=100, unique=True,
                           help_text=_("pls input unique geo coordinates"))
    depth = models.PositiveSmallIntegerField(_("Depth"), blank=True, null=True)
    abbreviation = models.CharField(_("Abbreviation"), max_length=50, blank=True, null=True)
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Station")
        verbose_name_plural = _("Stations")

    
    def __unicode__(self):
        return u"%s %s" % (self.name, self.wo)


class TypeResearch(models.Model):
    type = models.CharField(_("Type of research"), max_length=50, unique=True,
                            help_text=_("input type of research"))
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Type of research")
        verbose_name_plural = _("Types of research")

    
    def __unicode__(self):
        return u"%s" % self.type


class AnalysisParameter(models.Model):
    name = models.CharField(_("Name parameter"), unique=True, max_length=50)
    type = models.ForeignKey(TypeResearch, verbose_name=_("Type of research"))
    unit = models.CharField(_("Unit"), max_length=14)
    descr = models.CharField(_("Description"), max_length= 256,blank=True, null=True)
    have = models.BooleanField(_("Have?"), default=False,
                               help_text=_("Dlja bioticheskih. Esli opredelili  s pomoshh'ju krasitelja "
                                           "bakterii, no ne vhodili v zadachi issledovanija"))
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Analysis parameter")
        verbose_name_plural = _("Analysis parameters")

    
    def __unicode__(self):
        return u"%s" % (self.name)


class TypeSample(models.Model):
    type = models.CharField(_("Type of sample"), max_length=50, unique=True,
                            help_text=_("input type of sample"))
    descr = models.CharField(_("Description"), max_length=512, blank=True, null=True)
    value = models.CharField(_("V 4em merim"), max_length=30, blank=True, null=True,
                             help_text=_("merim v mm3, litrah, grammah ili kg"))
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Type of sample")
        verbose_name_plural = _("Types of sample")

    
    def __unicode__(self):
        return u"%s" % self.type

class TypeEquipment(models.Model):
    type = models.CharField(_("Type of equipment or consumables"), max_length=50, unique=True,
                            help_text=_("input type of equipment or consumables"))
    depends = models.ForeignKey('self', verbose_name=_("Depends on"), blank=True, null=True,)
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Type of equipment or consumables")
        verbose_name_plural = _("Types of equipment or consumables")

    
    def __unicode__(self):
        return u"%s" % self.type


class Equipment(models.Model):
    name = models.CharField(_("Name"), max_length=70, unique=True,
                            help_text=_("Name of equipment or consumables"))
    type = models.ForeignKey(TypeEquipment, verbose_name = _("Type of equipment or consumables"))
    error = models.TextField(_("Pogreshnost"), blank=True, null=True)
    desc = models.TextField(_("Description"), max_length=1024)
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Equipment and consumables")
        verbose_name_plural = _("Equipment and consumables")

    
    def __unicode__(self):
        return u"%s %s" % (self.name, self.type)

class Sample(models.Model):
    code = models.CharField(_("Code of sample"), max_length=50, help_text=_("Shifr proby"), unique=True)
    station = models.ForeignKey(Station, verbose_name=_("Station"))
    type_sample = models.ForeignKey(TypeSample, verbose_name = _("Type of sample"))
    date_time = models.DateTimeField(_("Date and time of sampling"))
    depth = models.PositiveSmallIntegerField(_("Depth"), help_text=_("Glubina 1"))
    depth2 = models.PositiveSmallIntegerField(_("Depth niz"), blank=True, null=True,
                                              help_text=_("Glubina 2, esli entigral'naya"))
    takenb = models.ManyToManyField(Researcher, verbose_name=_("Taken by..."))
    takene = models.ManyToManyField(Equipment, verbose_name=_("Taken equipment"))
    volume = models.CharField(_("Sample volume"), max_length=30, blank=True, null=True)
    descr = models.TextField(_("Description"), blank=True, null=True)
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Sample")
        verbose_name_plural = _("Samples")

    
    def __unicode__(self):
        return u"%s %s" % (self.code, self.station)


class Method(models.Model):
    name = models.CharField(_("Method name"), max_length=100)
    ref = models.ManyToManyField(Publication, verbose_name=_("Refers to"))
    used = models.ManyToManyField(Equipment, verbose_name=_("Used equipment"))
    descr = models.TextField(_("Description"), max_length=5110, blank=True, null=True)
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Method")
        verbose_name_plural = _("Methods")

    
    def __unicode__(self):
        return u"%s" % self.name




class SampleAnalysis(models.Model):
    sample = models.ForeignKey(Sample, verbose_name=_("Sample"))
    parameter = models.ForeignKey(AnalysisParameter, verbose_name = _("Analysis parameter"))
    researcher = models.ManyToManyField(Researcher, verbose_name=_("Reseacher(s)"))
    method = models.ForeignKey(Method, verbose_name=_("Method"), blank=True, null=True)
    equipment = models.ForeignKey(Equipment, verbose_name=_("Equipment"), blank=True, null=True)
    result = models.CharField(_("Result"), max_length=1024,
                              help_text=_("Pls input result here"))
    file = models.FileField(_("File analyses"), upload_to="files/analyses/%Y/%m/%d/", blank=True, null=True,
                            help_text=_("Upload file with analyses result"))
    dta = models.DateTimeField(_("Date/time analyses"), blank=True, null=True)
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)
    class Meta:
        verbose_name = _("Sample analysis")
        verbose_name_plural = _("Analysis of samples")
    
    def __unicode__(self):
        return u"%s %s" % (self.sample, self.result)


class Gene(models.Model):
    gene = models.CharField(_("Gene"), max_length=50)
    #TODO: dobavit' ssylki na bd taxonov
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)
    class Meta:
        verbose_name = _("Gene")
        verbose_name_plural = _("Genes")
    
    def __unicode__(self):
        return u"%s" % self.gene


class ProgramPipe(models.Model):
    name = models.CharField(_("Program name"), max_length=30)
    version = models.CharField(_("Program version"), max_length=20)
    os = models.CharField(_("Operation system"), max_length=50,
                          help_text=_("Please write here full version your operation system"))
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)


    class Meta:
        verbose_name = _("Program Pipeline")
        verbose_name_plural = _("Programs Pipeline")
    
    def __unicode__(self):
        return u"%s %s" % (self.name, self.version)


class Pipeline(models.Model):
    name = models.CharField(_("Pipeline name"), max_length=40)
    program = models.ForeignKey(ProgramPipe, verbose_name = _("Program Pipeline"))
    #dalee dobavit' parametry
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Pipeline")
        verbose_name_plural = _("Pipelines")

    
    def __unicode__(self):
        return u"%s" % self.name


class Amplicon(models.Model):
    descr = models.TextField(_("Description"))
    gene = models.ForeignKey(Gene, verbose_name=_("Gene"))
    sample = models.ForeignKey(Sample, verbose_name=_("Sample"))
    method = models.ForeignKey(Method, verbose_name=_("Method analyses"))
    date = models.DateField(_("Date of analyse"))
    research = models.ManyToManyField(Researcher, verbose_name=_("Researcher"),
                                 help_text=_("m:n or 1:n???"))
    region = models.TextField(_("Region"), blank=True, null=True)
    chao = models.FloatField(_("Chao1 0.03"), blank=True, null=True)
    shannon = models.FloatField(_("Shannon 0.03"),blank=True, null=True)
    sraid = models.CharField(_("SRAid in NCBI SRA"), max_length=10, blank=True, null=True)
    lenbp = models.IntegerField(_("length bp"), blank=True, null=True)
    pipe = models.ForeignKey(Pipeline, verbose_name=_("Pipeline"))
    identa = models.CharField(_("Amplicon identifier"), max_length=100)
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)
    class Meta:
        verbose_name = _("Amplicon")
        verbose_name_plural = _("Amplicons")
    
    def __unicode__(self):
        return u"%s" % self.identa


class TaxBase(models.Model):
    name = models.CharField(_("DB name"), max_length=50,
                            help_text=_("name database, ex:NCBI"))
    basen = models.CharField(_("name"), max_length=50,
                             help_text=_("db name for connect"))
    basev = models.CharField(_("database version"), max_length=15)
    base_url = models.URLField(_("Database URL"))
    base_user = models.CharField(_("db user"), max_length=20,
                                 help_text=_("user for connect"))
    base_pass = models.CharField(_("Password"), max_length=40,
                                 help_text=_("password for connect"))
    base_port = models.PositiveIntegerField(_("Port db"))
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Taxonomy Base")
        verbose_name_plural = _("Taxonomy Bases")
    
    def __unicode__(self):
        return u"%s %s" % (self.name, self.basev)


class TaxIDs(models.Model):
    base = models.ForeignKey(TaxBase, verbose_name = _("Taxonomy Base"))
    taxID = models.IntegerField(_("TaxID"))
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)
    class Meta:
        verbose_name = _("TaxIDs")
        verbose_name_plural = _("TaxIDs")
    
    def __unicode__(self):
        return u"%s %s" % (self.base, self.taxID)


class OTU(models.Model):
    pipe = models.ForeignKey(Pipeline, verbose_name=_("Pipeline"))
    taxID = models.ForeignKey(TaxIDs, verbose_name = _("TaxIDs"))
    ref_seq = models.TextField(_("Ref seq"))
    read = models.PositiveIntegerField(_("Count reads"))
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("OTU")
        verbose_name_plural = _("OTU's")

    
    def __unicode__(self):
        return u"%s" % self.reads

class Reads(models.Model):
    ampl = models.ForeignKey(Amplicon, verbose_name=_("Amplicon"))
    otiu = models.ForeignKey(OTU, verbose_name=_("OTU"))
    rri = models.TextField(_("Raw read id"))
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)
    class Meta:
        verbose_name = _("Reads")
        verbose_name_plural = _("Reads")
    
    def __unicode__(self):
        return u"%s" % self.ampl

class Seq_run(models.Model):
    data = models.DateField(_("Date"), help_text=_("Run date"))
    org = models.ForeignKey(Organisation, verbose_name=_("Organisation"))
    research= models.ForeignKey(Researcher, verbose_name=_("Research"))
    descr = models.TextField(_("Description"), blank=True, null=True)
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)
    class Meta:
        verbose_name = _("Sequencing run")
        verbose_name_plural = _("Sequencing runs")

        def __unicode__(self):
            return u"%s %s" % (self.data, self.research)

class Seq_result(models.Model):
    ampl = models.ForeignKey(Amplicon, verbose_name=_("Amplicon"))
    file = models.FileField(_("File with result"), upload_to="files/seqres/%Y/%m/%d/", blank=True, null=True)
    plathorm = models.ForeignKey(Equipment, verbose_name=_("Plathorm seq"))
    run = models.ForeignKey(Seq_run, verbose_name = _("Sequencing run"))
    date_added = models.DateTimeField(_("Date time added"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Sequencing result")
        verbose_name_plural = _("Sequencing results")
    
    def __unicode__(self):
        return u"%s" % self.ampl