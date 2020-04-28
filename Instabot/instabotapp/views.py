from django.shortcuts import render, redirect
from .forms import DetailForm
from .models import DetailAccount
from django.views.generic import *
from django.urls import reverse
from django.http import HttpResponseRedirect

import os
import cv2
import exifread
import piexif
from instabot import Bot
from PIL import Image, ImageDraw, ImageFont
from PIL.ExifTags import TAGS

# from imgcleaner import *

class FormPosting(View):
    template_name = 'detail_form.html'
    form_class = DetailForm

    def get(self, request, *args, **kwargs):
        form = DetailForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = DetailForm()
        if request.method == "POST":
            form = DetailForm(request.POST, request.FILES)
            try:
                if form.is_valid():
                    form.save()
                    filename = self.covert_to_jpg(request.FILES['select_image'].name)
                    self.exifcleaner(filename)
                    self.imagecleaner(filename)
                    self.template_name = self.upload_photo_script(form)
                    # from django.http import HttpResponseRedirect
                    # return HttpResponseRedirect(reverse('successurl'))
                else: 
                    form = DetailForm() 
            except:
                return HttpResponseRedirect(reverse('errorurl'))
        return render(request, self.template_name, {'form':form})

    
    def covert_to_jpg(self, filename):
        from django.conf import settings
        os.chdir(settings.BASE_DIR+"/media/")
        im = Image.open(filename)
        file_ext = filename.split(".")
        if file_ext[1] in ['jpg', "jpeg"]:
            return filename
        else:
            rgb_im = im.convert('RGB')
            new_filename = file_ext[0] + ".jpeg"
            rgb_im.save(new_filename)
            os.remove(filename)
            return new_filename

    def exifcleaner(self, filename):
        image = Image.open(filename)
        image.getexif().clear()
        image.save("clean_" + filename)
        os.remove(filename)
        exif = piexif.load("clean_" + filename)
        image = Image.open("clean_" + filename)
        image_clean = Image.new(image.mode, image.size)
        image_clean.putdata(list(image.getdata()))
        image_clean.save("clean_" + filename)
        print("--------------Done :")
    
    def imagecleaner(self, filename):
        img = cv2.imread("clean_" + filename, cv2.IMREAD_UNCHANGED)
        try:
            mask = cv2.inRange(img, (255, 55, 0), (255, 255, 10))
            img[mask != 0] = [0, 0, 255]
            img_cord = (
                img.shape[1] - (img.shape[1] // 10),
                img.shape[0] - (img.shape[0] // 10))
            resized = cv2.resize(img, img_cord, interpolation=cv2.INTER_AREA)
            cv2.imwrite("clean_" + filename, resized)
        except:
            cv2.imwrite("clean_" + filename)
    
    def upload_photo_script(self, form):
        try:
            import pdb; pdb.set_trace()
            data = form.clean()
            username = data['username']
            password = data['password']
            caption = data['caption']
            filename = data['select_image'].name
            bot = Bot()
            bot.login(username=username, password=password)
            bot.upload_photo("clean_" + filename, caption=caption)
            os.remove(filename)
            os.remove("clean_" + filename)
            template_name = 'success.html'
            return template_name
        except:
            template_name = "error_message.html"
            return template_name

# def checking_existence(filename):
#     try:
#         if dir:
#             for x in dir:
#                 if x.startswith("clean_"):
#                     os.remove(x)
#         else:
#             pass
#     except:
#         print("Something Went Wrong. Try Again Later!")


# def exifcleaner(filename):
#     image = Image.open(filename)
#     image.getexif().clear()
#     image.save("clean_" + filename)

#     exif = piexif.load("clean_" + filename)
#     # print(exif)

#     image = Image.open("clean_" + filename)
#     # print(image._getexif())
#     image_clean = Image.new(image.mode, image.size)
#     image_clean.putdata(list(image.getdata()))
#     image_clean.save("clean_" + filename)


# def imagecleaner(filename):
#     img = cv2.imread("clean_" + filename, cv2.IMREAD_UNCHANGED)
#     # from PyQt5.QtCore import pyqtRemoveInputHook

#     # from pdb import set_trace
#     # pyqtRemoveInputHook()
#     # set_trace()
#     mask = cv2.inRange(img, (255, 55, 0), (255, 255, 10))
#     img[mask != 0] = [0, 0, 255]
#     img_cord = (
#         img.shape[1] - (img.shape[1] // 10),
#         img.shape[0] - (img.shape[0] // 10),
#     )
#     resized = cv2.resize(img, img_cord, interpolation=cv2.INTER_AREA)
#     cv2.imwrite("clean_" + filename, resized)

def successf(request):
    return render(request, 'success.html')

def errorf(request):
    return render(request, 'error_message.html')