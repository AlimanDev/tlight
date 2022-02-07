def create_uuid(obj):
    if obj.pk and not obj.uuid:
        obj.uuid = f'{obj.pk}{obj.UID}'
        obj.save(update_fields=['uuid'])
