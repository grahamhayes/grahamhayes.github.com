@classmethod
def _rename_path_segment(cls, obj_adapter, object, path_segment):

    # Check if the object is a list - lists will just have an index as a
    # value, ands this can't be renamed
    if issubclass(obj_adapter.ADAPTER_OBJECT, objects.ListObjectMixin):
        obj_adapter = cls.get_object_adapter(
            cls.ADAPTER_FORMAT,
            obj_adapter.ADAPTER_OBJECT.LIST_ITEM_TYPE.obj_name())
        # Return the segment as is, and the next adapter (which is the
        # LIST_ITEM_TYPE)
        return path_segment, obj_adapter

    for key, value in obj_adapter.MODIFICATIONS.get(
            'fields', {}).items():

        # Check if this field as actually a nested object
        if object.FIELDS.get(path_segment, {}).get('relation', False):

            obj_cls = object.FIELDS.get(path_segment).get('relation_cls')
            obj_adapter = cls.get_object_adapter(
                cls.ADAPTER_FORMAT,
                obj_cls)

            object = objects.DesignateObject.obj_cls_from_name(obj_cls)()
            # Recurse down into this object
            path_segment, obj_adapter = cls._rename_path_segment(
                obj_adapter, object, path_segment)

            # No need to continue the loop
            break

        if not isinstance(
            value.get(
                'rename', NotSpecifiedSential()), NotSpecifiedSential)\
                and path_segment == value.get('rename'):
            # Just do the rename
            path_segment = key

    return path_segment, obj_adapter