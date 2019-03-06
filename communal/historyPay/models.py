from django.db import models

class Period(models.Model):
    name = models.CharField(max_length=50, help_text="Наименование периода")
    begin_d = models.DateField(help_text='Дата начала периода')
    end_d   = models.DateField(help_text='Дата окончанияе периода')
    comment = models.TextField(max_length=500, help_text='Примечание', blank=True, null=True)

    class Meta:
        ordering = ["-begin_d"]
 
#    def get_absolute_url(self):
#        return reverse('model-detail-view', args=[str(self.id)])
    def __repr__(self):
        return 'Period(name=%r, begin_d=%r, end_d=%r)' %(self.name, self.begin_d, self.end_d)
    def __str__(self):
        return 'Период [%s - %s]' % (self.begin_d, self.end_d)

class ServiceProvider(models.Model):
    name = models.CharField(max_length=50, help_text="Наименование поставщика услуг")

    class Meta:
        ordering = ["name"]            
    def __repr__(self):
        return 'ServiceProvider(name=%r)' % (self.name)
    def __str__(self):
        return 'Поставщик %s' % (self.name)

class Pay(models.Model):
    pass 
    