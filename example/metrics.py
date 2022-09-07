import os
import sys
import cv2
from sewar.full_ref import psnr, psnrb, ssim


def set_index_and_coordinates(kp, des):
    index_dict = {}
    for i in range(len(kp)):
        if (kp[i], des[i], kp[i].pt) not in index_dict.values():
            index_dict[i] = (kp[i], des[i], kp[i].pt)
    return index_dict


def dist(v1, v2, dist_type: str):
    """
    in case of dist_type = 'des':
        calculate euclidean distance between descroptors vectors
    in case of dist_type = 'kp':
        calculate diameter of the meaningful keypoint neighborhood for each kp1, kp2
    in case of dist_type = 'coord':
        calculate euclidean distance between coordinates
    """
    if dist_type == 'des':
        summ = 0
        for i in range(len(v1)):
            summ += abs(v1[i] - v2[i])
        return summ

    if dist_type == 'kp':
        return abs(v1.size - v2.size)

    if dist_type == 'coord':
        summ = 0
        for i in range(len(v1)):
            summ += abs(v1[i] - v2[i])
        return summ


def get_matches(kp_idx1: dict, kp_idx2: dict, radius = 1.0):
    """
    get simple matches for two dataframes of coordinates of features of images
    """
    matches = {}
    to_delete = -1
    for k1,v1 in kp_idx1.items():
        for k2, v2 in kp_idx2.items():
            if dist(v1[2], v2[2], dist_type='coord') < radius:
                if k1 in matches:
                    # if need distance to be 'kp' - switch dist_type and also [1] -> [0]
                    if dist(kp_idx1[k1][1], v2[1], dist_type='des') > dist(v1[1], v2[1], dist_type='des'):
                        matches[k1] = k2
                        to_delete = k2

                else:
                    matches[k1] = k2
                    to_delete = k2

        if to_delete in kp_idx2:
            del kp_idx2[to_delete]
    return matches


def get_cross_matches(matches1, matches2):
    """
    calculate cross match features
    """
    cross_matches = 0
    for k1, v1 in matches1.items():
        if v1 in matches2:
            if matches2[v1] == k1:
                cross_matches += 1
    return cross_matches


def coordinates_match(img1, img2, radius = 1, cross_match = False):
    """
    SIFT calculated features
    feature matching using euclidean proximity
    """
    print('images shape:', img1.shape)

    # SIFT feature detector
    sift = cv2.xfeatures2d.SIFT_create()
    kp_im1, des_im1 = sift.detectAndCompute(img1, None)
    kp_im2, des_im2 = sift.detectAndCompute(img2, None)

    # get coordinates of features and set index
    idx_im1 = set_index_and_coordinates(kp_im1, des_im1)
    idx_im2 = set_index_and_coordinates(kp_im2, des_im2)
    all_matches = len(idx_im2)

    print('radius value:', radius)
    print('number of features for img1:', len(idx_im1))
    print('number of features for img2:', all_matches)

    if not cross_match:
        # simple match
        im1_VS_im2_match = get_matches(idx_im1, idx_im2, radius = radius)

        print('number of matching:', len(im1_VS_im2_match))

    if cross_match:
        # simple match
        im1_VS_im2_match = get_matches(idx_im1, idx_im2, radius = radius)
        idx_im2 = set_index_and_coordinates(kp_im2, des_im2)
        im2_VS_im1_match = get_matches(idx_im2, idx_im1, radius = radius)

        # cross_match
        cross_matches = get_cross_matches(im1_VS_im2_match, im2_VS_im1_match)
        cross_match_value = cross_matches/all_matches

        print('number of img1 VS img2 matching:', len(im1_VS_im2_match))
        print('number of img2 VS img1 matching:', len(im2_VS_im1_match))
        print('cross match value:', cross_match_value)

    return cross_match_value

dir1 = sys.argv[1]
dir2 = sys.argv[2]

imgCount = 0
psnrSum = 0.0
psnrbSum = 0.0
featureSum = 0.0
ssimSum = [0.0, 0.0]
ssimTemp = []

for file in os.listdir(dir2):
    if file[-4:] == "jpeg":
        imgCount += 1
        img1 = cv2.imread(dir1 + '/' + file[:-4] + "tiff")
        img2 = cv2.imread(dir2 + '/' + file)
        psnrSum += psnr(img1, img2)
        psnrbSum += psnrb(img1, img2)
        featureSum += coordinates_match(img1, img2, 1, True)
        ssimTemp.extend(list(ssim(img1, img2)))
        ssimSum[0] += ssimTemp[0]
        ssimSum[1] += ssimTemp[1]
        ssimTemp.clear()

metricsFile = open("results.csv", "a")
metricsFile.write(dir1 + ',' + dir2 + ',' + str(psnrSum / imgCount) + ',' + str(psnrbSum / imgCount) + ',' + str(ssimSum[0] / imgCount) + ' ' + str(ssimSum[1] / imgCount) + ',' + str(featureSum / imgCount) + '\n')
