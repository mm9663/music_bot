from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError
from mutagen.mp3 import MP3
import datetime

def show_id3_tags(file_path):
    try:
        tags = EasyID3(file_path)
    except ID3NoHeaderError:
        tags = None
    #print(type(tags['title']))
    s = ""
    try:
        s = '{}'.format(tags['artist'][0]) + ' - ' 
    except:
        print("cannot read artist. "+file_path)
        s = "Unknown Artist - "
    try:
        s += '{}'.format(tags['title'][0])
    except:
        print("cannot read title. "+file_path)
        s += "Unknown Title"
    finally:
        return s
def get_mp3_length(file_path):
    try:
        mp3 = MP3(file_path)
        td = datetime.timedelta(seconds=int(mp3.info.length))
    except:
        td = "[??:??]"
    finally:
        return '{}'.format(td)

"""
fp = './playlist/1009.mp3'
i = 0
print('`{}.` '.format(i+1)+show_id3_tags(fp) + get_mp3_length(fp))
"""
