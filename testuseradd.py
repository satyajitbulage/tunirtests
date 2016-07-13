"""
This test checks addition of user 
"""
import unittest
from .testutils import system


class UserAddtest(unittest.TestCase):
    """
    Useradd test
    """

    def test_useradd(self):
        out, err, retcode = system("sudo useradd test_satyajit")
        self.assertEqual(retcode, 0, out)
        out, err, retcode = system("cat /etc/passwd")
        self.assertEqual(retcode, 0, out)
        out = out.decode("utf-8")
        self.assertIn('test_satyajit', out)
        out, err, retcode = system("sudo su test_satyajit; exit")
        self.assertEqual(retcode, 0, out)
        out, err, retcode = system("sudo userdel test_satyajit")
        self.assertEqual(retcode, 0, out)
        print(out, err, retcode)


if __name__ == '__main__':
    unittest.main()
