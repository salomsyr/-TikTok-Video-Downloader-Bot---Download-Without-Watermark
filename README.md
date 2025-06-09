<div align="center">
  
**© 2025 Developed by ALSALOM**  
[www.alsalom.com](https://www.alsalom.com)

<div dir="rtl" align="center">
  
**© 2025 تم التطوير بواسطة شركة السَّلَم**  
[www.alsalom.com](https://www.alsalom.com)

</div>
</div>

---

# 🚀 TikTok Video Downloader Bot - Download Without Watermark

<div dir="rtl">
# 🚀 بوت تيليجرام لتحميل فيديوهات التيك توك بدون علامة مائية
</div>

A powerful Telegram bot that lets you download TikTok videos without watermarks. Fast, reliable, and easy to use!

<div dir="rtl">
بوت تيليجرام قوي يمكنك من تحميل فيديوهات التيك توك بدون علامة مائية. سريع، موثوق وسهل الاستخدام!
</div>

![GitHub stars](https://img.shields.io/github/stars/username/repo?style=social) ![GitHub forks](https://img.shields.io/github/forks/username/repo?style=social) ![GitHub license](https://img.shields.io/github/license/username/repo)

<div dir="rtl">
بوت تيليجرام لتحميل فيديوهات تيك توك بدون علامة مائية.
</div>

## 🌟 Features | المميزات

- Download TikTok videos without watermarks
  <div dir="rtl">تحميل فيديوهات تيك توك بدون علامة مائية</div>
- Simple and easy to use
  <div dir="rtl">سهل الاستخدام</div>
- Supports direct links from TikTok app
  <div dir="rtl">يدعم الروابط المباشرة من تطبيق تيك توك</div>
- Fast and reliable downloads
  <div dir="rtl">تحميل سريع وموثوق</div>

## ⚙️ Requirements | المتطلبات

- Python 3.7 or higher
  <div dir="rtl">بايثون 3.7 أو أحدث</div>
- pip package manager
  <div dir="rtl">مدير حزم بايثون</div>
- ffmpeg (for video processing)
  <div dir="rtl">(للمعالجة الفيديوهات) ffmpeg</div>

## 🚀 One-Click Setup | التثبيت بنقرة واحدة

### Method 1: Automatic Setup (Recommended)
<div dir="rtl">
### الطريقة الأولى: التثبيت التلقائي (موصى به)
</div>

1. Download the bot files
   <div dir="rtl">قم بتحميل ملفات البوت</div>
2. Double-click on `start.bat`
   <div dir="rtl">انقر مرتين على ملف `start.bat`</div>
3. That's it! The bot will automatically:
   - Install Python if needed
   - Install all required packages
   - Ask you for your Telegram bot token (get it from @BotFather)
   - Start the bot

   <div dir="rtl">
   هذا كل شيء! سيقوم البوت تلقائياً بـ:
   - تثبيت بايثون إذا لم يكن مثبتاً
   - تثبيت جميع المكتبات المطلوبة
   - يطلب منك إدخال توكن البوت (احصل عليه من @BotFather)
   - تشغيل البوت
   </div>

> **Note:** First-time setup might take a few minutes to complete.
> <div dir="rtl">**ملاحظة:** قد تستغرق عملية الإعداد الأولى بضع دقائق.</div>

### Method 2: Manual Installation (Advanced Users)
<div dir="rtl">
### الطريقة الثانية: التثبيت اليدوي (للمستخدمين المتقدمين)
</div>

1. Clone this repository or download the files
   <div dir="rtl">قم باستنساخ المستودع أو تحميل الملفات</div>
2. Install the required packages:
   <div dir="rtl">قم بتثبيت الحزم المطلوبة:</div>
   ```
   pip install -r requirements.txt
   ```
3. Run the bot:
   <div dir="rtl">قم بتشغيل البوت:</div>
   ```
   python tiktok_bot.py
   ```

## 🎮 Usage | طريقة الاستخدام

1. Start the bot by running `python tiktok_bot.py` or using `start.bat`
   <div dir="rtl">قم بتشغيل البوت عن طريق كتابة `python tiktok_bot.py` أو باستخدام ملف `start.bat`</div>
2. Open Telegram and find your bot
   <div dir="rtl">افتح تطبيق تيليجرام وابحث عن البوت الخاص بك</div>
3. Send any TikTok video link to the bot
   <div dir="rtl">أرسل أي رابط فيديو تيك توك للبوت</div>
4. The bot will download and send you the video without watermark
   <div dir="rtl">سيقوم البوت بتحميل الفيديو وإرساله لك بدون علامة مائية</div>

## 🔧 Customization | التخصيص

You can customize the bot name by editing the `BOT_NAME` variable in `tiktok_bot.py`
<div dir="rtl">
يمكنك تخصيص اسم البوت عن طريق تعديل المتغير `BOT_NAME` في ملف `tiktok_bot.py`
</div>

## 📝 Notes | ملاحظات

- The bot requires an active internet connection
  <div dir="rtl">يحتاج البوت إلى اتصال بالإنترنت</div>
- Some videos might be restricted by TikTok
  <div dir="rtl">بعض الفيديوهات قد تكون مقيدة من تيك توك</div>
- Make sure you have enough storage space for downloaded videos
  <div dir="rtl">تأكد من توفر مساحة كافية لتخزين الفيديوهات المحملة</div>

## ☁️ 24/7 Hosting Guide | دليل التشغيل على الاستضافة

### Files to Upload for Hosting | الملفات المطلوبة للرفع على الاستضافة

For 24/7 operation, you'll need to upload these files to your hosting provider:
<div dir="rtl">
لتشغيل البوت على مدار الساعة، ستحتاج لرفع الملفات التالية على مزود الاستضافة:
</div>

```
📁 tiktok-downloader-bot/
├── tiktok_bot.py      # Main bot code
├── requirements.txt    # Required Python packages
├── .env               # Your bot token (create this file)
├── start.sh           # Startup script for Linux hosting
└── README.md          # This guide
```

### Step-by-Step Hosting Guide | خطوات التشغيل على الاستضافة

1. **Get a VPS or Hosting**
   - Recommended: Ubuntu 20.04/22.04 VPS (from DigitalOcean, Linode, etc.)
   - Minimum requirements: 1GB RAM, 1 CPU core, 25GB storage
   
   <div dir="rtl">
   **احصل على سيرفر VPS أو استضافة**
   - موصى به: خادم VPS أوبنتو 20.04/22.04 (من DigitalOcean أو Linode أو غيرها)
   - الحد الأدنى: 1 جيجابايت ذاكرة عشوائية، معالج أحادي، 25 جيجابايت مساحة تخزين
   </div>

2. **Connect to Your Server**
   ```bash
   ssh root@your_server_ip
   ```
   <div dir="rtl">
   **الاتصال بالسيرفر**
   </div>

3. **Install Required Software**
   ```bash
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install Python and pip
   sudo apt install python3 python3-pip python3-venv ffmpeg -y
   
   # Install git (if needed)
   sudo apt install git -y
   ```
   <div dir="rtl">
   **تثبيت البرامج المطلوبة**
   </div>

4. **Upload Bot Files**
   - Use SFTP (like FileZilla) or SCP to upload the files
   - Or clone directly:
   ```bash
   git clone your_repository_url
   cd your_repository_name
   ```
   <div dir="rtl">
   **رفع ملفات البوت**
   - استخدم SFTP (مثل FileZilla) أو SCP لرفع الملفات
   - أو استنسخ مباشرة من المستودع
   </div>

5. **Create .env File**
   ```bash
   echo "TELEGRAM_BOT_TOKEN=your_bot_token_here" > .env
   ```
   <div dir="rtl">
   **إنشاء ملف .env**
   </div>

6. **Create start.sh**
   Create a file named `start.sh` with these contents:
   ```bash
   #!/bin/bash
   cd $(dirname "$0")
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python3 tiktok_bot.py
   ```
   Then make it executable:
   ```bash
   chmod +x start.sh
   ```
   <div dir="rtl">
   **إنشاء ملف start.sh**
   </div>

7. **Run with PM2 (Keeps it running 24/7)**
   ```bash
   # Install Node.js and npm
   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   sudo apt install -y nodejs
   
   # Install PM2
   sudo npm install -g pm2
   
   # Start the bot with PM2
   pm2 start start.sh --name "tiktok-bot"
   
   # Make PM2 start on boot
   pm2 startup
   pm2 save
   ```
   <div dir="rtl">
   **التشغيل باستخدام PM2 (لضمان استمرارية العمل)**
   </div>

### Managing Your Bot | إدارة البوت

- View logs: `pm2 logs tiktok-bot`
- Restart bot: `pm2 restart tiktok-bot`
- Stop bot: `pm2 stop tiktok-bot`
- Delete bot: `pm2 delete tiktok-bot`

<div dir="rtl">
- عرض السجلات: `pm2 logs tiktok-bot`
- إعادة تشغيل البوت: `pm2 restart tiktok-bot`
- إيقاف البوت: `pm2 stop tiktok-bot`
- حذف البوت: `pm2 delete tiktok-bot`
</div>

## 📜 License | الترخيص

MIT License

## 🤝 Support | الدعم

For support, please open an issue on GitHub
<div dir="rtl">
للحصول على الدعم، يرجى فتح مشكلة جديدة على جيت هاب
</div>

## Logs

Logs are saved to `bot.log` in the same directory as the script.

## Requirements

- python-telegram-bot==20.7
- yt-dlp==2025.5.22
- python-dotenv==1.1.0

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue on the GitHub repository.
