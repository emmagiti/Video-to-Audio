#!/usr/bin/env python
# coding: utf-8

# ### convert video to audio

# In[ ]:


pip install moviepy


# In[ ]:


import moviepy.editor
from tkinter.filedialog import *

video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
audio = video.audio

audio.write_audiofile("sample.mp3")
print("Completed!")


# In[ ]:




