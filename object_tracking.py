# In this file we learn object tracking.

print("Hello World")

# We need to specify the initial location of the object for smooth object tracking.

"""import cv2 as cv
import sys
import os
import numpy as np

video_input = "C:\myprogsPY\OpenCV\AeroNITK_Assgt_video_1.mp4"

def drawRectangle(frame,bbox): # This function basically draws a rectangle on the image 'frame' by tkaing coordinates of the bounding box(bbox).
    p1 = (int(bbox[0]),int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]),int(bbox[1] + bbox[3]))
    cv.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

def displayRectangle(frame,bbox): # This function displays the drawn rectangle from previous function on a copy of the image 'frame'.
    frameCopy = frame.copy()
    drawRectangle(frameCopy, bbox)
    frameCopy = cv.cvtColor(frameCopy, cv.COLOR_RGB2BGR)
    cv.imshow('Image',frameCopy)

def drawText(frame, txt, location, color=(50, 170, 50)): # This function writes text on the image 'frame'.
    cv.putText(frame, txt, location, cv.FONT_HERSHEY_SIMPLEX, 1, color, 3)

# Set up tracker
tracker_types = ["BOOSTING","MIL","KCF","CSRT","TLD","MEDIANFLOW","GOTURN","MOSSE"] # These are all the different tracking algorithms in OpenCV.

# Change the index to change the tracker type
tracker_type = tracker_types[2]

if tracker_type == "BOOSTING":
    tracker = cv.legacy.TrackerBoosting.create()
elif tracker_type == "MIL":
    tracker = cv.legacy.TrackerMIL.create()
elif tracker_type == "KCF":
    tracker = cv.TrackerKCF.create()
elif tracker_type == "CSRT":
    tracker = cv.TrackerCSRT.create()
elif tracker_type == "TLD":
    tracker = cv.legacy.TrackerTLD.create()
elif tracker_type == "MEDIANFLOW":
    tracker = cv.legacy.TrackerMedianFlow.create()
elif tracker_type == "GOTURN":
    tracker = cv.TrackerGOTURN.create()
else:
    tracker = cv.legacy.TrackerMOSSE.create()

# Detailed explaination of all different algorithms - https://gemini.google.com/app/5342d2ffef427a8f

video = cv.VideoCapture(video_input)
ok, frame = video.read()
width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

print(width) # Output is 1920.
print(height) # Output is 1080.

# Writing on the video-

video_output = "silver_car-" + tracker_type + ".mp4"
video_out = cv.VideoWriter(video_output,cv.VideoWriter_fourcc(*"mp4v"),20,(width,height))

# Defining a bounding box-

bbox = cv.selectROI(frame,False)
print(bbox)""" # This is right if the object to be tracked is in the first frame but in our video it isnt in the first frame and hence we cant use it.

# We have to setup a way in which when the object appears for the first time we have to stop the video and draw the box.

"""video = cv.VideoCapture(video_input)
win_name = 'Video'
cv.namedWindow(win_name, cv.WINDOW_NORMAL)

while video.isOpened():
    has_frame, frame = video.read()
    cv.imshow("Video",frame)

    # We have to stop when object is seen and draw the bounding box-
    key = cv.waitKey(30) & 0xFF
    if key == ord('s'):
        bbox = cv.selectROI("Tracking Setup",frame,fromCenter = False,showCrosshair = True)
        print(bbox) # (500,20,95,75)
        cv.destroyWindow("Tracking Setup")
    elif key == ord('q'):
        break

video.release()
cv.destroyAllWindows()
     
while True:
    ok,frame = video.read()
    if not ok:
        break

    # Start timer-
    timer = cv.getTickCount()

    # Update tracker-
    ok,bbox = tracker.update(frame)

    # Calculate FPS-
    fps = cv.getTickFrequency()/(cv.getTickCount() - timer)

    # Drawing the bbox-
    if ok:
        drawRectangle(frame,bbox)
    
    # Displaying the video-
    cv.imshow("Tracking Window",frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Writing the video to the video_out file-
    if video_out:
        video_out.write(frame)

video.release()
if video_out:
    video_out.release()
cv.destroyAllWindows()"""


# Code from Gemini-
"""import cv2 as cv
import sys
import os
import numpy as np

# 1. FIX: Added 'r' before the string to make it a raw string (ignores escape chars)
video_input = r"C:\myprogsPY\OpenCV\AeroNITK_Assgt_video_1.mp4"

def drawRectangle(frame, bbox):
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

# Set up tracker
tracker_types = ["BOOSTING","MIL","KCF","CSRT","TLD","MEDIANFLOW","GOTURN","MOSSE"]
tracker_type = tracker_types[2] # KCF

if tracker_type == "BOOSTING":
    tracker = cv.legacy.TrackerBoosting.create()
elif tracker_type == "MIL":
    tracker = cv.legacy.TrackerMIL.create()
elif tracker_type == "KCF":
    tracker = cv.TrackerKCF.create()
elif tracker_type == "CSRT":
    tracker = cv.TrackerCSRT.create()
elif tracker_type == "TLD":
    tracker = cv.legacy.TrackerTLD.create()
elif tracker_type == "MEDIANFLOW":
    tracker = cv.legacy.TrackerMedianFlow.create()
elif tracker_type == "GOTURN":
    tracker = cv.TrackerGOTURN.create()
else:
    tracker = cv.legacy.TrackerMOSSE.create()

video = cv.VideoCapture(video_input)
if not video.isOpened():
    print("Error: Could not open video.")
    sys.exit()

width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

video_output = "silver_car-" + tracker_type + ".mp4"
video_out = cv.VideoWriter(video_output, cv.VideoWriter_fourcc(*"mp4v"), 20, (width, height))

# 2. FIX: Play video until the object appears, then press 's' to select ROI
bbox = None
win_name = 'Video Setup'
cv.namedWindow(win_name, cv.WINDOW_NORMAL)

while video.isOpened():
    has_frame, frame = video.read()
    if not has_frame:
        print("Reached end of video without selection.")
        break
        
    cv.imshow(win_name, frame)
    key = cv.waitKey(30) & 0xFF
    
    if key == ord('s'):
        # Select ROI
        bbox = cv.selectROI("Tracking Setup", frame, fromCenter=False, showCrosshair=True)
        cv.destroyWindow("Tracking Setup")
        
        # 3. CRITICAL FIX: Initialize the tracker with the selected bounding box!
        tracker.init(frame, bbox)
        break
    elif key == ord('q'):
        break

cv.destroyWindow(win_name)

# 4. Main Tracking Loop
while True:
    ok, frame = video.read()
    if not ok:
        break

    timer = cv.getTickCount()

    # Update tracker
    ok, bbox = tracker.update(frame)

    fps = cv.getTickFrequency() / (cv.getTickCount() - timer)

    # Drawing the bbox if tracking was successful
    if ok:
        drawRectangle(frame, bbox)
    else:
        cv.putText(frame, "Tracking failure detected", (100, 80), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    
    cv.imshow("Tracking Window", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
    if video_out:
        video_out.write(frame)

video.release()
if video_out:
    video_out.release()
cv.destroyAllWindows()"""

# Corrected code-
"""import cv2 as cv
import sys
import os
import numpy as np

video_input = r"C:\myprogsPY\OpenCV\AeroNITK_Assgt_video_1.mp4"

def drawRectangle(frame, bbox):
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

# Set up tracker
tracker_types = ["BOOSTING","MIL","KCF","CSRT","TLD","MEDIANFLOW","GOTURN","MOSSE"]

# --- CHANGED: Swapped tracker_type from index 2 (KCF) to index 3 (CSRT) ---
tracker_type = tracker_types[3] 

if tracker_type == "BOOSTING":
    tracker = cv.legacy.TrackerBoosting.create()
elif tracker_type == "MIL":
    tracker = cv.legacy.TrackerMIL.create()
elif tracker_type == "KCF":
    tracker = cv.TrackerKCF.create()
elif tracker_type == "CSRT":
    tracker = cv.TrackerCSRT.create()
elif tracker_type == "TLD":
    tracker = cv.legacy.TrackerTLD.create()
elif tracker_type == "MEDIANFLOW":
    tracker = cv.legacy.TrackerMedianFlow.create()
elif tracker_type == "GOTURN":
    tracker = cv.TrackerGOTURN.create()
else:
    tracker = cv.legacy.TrackerMOSSE.create()

video = cv.VideoCapture(video_input)
if not video.isOpened():
    print("Error: Could not open video.")
    sys.exit()

width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

video_output = "silver_car-" + tracker_type + ".mp4"
video_out = cv.VideoWriter(video_output, cv.VideoWriter_fourcc(*"mp4v"), 20, (width, height))

# Play video until the object appears, then press 's' to select ROI
bbox = None
win_name = 'Video Setup'
cv.namedWindow(win_name, cv.WINDOW_NORMAL)

while video.isOpened():
    has_frame, frame = video.read()
    if not has_frame:
        print("Reached end of video without selection.")
        break
        
    cv.imshow(win_name, frame)
    key = cv.waitKey(30) & 0xFF
    
    if key == ord('s'):
        bbox = cv.selectROI("Tracking Setup", frame, fromCenter=False, showCrosshair=True)
        cv.destroyWindow("Tracking Setup")
        
        tracker.init(frame, bbox)
        break
    elif key == ord('q'):
        break

cv.destroyWindow(win_name)

# Main Tracking Loop
while True:
    ok, frame = video.read()
    if not ok:
        break

    timer = cv.getTickCount()

    # Update tracker
    ok, bbox = tracker.update(frame)

    fps = cv.getTickFrequency() / (cv.getTickCount() - timer)

    # Drawing the bbox if tracking was successful
    if ok:
        drawRectangle(frame, bbox)
    else:
        # If CSRT briefly loses the car, we display a warning but DON'T stop the video.
        # It allows the loop to continue writing and rendering frames till the end.
        cv.putText(frame, "Tracking failure detected", (100, 80), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    
    cv.imshow("Tracking Window", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
    if video_out:
        video_out.write(frame)

video.release()
if video_out:
    video_out.release()
cv.destroyAllWindows()"""

# Another code-
import cv2 as cv
import sys
import os
import numpy as np

# 1. Video Path (using raw string to avoid escape character bugs)
video_input = r"C:\myprogsPY\OpenCV\AeroNITK_Assgt_video_1.mp4"

def drawRectangle(frame, bbox):
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

# Set up tracker
tracker_types = ["BOOSTING","MIL","KCF","CSRT","TLD","MEDIANFLOW","GOTURN","MOSSE"]
# Using CSRT (Index 3) because it handles scale changes and stays locked until the end
tracker_type = tracker_types[3] 

if tracker_type == "BOOSTING":
    tracker = cv.legacy.TrackerBoosting.create()
elif tracker_type == "MIL":
    tracker = cv.legacy.TrackerMIL.create()
elif tracker_type == "KCF":
    tracker = cv.TrackerKCF.create()
elif tracker_type == "CSRT":
    tracker = cv.TrackerCSRT.create()
elif tracker_type == "TLD":
    tracker = cv.legacy.TrackerTLD.create()
elif tracker_type == "MEDIANFLOW":
    tracker = cv.legacy.TrackerMedianFlow.create()
elif tracker_type == "GOTURN":
    tracker = cv.TrackerGOTURN.create()
else:
    tracker = cv.legacy.TrackerMOSSE.create()

video = cv.VideoCapture(video_input)
if not video.isOpened():
    print("Error: Could not open video.")
    sys.exit()

width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

video_output = "silver_car-" + tracker_type + ".mp4"
video_out = cv.VideoWriter(video_output, cv.VideoWriter_fourcc(*"mp4v"), 20, (width, height))

# Setup the initial playback window so it fits your 1265x684 screen perfectly
win_name = 'Video Setup'
cv.namedWindow(win_name, cv.WINDOW_NORMAL)
cv.resizeWindow(win_name, 960, 540)

bbox = None

print("Instructions: Press 's' when the car appears to select it. Press 'q' to quit.")

while video.isOpened():
    has_frame, frame = video.read()
    if not has_frame:
        print("Reached end of video without selection.")
        break
        
    cv.imshow(win_name, frame)
    key = cv.waitKey(30) & 0xFF
    
    if key == ord('s'):
        # --- FIX FOR OVERSIZED WINDOW ---
        win_roi = "Tracking Setup"
        cv.namedWindow(win_roi, cv.WINDOW_NORMAL)
        cv.resizeWindow(win_roi, 960, 540) # Forces the selection window to fit your screen
        
        # Select ROI inside the explicitly scaled window
        bbox = cv.selectROI(win_roi, frame, fromCenter=False, showCrosshair=True)
        cv.destroyWindow(win_roi)
        
        # Initialize the tracker with the selected coordinates
        tracker.init(frame, bbox)
        break
        
    elif key == ord('q'):
        break

# Close the setup window before moving to the main loop
cv.destroyWindow(win_name)

# Create a resizable window for the final tracking playback as well
cv.namedWindow("Tracking Window", cv.WINDOW_NORMAL)
cv.resizeWindow("Tracking Window", 960, 540)

# Main Tracking Loop
while True:
    ok, frame = video.read()
    if not ok:
        break

    timer = cv.getTickCount()

    # Update tracker
    ok, bbox = tracker.update(frame)

    fps = cv.getTickFrequency() / (cv.getTickCount() - timer)

    # Drawing the bbox if tracking was successful
    if ok:
        drawRectangle(frame, bbox)
    else:
        cv.putText(frame, "Tracking failure detected", (100, 80), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    
    cv.imshow("Tracking Window", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
    if video_out:
        video_out.write(frame)

video.release()
if video_out:
    video_out.release()
cv.destroyAllWindows()
print("Tracking completed successfully!")

