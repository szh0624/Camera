[app]

# Application title
title = Camera App

# Package name
package.name = camerapp

# Package domain
package.domain = org.camerapp

# Source directory
source.include_exts = py,png,jpg,kv,atlas

# Application requirements
requirements = python3,kivy,kivymd,android

# Main application file
source.main = main.py

# Android specific
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.sdk = 24
android.ndk = 23b
android.arch = armeabi-v7a

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 1

# Presplash
presplash.filename = %(source.dir)s/data/presplash.png

# Icon
icon.filename = %(source.dir)s/data/icon.png

[buildozer]

# Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2
