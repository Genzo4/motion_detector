from motion_detector_g4 import MotionDetector


md = MotionDetector(min_area=2000)
md.apply_first_frame('tests\\images\\01_frame_1.png')
print('Is motion? ' + str(md.check_motion('tests\\images\\01_frame_2.png')))
print('Is motion? ' + str(md.check_motion('tests\\images\\01_frame_3.png')))
