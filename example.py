from motion_detector_g4 import MotionDetector


md = MotionDetector(minArea=2000)
md.applyFirstFrame('tests\\images\\01_frame_1.png')
print('Is motion? ' + str(md.checkMotion('tests\\images\\01_frame_2.png')))
print('Is motion? ' + str(md.checkMotion('tests\\images\\01_frame_3.png')))
