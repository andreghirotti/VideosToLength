import os
import cv2

videosFolder = input("Enter the path of the folder you would like to search: ")
print()
print('Retrieving videos from: ' + videosFolder)
print()
print()

totalDuration: float = 0
nOfVideos: int = 0

for filename in os.listdir(videosFolder):

    if filename.endswith('.mp4') or filename.endswith('.mkv') or filename.endswith('.avi') or filename.endswith('.mov') or filename.endswith('.wmv'):
        totalDuration = totalDuration + 1
        video = cv2.VideoCapture(os.path.join(videosFolder, filename))

        duration: float = int(video.get(cv2.CAP_PROP_FRAME_COUNT)) / int(video.get(cv2.CAP_PROP_FPS))

        totalDuration = totalDuration + duration

        nOfVideos = nOfVideos + 1
        print('Video: \'' + filename + '\' | duration: ' + str('{0:.2f}'.format(duration)) + ' seconds')

if nOfVideos == 0: print('No videos found in folder')
else:
    print()


    totalDurationHours = totalDuration//3600
    totalDuration = totalDuration%3600
    totalDurationMinutes = totalDuration//60
    totalDurationSeconds = float(totalDuration)%60

    if totalDurationHours > 0:
        print('Total duration: ' + str('{0:.0f}'.format(totalDurationHours)) + ' hours, ' + str(totalDurationMinutes) + ' minutes, ' + str('{0:.2f}'.format(totalDurationSeconds)) + ' seconds')
    elif totalDurationMinutes > 0:
        print('Total duration: ' + str('{0:.0f}'.format(totalDurationMinutes)) + ' minutes, ' + str('{0:.2f}'.format(totalDurationSeconds)) + ' seconds')
    else:
        print('Total duration: ' + str('{0:.2f}'.format(totalDurationSeconds)) + ' seconds')
    print('Number of videos: ' + str(nOfVideos))
    print()
    input("Press enter to close program")