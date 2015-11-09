def _render_object(cls, object, *args, **kwargs):
    # The dict we will return to be rendered to JSON / output format
    r_obj = {}
    # Loop over all fields that are supposed to be output
    for key, value in cls.MODIFICATIONS['fields'].items():
        # Get properties for this field
        field_props = cls.MODIFICATIONS['fields'][key]
        # Check if it has to be renamed
        if field_props.get('rename', False):
            obj = getattr(object, field_props.get('rename'))
            # if rename is specified we need to change the key
            obj_key = field_props.get('rename')
        else:
            # if not, move on
            obj = getattr(object, key, None)
            obj_key = key