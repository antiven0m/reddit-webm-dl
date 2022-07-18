import os
import subprocess
import glob
import argparse


def dl_reddit_vid(url, quality):
    subprocess.call('youtube-dl -o %(title)s.%(ext)s {}'.format(url), shell=True, stdout=subprocess.PIPE)
    f = glob.glob('*.mp4')
    subprocess.call(['ffmpeg', '-i', os.path.join(os.path.basename(f[0])), '-c:v', 'libvpx-vp9', '-crf', quality, '-b:v', '0', os.path.join(os.path.basename(f[0])[:-4]) + '.webm'], shell=True)
    os.remove(f[0])


def main():
    parser = argparse.ArgumentParser(description='Download Reddit videos and convert them to webms.')
    parser.add_argument('url', help='The URL of the Reddit video post.')
    parser.add_argument('-q', '--quality', help='The quality of the video. Default is high.', choices=['low', 'medium', 'high'], default='high')
    args = parser.parse_args()
    if args.quality == 'low':
        quality = '15'
    elif args.quality == 'medium':
        quality = '25'
    elif args.quality == 'high':
        quality = '35'
    dl_reddit_vid(args.url, quality)


if __name__ == '__main__':
    main()
