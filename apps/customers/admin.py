from django.contrib import admin
from apps.customers.models import client, department, organization


class ClientSocialAccountInline(admin.StackedInline):
    model = client.SocialAccount
    extra = 1


class ClientEmailInline(admin.StackedInline):
    model = client.Email
    extra = 1


class ClientOtherPhoneInline(admin.StackedInline):
    model = client.AdditionalPhone
    extra = 1


@admin.register(client.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', )


@admin.register(organization.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', )


@admin.register(department.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', )


# @admin.register(client.Client)
# class ClientAdmin(admin.ModelAdmin):
#     search_fields = ('uid', 'get_full_name', 'phone')
#     list_display = ('uid', 'get_full_name', 'phone', 'date_joined', 'is_active')
#     list_editable = ('is_active',)
#     fields = (
#         'uid', 'first_name', 'last_name', 'patronymic', 'client_type', 'gender',
#         'phone', 'is_active', 'other_phones', 'emails', 'social_accounts', 'departments', 'date_joined',
#         'updated_at', 'status_change_at'
#     )
#     readonly_fields = ('uid', 'updated_at', 'date_joined', 'status_change_at')
#     autocomplete_fields = ('departments',)
#     # inlines = [ClientOtherPhoneInline, ClientEmailInline, ClientOtherPhoneInline]
#
#     def uid(self, client):
#         return client.uid
#
#     uid.short_description = 'ID клиента'
#
#     def get_full_name(self, client):
#         return client.get_full_name()
#
#     get_full_name.short_description = 'Ф.И.О'
#
#
# @admin.register(department.Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     list_display = ('uid', 'name', 'client_count')
#     search_fields = ('uid', 'name', 'legal_person__short_name', 'legal_person__full_name')
#     fields = (
#         'uid', 'name', 'parent', 'legal_person', 'children', 'client_count'
#     )
#     readonly_fields = ('uid', 'client_count')
#     autocomplete_fields = ('parent',)
#
#     # inlines = ('LegalPersonInline',)
#
#     def uid(self, department) -> str:
#         return department.uid
#
#     uid.short_description = 'ID Департамента'
#
#     def client_count(self, department) -> str:
#         return str(department.client_count)
#
#     client_count.short_description = 'Кол-во клиентов'
#
#
# @admin.register(organization.Organization)
# class LegalPersonAdmin(admin.ModelAdmin):
#     search_fields = ('uid', 'short_name', 'full_name', 'kpp', 'inn')
#     list_display = ('uid', 'short_name', 'full_name', 'kpp', 'inn', 'created_at',)
#     fields = (
#         'uid', 'full_name', 'short_name', 'kpp', 'inn', 'created_at', 'updated_at'
#     )
#     readonly_fields = ('uid', 'created_at', 'updated_at')
#
#     def uid(self, client):
#         return client.uid
#
#     uid.short_description = 'ID Юридического лица'
#
#     def get_full_name(self, client):
#         return client.get_full_name()
#
#     get_full_name.short_description = 'Ф.И.О'
