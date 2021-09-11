import os, subprocess, argparse, glob

def download_reddit_video(url, output_dir):
    subprocess.call('youtube-dl -o {}/%(title)s.%(ext)s {}'.format(output_dir, url), shell=True)
    f = glob.glob(output_dir + '\\*.mp4')
    subprocess.call(['ffmpeg', '-i', os.path.join(output_dir, os.path.basename(f[0])), '-c:v', 'libvpx-vp9', '-crf', '31', '-b:v', '0', os.path.join(output_dir, os.path.basename(f[0])[:-4]) + '.webm'], shell=True)
    os.remove(f[0])

def massconvert_webm(input_dir):
    f = glob.glob(input_dir + '\\*.mp4')
    for vid in f:
        subprocess.call(['ffmpeg', '-i', vid, '-c:v', 'libvpx-vp9', '-crf', '31', '-b:v', '0', os.path.basename(vid)[:-4] + '.webm'], shell=True)
        os.remove(vid)

def main():
    parser = argparse.ArgumentParser(description='Downloads a reddit video and converts it to a webm', usage='py reddit-dl.py -u [url] -d c:/memes')
    parser.add_argument('-u', '--url', dest='url', help='The url of the reddit video', required=True)
    parser.add_argument('-d', '--dir', dest='dir', help='The output directory', required=False)
    args = parser.parse_args()
    download_reddit_video(args.url, args.dir)

if __name__ == '__main__':
    main()
    
