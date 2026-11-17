import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detect(self):
        data = {"I am glad this happened": "joy",
                "I am really mad about this": "anger",
                "I feel disgusted just hearing about this": "disgust",
                "I am so sad about this": "sadness",
                "I am really afraid that this will happen": "fear"}
        for statement, emotion in data.items():
            self.assertEqual(emotion_detector(statement)["dominant_emotion"], emotion)


unittest.main()