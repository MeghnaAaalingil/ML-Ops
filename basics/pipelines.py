# Import necessary modules
import os

# Install ZenML if not already installed
try:
    import zenml
except ImportError:
    os.system('pip install zenml')

# Remove the .zen directory if it exists
import shutil

zen_path = '.zen'
if os.path.exists(zen_path) and os.path.isdir(zen_path):
    shutil.rmtree(zen_path)
    print(f"Removed directory: {zen_path}")
else:
    print(f"Directory does not exist: {zen_path}")

# Initialize ZenML
os.system('zenml init')

# Check if running in Google Colab
def in_google_colab():
    try:
        from google.colab import drive
        return True
    except ImportError:
        return False

# Install and authenticate ngrok if in Google Colab
NGROK_TOKEN = "2mnxVcR5odxKngSzOkjaGFhTew5_5NeWanPMKhz6p8kLuhadH"
if in_google_colab():
    os.system('pip install pyngrok')
    from pyngrok import ngrok
    ngrok.set_auth_token(NGROK_TOKEN)

print("Script executed successfully.")
