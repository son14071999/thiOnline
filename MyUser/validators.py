from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 2097152:
        raise ValidationError("Kích thước ảnh dưới 2 MB")
    else:
        return value