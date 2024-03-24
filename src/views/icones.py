
import customtkinter as ctk
from PIL import Image
import os

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icon")



illustration_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "illustration.png")),
                          dark_image=Image.open(os.path.join(image_path, "illustration.png")), size=(400, 400))

linkedin_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "linkedin.png")),
                          dark_image=Image.open(os.path.join(image_path, "linkedin.png")), size=(60, 60))

github_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "github.png")),
                          dark_image=Image.open(os.path.join(image_path, "github.png")), size=(60, 60))

website_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "website.png")),
                          dark_image=Image.open(os.path.join(image_path, "website.png")), size=(60, 60))

world1_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "world1.png")),
                          dark_image=Image.open(os.path.join(image_path, "world1.png")), size=(200, 200))


world2_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "world2.png")),
                          dark_image=Image.open(os.path.join(image_path, "world2.png")), size=(200, 200))


world3_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "world3.png")),
                          dark_image=Image.open(os.path.join(image_path, "world3.png")), size=(200, 200))

back_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "back_black.png")),
                          dark_image=Image.open(os.path.join(image_path, "back_light.png")), size=(60, 60))



copy_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "copy.png")),
                          dark_image=Image.open(os.path.join(image_path, "copy.png")), size=(50, 50))