from dotenv import load_dotenv
import os


load_dotenv('configs/.env')

SHEET_ID = os.getenv('SHEET_ID')
FLODER_NAME = os.getenv('FLODER_NAME')#
DRIVE_ID  = os.getenv('DRIVE_ID')
