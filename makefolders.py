import os


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_compression_folders():
    create_folder("264CRF15")
    create_folder("264CRF24")
    create_folder("264CRF28")
    create_folder("JPEG60")
    create_folder("JPEG80")
    create_folder("JPEG90")


def create_program_folders():
    create_folder("ffmpeg")
    create_folder("jpeg2png")
    create_folder("jpegqs")
    create_folder("knusperli")

    os.chdir("ffmpeg")
    create_compression_folders()
    os.chdir(os.pardir)
    os.chdir("jpeg2png")
    create_compression_folders()
    os.chdir(os.pardir)
    os.chdir("jpegqs")
    create_compression_folders()
    os.chdir(os.pardir)
    os.chdir("knusperli")
    create_compression_folders()
    os.chdir(os.pardir)


if (not os.path.exists("images") and not os.path.exists("original")) or not os.path.exists("masks"):
    print("Work folder is missing folders")
    exit()

if not os.path.exists("original"):
    os.rename("images", "original")

create_folder("compressed")
create_folder("restored")
create_folder("databases")
create_folder("output")

create_folder("databases/original")
create_folder("output/original")

os.chdir("compressed")
create_compression_folders()
os.chdir(os.pardir)

os.chdir("restored")
create_program_folders()
os.chdir(os.pardir)

os.chdir("databases")
create_program_folders()
os.chdir(os.pardir)

os.chdir("output")
create_program_folders()
os.chdir(os.pardir)
