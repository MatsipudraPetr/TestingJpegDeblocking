import os
import sys

if len(sys.argv) < 2:
    print("Wrong argument.\nUse knusperli, jpegqs, jpeg2png or ffmpeg as the first argument\nUse JPEG60, JPEG80, JPEG90, 264CRF15, 264CRF24 or 264CRF28 as the second argument")
    exit()

if sys.argv[1] == "original":
    images = "./original"
    database = "./databases/original/database.db"
    output = "./output/original"
    os.system("colmap feature_extractor --database_path " + database + " --image_path " + images + " --ImageReader.mask_path ./masks --ImageReader.camera_model SIMPLE_RADIAL --ImageReader.single_camera true --ImageReader.single_camera_per_folder false --ImageReader.single_camera_per_image false")
    os.system("colmap exhaustive_matcher --database_path " + database)
    os.system("colmap mapper --database_path " + database + " --image_path " + images + " --output_path " + output + " --Mapper.init_min_tri_angle 0.5 --Mapper.init_max_forward_motion 0.95 --Mapper.tri_continue_max_angle_error 0.5 --Mapper.tri_create_max_angle_error 0.5 --Mapper.tri_min_angle 0.5 --Mapper.filter_max_reproj_error 5 --Mapper.filter_min_tri_angle 0.5")
    os.system("colmap model_converter --input_path " + output + "/0 --output_path " + output + "/0 --output_type TXT")
    exit()

if sys.argv[1] not in ("ffmpeg", "jpeg2png", "jpegqs", "knusperli"):
    print("Wrong argument.\nUse knusperli, jpegqs, jpeg2png or ffmpeg as the first argument")
    exit()

if sys.argv[2] not in ("JPEG60", "JPEG80", "JPEG90", "264CRF15", "264CRF24", "264CRF28"):
    print("Wrong argument.\nUse JPEG60, JPEG80, JPEG90, 264CRF15, 264CRF24 or 264CRF28 as the second argument")
    exit()

images = "./restored/" + sys.argv[1] + '/' + sys.argv[2]
database = "./databases/" + sys.argv[1] + '/' + sys.argv[2] + '/' + "database.db"
output = "./output/" + sys.argv[1] + '/' + sys.argv[2]

os.system("colmap feature_extractor --database_path " + database + " --image_path " + images + " --ImageReader.mask_path ./masks --ImageReader.camera_model SIMPLE_RADIAL --ImageReader.single_camera true --ImageReader.single_camera_per_folder false --ImageReader.single_camera_per_image false")
os.system("colmap exhaustive_matcher --database_path " + database)
os.system("colmap mapper --database_path " + database + " --image_path " + images + " --output_path " + output + " --Mapper.init_min_tri_angle 0.5 --Mapper.init_max_forward_motion 0.95 --Mapper.tri_continue_max_angle_error 0.5 --Mapper.tri_create_max_angle_error 0.5 --Mapper.tri_min_angle 0.5 --Mapper.filter_max_reproj_error 5 --Mapper.filter_min_tri_angle 0.5")
os.system("colmap model_converter --input_path " + output + "/0 --output_path " + output + "/0 --output_type TXT")
