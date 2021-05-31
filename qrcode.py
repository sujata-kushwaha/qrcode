import pyqrcode
# import png  #install pypng
import svg #install pysvg
from pyqrcode import QRCode
a="i'm anuradha kushwaha now i'm studing btech feild in a IT"
url=pyqrcode.create(a)
url.svg("myqr.svg",scale=7)
# url.png("myqr.png",scale=8)
