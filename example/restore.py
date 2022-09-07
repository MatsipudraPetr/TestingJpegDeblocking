import os
import sys

if len(sys.argv) < 2:
    print("Wrong argument.\nUse knusperli, jpegqs, jpeg2png or ffmpeg as the first argument\nUse JPEG60, JPEG80, JPEG90, 264CRF15, 264CRF24 or 264CRF28 as the second argument")

elif sys.argv[2] not in ("JPEG60", "JPEG80", "JPEG90", "264CRF15", "264CRF24", "264CRF28"):
    print("Wrong argument.\nUse JPEG60, JPEG80, JPEG90, 264CRF15, 264CRF24 or 264CRF28 as the second argument")

elif sys.argv[1] == "ffmpeg":
    inputdir = "./compressed/" + sys.argv[2] + "/"
    outputdir = "./restored/ffmpeg/" + sys.argv[2] + "/"
    for infile in os.listdir(inputdir):
        if infile[-4:] == "jpeg":
            outfile = infile[:-4] + "tiff"
            os.system("../ffmpeg -i " + inputdir + infile + " -vf deblock=filter=strong:block=4:alpha=0.12:beta=0.07:gamma=0.06:delta=0.05:planes=1 -qmin 1 -qscale:v 1 " + outputdir + outfile)
            print(infile + " restored")

elif sys.argv[1] == "jpeg2png":
    inputdir = "./compressed/" + sys.argv[2] + "/"
    outputdir = "./restored/jpeg2png/" + sys.argv[2] + "/"
    for infile in os.listdir(inputdir):
        if infile[-4:] == "jpeg":
            outfile = infile[:-4] + "tiff"
            os.system("../jpeg2png " + inputdir + infile + " -o " + outputdir + outfile)
            print(infile + " restored")

elif sys.argv[1] == "jpegqs":
    inputdir = "./compressed/" + sys.argv[2] + "/"
    outputdir = "./restored/jpegqs/" + sys.argv[2] + "/"
    for infile in os.listdir(inputdir):
        if infile[-4:] == "jpeg":
            outfile = infile[:-4] + "tiff"
            os.system("../jpegqs " + inputdir + infile + " " + outputdir + outfile)
            print(infile + " restored")

elif sys.argv[1] == "knusperli":
    inputdir = "./compressed/" + sys.argv[2] + "/"
    outputdir = "./restored/knusperli/" + sys.argv[2] + "/"
    for infile in os.listdir(inputdir):
        if infile[-4:] == "jpeg":
            outfile = infile[:-4] + "tiff"
            os.system("../knusperli " + inputdir + infile + " " + outputdir + outfile)
            print(infile + " restored")

else:
    print("Wrong argument.\nUse knusperli, jpegqs, jpeg2png or ffmpeg as the first argument")
