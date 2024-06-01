import os
import time

# List of wallpaper file paths
wallpapers = [
    "/path/to/wallpaper1.jpg",
    "/path/to/wallpaper2.jpg",
    "/path/to/wallpaper3.jpg"
]

# Function to change the wallpaper
def set_wallpaper(wallpaper_path):
    os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{wallpaper_path}")

# Main function to switch wallpapers every 30 seconds
def switch_wallpapers():
    while True:
        for wallpaper in wallpapers:
            set_wallpaper(wallpaper)
            time.sleep(30)  # Switch wallpaper every 30 seconds

if __name__ == "__main__":
    switch_wallpapers()
