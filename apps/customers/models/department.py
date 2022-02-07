from django.utils.translation import gettext_lazy as _
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Department(MPTTModel):
    UID = '03'

    name = models.CharField(_('Name'), max_length=100)
    parent = TreeForeignKey('self', verbose_name=_('Parent'), related_name='children', on_delete=models.CASCADE,
                            null=True, blank=True)
    client = models.ForeignKey(to="customers.Client", verbose_name=_('Client'),
                               related_name='departments', on_delete=models.CASCADE)

    class MPTTMeta:
        db_table = 'departments'
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    @property
    def uid(self) -> str:
        return f'{self.pk}03' if self.pk else ''
