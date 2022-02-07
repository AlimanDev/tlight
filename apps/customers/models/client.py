from django.utils import timezone as time_zone
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField
from timezone_field import TimeZoneField


class Client(models.Model):
    UID = '01'

    class GenderEnum(models.TextChoices):
        MAN = "man", _("Man")
        WOMAN = "woman", _("Woman")
        UNKNOWN = "unknown", _("Unknown")

    class ClientTypesEnum(models.TextChoices):
        PRIMARY = "primary", _("Primary")
        REPEATED = "repeated", _("Repeated")
        EXTERNAL = "external", _("External")
        INDIRECT = "indirect", _("Indirect")

    uuid = models.CharField(_('UID'), blank=True)
    first_name = models.CharField(_('First name'), max_length=50)
    last_name = models.CharField(_('Last name'), max_length=50)
    patronymic = models.CharField(_('Patronymic'), max_length=50)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    client_type = models.CharField(_('Client Type'), max_length=10, choices=ClientTypesEnum.choices)
    gender = models.CharField(_('Gender'), max_length=10, choices=GenderEnum.choices)
    timezone = TimeZoneField(_('Timezone'), default=settings.TIME_ZONE)
    is_active = models.BooleanField(_('Active'), default=True)
    status_change_at = models.DateTimeField(default=time_zone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'clients'
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    def create_uuid(self):
        if self.pk and not self.uuid:
            self.uuid = f'{self.pk}{self.UID}'
            self.save(update_fields=['uid'])

    def re_save_field_status_change_at(self, kwargs: dict):
        if kwargs.get('is_active') and kwargs.get('is_active') != self.is_active:
            self.status_change_at = time_zone.now

    def save(self, *args, **kwargs):
        self.re_save_field_status_change_at(kwargs)
        super(self).save(*args, **kwargs)
        self.create_uuid()

    def __str__(self):
        return self.uuid

    def get_phone(self) -> str:
        return self.phone.as_e16


class AdditionalPhone(models.Model):
    client = models.ForeignKey(Client, verbose_name=_('Client'), related_name='phone_more', on_delete=models.CASCADE)
    phone = PhoneNumberField(null=False, blank=False)

    class Meta:
        db_table = 'client_phones'
        verbose_name = _('Client Phone')
        verbose_name_plural = _('Client Phones')

    def __str__(self):
        return self.phone


class Email(models.Model):
    client = models.ForeignKey(Client, verbose_name=_('Client'), related_name='emails', on_delete=models.CASCADE)
    email = models.EmailField(verbose_name=_('Email'))

    class Meta:
        db_table = 'client_emails'
        verbose_name = _('Client Email')
        verbose_name_plural = _('Client Emails')


class SocialAccount(models.Model):
    ONLY_ONE = ['ok', 'instagram', 'telegram', 'whatsapp', 'viber']

    class AccountTypesEnum(models.TextChoices):
        VK = "vk", _("VK")
        FB = "fb", _("FB")
        OK = "ok", _("OK")
        INSTA = 'instagram', _("Instagram")
        TELEGRAM = 'telegram', _("Telegram")
        WHATSAPP = 'whatsapp', _("Whatsapp")
        VIBER = 'viber', _("Viber")

    client = models.ForeignKey(Client, verbose_name=_('Social Accounts'), related_name='social_accounts',
                               on_delete=models.CASCADE)
    account_type = models.CharField(max_length=9, choices=AccountTypesEnum.choices)
    link = models.CharField(max_length=50)

    class Meta:
        db_table = 'client_social_accounts'
        verbose_name = _('Social Account')
        verbose_name_plural = _('Social Accounts')

    def check_social_account_for_duplicate(self, kwargs):
        if kwargs.get('account_type') in self.ONLY_ONE:
            if kwargs.get('account_type') in [account.account_type for account in self.client.social_accounts.all()]:
                return False
        return True

    def save(self, *args, **kwargs):
        if self.check_social_account_for_duplicate(kwargs):
            super(self).save(*args, **kwargs)
