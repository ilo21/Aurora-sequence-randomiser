import os, itertools, random

outputFolder = './SequenceFiles/'
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

forceFileName = 'ForceSequence{}.dsf' 
velocityFileName = 'VelocitySequence{}.dsf' 

headers = 'DMCv5 Sequence File \nBase File:  \nProtocol File\tTimed?\tTimeToWait\tFileMarker\tRepeat\n'
forceLineText = 'C:\\Users\\oumth89\\Desktop\\Protocols\\Oumie ex force{}.dpf\tTimed\t5.000\t{}\t0\t\n' 
velocityLineText = 'C:\\Users\\oumth89\\Desktop\\Protocols\\Oumie ex2 length{}.dpf\tTimed\t5.000\t{}\t0\t\n'

forces = [20, 60, 100, 260,1000]

allForcePermutations = list(itertools.permutations(forces))
randomForcePermutations = random.sample(allForcePermutations, len(allForcePermutations))

for f,seq in enumerate(randomForcePermutations):
    forceFile = open(outputFolder + forceFileName .format(f+1), 'w')
    forceFile.write(headers)
    for n,value in enumerate(randomForcePermutations[f]):
        forceFile.write(forceLineText .format(value,n+1))
    forceFile.close()


velocities = [1, 3, 10, 30, 100, 300]

allVelocityPermutations = list(itertools.permutations(velocities))
randomVelocityPermutations = random.sample(allVelocityPermutations, len(allVelocityPermutations))

for f,seq in enumerate(randomVelocityPermutations):
    velocityFile = open(outputFolder + velocityFileName .format(f+1), 'w')
    velocityFile.write(headers)
    for n,value in enumerate(randomVelocityPermutations[f]):
        velocityFile.write(velocityLineText .format(value,n+1))
    velocityFile.close()