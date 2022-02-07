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
    list_display = ('id', 'uuid', 'phone')
    list_display_links = ('uuid', )


@admin.register(organization.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid')
    list_display_links = ('uuid',)


@admin.register(department.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid')
    list_display_links = ('uuid',)
