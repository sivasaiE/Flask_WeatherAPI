import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
# String which represents the QR code 
s = "www.google.com"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the svg file naming "myqr.svg" 
url.svg("google_qr_code.svg", scale = 8) 
  
# Create and save the png file naming "myqr.png" 
url.png('google_qr_code.png', scale = 6) 