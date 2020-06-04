import unittest
import  valuefile

class TestStringMethods(unittest.TestCase):

    webAppValue=valuefile.WebAppValue()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_head(self):
        # webAppValue=valuefile.WebAppValue()
        self.assertEqual(self.webAppValue.getHomeHandlerHeaders(), 'text/plain')

    def test_getHomeHandlerWrite(self):
        # webAppValue=valuefile.WebAppValue()
        self.assertEqual(self.webAppValue.getHomeHandlerWrite(), 'Welcome to the "Distributed Load Testing Using Kubernetes2" sample web app\n')


if __name__ == '__main__':
    unittest.main()