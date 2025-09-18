import requests
import json
import os
from time import sleep

class RubikaBot:
    def __init__(self):
        # Initialize base URL and session
        self.base_url = 'https://messengerg2c280.iranlms.ir/'
        self.session = requests.Session()
        self.phone_number = None
        self.authenticated = False

    def login(self, phone_number):
        # Store phone number and attempt to send verification code
        self.phone_number = phone_number
        print(f"در حال ارسال کد تأیید به شماره تلفن {phone_number}...\n"
              f"Sending verification code to phone number {phone_number}...\n"
              f"正在向电话号码 {phone_number} 发送验证码...\n"
              f"Отправка кода подтверждения на номер телефона {phone_number}...")
        
        # Send request to get verification code
        try:
            url = f'{self.base_url}auth/send_code'
            response = self.session.post(url, json={'phone_number': self.phone_number})
            response_data = response.json()
            
            if response_data.get('status') == 'OK':
                print("کد تأیید به شماره تلفن ارسال شده است.\n"
                      "Verification code sent to phone number.\n"
                      "验证码已发送至电话号码。\n"
                      "Код подтверждения отправлен на номер телефона.")
                return True
            else:
                print(f"خطا در ارسال کد تأیید: {response_data.get('status')}\n"
                      f"Error sending verification code: {response_data.get('status')}\n"
                      f"发送验证码时出错：{response_data.get('status')}\n"
                      f"Ошибка при отправке кода подтверждения: {response_data.get('status')}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"خطا در اتصال به API: {e}\n"
                  f"Error connecting to API: {e}\n"
                  f"连接到 API 时出错：{e}\n"
                  f"Ошибка подключения к API: {e}")
            return False

    def verify_code(self, verification_code):
        # Attempt to verify the provided code
        print("در حال تأیید کد...\n"
              "Verifying code...\n"
              "正在验证代码...\n"
              "Проверка кода...")
        try:
            url = f'{self.base_url}auth/verify_code'
            response = self.session.post(url, json={'phone_number': self.phone_number, 'code': verification_code})
            response_data = response.json()
            
            if response_data.get('status') == 'OK':
                print("تأیید با موفقیت انجام شد!\n"
                      "Verification successful!\n"
                      "验证成功！\n"
                      "Проверка прошла успешно!")
                self.authenticated = True
                return True
            else:
                print(f"خطا در تأیید کد: {response_data.get('status')}\n"
                      f"Error verifying code: {response_data.get('status')}\n"
                      f"验证代码时出错：{response_data.get('status')}\n"
                      f"Ошибка при проверке кода: {response_data.get('status')}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"خطا در اتصال به API: {e}\n"
                  f"Error connecting to API: {e}\n"
                  f"连接到 API 时出错：{e}\n"
                  f"Ошибка подключения к API: {e}")
            return False

    def download_files(self, links, save):
        # Start downloading files from provided links
        print('   \033[1;33mStarting to download Files . . .\n\033[1;32m\n'
              '   \033[1;33mStarting to download Files . . .\n\033[1;32m\n'
              '   \033[1;33m开始下载文件 . . .\n\033[1;32m\n'
              '   \033[1;33mНачинается загрузка файлов . . .\n\033[1;32m')
        for link in links:
            try:
                get_info = bot.get_link_info(link)
                guid = get_info['object_guid']
                message_id = get_info['message_id']
                don = bot.download_file(guid, message_id, save=save)
                print(f"{don}\n"
                      f"Developed by Hamid Yarali\n"
                      f"GitHub: https://github.com/HamidYaraliOfficial\n"
                      f"Instagram: https://www.instagram.com/hamidyaraliofficial?igsh=MWpxZjhhMHZuNnlpYQ==\n"
                      f"Telegram: @Hamid_Yarali\n")
                if not save:
                    os.remove(don['file_inline']['file_name'])
                sleep(8)
            except Exception as e:
                print(f"خطا در دانلود فایل: {e}\n"
                      f"Error downloading file: {e}\n"
                      f"下载文件时出错：{e}\n"
                      f"Ошибка при загрузке файла: {e}")

# Example usage
if __name__ == "__main__":
    bot = RubikaBot()
    
    # Prompt user for phone number and login
    phone_number = input("لطفا شماره تلفن خود را وارد کنید (با کد کشور):\n"
                         "Please enter your phone number (with country code):\n"
                         "请输入您的电话号码（带国家代码）：\n"
                         "Пожалуйста, введите ваш номер телефона (с кодом страны): ")
    
    if bot.login(phone_number):
        verification_code = input("لطفا کد تأیید را وارد کنید:\n"
                                 "Please enter the verification code:\n"
                                 "请输入验证码：\n"
                                 "Пожалуйста, введите код подтверждения: ")
        if bot.verify_code(verification_code):
            # If verified, start downloading posts
            links = [
                'link1',  # Replace with actual post links
                'link2',
                'link3'
            ]
            save = input('آیا می‌خواهید فایل‌های دانلود شده ذخیره شوند؟ [y / n]:\n'
                         'Do you want to save the downloaded files? [y / n]:\n'
                         '您想保存下载的文件吗？[y / n]:\n'
                         'Хотите сохранить загруженные файлы? [y / n]: ').lower() == 'y'
            bot.download_files(links, save)