import pytest
from motion_detector_g4 import MotionDetector


def test_01_1():
    md = MotionDetector()
    md.applyFirstFrame('tests\\images\\01_frame_1.png')
    assert md.checkMotion('tests\\images\\01_frame_2.png') == False


def test_01_2():
    md = MotionDetector()
    md.applyFirstFrame('tests\\images\\01_frame_2.png')
    assert md.checkMotion('tests\\images\\01_frame_3.png') == False


def test_01_3():
    md = MotionDetector()
    md.applyFirstFrame('tests\\images\\01_frame_3.png')
    assert md.checkMotion('tests\\images\\01_frame_4.png') == False


def test_01_4():
    md = MotionDetector(minArea=2000)
    md.applyFirstFrame('tests\\images\\01_frame_1.png')
    assert md.checkMotion('tests\\images\\01_frame_2.png') == True


def test_01_5():
    md = MotionDetector(minArea=2000)
    md.applyFirstFrame('tests\\images\\01_frame_2.png')
    assert md.checkMotion('tests\\images\\01_frame_3.png') == True


def test_01_6():
    md = MotionDetector(minArea=2000)
    md.applyFirstFrame('tests\\images\\01_frame_1.png')
    assert md.checkMotion('tests\\images\\01_frame_2.png') == True
    assert md.checkMotion('tests\\images\\01_frame_3.png') == True


def test_01_7():
    md = MotionDetector()
    md.applyFirstFrame('tests\\images\\01_frame_1.png')
    assert md.checkMotion('tests\\images\\01_frame_2.png') == False
    assert md.checkMotion('tests\\images\\01_frame_3.png') == False


def test_02_1():
    md = MotionDetector()
    md.applyFirstFrame('tests\\images\\02_frame_1.png')
    assert md.checkMotion('tests\\images\\02_frame_2.png') == False


def test_03_1():
    md = MotionDetector()
    md.applyFirstFrame('tests\\images\\03_frame_1.bmp')
    assert md.checkMotion('tests\\images\\03_frame_2.bmp') == False


def test_03_2():
    md = MotionDetector()
    md.applyFirstFrame('tests\\images\\03_frame_1.bmp')
    assert md.checkMotion('tests\\images\\03_frame_2.bmp') == False
    assert md.checkMotion('tests\\images\\03_frame_3.bmp') == False


def test_03_3():
    md = MotionDetector()
    md.applyFirstFrame('tests\\images\\03_frame_3.bmp')
    assert md.checkMotion('tests\\images\\03_frame_4.bmp') == True
