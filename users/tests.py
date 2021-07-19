from quiz.models import Quiz, Question, Choice
from django.test import TestCase

# # Create your tests here.


from django.contrib.auth.models import User


class Test_Home_View(TestCase):
    def setUp(self):
        User.objects.create_user(username="user", password="pass")
        User.objects.create_superuser(
            username="super", email="test@gmail.com", password="pass")

# bellow ok


class Test_LoginView(TestCase):
    def setUp(self):
        User.objects.create_user(username="user", password="pass")
        User.objects.create_superuser(
            username="super", email="test@gmail.com", password="pass")

    def test_login_get(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_post_pass(self):
        args = {'username': 'user', 'password': 'pass'}
        response = self.client.post('/login/', args, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/index.html')
    # bellow not ok

    def test_login_post_fail(self):
        args = {'username': 'dfsgsfg', 'password': 'pass'}
        response = self.client.post('/login/', args, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')


class Test_RegisterView(TestCase):
    def test_register_get(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
    # bellow ok

    def test_register_pass(self):
        args = {'username': 'user', 'password': 'pass'}
        response = self.client.post('/register/', args, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register_fail(self):
        args = {'username': '', 'password': ''}
        response = self.client.post('/register/', args, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

# bellow ok


class Test_LogoutView(TestCase):
    def test_signup_get(self):
        self.client.login(username='user', password='pass')
        response = self.client.get('/logout/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/logout.html')


# class TestResultView(TestCase):
#     def setUp(self):
#         User.objects.create_user(username="user", password="pass")
#         User.objects.create_superuser(
#             username="super", email="test@gmail.com", password="pass")


class Test_Single_quizview(TestCase):
    def setUp(self):
        User.objects.create_user(username="user", password="pass")
        User.objects.create_superuser(
            username="super", email="test@gmail.com", password="pass")

    def test_login_post_pass_index_page(self):
        args = {'username': 'user', 'password': 'pass'}
        response = self.client.post('/quiz/', args, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/index.html')

    def test_get_quiz_page(self):
        args = {'quiz_id': '1'}
        response = self.client.get('/quiz/', args, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/index.html')

    def test_post_quiz__create_page(self):
        args = {'quiz_title': 'computer', 'num_questions': 10}
        response = self.client.post('/quiz/create/', args, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/create_quiz.html')

    def test_get_quiz_page(self):
        args = {'quiz_id': 1, 'question_id': 1}
        response = self.client.get('/quiz/', args, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/index.html')

    def test_get_create_question_page(self):
        args = {'quiz_id': 1, 'question_id': 1, 'vote': 'vote'}
        response = self.client.get('/quiz/', args, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/index.html')
# /quiz/create/7/2/


class SimpleTest(TestCase):
    def test_get_results_page(self):
        args = {'quiz_id': 1, 'results': 'results'}
        response = self.client.get('/quiz/', args, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_create_question_page(self):
        response = self.client.get('/quiz/create/')
        self.assertEqual(response.status_code, 200)
