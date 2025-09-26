
# Set your Cloudinary credentials
# ==============================
from dotenv import load_dotenv
load_dotenv()

# Import the Cloudinary libraries
# ==============================
import cloudinary
from cloudinary import Config
import cloudinary.uploader

# Set configuration parameter: return "https" URLs by setting secure=True  
# ==============================
config: Config = cloudinary.config(secure=True)


def uploadImage(file) -> str:

  # Upload the image and get its URL
  # ==============================

  # Upload the image.
  # Set the asset's public ID and allow overwriting the asset with new versions
  response = cloudinary.uploader.upload(
        file,
        unique_filename=False,
        overwrite=True,
        asset_folder="chat-stream-api",
        resource_type="auto",
    )
  return response.get("secure_url")
