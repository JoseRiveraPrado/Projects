import unittest
from image_processing.yolo_model import load_yolo

class TestModel(unittest.TestCase):
    def test_model_loading(self):
        net, classes, output_layers = load_yolo("C:/Projects/obj.cfg", "C:/Projects/backup/obj_last.weights", "C:/Projects/obj.names")
        self.assertIsNotNone(net)
        self.assertEqual(len(classes), 2)

if __name__ == '__main__':
    unittest.main()
