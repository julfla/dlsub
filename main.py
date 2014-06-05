from optparse import OptionParser
import os.path
import open_subtitles

language = 'eng'

def main():
    usage = "usage: %prog [options] video1 video2 ..."
    parser = OptionParser(usage)
    # parser.add_option("-q", "--quiet",
    #                  action="store_false", dest="verbose")
    (options, args) = parser.parse_args()
    if len(args) == 0:
        print "No file provided."
        return -1
    for video_path in args:
        if not os.path.isfile(video_path):
            print '{} file does not exist, skipping.'.format( video_path )
        else:
            open_subtitles.download_sub( video_path, language)

if __name__ == "__main__":
    main()


