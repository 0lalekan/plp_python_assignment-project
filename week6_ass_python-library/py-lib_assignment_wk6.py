import os
import requests
from urllib.parse import urlparse

def fetch_image():
    url = input("Enter the URL of the image: ").strip()

    # Create the folder if it doesn’t exist
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise error for bad status codes

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, create one
        if not filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join(folder, filename)

        # Save image in binary mode
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✅ Image successfully fetched and saved as {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching image: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

# Run the function
if __name__ == "__main__":
    fetch_image()
