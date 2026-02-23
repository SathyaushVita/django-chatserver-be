

from django.conf import settings
import base64
import os
import uuid
from azure.storage.blob import BlobServiceClient




def save_image_to_folder(image_data, _id, name, entity_type):
    decoded_image = base64.b64decode(image_data)
    folder_name = str(_id)
    img_url = settings.FILE_URL
    folder_path = os.path.join(img_url, entity_type, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    image_name = f"{name}_{uuid.uuid4().hex[:8]}.jpg"
    image_path = os.path.join(folder_path, image_name)
    with open(image_path, "wb") as image_file:
        image_file.write(decoded_image)
    relative_image_path = os.path.join(entity_type, folder_name, image_name)
    return relative_image_path



def save_image_to_azure(image_data, _id, name, entity_type):
    decoded_image = base64.b64decode(image_data)
    folder_name = str(_id)
    image_name = f"{name}_{uuid.uuid4().hex[:8]}.jpg"
    container_name = 'sathayush'
    folder_path = f"{entity_type}/{folder_name}/"
    blob_name = f"{folder_path}{image_name}"
    
    blob_service_client = BlobServiceClient.from_connection_string(settings.AZURE_STORAGE_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.upload_blob(decoded_image, blob_type="BlockBlob", overwrite=True)
    
    # Return full URL
    return f"{settings.FILE_URL}{blob_name}"


def save_video_to_azure(video_data, _id, name, entity_type):
    try:
        decoded_video = base64.b64decode(video_data)
        folder_name = str(_id)
        video_name = f"{name}_{uuid.uuid4().hex[:8]}.mp4"
        container_name = 'sathayush'
        folder_path = f"{entity_type}/{folder_name}/"
        blob_name = f"{folder_path}{video_name}"

        blob_service_client = BlobServiceClient.from_connection_string(settings.AZURE_STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_client.upload_blob(decoded_video, blob_type="BlockBlob", overwrite=True)

        # Return full URL
        return f"{settings.FILE_URL}{blob_name}"
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
