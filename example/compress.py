import os
import sys

if len(sys.argv) < 2:
    print("Wrong argument.\nUse JPEG60, JPEG80, JPEG90, 264CRF15, 264CRF24 or 264CRF28 as an argument")

elif sys.argv[1] == "JPEG60":
    from PIL import Image
    for infile in os.listdir("./original"):
        if infile[-4:] == "tiff":
            outfile = infile[:-4] + "jpeg"
            im = Image.open("./original/" + infile)
            out = im.convert("RGB")
            out.save("./compressed/JPEG60/" + outfile, "JPEG", quality=60)

elif sys.argv[1] == "JPEG80":
    from PIL import Image
    for infile in os.listdir("./original"):
        if infile[-4:] == "tiff":
            outfile = infile[:-4] + "jpeg"
            im = Image.open("./original/" + infile)
            out = im.convert("RGB")
            out.save("./compressed/JPEG80/" + outfile, "JPEG", quality=80)

elif sys.argv[1] == "JPEG90":
    from PIL import Image
    for infile in os.listdir("./original"):
        if infile[-4:] == "tiff":
            outfile = infile[:-4] + "jpeg"
            im = Image.open("./original/" + infile)
            out = im.convert("RGB")
            out.save("./compressed/JPEG90/" + outfile, "JPEG", quality=90)

elif sys.argv[1] == "264CRF15":
    os.system("../ffmpeg -framerate 10 -pattern_type glob -i './original/*.tiff' -bufsize 30000k -c:v libx264 "
              "-profile:v high422 -crf 15 -pix_fmt yuv420p ./compressed/264CRF15/out.mpeg")
    os.system("../ffmpeg -r 1 -i './compressed/264CRF15/out.mpeg' -qmin 1 -qscale:v 1 -r 1 -start_number " + min(os.listdir("original"))[:-4] + " -pix_fmt yuvj420p './compressed/264CRF15/%010d.jpeg'")

elif sys.argv[1] == "264CRF24":
    os.system("../ffmpeg -framerate 10 -pattern_type glob -i './original/*.tiff' -bufsize 30000k -c:v libx264 "
              "-profile:v high422 -crf 24 -pix_fmt yuv420p ./compressed/264CRF24/out.mpeg")
    os.system("../ffmpeg -r 1 -i './compressed/264CRF24/out.mpeg' -qmin 1 -qscale:v 1 -r 1 -start_number " + min(os.listdir("original"))[:-4] + " -pix_fmt yuvj420p './compressed/264CRF24/%010d.jpeg'")

elif sys.argv[1] == "264CRF28":
    os.system("../ffmpeg -framerate 10 -pattern_type glob -i './original/*.tiff' -bufsize 30000k -c:v libx264 "
              "-profile:v high422 -crf 28 -pix_fmt yuv420p ./compressed/264CRF28/out.mpeg")
    os.system("../ffmpeg -r 1 -i './compressed/264CRF28/out.mpeg' -qmin 1 -qscale:v 1 -r 1 -start_number " + min(os.listdir("original"))[:-4] + " -pix_fmt yuvj420p './compressed/264CRF28/%010d.jpeg'")

else:
    print("Wrong argument.\nUse JPEG60, JPEG80, JPEG90, 264CRF15, 264CRF24 or 264CRF28 as an argument")
