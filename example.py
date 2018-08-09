# Import everything needed to edit video clips
from moviepy.editor import *

client_name = "Shane"
client_appointment_time = "2:30pm"
client_date_time = "Thursday August 14th"
client_barber = "John Smith"

# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clip = VideoFileClip("bshop.mp4")


# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip("Hi "+client_name,fontsize=170,color='black', font="Georgia", bg_color="white")

# Say that you want it to appear 10s at the center of the screen
txt_clip = txt_clip.set_pos('center').set_duration(3)

appointment_time_clip = TextClip(client_appointment_time+" "+client_date_time, fontsize=140, color='black',font="Georgia", bg_color="white")

appointment_time_clip = appointment_time_clip.set_pos('center').set_start(t='00:00:07.05').set_duration(3)

barber_name = TextClip(client_barber, fontsize=170, color='black',font="Georgia", bg_color="white")

barber_name = barber_name.set_pos('center').set_start(t='00:00:15.05').set_duration(3)
# Overlay the text clip on the first video clip
video = CompositeVideoClip([clip, txt_clip, appointment_time_clip, barber_name])

# Write the result to a file (many options available !)
video.write_videofile("bla.mp4")