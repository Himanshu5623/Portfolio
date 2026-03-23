from django.test import TestCase
from django.urls import reverse


class PortfolioPageTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_page_loads(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_projects_page_loads(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects.html')

    def test_skills_page_loads(self):
        response = self.client.get(reverse('skills'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'skills.html')
