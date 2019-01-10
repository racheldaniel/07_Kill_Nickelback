# Define a set that contains tuples. Each tuple should contain two strings:

# The name of an artist
# A song by that artist
# Make sure that some of the songs are from the band Nickelback.

songs = {
    ('Regina Spektor', 'Music Box'),
    ('Rufus Wainwright', 'Poses'),
    ('Nickelback', 'Too Bad'),
    ('Horseshoes & Handgrenades', 'Whiskey'),
    ('Nickelback', 'Far Away')
}

# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

good_songs = {s for s in songs if s[0] != 'Nickelback'}

print(good_songs)
