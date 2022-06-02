import pytest
from motion_detector_g4 import MotionDetector
import os
import glob
from itertools import chain
import os
import glob
from itertools import chain
import cv2


def _removeTempFiles() -> None:
    """
    Remove temp files
    :rtype: None
    :return: None
    """

    removeFiles = glob.iglob('tests/images/*.clear.*')
    removeFiles = chain(removeFiles, glob.iglob('tests/images/*.mask.*'))
    removeFiles = chain(removeFiles, glob.iglob('tests/images/*.blobs.*'))
    removeFiles = chain(removeFiles, glob.iglob('tests/images/*.blobs2.*'))

    for _file in removeFiles:
        os.remove(_file)


def test_1():
    md = MotionDetector()
    md.applyFirstFrame('tests/images/01_frame_1.png')
    md.checkMotion('tests/images/01_frame_2.png')
    assert os.path.exists('tests/images/01_frame_2.clear.png') == False
    assert os.path.exists('tests/images/01_frame_2.mask.png') == False
    assert os.path.exists('tests/images/01_frame_2.blobs.png') == False
    assert os.path.exists('tests/images/01_frame_2.blobs2.png') == False
    _removeTempFiles()


def test_2():
    md = MotionDetector(debug=True)
    md.applyFirstFrame('tests/images/01_frame_1.png')
    md.checkMotion('tests/images/01_frame_2.png')
    assert os.path.exists('tests/images/01_frame_2.clear.png') == True
    assert os.path.exists('tests/images/01_frame_2.mask.png') == True
    assert os.path.exists('tests/images/01_frame_2.blobs.png') == False
    assert os.path.exists('tests/images/01_frame_2.blobs2.png') == False
    _removeTempFiles()


def test_3():
    md = MotionDetector(minArea=2000, debug=True)
    md.applyFirstFrame('tests/images/01_frame_1.png')
    md.checkMotion('tests/images/01_frame_2.png')
    assert os.path.exists('tests/images/01_frame_2.clear.png') == True
    assert os.path.exists('tests/images/01_frame_2.mask.png') == True
    assert os.path.exists('tests/images/01_frame_2.blobs.png') == True
    assert os.path.exists('tests/images/01_frame_2.blobs2.png') == True
    _removeTempFiles()


def test_mask():
    md = MotionDetector(debug=True)
    md.applyFirstFrame('tests/images/01_frame_1.png')
    md.checkMotion('tests/images/01_frame_2.png')

    frameMask = cv2.imread('tests/images/01_frame_2.mask.png')

    (b, g, r) = frameMask[17, 65]
    assert int(r) + int(g) + int(b) == 765

    (b, g, r) = frameMask[38, 36]
    assert int(r) + int(g) + int(b) == 0

    (b, g, r) = frameMask[104, 1713]
    assert int(r) + int(g) + int(b) == 765

    (b, g, r) = frameMask[53, 1752]
    assert int(r) + int(g) + int(b) == 0

    (b, g, r) = frameMask[881, 1868]
    assert int(r) + int(g) + int(b) == 765

    (b, g, r) = frameMask[877, 1834]
    assert int(r) + int(g) + int(b) == 0

    (b, g, r) = frameMask[1002, 62]
    assert int(r) + int(g) + int(b) == 765

    (b, g, r) = frameMask[994, 140]
    assert int(r) + int(g) + int(b) == 0

    _removeTempFiles()


def test_clear():
    md = MotionDetector(debug=True)
    md.applyFirstFrame('tests/images/01_frame_1.png')
    md.checkMotion('tests/images/01_frame_2.png')

    frameClear = cv2.imread('tests/images/01_frame_2.clear.png')

    (b, g, r) = frameClear[17, 65]
    assert int(r) + int(g) + int(b) == 0

    (b, g, r) = frameClear[38, 36]
    assert int(r) + int(g) + int(b) == 0

    (b, g, r) = frameClear[104, 1713]
    assert int(r) + int(g) + int(b) == 0

    (b, g, r) = frameClear[53, 1752]
    assert int(r) + int(g) + int(b) == 0

    (b, g, r) = frameClear[881, 1868]
    assert int(r) + int(g) + int(b) == 765

    (b, g, r) = frameClear[877, 1834]
    assert int(r) + int(g) + int(b) == 0

    (b, g, r) = frameClear[1002, 62]
    assert int(r) + int(g) + int(b) == 0

    (b, g, r) = frameClear[994, 140]
    assert int(r) + int(g) + int(b) == 0

    _removeTempFiles()
