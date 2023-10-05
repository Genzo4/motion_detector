import pytest
from motion_detector_g4 import MotionDetector
from cv2 import cv2


frame_1_path = 'tests/images/01_frame_1.png'
frame_2_path = 'tests/images/01_frame_2.png'
frame_3_path = 'tests/images/01_frame_3.png'
frame_4_path = 'tests/images/01_frame_4.png'

frame_1 = cv2.imread(frame_1_path)
frame_2 = cv2.imread(frame_2_path)
frame_3 = cv2.imread(frame_3_path)
frame_4 = cv2.imread(frame_4_path)


def test_1():
    md = MotionDetector()
    md.apply_first_frame(frame_1)
    assert md.check_motion(frame_2) is False


def test_2():
    md = MotionDetector()
    md.apply_first_frame(frame_2)
    assert md.check_motion(frame_3) is False


def test_3():
    md = MotionDetector()
    md.apply_first_frame(frame_3)
    assert md.check_motion(frame_4) is False


def test_4():
    md = MotionDetector(min_area=2000)
    md.apply_first_frame(frame_1)
    assert md.check_motion(frame_2) is True


def test_5():
    md = MotionDetector(min_area=2000)
    md.apply_first_frame(frame_2)
    assert md.check_motion(frame_3) is True


def test_6():
    md = MotionDetector(min_area=2000)
    md.apply_first_frame(frame_1)
    assert md.check_motion(frame_2) is True
    assert md.check_motion(frame_3) is True


def test_7():
    md = MotionDetector()
    md.apply_first_frame(frame_1)
    assert md.check_motion(frame_2) is False
    assert md.check_motion(frame_3) is False
