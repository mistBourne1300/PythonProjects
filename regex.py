import re

TEXT_TO_SEARCH = "And again, verily I say unto you, if a man marry a wife by my word, which is my law, and by the new and everlasting covenant, and it is sealed unto them by the Holy Spirit of promise, by him who is anointed, unto whom I have appointed this power and the keys of this priesthood; and it shall be said unto them—Ye shall come forth in the first resurrection; and if it be after the first resurrection, in the next resurrection; and shall inherit thrones, kingdoms, principalities, and powers, dominions, all heights and depths—then shall it be written in the Lamb’s Book of Life, that he shall commit no murder whereby to shed innocent blood, and if ye abide in my covenant, and commit no murder whereby to shed innocent blood, it shall be done unto them in all things whatsoever my servant hath put upon them, in time, and through all eternity; and shall be of full force when they are out of the world; and they shall pass by the angels, and the gods, which are set there, to their exaltation and glory in all things, as hath been sealed upon their heads, which glory shall be a fulness and a continuation of the seeds forever and ever."
#D&C 132:19
TEXT_TO_SEARCH += "\nThen shall they be gods, because they have no end; therefore shall they be from everlasting to everlasting, because they continue; then shall they be above all, because all things are subject unto them. Then shall they be gods, because they have all power, and the angels are subject unto them."

"""user = 'chase'
currdir = fr'~/User/{user}/Desktop'
print(currdir)"""

searchString = '(gods|angels|the[my])'

pattern = re.compile(fr'{searchString}')
print(bool(pattern.search(TEXT_TO_SEARCH)))

matches = pattern.finditer(TEXT_TO_SEARCH)
for match in matches:
    print(match)


