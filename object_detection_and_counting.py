# This file detects objects and counts the number of the detected objects.

print("Hello World")
"""import cv2
import numpy as np

# Initialize video capture (replace with your video path if needed)
cap = cv2.VideoCapture(r"C:\myprogsPY\OpenCV\AeroNITK_Assgt_video_2.mp4")

# Coordinates for the virtual counting line (adjust based on frame resolution)
# Format: (x1, y1) to (x2, y2)
COUNT_LINE_Y = 500  # Example horizontal line across the middle

# Tracking variables
white_car_count = 0
red_car_count = 0
tracked_cars = {}
car_id_counter = 0

def get_vehicle_color(roi_hsv):
    Determines if the detected object is Red or White based on HSV thresholds
    # Red has two ranges in HSV
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])
    
    # White: Low saturation, High value
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 30, 255])
    
    mask_red1 = cv2.inRange(roi_hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(roi_hsv, lower_red2, upper_red2)
    mask_red = mask_red1 + mask_red2
    
    mask_white = cv2.inRange(roi_hsv, lower_white, upper_white)
    
    if np.sum(mask_red) > np.sum(mask_white) and np.sum(mask_red) > 500:
        return "Red"
    elif np.sum(mask_white) > 500:
        return "White"
    return None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
        
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Simple Background Subtraction or Thresholding to find moving/distinct objects
    # For a top-down view, thresholding or contour detection on edges works well
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    current_centroids = []
    
    for contour in contours:
        if cv2.contourArea(contour) < 400:  # Filter out noise
            continue
            
        (x, y, w, h) = cv2.boundingRect(contour)
        cx = int(x + w / 2)
        cy = int(y + h / 2)
        
        # Crop the bounding box to analyze color
        roi_hsv = hsv[y:y+h, x:x+w]
        color = get_vehicle_color(roi_hsv)
        
        if color in ["White", "Red"]:
            current_centroids.append((cx, cy, color, (x, y, w, h)))

    # --- Basic Tracking & Counting Logic ---
    # Draw the counting line
    cv2.line(frame, (0, COUNT_LINE_Y), (frame.shape[1], COUNT_LINE_Y), (0, 255, 255), 2)
    
    for (cx, cy, color, bbox) in current_centroids:
        x, y, w, h = bbox
        
        # Draw bounding box and centroid
        color_bgr = (0, 0, 255) if color == "Red" else (255, 255, 255)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color_bgr, 2)
        cv2.circle(frame, (cx, cy), 4, (0, 255, 0), -1)
        
        # Check if the car crosses the line (simple cross check)
        # In a full tracking implementation, you would match IDs across frames.
        # This checks if a centroid is right at the threshold zone.
        if COUNT_LINE_Y - 5 < cy < COUNT_LINE_Y + 5:
            if color == "White":
                white_car_count += 1
            elif color == "Red":
                red_car_count += 1
                
    # Display counts on frame
    cv2.putText(frame, f"White Cars: {white_car_count}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f"Red Cars: {red_car_count}", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv2.imshow("Intersection Counter", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()"""


import cv2
import numpy as np

# Load the video file
video_path = r"C:\myprogsPY\OpenCV\AeroNITK_Assgt_video_2.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Create a resizable window first
cv2.namedWindow("Car Counting Assessment", cv2.WINDOW_NORMAL)
# Force the window to a clean desktop size (e.g., 1280x720)
cv2.resizeWindow("Car Counting Assessment", 1280, 720)

# Define a counting line relative to the display size we choose
# Since we will resize the frame to 1280x720, the mid-line X will be 640
COUNT_LINE_X = 640  

# Tracking sets to keep track of cars that have already crossed
crossed_white_ids = set()
crossed_red_ids = set()

white_count = 0
red_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # --- CRITICAL FIX FOR YOUR SCREEN ---
    # Downscale the frame immediately so it fits nicely on your monitor
    frame = cv2.resize(frame, (1280, 720))
    height, width, _ = frame.shape
    
    # Convert to HSV for robust color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 1. COLOR SEGMENTATION (MASKS)
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 40, 255])
    white_mask = cv2.inRange(hsv, lower_white, upper_white)
    
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([165, 70, 50])
    upper_red2 = np.array([180, 255, 255])
    red_mask = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)
    
    # 2. MORPHOLOGICAL CLEANUP 
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_CLOSE, kernel)
    white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_OPEN, kernel)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
    
    # 3. DETECT AND COUNT WHITE CARS
    contours_white, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours_white:
        area = cv2.contourArea(cnt)
        if 400 < area < 5000:  # Scaled down area thresholds since image resolution dropped
            x, y, w, h = cv2.boundingRect(cnt)
            cx, cy = int(x + w/2), int(y + h/2)
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
            
            if COUNT_LINE_X - 15 < cx < COUNT_LINE_X + 15:
                car_id = f"w_{cy // 25}" 
                if car_id not in crossed_white_ids:
                    crossed_white_ids.add(car_id)
                    white_count += 1

    # 4. DETECT AND COUNT RED CARS
    contours_red, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours_red:
        area = cv2.contourArea(cnt)
        if 300 < area < 5000:  # Scaled down area thresholds
            x, y, w, h = cv2.boundingRect(cnt)
            cx, cy = int(x + w/2), int(y + h/2)
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
            
            if COUNT_LINE_X - 15 < cx < COUNT_LINE_X + 15:
                car_id = f"r_{cy // 25}"
                if car_id not in crossed_red_ids:
                    crossed_red_ids.add(car_id)
                    red_count += 1

    # 5. DISPLAY RESULTS
    cv2.line(frame, (COUNT_LINE_X, 0), (COUNT_LINE_X, height), (0, 255, 255), 2)
    
    cv2.putText(frame, f"White Cars: {white_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f"Red Cars: {red_count}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv2.imshow("Car Counting Assessment", frame)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()