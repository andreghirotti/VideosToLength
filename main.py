import os
import cv2

videosFolder = input("Enter the path of the folder you would like to search: ")
print()
print('Retrieving videos from: ' + videosFolder)
print()
print(os.listdir(videosFolder))
print()
print()

totalDuration: float = 0

for filename in os.listdir(videosFolder):
    video = cv2.VideoCapture(os.path.join(videosFolder, filename))

    duration: float = int(video.get(cv2.CAP_PROP_FRAME_COUNT)) / int(video.get(cv2.CAP_PROP_FPS))

    totalDuration = totalDuration + duration
    totalDurationHours = totalDuration//3600
    totalDuration = totalDuration%3600
    totalDurationMinutes = totalDuration//60
    totalDurationSeconds = float(totalDuration)%60


    print('Video: \'' + filename + '\' | duration: ' + str('{0:.2f}'.format(duration)) + ' seconds')

print()

if totalDurationHours > 0:
    print('Total duration: ' + str('{0:.0f}'.format(totalDurationHours)) + ' hours, ' + str(totalDurationMinutes) + ' minutes, ' + str('{0:.2f}'.format(totalDurationSeconds)) + ' seconds')
elif totalDurationMinutes > 0:
    print('Total duration: ' + str('{0:.0f}'.format(totalDurationMinutes)) + ' minutes, ' + str('{0:.2f}'.format(totalDurationSeconds)) + ' seconds')
else:
    print('Total duration: ' + str('{0:.2f}'.format(totalDurationSeconds)) + ' seconds')
