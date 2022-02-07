from django.utils.translation import gettext_lazy as _
from django.db import models

from core.libs.utils import create_uuid


class Organization(models.Model):
    UID = '02'

    uuid = models.CharField(_('UID'), max_length=250, blank=True)
    name = models.CharField(_('Name organization'), max_length=150)
    short_name = models.CharField(_('Short Name organization'), max_length=10)
    tin = models.CharField(_('TIN'), max_length=12)
    ppc = models.CharField(_('Checkpoint'), max_length=9)
    departments = models.ManyToManyField('customers.Department', verbose_name=_('Departments'),
                                         related_name='departments', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'organizations'
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')

    def create_uuid(self):
        self.uuid = f'{self.pk}{self.UID}'
        self.save(update_fields=['uuid'])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.pk and not self.uuid:
            create_uuid(self)
