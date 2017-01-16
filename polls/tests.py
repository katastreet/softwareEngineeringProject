import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Question


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):  # name should begin with test
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


def create_question(question_text, days):
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)

#  a testcase inherited class to check if future question are dispalyed
#  also check with past question as well


class QuestionViewTests(TestCase):
    def test_index_view_with_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latestQuestionList'], [])

    def test_index_view_with_a_past_and_a_future_question(self):
        create_question(question_text="Past Question.", days=-1)
        create_question(question_text="Future Question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latestQuestionList'], ['<Question: Past Question.>'])


class QuestionIndexDetialTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        future_question = create_question(question_text='Future Question.', days=5)
        response = self.client.get(reverse('polls:detail', args=(future_question.id, )))
        self.assertEqual(response.status_code, 404)
