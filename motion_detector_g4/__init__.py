from cv2 import cv2, SimpleBlobDetector
import numpy


class MotionDetector:

    def __init__(self, minArea = 4000, maxArea = 150000, denoiseSize = 10, debug = False):
        """
        :param minArea: Min blob size
        :param maxArea: Max blob size
        :param denoiseSize: Max size of denoise area
        :param debug: Debug mod
        """

        self.debug = debug

        self.backSub = cv2.createBackgroundSubtractorMOG2(history=2, detectShadows=False)

        self.denoiseKernel = numpy.ones((denoiseSize, denoiseSize), numpy.uint8)

        self.blobDetector = self._createBlobDetector(minArea, maxArea)

    def _createBlobDetector(self, minArea: int, maxArea: int) -> SimpleBlobDetector:
        """
        Create and config OpenCV Simple Blob Detector

        :param minArea: Min blob size
        :param maxArea: Max blob size
        :return: SimpleBlobDetector
        """

        params = cv2.SimpleBlobDetector_Params()

        params.filterByColor = False

        params.minRepeatability = 1
        params.minThreshold = 250
        params.maxThreshold = 255

        # Filter by Area
        params.filterByArea = True
        params.minArea = minArea
        params.maxArea = maxArea

        params.filterByCircularity = False
        params.filterByConvexity = False
        params.filterByInertia = False

        return cv2.SimpleBlobDetector_create(params)

    def applyFirstFrame(self, firstFramePath: str) -> None:
        """
        :param firstFramePath:
        :return: None
        """

        firstFrame = cv2.imread(firstFramePath)

        self.backSub.apply(firstFrame)

    def checkMotion(self, nextFramePath: str) -> bool:
        """
        :param nextFramePath: Next frame for comparison
        :return: bool
        """

        nextFrame = cv2.imread(nextFramePath)

        # 1. Delete background

        frameMask = self.backSub.apply(nextFrame)

        if self.debug:
            cv2.imwrite(nextFramePath + '.mask', frameMask)

        # 2. Clear noises
        frameClear = cv2.morphologyEx(frameMask, cv2.MORPH_OPEN, self.denoiseKernel)

        if self.debug:
            cv2.imwrite(nextFramePath + '.clear', frameClear)

        # 3. Search blobs

        blobs = self.blobDetector.detect(frameClear)

        if len(blobs) > 0:
            if self.debug:
                frameWithBlobs = cv2.drawKeypoints(nextFrame, blobs, numpy.array([]), (0, 0, 255),
                                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                frameMaskWithBlobs = cv2.drawKeypoints(frameClear, blobs, numpy.array([]), (0, 0, 255),
                                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

                cv2.imwrite(nextFramePath + '.blobs', frameWithBlobs)
                cv2.imwrite(nextFramePath + '.blobs2', frameMaskWithBlobs)

            return True

        return False