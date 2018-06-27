from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from django.urls import reverse


class PasswordResetMailTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='lara', email='lara@doe.com', password='123')
        self.response = self.client.post(reverse('password_reset'), {'email': 'lara@doe.com'})
        self.email = mail.outbox[0]

    def test_email_subject(self):
        self.assertEqual('[Learnflows] Password Reset Request', self.email.subject)

    def test_email_body(self):
        context = self.response.context
        token = context.get('token')
        uid = context.get('uid')
        password_reset_token_url = reverse('password_reset_confirm', kwargs={
            'uidb64': uid,
            'token': token
        })
        self.assertIn(password_reset_token_url, self.email.body)
        self.assertIn('lara', self.email.body)
        self.assertIn('lara@doe.com', self.email.body)

    def test_email_to(self):
        self.assertEqual(['lara@doe.com', ], self.email.to)