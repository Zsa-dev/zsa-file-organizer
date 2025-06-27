
import os
import shutil

# مسیر پوشه Downloads کاربر
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
organized_folder = os.path.join(downloads_folder, "organized")

# دیکشنری دسته‌بندی فایل‌ها
file_types = {
    "ZSA images": [".jpg", ".jpeg", ".png", ".gif"],
    "ZSA videos": [".mp4", ".mov", ".avi"],
    "ZSA documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "ZSA archives": [".zip", ".rar", ".7z"],
}

# ساخت پوشه اصلی 'organized' در Downloads
os.makedirs(organized_folder, exist_ok=True)

# ساخت پوشه‌های دسته‌بندی‌شده
for folder in file_types:
    folder_path = os.path.join(organized_folder, folder)
    os.makedirs(folder_path, exist_ok=True)

# ساخت پوشه 'other' برای فایل‌هایی که دسته‌بندی نمی‌شوند
other_folder = os.path.join(organized_folder, "other")
os.makedirs(other_folder, exist_ok=True)

# پردازش فایل‌ها
for filename in os.listdir(downloads_folder):
    filepath = os.path.join(downloads_folder, filename)

    # فقط فایل‌ها پردازش شوند (نه پوشه‌ها)
    if os.path.isfile(filepath):
        moved = False
        for folder, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                destination = os.path.join(organized_folder, folder, filename)
                shutil.move(filepath, destination)
                moved = True
                print(f"Moved: {filename} → {folder}")
                break

        if not moved:
            destination = os.path.join(other_folder, filename)
            shutil.move(filepath, destination)
            print(f"Moved: {filename} → other")

