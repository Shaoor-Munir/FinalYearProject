from collections import defaultdict

import pickle

import numpy as np
import xlsxwriter
from sklearn.kernel_ridge import KernelRidge

from VideoProcessing.featureextraction import FeatureExtraction
from VideoProcessing.frameextraction import FrameExtraction


class KernelRidgeModel:
    def __init__(self, featuresDict=None, labelsDict=None):
        self.featuresDict = featuresDict
        self.labelsDict = labelsDict

    def generate(self):
        neuroticismModelRightEye = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # neuroticismModelLeftEye = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # neuroticismModelFace = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # neuroticismModelSmile = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        #
        # extraversionModelRightEye = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # extraversionModelLeftEye = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # extraversionModelFace = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # extraversionModelSmile = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        #
        # conscientiousnessModelRightEye = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # conscientiousnessModelLeftEye = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # conscientiousnessModelFace = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # conscientiousnessModelSmile = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        #
        # agreeablenessModelRightEye = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # agreeablenessModelLeftEye = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # agreeablenessModelFace = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # agreeablenessModelSmile = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        #
        # opennessModelRightEye = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # opennessModelLeftEye = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # opennessModelFace = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)
        # opennessModelSmile = KernelRidge(kernel='rbf', alpha=0.1, gamma=0.1)

        neuroticismModelRightEye.fit(self.featuresDict['righteye'], self.labelsDict['righteye']['neuroticism'])
        # neuroticismModelLeftEye.fit(self.featuresDict['lefteye'], self.labelsDict['lefteye']['neuroticism'])
        # neuroticismModelFace.fit(self.featuresDict['face'], self.labelsDict['face']['neuroticism'])
        # neuroticismModelSmile.fit(self.featuresDict['smile'], self.labelsDict['smile']['neuroticism'])
        #
        # opennessModelRightEye.fit(self.featuresDict['righteye'], self.labelsDict['righteye']['openness'])
        # opennessModelLeftEye.fit(self.featuresDict['lefteye'], self.labelsDict['lefteye']['openness'])
        # opennessModelFace.fit(self.featuresDict['face'], self.labelsDict['face']['openness'])
        # opennessModelSmile.fit(self.featuresDict['smile'], self.labelsDict['smile']['openness'])
        #
        # agreeablenessModelRightEye.fit(self.featuresDict['righteye'], self.labelsDict['righteye']['agreeableness'])
        # agreeablenessModelLeftEye.fit(self.featuresDict['lefteye'], self.labelsDict['lefteye']['agreeableness'])
        # agreeablenessModelFace.fit(self.featuresDict['face'], self.labelsDict['face']['agreeableness'])
        # agreeablenessModelSmile.fit(self.featuresDict['smile'], self.labelsDict['smile']['agreeableness'])
        #
        # extraversionModelRightEye.fit(self.featuresDict['righteye'], self.labelsDict['righteye']['extraversion'])
        # extraversionModelLeftEye.fit(self.featuresDict['lefteye'], self.labelsDict['lefteye']['extraversion'])
        # extraversionModelFace.fit(self.featuresDict['face'], self.labelsDict['face']['extraversion'])
        # extraversionModelSmile.fit(self.featuresDict['smile'], self.labelsDict['smile']['extraversion'])

        # conscientiousnessModelRightEye.fit(self.featuresDict['righteye'],
        #                                    self.labelsDict['righteye']['conscientiousness'])
        # conscientiousnessModelLeftEye.fit(self.featuresDict['lefteye'], self.labelsDict['lefteye']['conscientiousness'])
        # conscientiousnessModelFace.fit(self.featuresDict['face'], self.labelsDict['face']['conscientiousness'])
        # conscientiousnessModelSmile.fit(self.featuresDict['smile'], self.labelsDict['smile']['conscientiousness'])

        # KernelModelDict = defaultdict(dict)

        # KernelModelDict['face']['openness'] = opennessModelFace
        # KernelModelDict['face']['agreeableness'] = agreeablenessModelFace
        # KernelModelDict['face']['extraversion'] = extraversionModelFace
        # KernelModelDict['face']['conscientiousness'] = conscientiousnessModelFace
        # KernelModelDict['face']['neuroticism'] = neuroticismModelFace
        #
        # KernelModelDict['smile']['openness'] = opennessModelSmile
        # KernelModelDict['smile']['agreeableness'] = agreeablenessModelSmile
        # KernelModelDict['smile']['extraversion'] = extraversionModelSmile
        # KernelModelDict['smile']['conscientiousness'] = conscientiousnessModelSmile
        # KernelModelDict['smile']['neuroticism'] = neuroticismModelSmile
        #
        # KernelModelDict['righteye']['openness'] = opennessModelRightEye
        # KernelModelDict['righteye']['agreeableness'] = agreeablenessModelRightEye
        # KernelModelDict['righteye']['extraversion'] = extraversionModelRightEye
        # KernelModelDict['righteye']['conscientiousness'] = conscientiousnessModelRightEye
        # KernelModelDict['righteye']['neuroticism'] = neuroticismModelRightEye
        #
        # KernelModelDict['lefteye']['openness'] = opennessModelLeftEye
        # KernelModelDict['lefteye']['agreeableness'] = agreeablenessModelLeftEye
        # KernelModelDict['lefteye']['extraversion'] = extraversionModelLeftEye
        # KernelModelDict['lefteye']['conscientiousness'] = conscientiousnessModelLeftEye
        # KernelModelDict['lefteye']['neuroticism'] = neuroticismModelLeftEye
        #
        # self.modelDict = KernelModelDict
        # return KernelModelDict

    def test(self, model=None, videoCount=1):

        if model is not None:
            self.modelDict = model

        workbook = xlsxwriter.Workbook('ridgeregression.xlsx')

        worksheet = workbook.add_worksheet()

        bold = workbook.add_format({'bold': True})

        worksheet.write('A1', 'Openness (Expected)', bold)
        worksheet.write('B1', 'Openness (Face)', bold)
        worksheet.write('C1', 'Openness (Left Eye)', bold)
        worksheet.write('D1', 'Openness (Right Eye)', bold)
        worksheet.write('E1', 'Openness (Smile)', bold)
        worksheet.write('F1', 'Openness (Combined)', bold)

        worksheet.write('G1', 'Extraversion (Expected)', bold)
        worksheet.write('H1', 'Extraversion (Face)', bold)
        worksheet.write('I1', 'Extraversion (Left Eye)', bold)
        worksheet.write('J1', 'Extraversion (Right Eye)', bold)
        worksheet.write('K1', 'Extraversion (Smile)', bold)
        worksheet.write('L1', 'Extraversion (Combined)', bold)

        worksheet.write('M1', 'Neuroticism (Expected)', bold)
        worksheet.write('N1', 'Neuroticism (Face)', bold)
        worksheet.write('O1', 'Neuroticism (Left Eye)', bold)
        worksheet.write('P1', 'Neuroticism (Right Eye)', bold)
        worksheet.write('Q1', 'Neuroticism (Smile)', bold)
        worksheet.write('R1', 'Neuroticism (Combined)', bold)

        worksheet.write('S1', 'Agreeableness (Expected)', bold)
        worksheet.write('T1', 'Agreeableness (Face)', bold)
        worksheet.write('U1', 'Agreeableness (Left Eye)', bold)
        worksheet.write('V1', 'Agreeableness (Right Eye)', bold)
        worksheet.write('W1', 'Agreeableness (Smile)', bold)
        worksheet.write('X1', 'Agreeableness (Combined)', bold)

        worksheet.write('Y1', 'Conscientiousness (Expected)', bold)
        worksheet.write('Z1', 'Conscientiousness (Face)', bold)
        worksheet.write('AA1', 'Conscientiousness (Left Eye)', bold)
        worksheet.write('AB1', 'Conscientiousness (Right Eye)', bold)
        worksheet.write('AC1', 'Conscientiousness (Smile)', bold)
        worksheet.write('AD1', 'Conscientiousness (Combined)', bold)

        worksheet.write('AE1', 'Openness (Error)', bold)
        worksheet.write('AF1', 'Extraversion (Error)', bold)
        worksheet.write('AG1', 'Neuroticism (Error)', bold)
        worksheet.write('AH1', 'Agreeableness (Erro)', bold)
        worksheet.write('AI1', 'Conscientiousness (Error)', bold)

        videosDataFile = open("AnnotationFiles/annotation_test.pkl", "rb")
        print('Loading data from pickle file.')
        videosData = pickle.load(videosDataFile, encoding='latin1')

        print('Getting names of all the video files.')
        videoNames = list(videosData['extraversion'].keys())

        videosFilePath = 'TestVideos/'

        frameExtractor = FrameExtraction(1, 200, videoNames, videosFilePath)

        for i, videoName in enumerate(videoNames):

            facesData, smileData, leftEyeData, rightEyeData = frameExtractor.extract_single(videoName)

            featureExtractor = FeatureExtraction(24, 8)

            featuresDict = featureExtractor.extract(facesData, smileData, leftEyeData, rightEyeData)

            if featuresDict['face']:
                opennessListFace = self.modelDict['face']['openness'].predict(featuresDict['face'])
                extraversionListFace = self.modelDict['face']['extraversion'].predict(featuresDict['face'])
                neuroticismListFace = self.modelDict['face']['neuroticism'].predict(featuresDict['face'])
                agreeablenessListFace = self.modelDict['face']['agreeableness'].predict(featuresDict['face'])
                conscientiousnessListFace = self.modelDict['face']['conscientiousness'].predict(featuresDict['face'])

            if featuresDict['righteye']:
                opennessListRightEye = self.modelDict['righteye']['openness'].predict(featuresDict['righteye'])
                extraversionListRightEye = self.modelDict['righteye']['extraversion'].predict(featuresDict['righteye'])
                neuroticismListRightEye = self.modelDict['righteye']['neuroticism'].predict(featuresDict['righteye'])
                agreeablenessListRightEye = self.modelDict['righteye']['agreeableness'].predict(
                    featuresDict['righteye'])
                conscientiousnessListRightEye = self.modelDict['righteye']['conscientiousness'].predict(
                    featuresDict['righteye'])

            if featuresDict['lefteye']:
                opennessListLeftEye = self.modelDict['lefteye']['openness'].predict(featuresDict['lefteye'])
                extraversionListLeftEye = self.modelDict['lefteye']['extraversion'].predict(featuresDict['lefteye'])
                neuroticismListLeftEye = self.modelDict['lefteye']['neuroticism'].predict(featuresDict['lefteye'])
                agreeablenessListLeftEye = self.modelDict['lefteye']['agreeableness'].predict(featuresDict['lefteye'])
                conscientiousnessListLeftEye = self.modelDict['lefteye']['conscientiousness'].predict(
                    featuresDict['lefteye'])

            if featuresDict['smile']:
                opennessListSmile = self.modelDict['smile']['openness'].predict(featuresDict['smile'])
                extraversionListSmile = self.modelDict['smile']['extraversion'].predict(featuresDict['smile'])
                neuroticismListSmile = self.modelDict['smile']['neuroticism'].predict(featuresDict['smile'])
                agreeablenessListSmile = self.modelDict['smile']['agreeableness'].predict(featuresDict['smile'])
                conscientiousnessListSmile = self.modelDict['smile']['conscientiousness'].predict(featuresDict['smile'])

            tempList = np.concatenate((opennessListFace, opennessListLeftEye, opennessListRightEye, opennessListSmile))

            worksheet.write(i + 1, 0, videosData['openness'][videoName])
            worksheet.write(i + 1, 1, sum(opennessListFace) / len(opennessListFace))
            worksheet.write(i + 1, 2, sum(opennessListLeftEye) / len(opennessListLeftEye))
            worksheet.write(i + 1, 3, sum(opennessListRightEye) / len(opennessListRightEye))
            worksheet.write(i + 1, 4, sum(opennessListSmile) / len(opennessListSmile))
            worksheet.write(i + 1, 5, sum(tempList) / len(tempList))

            tempList = np.concatenate(
                (extraversionListFace, extraversionListLeftEye, extraversionListRightEye, extraversionListSmile))

            worksheet.write(i + 1, 6, videosData['extraversion'][videoName])
            worksheet.write(i + 1, 7, sum(extraversionListFace) / len(extraversionListFace))
            worksheet.write(i + 1, 8, sum(extraversionListLeftEye) / len(extraversionListLeftEye))
            worksheet.write(i + 1, 9, sum(extraversionListRightEye) / len(extraversionListRightEye))
            worksheet.write(i + 1, 10, sum(extraversionListSmile) / len(extraversionListSmile))
            worksheet.write(i + 1, 11, sum(tempList) / len(tempList))

            tempList = np.concatenate(
                (neuroticismListFace, neuroticismListLeftEye, neuroticismListRightEye, neuroticismListSmile))

            worksheet.write(i + 1, 12, videosData['neuroticism'][videoName])
            worksheet.write(i + 1, 13, sum(neuroticismListFace) / len(neuroticismListFace))
            worksheet.write(i + 1, 14, sum(neuroticismListLeftEye) / len(neuroticismListLeftEye))
            worksheet.write(i + 1, 15, sum(neuroticismListRightEye) / len(neuroticismListRightEye))
            worksheet.write(i + 1, 16, sum(neuroticismListSmile) / len(neuroticismListSmile))
            worksheet.write(i + 1, 17, sum(tempList) / len(tempList))

            tempList = np.concatenate(
                (agreeablenessListFace, agreeablenessListLeftEye, agreeablenessListRightEye, agreeablenessListSmile))

            worksheet.write(i + 1, 18, videosData['agreeableness'][videoName])
            worksheet.write(i + 1, 19, sum(agreeablenessListFace) / len(agreeablenessListFace))
            worksheet.write(i + 1, 20, sum(agreeablenessListLeftEye) / len(agreeablenessListLeftEye))
            worksheet.write(i + 1, 21, sum(agreeablenessListRightEye) / len(agreeablenessListRightEye))
            worksheet.write(i + 1, 22, sum(agreeablenessListSmile) / len(agreeablenessListSmile))
            worksheet.write(i + 1, 23, sum(tempList) / len(tempList))

            tempList = np.concatenate((conscientiousnessListFace, conscientiousnessListLeftEye,
                                       conscientiousnessListRightEye, conscientiousnessListSmile))

            worksheet.write(i + 1, 24, videosData['conscientiousness'][videoName])
            worksheet.write(i + 1, 25, sum(conscientiousnessListFace) / len(conscientiousnessListFace))
            worksheet.write(i + 1, 26, sum(conscientiousnessListLeftEye) / len(conscientiousnessListLeftEye))
            worksheet.write(i + 1, 27, sum(conscientiousnessListRightEye) / len(conscientiousnessListRightEye))
            worksheet.write(i + 1, 28, sum(conscientiousnessListSmile) / len(conscientiousnessListSmile))
            worksheet.write(i + 1, 29, sum(tempList) / len(tempList))

            if i is videoCount - 1:
                break
        workbook.close()