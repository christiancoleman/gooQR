import qrcode
import sys

# https://dan.hersam.com/tools/gen-qr-code.html
# https://i.imgur.com/bN86wwh.png

# Label: Example
# User: alice@google.com
# Key: AABBCC993311ABC
# Digits: 9 Optional - defaults is 6 digits
# Period: 60 Optional - defaults is 30 seconds

# The format the Google Authenticator application expects QR data to be stored
# otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example&digits=9&period=60

IS_DEBUG = True 
PROG_NAME = 'gooQR'
BASE_OTP_SECRET = 'otpauth://totp/%s:%s?secret=%s&issuer=%s'
BASE_OTP_SECRET_FULL = 'otpauth://totp/%s:%s?secret=%s&issuer=%s&digits=%s&period=%s'
OPTIONAL_DIGITS = '&digits=%s'
OPTIONAL_PERDIO = '&period=%s'
NUM_ARGS = len(sys.argv)
LABEL = ''
USER = ''
SECRET_KEY = ''
DIGITS = ''
PERIOD = ''

def check_args():
	if NUM_ARGS != 4 and NUM_ARGS != 6:
		print("Enter a label, username/email, and secret key.")
		print("OR enter a label, username/email, secret key, digits (to enter at login), and period of time (in seconds).")
		print('')
		print('Examples:')
		print('python ' + PROG_NAME + " AWS alice@wonderland.com AABBCC993311ABC")
		print('python ' + PROG_NAME + " 'AWS - Jared' jared@notwonderland.com ZZZTOP123JJABRAMS 12 60")
		exit()

def get_args():
        global LABEL
        global USER
        global SECRET_KEY
        global DIGITS
        global PERIOD 

	LABEL = sys.argv[1]
	USER = sys.argv[2]
	SECRET_KEY = sys.argv[3]
	if NUM_ARGS == 6:
		DIGITS = sys.argv[4]
		PERIOD = sys.argv[5]

def debug_print():
    global LABEL
    global USER
    global SECRET_KEY
    global DIGITS
    global PERIOD

    print("sys.argv[0]=" + sys.argv[0])
    print("sys.argv[1]=" + sys.argv[1])
    print(LABEL)
    print(USER)
    print(SECRET_KEY)
    print(DIGITS)
    print(PERIOD)

def create_google_qr_img():
	if NUM_ARGS == 6:
		return qrcode.make(BASE_OTP_SECRET_FULL % (LABEL, USER, SECRET_KEY, LABEL, DIGITS, PERIOD))
	else:
		return qrcode.make(BASE_OTP_SECRET % (LABEL, USER, SECRET_KEY, LABEL))

def save_image(img):
	img.save(LABEL + '.png', 'PNG')

def main():
	check_args()
	get_args()
        if(IS_DEBUG): debug_print()
	img = create_google_qr_img()
	save_image(img)
	print('Everything looks good... Go ahead and try scanning your new barcode! :)')

main()
