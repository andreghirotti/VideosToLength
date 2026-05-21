import os
import cv2

videosFolder = input("Enter the path of the folder you would like to search: ")
print()
print('Retrieving videos from: ' + videosFolder)
print()
print()

totalDuration: float = 0
totalSize: float = 0
nOfVideos: int = 0

for filename in os.listdir(videosFolder):

    if filename.endswith('.mp4') or filename.endswith('.mkv') or filename.endswith('.avi') or filename.endswith('.mov') or filename.endswith('.wmv'):
        totalDuration = totalDuration + 1
        video = cv2.VideoCapture(os.path.join(videosFolder, filename))
        fileSize = os.path.getsize(os.path.join(videosFolder, filename))

        duration: float = int(video.get(cv2.CAP_PROP_FRAME_COUNT)) / int(video.get(cv2.CAP_PROP_FPS))

        totalDuration = totalDuration + duration
        totalSize += fileSize

        nOfVideos = nOfVideos + 1

        fileSizeStr = ''
        fileSizeTB = float(fileSize / 1024 / 1024 / 1024 / 1024)
        fileSizeGb = float(fileSize / 1024 / 1024 / 1024)
        fileSizeMb = float(fileSize / 1024 / 1024)
        fileSizeKb = float(fileSize / 1024)

        if fileSizeTB >= 1:
            fileSizeStr = str('{0:.2f}'.format(fileSizeTB)) + ' TB'
        elif fileSizeGb >= 1:
            fileSizeStr = str('{0:.2f}'.format(fileSizeGb)) + ' GB'
        elif fileSizeMb >= 1:
            fileSizeStr = str('{0:.2f}'.format(fileSizeMb)) + ' MB'
        elif fileSizeKb > 0:
            fileSizeStr = str('{0:.2f}'.format(fileSizeKb)) + ' KB'
        print('Video: \'' + filename + '\' | duration: ' + str('{0:.2f}'.format(duration)) + ' seconds ('+fileSizeStr+')')

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

    totalSizeTB = float(totalSize/1024/1024/1024/1024)
    totalSizeGb = float(totalSize/1024/1024/1024)
    totalSizeMb = float(totalSize/1024/1024)
    totalSizeKb = float(totalSize/1024)

    if totalSizeTB >= 1:
        print('Total size: ' + str('{0:.2f}'.format(totalSizeTB)) + ' TB')
    elif totalSizeGb >= 1:
        print('Total size: ' + str('{0:.2f}'.format(totalSizeGb)) + ' GB')
    elif totalSizeMb >= 1:
        print('Total size: ' + str('{0:.2f}'.format(totalSizeMb)) + ' MB')
    elif totalSizeKb > 0:
        print('Total size: ' + str('{0:.2f}'.format(totalSizeKb)) + ' KB')

    print('Number of videos: ' + str(nOfVideos))
    print()
    input("Press enter to close program")