from motion_detector_g4 import MotionDetector
from cv2 import cv2


print('Files method:')

md = MotionDetector(min_area=2000)

md.apply_first_frame('tests\\images\\01_frame_1.png')

print('Is motion? ' + str(md.check_motion('tests\\images\\01_frame_2.png')))
print('Is motion? ' + str(md.check_motion('tests\\images\\01_frame_3.png')))

# ------------------------------------------------------------------------------

print('\nFrames method:')

md_2 = MotionDetector(min_area=2000)

frame_1 = cv2.imread('tests\\images\\01_frame_1.png')
frame_2 = cv2.imread('tests\\images\\01_frame_2.png')
frame_3 = cv2.imread('tests\\images\\01_frame_3.png')

md_2.apply_first_frame(frame_1)
print('Is motion? ' + str(md.check_motion(frame_2)))
print('Is motion? ' + str(md.check_motion(frame_3)))
