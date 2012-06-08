import unittest
import summoner
import os

TEST_DIR = "/tmp/summoner_test"

class TestShellDetection(unittest.TestCase):
    def setUp(self):
        os.mkdir(TEST_DIR)
        self.current_path = os.environ["PATH"]

    def tearDown(self):
        os.putenv("PATH", self.current_path)
        os.system("rm -rf " + TEST_DIR)

    def test_git_detect_with_git(self):
        f = open(TEST_DIR + "/git", "w")
        f.close()
        os.chmod(TEST_DIR + "/git", 0777)
        os.putenv("PATH", TEST_DIR)
        self.assertTrue(summoner.detect_git())

    def test_git_detect_without_git(self):
        os.putenv("PATH", TEST_DIR)
        self.assertFalse(summoner.detect_git())

    def test_hub_detect_with_hub(self):
        f = open(TEST_DIR + "/hub", "w")
        f.close()
        os.chmod(TEST_DIR + "/hub", 0777)
        os.putenv("PATH", TEST_DIR)
        self.assertTrue(summoner.detect_hub())

    def test_hub_detect_without_hub(self):
        os.putenv("PATH", TEST_DIR)
        self.assertFalse(summoner.detect_hub())

if __name__ == '__main__':
    unittest.main()
