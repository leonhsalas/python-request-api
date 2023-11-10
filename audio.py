import moviepy.editor as mp

name = "The Most Horrible Parasite： Brain Eating Amoeba [7OPg-ksxZ4Y].mp4"

#Cargamos el fichero .mp4
clip = mp.VideoFileClip(name)

#Lo escribimos como audio y `.mp3`
clip.audio.write_audiofile("transformado_a.mp3")