import os
os.system("pip install captcha")
import sys
from captcha.image import ImageCaptcha
import random
import hashlib
import secrets


def captcha():
    random_string = secrets.token_bytes(32)
    hash_value = hashlib.sha256(random_string)
    hash_hex = hash_value.hexdigest()[8:]
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    captcha_text = "".join(random.choices(characters, k=4))
    image_captcha = ImageCaptcha(width=180, height=60, fonts=None, font_sizes=(42,))
    captcha_image = image_captcha.generate_image(captcha_text)
    image_captcha.create_noise_dots(captcha_image, (0, 0, 0), 10)
    image_captcha.create_noise_curve(captcha_image, (0, 0, 0))
    image_captcha.create_noise_curve(captcha_image, (0, 0, 0))
    filepath = os.path.join('captcha', f"{captcha_text}_{hash_hex}.png")
    captcha_image.save(filepath)

# 读取命令行参数
if len(sys.argv) < 2:
    print("请传入要生成的验证码数量")
    sys.exit(1)

if not os.path.exists('captcha'):
    os.makedirs('captcha')

num_captchas = int(sys.argv[1])


for i in range(num_captchas):
    captcha()
    if (i) % 100 == 0:
        if i == 0:
            print('开始生成')
        else:
            print(f'已生成{i}个')

print('生成结束')
