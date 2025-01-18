import logging

# إعداد logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# إعداد Handler (تسجيل في ملف)
file_handler = logging.FileHandler('checkout.log')
file_handler.setLevel(logging.INFO)

# إعداد Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# إضافة الـ Handler إلى الـ logger
logger.addHandler(file_handler)
