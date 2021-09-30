# import testing framework
import unittest

# import thing you want to test
from FileWriter import CreateFileWithName

# using uuid module to help generate unique file names
import uuid
# used in setup and cleanup
import os.path
import shutil

testFolder = os.path.join(os.getcwd(), 'TempTestArtifacts')

class TestCreateFileWithName(unittest.TestCase):

    """
    Setup hook defined by unittest. This method is ran before the suite is ran.
    Setup is more commonly used than teardown. We want to make sure our tests always start in a known state
    """
    @classmethod
    def setUpClass(cls):
        # If test directory exists, clean it up and make sure test folder exists
        if os.path.exists(testFolder):
            shutil.rmtree(testFolder)

        os.mkdir(testFolder)

    @classmethod
    def tearDownClass(cls):
        # If test directory exists, clean it up and make sure test folder exists
        if os.path.exists(testFolder):
            shutil.rmtree(testFolder)

    def test_file_with_unique_name_doesnt_have_poop_appended(self):
        """
        Verify that file with a unique name doesn't have poop appended
        """
        # Arrange
        filePath = os.path.join(testFolder, str(uuid.uuid4().hex))

        # Act
        actualCreatedFile = CreateFileWithName(filePath)

        # Assert
        expectedCreatedFile = filePath
        self.assertEqual(actualCreatedFile, expectedCreatedFile)

    def test_file_with_not_unique_name_has_poop_appended(self):
        """
        Verify that file with a non unique name has poop appended until it's unique
        """
        # Arrange
        filePath = os.path.join(testFolder, str(uuid.uuid4().hex))

        # Create file with unique name
        file = open(filePath, 'w+')
        file.close()

        # Act
        actualCreatedFile = CreateFileWithName(filePath)

        # Assert
        expectedCreatedFile = filePath + 'poop'
        self.assertEqual(actualCreatedFile, expectedCreatedFile)

# defines the command line entry point so you can run this test through command line
if __name__ == '__main__':
    unittest.main()