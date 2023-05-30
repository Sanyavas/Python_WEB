import hashlib

import cloudinary
import cloudinary.uploader

from src.conf.config import settings


class UploadService:
    cloudinary.config(
        cloud_name=settings.cloudinary_name,
        api_key=settings.cloudinary_api_key,
        api_secret=settings.cloudinary_api_secret,
        secure=True
    )

    @staticmethod
    def create_name_avatar(email: str, prefix: str):
        """
        The create_name_avatar function takes an email address and a prefix,
        and returns a string of the form 'prefix/name'. The name is derived from the
        email address by taking the first 12 characters of its SHA256 hash. This ensures that
        the name is unique for each user.

        :param email: str: Specify the type of data that is passed into the function
        :param prefix: str: Specify the folder where the avatar will be stored
        :return: A string
        """
        name = hashlib.sha256(email.encode()).hexdigest()[:12]
        return f"{prefix}/{name}"

    @staticmethod
    def upload(file, public_id):
        """
        The upload function takes a file and public_id as arguments.
        It then uploads the file to Cloudinary using the public_id provided.
        The function returns a dictionary containing information about the uploaded image.

        :param file: Specify the file to upload
        :param public_id: Specify the public id of the image
        :return: A dictionary of information about the uploaded image
        """
        r = cloudinary.uploader.upload(file, public_id=public_id, overwrite=True)
        return r

    @staticmethod
    def get_url_avatar(public_id, version):
        """
        The get_url_avatar function takes in a public_id and version number,
            then returns the url of the avatar image.

        :param public_id: Identify the image in cloudinary
        :param version: Specify the version of the image to be returned
        :return: A url for the avatar image
        """
        src_url = cloudinary.CloudinaryImage(public_id) \
            .build_url(width=250, height=250, crop='fill', version=version)
        return src_url



