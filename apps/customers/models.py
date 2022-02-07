from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField
from timezone_field import TimeZoneField


class Client(models.Model):
    class GenderEnum(models.TextChoices):
        MAN = "man", _("Man")
        WOMAN = "woman", _("Woman")
        UNKNOWN = "unknown", _("Unknown")

    class ClientTypesEnum(models.TextChoices):
        PRIMARY = "primary", _("Primary")
        REPEATED = "repeated", _("Repeated")
        EXTERNAL = "external", _("External")
        INDIRECT = "indirect", _("Indirect")

    phone = PhoneNumberField(null=False, blank=False, unique=True)
    uuid = models.CharField(_('UID'), blank=True)
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    patronymic = models.CharField('Patronymic', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status_change_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(_('Active'), default=True)
    client_type = models.CharField(_('Client Type'), max_length=10, choices=ClientTypesEnum.choices)
    gender = models.CharField(_('Gender'), max_length=10, choices=GenderEnum.choices)
    timezone = TimeZoneField(_('Timezone'), default=settings.TIME_ZONE)

    class Meta:
        db_table = 'clients'
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    def create_uuid(self):
        self.uuid = f'{self.pk}01'
        self.save(update_fields=['uid'])

    def save(self, *args, **kwargs):
        super(self).save(*args, **kwargs)
        if self.pk and not self.uuid:
            self.create_uuid()

    def get_phone(self) -> str:
        return self.phone.as_e16
