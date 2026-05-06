import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """
    情绪检测器的单元测试类。
    用于验证不同情感语句是否能返回正确的主导情绪。
    """
    
    def test_emotion_detector(self):
        # 测试 Joy (愉悦)
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        # 测试 Anger (愤怒)
        result_2 = emotion_detector('I am mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        # 测试 Disgust (厌恶)
        result_3 = emotion_detector('I am feel bad about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        
        # 测试 Sadness (悲伤)
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        
        # 测试 Fear (恐惧)
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    # 运行测试
    unittest.main()
