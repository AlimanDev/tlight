from django.utils.translation import gettext_lazy as _
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from core.libs.utils import create_uuid


class Department(MPTTModel):
    UID = '03'

    uuid = models.CharField(_('UID'), max_length=250, blank=True)
    name = models.CharField(_('Name'), max_length=100)
    parent = TreeForeignKey('self', verbose_name=_('Parent'), related_name='children', on_delete=models.CASCADE,
                            null=True, blank=True)
    client = models.ManyToManyField(to="customers.Client", verbose_name=_('Client'), related_name='departments')

    class MPTTMeta:
        db_table = 'departments'
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    def save(self, *args, **kwargs):
        super(self).save(*args, **kwargs)
        if self.pk and not self.uuid:
            create_uuid(self)

    def clients_count(self):
        return self.client.count()
