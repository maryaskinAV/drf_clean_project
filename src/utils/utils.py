import uuid


def upload_instance_image(instance, filename):

    ext = filename.split(".")[-1]
    new_filename = f"{uuid.uuid4()}.{ext}"
    return f"uploads/{instance.__class__.__name__.lower()}/{new_filename[2: 3]}/{new_filename}"
